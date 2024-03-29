
---

title: 爬虫如何隐藏Headles-Chrome不被检测出来
date: 2019-07-05 12:44:03
tags: [javascript, chrome, 爬虫, 逆向工程]

---

这是上一篇文章的对偶篇, 上一篇文章讲如何检测客户端是否是Chrome Headless, 这篇文章讲那些检测方法是如何失效的!
<!-- more -->

一篇名为[Detecting Chrome Headless](/2019/07/05/前端如何检测Chrome-Headless不被爬虫虐/)的短篇文章在网上引起讨论。关于黑客新闻的大多数讨论集中在作者有点可疑的断言上，即网络抓取是一种“恶意任务”，与广告欺诈和黑客网站属于同一类别。这总是一个有趣的辩论，但我真正对这篇文章提出的问题是它隐含地提倡了基于浏览器指纹识别来阻止用户的想法。就我而言，这通常是一个糟糕的想法，你更有可能阻止和挫败你的用户，而不是为那些你试图阻止的人提供任何有意义的威慑。

为了说明这一点，我通过了这篇文章中提出的所有测试，毫不奇怪，我的标准日常浏览器未通过某些测试(这说明这些方法很可能阻断正常的用户)。

### UserAgent

这几乎是唯一可以合法识别Chrome Headless的测试，但它也是最容易绕过的。在无头模式下运行Chrome时的默认userAgent是这样的:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36
```

要更改此设置，我们只需向Chrome提供`--user-agent`命令行选项即可。如果您直接从命令行运行Chrome，那么除了无头之外，您还需要包含此选项。

如果您使用的是Python+Selenium+ChromeDriver，则可以使用ChromeOptions.add_argument（）指定相同的选项。

```py
from selenium import webdriver

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

options = webdriver.ChromeOptions()
# specify headless mode
options.add_argument('headless')
# specify the desired user agent
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options)

# user-agent is now set
```

如果你想使用Chrome DevTools协议，这种方法会略有不同，但也可以做到。

CDP的nodejs代码:

```js
const CDP = require('chrome-remote-interface');

const userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

CDP(async function(client) {
  const {Network, Page} = client;
  await Page.enable();
  await Network.enable();
  await Network.setUserAgentOverride({userAgent});

  // user-agent is now set
});
```

如果你要用python, CDP也被人封装到了python中, 试试pychrome。

所有这些方法都将更改HTTP标头和window.navigator.userAgent中的用户代理。现在进入更具挑战性任务！

### Languages and Plugins

建议的两个测试是检查navigator.plugins.length === 0和navigator.languages ==''。通过JavaScript注入, 将每个页面的window.navigator覆盖，可以绕过这些。让我们现在专注于JavaScript来模拟这些值。一旦我们完成所有测试，我们将回过头来看看如何注入它，因为它们都需要立即注入。

我们基本上只想覆盖navigator的两个属性: plugins和languages。您的第一个想法可能是直接设置属性:

```js
navigator.languages = ['en-US', 'en'];
navigator.plugins = [1, 2, 3, 4, 5];
```

但这实际上并不会覆盖这些值，因为这些是带有getter函数作为访问器的只读属性。我们需要使用Object.defineProperty（）来重新定义具有新getter函数的属性。这可以如下完成。

```js
// overwrite the `languages` property to use a custom getter
Object.defineProperty(navigator, 'languages', {
  get: function() {
    return ['en-US', 'en'];
  },
});

// overwrite the `plugins` property to use a custom getter
Object.defineProperty(navigator, 'plugins', {
  get: function() {
    // this just needs to have `length > 0`, but we could mock the plugins too
    return [1, 2, 3, 4, 5];
  },
});
```

在页面上执行此JavaScript后，navigator.languages将返回['en-US'，'en']，navigator.plugins的长度为5. plugins可以做的更真实一点，但这不是必需的, 在这种情况下我们只检查数组的长度。

### WebGL Vendor and Renderer

下一个测试是创建一个WebGL上下文，然后检查供应商和渲染器字符串。供应商 Brian Paul或渲染器Mesa OffScreen暗示这可能是Chrome Headless。我无法在我的机器上重现这些字符串，但让我们看看如何在它们存在的情况下模拟这些值。我们只需硬编码WebGLRenderingContext.getParameter（），通过修改WebGLRenderingContext的原型来返回我们想要的供应商和渲染器字符串。修改原型可确保在创建的任何WegGlRenderingContext实例上调用我们的修补版本（例如，通过执行canvas.getContext（'webgl'））。

```js
const getParameter = WebGLRenderingContext.getParameter;
WebGLRenderingContext.prototype.getParameter = function(parameter) {
  // UNMASKED_VENDOR_WEBGL
  if (parameter === 37445) {
    return 'Intel Open Source Technology Center';
  }
  // UNMASKED_RENDERER_WEBGL
  if (parameter === 37446) {
    return 'Mesa DRI Intel(R) Ivybridge Mobile ';
  }

  return getParameter(parameter);
};
```

此版本getParameter（）返回任何我们想要的数据，同时不影响任何其他参数值的标准实现。这里的整数是唯一标识参数的标准常量。

### Broken Image

我们已经提到过，"破碎图像"测试确实没有意义，因为Chrome 60报告的图像大小为0x0，用于无法加载的图像。让我们来看看我们如何做到这一点，只是为了表明它也很容易绕过。这种方法结合了我们已经使用过的几种技术。

我们将再次修改原型，这次是HTMLImageElement，这样我们所做的更改将适用于在DOM中创建的任何图像。宽度和高度都是具有访问器的属性，因此我们还需要使用Object.defineProperty（）来覆盖其getter方法。对于损坏的图像，我们将返回20的宽度和高度，否则简单地遵循标准的getter实现。

```js
['height', 'width'].forEach(property => {
  // store the existing descriptor
  const imageDescriptor = Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, property);

  // redefine the property with a patched descriptor
  Object.defineProperty(HTMLImageElement.prototype, property, {
    ...imageDescriptor,
    get: function() {
      // return an arbitrary non-zero dimension if the image failed to load
      if (this.complete && this.naturalHeight == 0) {
        return 20;
      }
      // otherwise, return the actual dimension
      return imageDescriptor.get.apply(this);
    },
  });
});
```

### Retina/HiDPI Hairline Feature

最后提出的方法是使用Modernizr库检测对Hairline的支持。这是另一项测试，并没有真正有意义，因为大多数人没有HiDPI屏幕，大多数用户的浏览器不支持此功能。然而，即使用作测试也是有意义的，绕过它也是很简单的。

我们可以从Modernizr代码看到，测试基本上等于将id为modernizr的div标签与下面的样式表一起插入到页面中。


然后检查div的offsetHeight属性，如果它的值为1，则支持Hairline特征。我们需要做的就是修改HTMLDivElement的原型，使得如果id为modernizr，offsetHeight返回1。这个基本模式现在应该变得非常熟悉......

```js
// store the existing descriptor
const elementDescriptor = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');

// redefine the property with a patched descriptor
Object.defineProperty(HTMLDivElement.prototype, 'offsetHeight', {
  ...elementDescriptor,
  get: function() {
    if (this.id === 'modernizr') {
        return 1;
    }
    return elementDescriptor.get.apply(this);
  },
});
```

### 代码注入

在这一点上，我们有一堆JavaScript代码片段将绕过Chrome Headless测试。我们只需要Chrome在目标网站上的测试代码之前执行它们。使用Selenium通过调用WebDriver.executeScript（）将JavaScript注入页面是可能的，但遗憾的是，只有在文档的onload事件被触发后才会调用它。这意味着，如果有一个同步测试阻止页面加载，它在你能够注入js之前运行测试。

如果我们想要可靠地通过测试，那么我们需要找到一种方法来确保我们的代码在页面上的测试代码之前运行。我最喜欢的方法是编写一个小型Chrome扩展程序，将脚本注入任何访问过的页面的头部。不幸的是，Chrome Headless尚不支持扩展，在可预见的未来可能不会。在添加该功能之前，我们需要使用替代方法。

将JavaScript注入页面的更健壮的方法是实际修改所请求的HTML并在浏览器有机会查看原始文件之前注入脚本。这种技术更常用于提供站点自己脚本的修补版本，但它可以以相同的方式应用于此用例。我们将使用mitmproxy，一个非常容易编写脚本的TLS-capabable HTTP代理来注入我们的代码。

首先，我们需要同时安装mitmproxy和BeautifulSoup4。这些可能都是通过您系统的软件包管理器提供的，但如果需要，您也可以使用pip install mitmproxy bs4在virtualenv中安装它们。我们现在将制作一个名为inject.py的简短python脚本，其中包含以下内容。

```js
from bs4 import BeautifulSoup
from mitmproxy import ctx

# load in the javascript to inject
with open('content.js', 'r') as f:
    content_js = f.read()

def response(flow):
    # only process 200 responses of html content
    if flow.response.headers['Content-Type'] != 'text/html':
        return
    if not flow.response.status_code == 200:
        return

    # inject the script tag
    html = BeautifulSoup(flow.response.text, 'lxml')
    container = html.head or html.body
    if container:
        script = html.new_tag('script', type='text/javascript')
        script.string = content_js
        container.insert(0, script)
        flow.response.text = str(html)

        ctx.log.info('Successfully injected the content.js script.')
```

inject.py脚本定义了一个response(flow)函数，该函数将在每个响应被代理之前由mitmproxy调用。如果响应具有200个状态代码和text / html的内容类型，那么我们将脚本注入从content.js加载的内容。这里的content.js只包含我们在前面每个部分中开发的所有JavaScript测试。

要使用此脚本启动代理，我们现在可以运行以下代码。

```
mitmdump -p 8080 -s "inject.py"
```

启动chrome:

```
/opt/google/chrome-beta/chrome \
    --headless \
    --proxy-server=localhost:8080 \
    --remote-debugging-port=9222
 ```
 
` --headless`选项可预测地告诉Chrome以无头模式运行`--remote-debugging-port`指定我们将用于与之通信并控制实例的调试接口。您现在可以运行该命令，它只会等待我们在几分钟内连接到调试端口。

我们将使用Chrome远程接口来实际控制实例。这个界面有点类似于Selenium，但它只能使用Chrome，允许对某些事物进行更精细的控制。特别是，它允许我们接受来自mitmproxy的自签名证书。这可以通过ChromeDriver实现，因为acceptInsecureCerts被指定为W3规范的一部分，但这个特殊功能尚未在Chrome Headless中实现。

要安装Chrome远程接口，您可以运行`yarn add chrome-remote-interface`或与您选择的软件包管理器等效的接口。安装完成后，创建一个名为test-headless.js的文件，其中包含以下内容。

```js
const CDP = require('chrome-remote-interface');
const fs = require('fs');

// global settings
const filename = 'headless-results.png';
const url = 'https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html';
const userAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

CDP(async function(client) {
  const {Network, Page, Security} = client;
  await Page.enable();
  await Network.enable();
  await Network.setUserAgentOverride({userAgent});

  // ignore all certificate errors to support mitmproxy certificates
  await Security.enable();
  await Security.setOverrideCertificateErrors({override: true});
  Security.certificateError(({eventId}) => {
    Security.handleCertificateError({
        eventId,
        action: 'continue'
    });
  });

  // navigate to the page and wait for it to load
  await Page.navigate({url});
  await Page.loadEventFired();

  setTimeout(async function() {
    // save the screenshot
    const screenshot = await Page.captureScreenshot({format: 'png'});
    const buffer = new Buffer(screenshot.data, 'base64');
    fs.writeFile(filename, buffer, 'base64', function(err) {
      if (err) {
        console.error(`Error saving screenshot: `${err}`);
      } else {
        console.log(`"$`

此脚本将连接到我们当前运行的Headless Chrome实例，访问测试页，1秒后保存屏幕截图，然后退出。 Chrome本身已经在运行，并且已经配置为通过mitmproxy代理所有内容。因此，Chrome呈现的页面应在文档的head标记中包含我们的代码。

所有部分现在都已到位，我们现在可以使用`node test-headless.js`运行脚本（请注意，由于使用了async / await，这将需要至少7.6的节点版本）。当脚本运行时，我们应该在mitmdump终端中看到类似于以下内容的输出。

```
Loading script: inject.py
Proxy server listening at http://0.0.0.0:8080
127.0.0.1:57132: clientdisconnect
127.0.0.1:59524: clientconnect
127.0.0.1:59524: CONNECT intoli.com:443
 << Cannot establish TLS with client (sni: intoli.com): TlsException("(104, 'ECONNRESET')",)
127.0.0.1:59526: clientconnect
127.0.0.1:59524: clientdisconnect
Successfully injected the content.js script.
127.0.0.1:59526: GET https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.html
              << 200 OK 1.12k
127.0.0.1:59528: clientconnect
127.0.0.1:59526: GET https://intoli.com/blog/making-chrome-headless-undetectable/modernizr.js
              << 200 OK 2.43k
127.0.0.1:59528: CONNECT intoli.com:443
 << Cannot establish TLS with client (sni: intoli.com): TlsException("(-1, 'Unexpected EOF')",)
127.0.0.1:59530: clientconnect
127.0.0.1:59528: clientdisconnect
127.0.0.1:59526: GET https://intoli.com/blog/making-chrome-headless-undetectable/chrome-headless-test.js
              << 200 OK 2.27k
127.0.0.1:59526: GET https://intoli.com/nonexistent-image.png
              << 404 Not Found 189b
```

还有一些错误，但这些都不用担心，因为它们是客户端需要覆盖证书错误的结果。忽略这些，看起来我们看到了预期的请求，并且在返回chrome-headless-test.html响应之前成功注入了脚本标记。

最后，让我们看一下生成的headless-results.png，以验证我们现在是否通过了所有测试。

### 总结


这无疑是绕过测试的一种错综复杂的方法。我采用这条较长路线的原因是我想要真正强调的是，测试本身并没有检查任何不容易被欺骗的东西。

根本没有办法区分行为良好的机器人和人类用户。你为什么要这么做？如果机器人代表用户访问网站，并以与用户相同的价格浏览，那么真正的区别是什么？我可以完全理解基于滥用访问的阻止用户，但是它倾向于在风车上试图限制任何形式的自动访问。你最终会阻止无辜的用户，智能机器人将无法被发现。

如果你试图通过它的阻止机制来抓一个有点过于热心的网站，那么请随时与我们保持联系。 Intoli的团队成员是编写与人类用户无法区分的表现良好的机器人的专家。我们还可以帮助您提供自定义数据验证和分析工作流程，帮助您从数据中提取价值。

> 原文链接: https://intoli.com/blog/making-chrome-headless-undetectable/


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](爬虫如何隐藏Headles-Chrome不被检测出来.ipynb)
> 统计咨询请加QQ 2726725926, 微信 mllncn,  SPSS统计咨询是收费的
> 微博上@mlln-cn可以向我免费题问
> 请记住我的网址: mlln.cn 或者 jupyter.cn
