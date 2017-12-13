---
title: movipy NeedDownloadError缺少插件ffmped解决方法
date: 2017-11-08 14:24:25
tags: python
---

今天在开发psychopy的时候, 电脑新部署的环境, 运行psychopy时发现一个错误:

```python
File "/Users/macbook/python/main_video.py", line 3, in <module>
        from moviepy.editor import VideoFileClip
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/moviepy/editor.py", line 22, in <module>
        from .video.io.VideoFileClip import VideoFileClip
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/moviepy/video/io/VideoFileClip.py", line 3, in <module>
        from moviepy.video.VideoClip import VideoClip
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/moviepy/video/VideoClip.py", line 20, in <module>
        from .io.ffmpeg_writer import ffmpeg_write_image, ffmpeg_write_video
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/moviepy/video/io/ffmpeg_writer.py", line 19, in <module>
        from moviepy.config import get_setting
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/moviepy/config.py", line 38, in <module>
        FFMPEG_BINARY = get_exe()
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/imageio/plugins/ffmpeg.py", line 86, in get_exe
        raise NeedDownloadError('Need ffmpeg exe. '
    imageio.core.fetching.NeedDownloadError: Need ffmpeg exe. You can download it by calling:
      imageio.plugins.ffmpeg.download()
```

<!-- more -->

虽然它提示了你解决方法, 但是其实有风险, 下载过程很容易中断, 且中断以后它提示你已经下载完毕. 所以我建议还是手动下载, 方法如下:

- 确认你是windows系统, 因为我现在是在windows下开发的.

- 下载`ffmpeg.win32.exe`, 因为国外网站容易被墙, 所以我这里提供了自己的下载地址:{% asset_link ffmpeg.win32.exe ffmpeg.win32 %}

- 放到ffmpeg的appdata文件夹下, 我的文件夹路径是`C:\Users\wangluobu\AppData\Local\imageio\ffmpeg`, 你的路径很可能是只需要改一下系统用户名`wangluobu`

- 确保放进去的文件名一定改成`ffmpeg.win32.exe`, 因为程序里就是硬编码的这个文件名.

- 问题解决, 测试一下


