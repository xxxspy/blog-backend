
微软开发了一个帮助开发者学习officejs的代码编辑器， 它是一个office task pane插件， 可以在Excel、word等offic软件中加载。但是该插件的服务器在国外，国内访问很慢， 怎么办？我的第一想法是将这个插件的服务器部署到本地，下面是我的部署过程。

<!-- more -->

### 工具&环境

- VSCode 代码编辑器
- nodejs
- Windows系统

### 复制代码

```
>>> git clone https://github.com/OfficeDev/script-lab 
Cloning into 'script-lab'...
remote: Counting objects: 15924, done.
remote: Total 15924 (delta 0), reused 0 (delta 0), pack-reused 15924 eceiving objects:  99% (15914/15924), 39.03 MiB | 788.00 KiB/s
Receiving objects: 100% (15924/15924), 39.21 MiB | 778.00 KiB/s, done.
Resolving deltas: 100% (11305/11305), done.
```

### 配置VSCode

使用vscode打开script-lab工程目录， 工作区设置：

```json
    "terminal.integrated.env.windows": {
        "PATH":"D:\\mygits\\script-lab\\.env;D:\\Python27;D:\\Python27\\scripts"
    }

```
注意， 我们还配置了python2的路径， 因为yarn安装依赖的时候用到了python2.

### 安装yarn

打开vscode 终端， 输入命令：
```
npm install -g yarn
```

{% asset_img 终端安装yarn.jpg %}

### 安装依赖库

打开vscode 终端， 输入命令：
```
D:\mygits\script-lab>yarn install
yarn install v1.3.2
[1/5] Validating package.json...
[2/5] Resolving packages...
[3/5] Fetching packages...
info fsevents@1.1.2: The platform "win32" is incompatible with this module.
info "fsevents@1.1.2" is an optional dependency and failed compatibility check. Excluding it from installation.
[4/5] Linking dependencies...
warning " > @angular/core@4.0.0" has unmet peer dependency "rxjs@^5.0.1".
warning " > @angular/http@4.0.0" has unmet peer dependency "rxjs@^5.0.1".
warning " > @angular/router@4.0.0" has unmet peer dependency "rxjs@^5.0.1".
warning " > @ngrx/core@1.2.0" has unmet peer dependency "rxjs@^5.0.0-beta.12".
warning " > @ngrx/effects@2.0.2" has incorrect peer dependency "@angular/core@^2.0.0".
warning " > @ngrx/effects@2.0.2" has unmet peer dependency "rxjs@^5.0.0-beta.12".
warning " > @ngrx/store@2.2.1" has incorrect peer dependency "@angular/core@^2.0.0".
warning " > @ngrx/store@2.2.1" has unmet peer dependency "rxjs@^5.0.0-beta.12".
warning " > @ngrx/store-devtools@3.2.4" has unmet peer dependency "rxjs@^5.0.0-beta.12".
warning " > @ngrx/store-log-monitor@3.0.2" has unmet peer dependency "rxjs@^5.0.0-beta.11".
warning " > @ngrx/store-log-monitor@3.0.2" has incorrect peer dependency "@angular/core@^2.0.0-rc.6".
[5/5] Building fresh packages...
Done in 27.54s.
```

### 启动服务器

```
D:\mygits\script-lab>npm start

> script-lab@1.1.0 start D:\mygits\script-lab
> npm-run-all clean -p build:runtime_helpers:dev build:dev dev:*


> script-lab@1.1.0 clean D:\mygits\script-lab
> rimraf dist && rimraf .awcache


> script-lab@1.1.0 dev:copy D:\mygits\script-lab
> cpx "src/server/**/!(*.ts)" "dist/server" --watch


> script-lab@1.1.0 build:dev D:\mygits\script-lab
> webpack-dev-server --config config/webpack.dev.js --progress

[..................] / : info using node@v6.11.5
> script-lab@1.1.0 dev:server D:\mygits\script-lab
> tsc -p tsconfig.server.json --watch


> script-lab@1.1.0 build:runtime_helpers:dev D:\mygits\script-lab
> tsc -p src/runtime-helpers/tsconfig.json --watch


> script-lab@1.1.0 dev:config D:\mygits\script-lab
> cpx "config/env.config.js" "dist/server/core" --watch

 12% building modules 18/18 modules 0 active
Project is running at https://localhost:3100/
webpack output is served from /
Content not from webpack is served from D:\mygits\script-lab\dist\client
404s will fallback to /index.html
 12% building modules 18/19 modules 1 active ...lient\index.js?https://localhost:310012:55:57 - Compilation complete. Watching for file changes.


 12% building modules 22/40 modules 18 active ...s\script-lab\src\client\public\log.ts
[at-loader] Using typescript@2.2.2 from typescript and "tsconfig.json" from D:\mygits\script-lab\tsconfig.webpack.json (in a forked process).

 22% building modules 101/119 modules 18 active ...s\script-lab\src\client\public\log.ts12:55:59 - Compilation complete. Watching for file changes.


 94% asset optimization
[at-loader] Checking started in a separate process...

[at-loader] Ok, 0.675 sec.
[BS] Proxying: https://localhost:3100
[BS] Access URLs:
 ----------------------------------------
       Local: https://localhost:3000
    External: https://172.16.160.165:3000
 ----------------------------------------
          UI: http://localhost:3001
 UI External: http://172.16.160.165:3001
 ----------------------------------------
```

### 在浏览器中打开

看下图， 你会看到有证书问题， 忽略继续浏览即可。

{% asset_img 安全证书问题.jpg %}

最后你会看到如图所示的界面， 说明你的服务器已经在本地部署完毕了。

{% asset_img 在浏览器中打开.jpg %}

### 在word中加载

参考我上一篇文章{% asset_link officejs-script-lab本地部署过程 officejs-script-lab本地部署过程 %}, 你就知道， 我们现在需要做的就是把manifest放到共享文件夹里， 因为我在上一篇文章中设置过一个共享文件夹， 现在只需要将manifest文件放到该文件夹中。 script lab 的manifest在manifet文件夹下， 我们选择script-lab-local.xml即可。

{% asset_img 加载插件.jpg %}