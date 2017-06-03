# 安装部署

### 安装依赖

```
npm install 
```

### 增加对mathjax渲染的支持

 在目录`node_modules\kramed\lib\rules\inline.js`，修改如下：

```javascript
//  escape: /^\\([\\`*{}\[\]()#$+\-.!_>])/,
  escape: /^\\([`*\[\]()#$+\-.!_>])/
```

和

```javascript
//  em: /^\b_((?:__|[\s\S])+?)_\b|^\*((?:\*\*|[\s\S])+?)\*(?!\*)/,
  em: /^\*((?:\*\*|[\s\S])+?)\*(?!\*)/
```