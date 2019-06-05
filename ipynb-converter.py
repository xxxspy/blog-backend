import sys
import nbconvert
import os
import time
from ipython_genutils.path import ensure_dir_exists
import shutil

BASE = os.path.split(os.path.realpath(__file__))[0]
POST = os.path.join(BASE, 'source/_posts')
SITE_INFOS='''\n
本文章转载自于ipython notebook [{filename}]({source_link}).

### 联系我们

站长QQ: 1497369272(请注明来自mlln)
记住网址: mlln.cn
加入我们的讨论QQ群:680552969(请注明来自mlln) 
'''

class HexoWriter(nbconvert.writers.FilesWriter):
	def _add_headinfos(self, output, title):
		head = '''---
title: {}
date: {}
tags: notebook
---
本文章转载自于ipython notebook.
<!-- more -->
'''
		date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		head = head.format(title, date)
		output = head + '\n' + output
		return output

	def _handle_imgs(self, output):
		_output= []
		lines = output.split('\n')
		img_t='{%% asset_img %s %%}'
		for line in lines:
			if line.startswith('![png]') or \
				line.startswith('![svg]') or \
				line.startswith('![jpeg]'):
				filename = line.split('(')[1].split(')')[0]
				line= img_t % filename
			_output.append(line)
		return '\n'.join(_output)

	def _add_site_infos(self, output, filename, source_link):
		si = SITE_INFOS.format(filename = filename, source_link=source_link)
		return output + si

	def _edit_output(self, output, title, source_link):
		output = self._add_headinfos(output, title)
		output = self._handle_imgs(output)
		output = self._add_site_infos(output, title, source_link)
		return output

	def write(self, output, resources,resource_dir, md_filename, source_link):
		output_extension=resources.get('output_extension')
		output = self._edit_output(output, md_filename, source_link)
		self.build_directory=resource_dir
		super().write(output, resources, md_filename)
		# remove markdown file from resource_dir to POST dir
		md_filepath = os.path.join(resource_dir, md_filename + output_extension)
		to_path = os.path.join(POST, md_filename+output_extension)
		os.rename(md_filepath, to_path)



# mdcvt=nbconvert.MarkdownExporter()
# wt=nbconvert.writers.FilesWriter()

# md=mdcvt.from_filename(sys.argv[1])

# print(md[1]['outputs'].keys())
# print(md[1].keys())

# # open('test.md', 'w', encoding='utf8').write(md[0])

# wt.write(md[0], md[1], 'testname')

def write_fromfile(from_filename, md_filename=None, source_link=None):
	fname=os.path.split(from_filename)[1]
	extension='.ipynb'
	if fname.endswith(extension):
		fname = fname[:-len(extension)]
	if not md_filename:
		md_filename = fname

	mdcvt=nbconvert.MarkdownExporter()
	output, resources = mdcvt.from_filename(from_filename)
	output_extension=resources.get('output_extension')
	while md_filename.endswith(output_extension):
		md_filename= md_filename[:-len(output_extension)]

	n=0
	while os.path.exists(os.path.join(POST, md_filename + output_extension)):
		n += 1
		md_filename += '-{}'.format(n)

	resource_dir = os.path.join(POST, md_filename)

	if not source_link:
		source_link = fname + extension
		source_fpath = os.path.join(resource_dir, source_link )
		ensure_dir_exists(resource_dir)
		shutil.copyfile(from_filename, source_fpath)

	writer = HexoWriter()
	writer.write(output, resources, resource_dir, md_filename, source_link)

if __name__=='__main__':
	# notebook文件名, 必须为绝对路径
	from_filename = sys.argv[1]
	# 输出文件名, 可选, 如果没有设置, 默认使用notebook文件名
	if len(sys.argv)>2:
		md_filename = sys.argv[2]
	else:
		md_filename=None
	# source_link 是文章附带的资源文件夹路径
	# 如果不设定会使用文章的同名文件夹
	if len(sys.argv)>3:
		source_link = sys.argv[3]
	else:
		source_link = None
	write_fromfile(from_filename, md_filename, source_link)


