---
title: 工具分享图片格式的数学公式识别一键转latex或mathjax
date: 2024-07-10 11:30:46
tags:
---


LaTeX-OCR 是一款开源的数学公式识别工具，支持多种输入格式，包括图片、PDF、Word 等，并且可以一键将识别结果转换为 LaTeX 或 MathJax 格式。我最喜欢用的是它提供的gui，可以一键启动截屏，快速识别公式，
并将识别结果渲染到剪贴板，然后就可以直接粘贴到 LaTeX 文档中。同时在界面可以看到识别结果，方便调试。

<!-- more -->

## 软件预览

<img src="latex-ocr.png">

## 安装

- 首先你得自己安装python，要求版本不能低于3.7.

- 然后如果你没有安装PyTorch ，你可以根据[这里](https://pytorch.org/get-started/locally/)安装：

- 使用如下命令安装：

    ```bash
    pip install "pix2tex[gui]"
    ```
## 使用教程

命令行键入`latexocr`就可以启动软件。

按下快捷键`Alt+S`可以启动截屏

然后就可以自动识别，识别结果会存到剪贴板，然后就可以直接粘贴到 LaTeX 文档中。

## 视频教程

跳转链接：https://github.com/lukas-blecher/LaTeX-OCR?tab=readme-ov-file#pix2tex---latex-ocr
