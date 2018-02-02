import ftplib
import os
from pathlib import Path, PosixPath
import hashlib
import json
import unittest
import shutil
import sys

_dir=os.path.abspath(os.path.dirname(__file__))
_temp_md5_path=Path(_dir) / 'ftp' / '_temp_md5.json'
_temp_new_md5_path=Path(_dir) / 'ftp' / '_temp_new_md5.json'
_FILE='file'
_DIR='dir'

class Updater:
    
    myfolder=Path('/myfolder')
    remote_dir=Path('/htdocs')
    no_del=Path('/htdocs/ewh_logreport_no_delete')
    remote_md5_path=myfolder / 'md5.json'
    username = os.environ['ALI_FTP_USER']
    address = os.environ['ALI_FTP_ADDRESS']
    password = os.environ['ALI_FTP_PASSWORD']
    cached_folders=[]

    def __init__(self, public_dir, published_dir, md5_data_path):
        self.public_dir=Path(os.path.join(_dir, public_dir) )
        self.published_dir=Path(os.path.join(_dir, published_dir))
        self.md5_data_path=Path(os.path.join(_dir, md5_data_path))
        self._init_ftp()

    def _init_ftp(self):
        ftp=ftplib.FTP(self.address)
        ftp.login(self.username, self.password)
        ftp.encoding='utf8'
        self.ftp=ftp

    def remove_ftp_folder(self, path:Path):
        dir_name= path.stem
        parent=path.parent
        folders=self.ftp.nlst(parent.as_posix())
        if path.as_posix() in folders:
            allfiles=self.ftp_filepaths(path)
            for f in allfiles:
                self.ftp.delete(f)
            self.ftp.rmd(path.as_posix())
            if path in self.cached_folders:
                del self.cached_folders[self.cached_folders.index(path)]

    def create_ftp_folder(self, path:Path):
        if path in self.cached_folders:
            return
        dir_name= path.stem
        parent=path.parent
        root1=Path(self.remote_dir.parts[0],self.remote_dir.parts[1])

        root2=Path(self.myfolder.parts[0],self.myfolder.parts[1])
        if len(parent.parts)>=2 and (parent != root1) and (parent != root2):
            self.create_ftp_folder(parent)
        folders=self.ftp.nlst(parent.as_posix())
        if path.as_posix() not in folders:
            self.ftp.mkd(path.as_posix())
            self.cached_folders.append(path)

    def cwd(self, path=None):
        if path:
            self.ftp.cwd(path)
        else:
            self.ftp.cwd()
        self._wd=ftp.pwd()

    def ftp_filepaths(self, path):
        '''从ftp上获取path下所有文件路径'''
        path=Path(path)
        files=[]
        type, children=self._ftp_children(path)
        ignore_path=self.no_del.as_posix()
        if type == _FILE:
            files.extend(children)
        else:
            if path not in self.cached_folders:
                self.cached_folders.append(path)
            for p in children:
                if p.startswith(ignore_path):
                    continue
                _files=self.ftp_filepaths(p)
                files.extend(_files)
        return files


    def _ftp_children(self, path):
        '''从ftp上获取path下所有文件和文件夹路径'''
        path=Path(path)
        if path.as_posix().startswith(self.no_del.as_posix()):
            return _FILE, []
        file_dirs=self.ftp.nlst(path.as_posix())
        if len(file_dirs) == 1 and file_dirs[0]==path.as_posix():
            # this path is a file path
            return _FILE, file_dirs
        else:
            # this path is a directory
            return _DIR, file_dirs

    def _local(self, local_dir, path):
        assert path.startswith(self.remote_dir)
        path = path[len(self.remote_dir)+1:]
        return os.path.join(local_dir, path)

    def download(self):
        all_files=self.ftp_filepaths(self.remote_dir)
        local_files=[self._local(self.published_dir, p) for p in all_files]

        for i in range(len(all_files)):
            remote_path=all_files[i]
            local_path=local_files[i]

            if not os.path.exists(local_path):
                print('fetching '+ remote_path)
                p=Path(local_path)
                p.parent.mkdir(parents=True, exist_ok=True)

            f=open(local_path, 'wb')
            self.ftp.retrbinary('RETR '+remote_path, f.write)

    def _md5(self, filename):
        m=hashlib.md5()
        f=open(str(filename),'rb')
        m.update(f.read())
        f.close()
        return m.hexdigest()

    def _same_md5(self, path):
        if not hasattr(self, 'new_md5_data'):
            if _temp_new_md5_path.exists():
                self.new_md5_data=json.loads(_temp_new_md5_path.read_text())
            else:
                self.new_md5_data = {}
        if not hasattr(self, 'md5_data'):

            p= self.md5_data_path
            if _temp_md5_path.exists():
                self.md5_data=json.loads(_temp_md5_path.read_text())
            elif p.exists():
                self.md5_data=json.loads(p.read_text())
            else:
                self.md5_data=data={}

        if str(path) in self.md5_data:
            md5=self.md5_data[str(path)]
        else:
            md5=self._md5(self.published_dir / path)
            self.md5_data[str(path)]=md5

        md5_new=self._md5(self.public_dir / path)

        b= md5==md5_new
        if not b:
            self.new_md5_data[str(path)]=md5_new
        return b

    def compare(self):
        to_publish=self._files(self.public_dir, self.public_dir)
        published_files=self._files(self.published_dir, self.published_dir)
        update_files=[]
        remove_files=published_files[:]
        new_files=[]
        ignore_files=[]
        for pf in to_publish:
            if pf in published_files:
                del remove_files[remove_files.index(pf)]
                if self._same_md5(pf):
                    ignore_files.append(pf)
                else:
                    update_files.append(pf)
            else:
                new_files.append(pf)
        return update_files,remove_files,new_files,ignore_files

    def movefiles(self, update_files=[],remove_files=[],new_files=[],ignore_files=[]):
        for uf in update_files + new_files:
            f= self.public_dir / uf
            t=self.published_dir / uf
            if not t.parent.exists():
                t.parent.mkdir(parents=True)
            shutil.copy2(str(f),str(t))
            print('Copy to: '+ str(t))
        for rf in remove_files:
            (self.published_dir / rf).unlink()
            print('Del : ' + str(rf))


    def handle_md5_datas(self, remove_files=[]):

        md5s={}
        if hasattr(self, 'md5_data') and self.md5_data:
            md5s.update(self.md5_data)
        if hasattr(self, 'new_md5_data') and self.new_md5_data:
            md5s.update(self.new_md5_data)

        for f in remove_files:
            f=str(f)
            if f in md5s:
                del md5s[f]

        if md5s:
            self.md5_data_path.write_text(json.dumps(md5s))
            file=self.md5_data_path.open('rb')
            self.ftp.storbinary('STOR ' + self.remote_md5_path.as_posix() , file)
            file.close()

        return md5s


    def execute(self, update_files,remove_files,new_files,chunck_size=10):
        deleted=[]
        for f in remove_files:
            print('Removing file: '+ (self.remote_dir / f).as_posix())
            try:
                self.ftp.delete((self.remote_dir / f).as_posix())
            except Exception as e:
                print('Error Removing: '+ (self.remote_dir / f).as_posix())
            deleted.append(f)
            if len(deleted)>=chunck_size:
                self.movefiles(remove_files=deleted)
                deleted=[]
        if deleted:
            self.movefiles(remove_files=deleted)
            deleted=[]

        uploaded=[]
        for f in new_files:
            rf=self.remote_dir / f
            lf=self.public_dir / f
            print('Upload File: ' + rf.as_posix())
            file=lf.open('rb')
            if rf.parent not in self.cached_folders:
                self.create_ftp_folder(rf.parent)
            self.ftp.storbinary('STOR ' + rf.as_posix(), file)
            file.close()
            uploaded.append(f)
            if len(uploaded)>=chunck_size:
                self.movefiles(new_files=uploaded)
                uploaded=[]
        if uploaded:
            self.movefiles(new_files=uploaded)
            uploaded=[]

        updated=[]
        for f in update_files:
            rf=self.remote_dir / f
            lf=self.public_dir / f
            print('Update file: '+ rf.as_posix())
            file=lf.open('rb')
            self.ftp.storbinary('STOR ' + rf.as_posix(), file)
            file.close()
            if len(updated)>=chunck_size:
                self.movefiles(update_files=updated)
                updated=[]
        if updated:
            self.movefiles(update_files=updated)
            updated=[]

        return deleted, uploaded, updated

    def to_ftp(self):
        rtn=self.compare()
        self.execute(*rtn[:3])
        self.movefiles(*rtn)
        self.handle_md5_datas(rtn[1])
        self.del_temp_data()

    def to_local(self):
        raise NotImplementedError

    def _files(self, path, relative_to):
        path=Path(path)
        assert not path.is_file(), 'Not a Folder: ' + str(path)
        files=[]
        for child in path.iterdir():
            if child.is_file():

                relative= child.relative_to(relative_to)
                files.append(relative)
            else:
                _fs=self._files(child, relative_to)
                files.extend(_fs)
        return files
    def close(self):
        self.ftp.close()

    def save_temp_data(self):
        if hasattr(self, 'md5_data') :
            _temp_md5_path.write_text(json.dumps(self.md5_data))
        if hasattr(self, 'new_md5_data'):
            _temp_new_md5_path.write_text(json.dumps(self.new_md5_data))
    def del_temp_data(self):
        if _temp_md5_path.exists():
            _temp_md5_path.unlink()
        if _temp_new_md5_path.exists():
            _temp_new_md5_path.unlink()


class TextUpdater(unittest.TestCase):
    def setUp(self):
        public_dir='___public_test'
        published_dir='____ftp_test/public'
        md5_data_path='____ftp_test/md5.json'

        self.updater=Updater(public_dir, published_dir, md5_data_path)
        self.updater.remote_dir =self.updater.remote_dir / 'test'
        self.updater.myfolder = self.updater.myfolder / 'test'
        self.updater.create_ftp_folder(self.updater.remote_dir)
        self.updater.create_ftp_folder(self.updater.myfolder)
        self.updater.public_dir.mkdir(parents=True, exist_ok=True)
        self.updater.published_dir.mkdir(parents=True, exist_ok=True)


    def test_compare(self):
        pcd=self.updater.public_dir
        psd=self.updater.published_dir
        md5=self.updater.md5_data_path
        f=(psd / 'to_remove.txt');f.write_text('remove content')
        f=(pcd / 'to_update.txt');f.write_text('update content')
        f=(psd / 'to_update.txt');f.write_text('old content')
        f=(pcd / 'to_add.txt');f.write_text('add content')
        f=(pcd / 'to_add2.txt');f.write_text('add content 2')
        f=(psd / 'to_ignore.txt');f.write_text('ignore content')
        f=(pcd / 'to_ignore.txt');f.write_text('ignore content')
        rtn=self.updater.compare()
        lens=[['to_update.txt'],['to_remove.txt'],['to_add.txt','to_add2.txt'],['to_ignore.txt']]
        for i,r in enumerate(rtn):
            for j,p in enumerate(r):
                self.assertEqual(str(p), lens[i][j])


        update_files,remove_files,new_files,ignore_files=rtn

        self.updater.movefiles(update_files,remove_files,new_files,ignore_files)
        self.assertEqual((pcd / update_files[0]).exists(), True)
        self.assertEqual( (pcd / update_files[0]).read_text(),(psd / update_files[0]).read_text())
        self.assertEqual((psd / remove_files[0]).exists(), False)
        self.assertEqual((psd / new_files[0]).read_text()[:11], 'add content')
        self.assertEqual((psd / ignore_files[0]).read_text(), 'ignore content')

        self.updater.execute(*rtn[:3])

        md5s=self.updater.handle_md5_datas(remove_files)
        _md5s={}
        _md5s.update(self.updater.md5_data)
        _md5s.update(self.updater.new_md5_data)
        self.assertDictEqual(json.loads(self.updater.md5_data_path.read_text()), _md5s)



    def tearDown(self):
        files=self.updater._files(self.updater.public_dir, self.updater.public_dir)
        try:
            self.updater.md5_data_path.unlink()
        except FileNotFoundError:
            pass
        for f in files:
            (self.updater.public_dir / f).unlink()
        self.updater.public_dir.rmdir()

        files= self .updater._files(self.updater.published_dir, self.updater.published_dir)
        for f in files:
            (self.updater.published_dir / f).unlink()
        self.updater.published_dir.rmdir()
        Path('____ftp_test').rmdir()

        ## remove ftp files

        self.updater.remove_ftp_folder(self.updater.remote_dir)
        self.updater.remove_ftp_folder(self.updater.myfolder)
        self.updater.ftp.close()

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='publish':
        public_dir='public'
        published_dir='ftp/public'
        md5_data_path='ftp/md5.json'
        updater=Updater(public_dir, published_dir, md5_data_path)
        try:
            updater.to_ftp()
        except:
            updater.save_temp_data()
            updater.close()     
            raise           

        updater.close()
    else:
        print('Nothing hanppend!')