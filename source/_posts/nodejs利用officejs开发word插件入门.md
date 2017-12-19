---
title: nodejs利用officejs开发word插件入门
date: 2017-12-19
tags: [officejs, nodejs]
author: mlln.cn
---

officejs是微软公司推出的开发office插件的javascript框架。下面我过通过例子来实践一下如何开始用nodejs来开发word插件。

### 安装nodejs

此处略去一百字。

### 安装yo generator-office 

```
npm install –g yo generator-office 
```

参数`-g`表示全局安装

### 新建一个project文件夹

此处略去n个字

### 新建project

- 打开cmd
- cd到你所新建的project文件夹
- 运行命令`yo office`
- 按照提示输入信息， 我的部分选择是， 其他不重要你自己选：
    - The supported Office application: word
    - Use TypeScript: Yes
    - Choose framework: react
- 完成以后的目录结构如下图

{% asset_img 目录结构.jpg %}

### https证书安装

office插件必须使用https协议与服务器通讯， 所以我们需要事先安装一个证书。`yo office` 命令已经为你生成了一个开发环境的证书， 你直接安装它即可。

- 在certs目录下
- 双击`ca.crt`文件
- 点击`安装证书`
- 存储位置选择`本地计算机`
- 将所有证书都放入下列存储位置-个人
- 点击`完成`

### 启动服务器

```
npm start
```

现在你打开浏览器， 输入网址`https://localhost:3000/`就能看到初始化的页面了。

### 安装插件

一个初始化的插件完成以后，你需要将其安装到word里。这是一个比较繁琐的过程下面我来截图介绍一下。

#### 创建共享文件夹

你需要创建一个共享文件夹用于存放manifest文件， office会从该共享文件夹查找manifest。

- 右键单击你需要共享的文件夹， 选择属性
- 切换到共享标签
- 点击共享按钮
- 把文件夹共享给自己

参考下图：

{% asset_img 创建共享文件夹.jpg %}

#### 复制manifest文件

你可以在你的工程目录下找到这个manifest文件， 这是命令`yo office`替你创建的一个文件。我的文件名是`my-office-add-in-manifest.xml`，这个文件的名字跟你设置的addin的名称一样。

这个文件的内容是(关于如何写manifest文件， 我会在接下来的文章中介绍):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<OfficeApp
          xmlns="http://schemas.microsoft.com/office/appforoffice/1.1"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:bt="http://schemas.microsoft.com/office/officeappbasictypes/1.0"
          xmlns:ov="http://schemas.microsoft.com/office/taskpaneappversionoverrides"
          xsi:type="TaskPaneApp">

  <!-- Begin Basic Settings: Add-in metadata, used for all versions of Office unless override provided. -->

  <!-- IMPORTANT! Id must be unique for your add-in, if you reuse this manifest ensure that you change this id to a new GUID. -->
  <Id>09a337df-4cbf-437c-8665-6c0ed4189344</Id>

  <!--Version. Updates from the store only get triggered if there is a version change. -->
  <Version>1.0.0.0</Version>
  <ProviderName>[Provider name]</ProviderName>
  <DefaultLocale>en-US</DefaultLocale>
  <!-- The display name of your add-in. Used on the store and various places of the Office UI such as the add-ins dialog. -->
  <DisplayName DefaultValue="My Office Add-in" />
  <Description DefaultValue="[Document Add-in description]"/>

  <!-- Icon for your add-in. Used on installation screens and the add-ins dialog. -->
  <IconUrl DefaultValue="https://localhost:3000/assets/icon-32.png" />
  <HighResolutionIconUrl DefaultValue="https://localhost:3000/assets/icon-80.png"/>

  <!--If you plan to submit this add-in to the Office Store, uncomment the SupportUrl element below-->
  <!--<SupportUrl DefaultValue="[Insert the URL of a page that provides support information for the app]">-->

  <!-- Domains that will be allowed when navigating. For example, if you use ShowTaskpane and then have an href link, navigation will only be allowed if the domain is on this list. -->
  <AppDomains>
    <AppDomain>AppDomain1</AppDomain>
    <AppDomain>AppDomain2</AppDomain>
    <AppDomain>AppDomain3</AppDomain>
  </AppDomains>
  <!--End Basic Settings. -->

  <!--Begin TaskPane Mode integration. This section is used if there are no VersionOverrides or if the Office client version does not support add-in commands. -->
  <Hosts>
    <Host Name="Document" />
  </Hosts>
  <DefaultSettings>
    <SourceLocation DefaultValue="https://localhost:3000/index.html" />
  </DefaultSettings>
  <!-- End TaskPane Mode integration.  -->

  <Permissions>ReadWriteDocument</Permissions>

  <!-- Begin Add-in Commands Mode integration. -->
  <VersionOverrides xmlns="http://schemas.microsoft.com/office/taskpaneappversionoverrides" xsi:type="VersionOverridesV1_0">

    <!-- The Hosts node is required. -->
    <Hosts>
      <!-- Each host can have a different set of commands. -->
      <!-- Excel host is Workbook, Word host is Document, and PowerPoint host is Presentation. -->
      <!-- Make sure the hosts you override match the hosts declared in the top section of the manifest. -->
      <Host xsi:type="Document">
        <!-- Form factor. Currently only DesktopFormFactor is supported. -->
        <DesktopFormFactor>
          <!--"This code enables a customizable message to be displayed when the add-in is loaded successfully upon individual install."-->
          <GetStarted>
            <!-- Title of the Getting Started callout. resid points to a ShortString resource -->
            <Title resid="Contoso.GetStarted.Title"/>

            <!-- Description of the Getting Started callout. resid points to a LongString resource -->
            <Description resid="Contoso.GetStarted.Description"/>

            <!-- Point to a url resource which details how the add-in should be used. -->
            <LearnMoreUrl resid="Contoso.GetStarted.LearnMoreUrl"/>
          </GetStarted>
          <!-- Function file is a HTML page that includes the JavaScript where functions for ExecuteAction will be called.
            Think of the FunctionFile as the code behind ExecuteFunction. -->
          <FunctionFile resid="Contoso.DesktopFunctionFile.Url" />

          <!-- PrimaryCommandSurface is the main Office Ribbon. -->
          <ExtensionPoint xsi:type="PrimaryCommandSurface">
            <!-- Use OfficeTab to extend an existing Tab. Use CustomTab to create a new tab. -->
            <OfficeTab id="TabHome">
              <!-- Ensure you provide a unique id for the group. Recommendation for any IDs is to namespace using your company name. -->
              <Group id="Contoso.Group1">
                <!-- Label for your group. resid must point to a ShortString resource. -->
                <Label resid="Contoso.Group1Label" />
                <!-- Icons. Required sizes 16,32,80, optional 20, 24, 40, 48, 64. Strongly recommended to provide all sizes for great UX. -->
                <!-- Use PNG icons. All URLs on the resources section must use HTTPS. -->
                <Icon>
                  <bt:Image size="16" resid="Contoso.tpicon_16x16" />
                  <bt:Image size="32" resid="Contoso.tpicon_32x32" />
                  <bt:Image size="80" resid="Contoso.tpicon_80x80" />
                </Icon>

                <!-- Control. It can be of type "Button" or "Menu". -->
                <Control xsi:type="Button" id="Contoso.TaskpaneButton">
                  <Label resid="Contoso.TaskpaneButton.Label" />
                  <Supertip>
                    <!-- ToolTip title. resid must point to a ShortString resource. -->
                    <Title resid="Contoso.TaskpaneButton.Label" />
                    <!-- ToolTip description. resid must point to a LongString resource. -->
                    <Description resid="Contoso.TaskpaneButton.Tooltip" />
                  </Supertip>
                  <Icon>
                    <bt:Image size="16" resid="Contoso.tpicon_16x16" />
                    <bt:Image size="32" resid="Contoso.tpicon_32x32" />
                    <bt:Image size="80" resid="Contoso.tpicon_80x80" />
                  </Icon>

                  <!-- This is what happens when the command is triggered (E.g. click on the Ribbon). Supported actions are ExecuteFunction or ShowTaskpane. -->
                  <Action xsi:type="ShowTaskpane">
                    <TaskpaneId>ButtonId1</TaskpaneId>
                    <!-- Provide a url resource id for the location that will be displayed on the task pane. -->
                    <SourceLocation resid="Contoso.Taskpane.Url" />
                  </Action>
                </Control>
              </Group>
            </OfficeTab>
          </ExtensionPoint>
        </DesktopFormFactor>
      </Host>
    </Hosts>

    <!-- You can use resources across hosts and form factors. -->
    <Resources>
      <bt:Images>
        <bt:Image id="Contoso.tpicon_16x16" DefaultValue="https://localhost:3000/assets/icon-16.png" />
        <bt:Image id="Contoso.tpicon_32x32" DefaultValue="https://localhost:3000/assets/icon-32.png" />
        <bt:Image id="Contoso.tpicon_80x80" DefaultValue="https://localhost:3000/assets/icon-80.png" />
      </bt:Images>
      <bt:Urls>
        <bt:Url id="Contoso.Taskpane.Url" DefaultValue="https://localhost:3000/index.html" />
        <bt:Url id="Contoso.GetStarted.LearnMoreUrl" DefaultValue="https://go.microsoft.com/fwlink/?LinkId=276812" />
        <bt:Url id="Contoso.DesktopFunctionFile.Url" DefaultValue="https://localhost:3000/function-file/function-file.html" />
      </bt:Urls>
      <!-- ShortStrings max characters==125. -->
      <bt:ShortStrings>
        <bt:String id="Contoso.TaskpaneButton.Label" DefaultValue="Show Taskpane" />
        <bt:String id="Contoso.Group1Label" DefaultValue="Commands Group" />
        <bt:String id="Contoso.GetStarted.Title" DefaultValue="Get started with your sample add-in!" />
      </bt:ShortStrings>
      <!-- LongStrings max characters==250. -->
      <bt:LongStrings>
        <bt:String id="Contoso.TaskpaneButton.Tooltip" DefaultValue="Click to Show a Taskpane" />
        <bt:String id="Contoso.GetStarted.Description" DefaultValue="Your sample add-in loaded succesfully. Go to the HOME tab and click the 'Show Taskpane' button to get started." />
      </bt:LongStrings>
    </Resources>
  </VersionOverrides>
  <!-- End Add-in Commands Mode integration. -->

</OfficeApp>

```

#### 设置加载目录

这一步是要让office知道去哪里找manifest文件。

- 打开word软件
- 依次打`开信任中心`-`受信任的加载目录`-将你的共享文件夹添加到这个列表
- 点击`确定`

参考下图：

{% asset_img 添加共享位置.jpg %}


#### 添加加载项

现在你就可以在word的如下位置找到你所创建的插件了。

{% asset_img 添加加载项.jpg %}

#### 查看加载项

你会在如下位置看到你的插件启动按钮。

{% asset_img 展示效果.jpg %}

打开你的加载项看看效果

{% asset_img 加载项打开.jpg %}




