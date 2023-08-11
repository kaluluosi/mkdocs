# MkDocs安装

一份详细的指南。

---

## 要求

MkDocs 要求最近版本的[Python]和 Python 包管理器[pip] 在你的系统上已经被安装。

你可以在命令行中检查是否已经安装了这些软件包：

```console
$ python --version
Python 3.8.2
$ pip --version
pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
```

如果你已经安装了这些软件包，可以跳到[安装MkDocs](#installing-mkdocs)。

### 安装Python

使用你喜欢的包管理器安装[Python]，或从[python.org]下载适合你系统的安装程序并运行它。

> 注意：
> 如果你正在Windows上安装Python，请确保选中将Python添加到你的PATH的框（如果安装程序提供这个选项）（通常默认关闭）。
>
> ![添加Python到PATH](../img/win-py-install.png)

### 安装pip

如果你使用的是最近版本的Python，则Python包管理器[pip]可能已经默认安装了。但是，你可能需要升级pip到最新版本：

```bash
pip install --upgrade pip
```

如果你是第一次安装pip，下载[get-pip.py]。 然后运行以下命令安装它：

```bash
python get-pip.py
```

## 安装MkDocs

使用pip安装`mkdocs`包：

```bash
pip install mkdocs
```

现在你应该在你的系统上安装了`mkdocs`命令。运行`mkdocs --version`检查是否一切正常工作。

```console
$ mkdocs --version
mkdocs, version 1.2.0 from /usr/local/lib/python3.8/site-packages/mkdocs (Python 3.8)
```

> 注意：
> 如果你想要安装MkDocs的man页，[click-man]工具可以为你生成和安装它们。只需要运行以下两个命令：
>
> ```bash
> pip install click-man
> click-man --target path/to/man/pages mkdocs
> ```
>
> 参见[click-man documentation] 解释为什么man页没有自动由pip生成和安装。

<!-- -->
> 注意：
> 如果你正在使用Windows，则上述某些命令可能无法直接使用。
>
> 一个快速的解决办法可能是在每个Python命令前加上`python -m`，像这样：
>
> ```bash
> python -m pip install mkdocs
> python -m mkdocs
> ```
>
> 对于一个更加永久的解决办法，你可能需要编辑你的`PATH`环境变量去包括Python安装的`Scripts`目录。最近版本的Python包括一个脚本帮助你完成这个任务。进入你的Python安装目录（例如`C:\Python38\`），打开`Tools`，然后是`Scripts`文件夹，并通过双击`win_add2path.py`文件运行。另外，你也可以下载[script][a2p]并运行它（`python win_add2path.py`）。

[Python]: https://www.python.org/
[python.org]: https://www.python.org/downloads/
[pip]: https://pip.readthedocs.io/en/stable/installing/
[get-pip.py]: https://bootstrap.pypa.io/get-pip.py
[click-man]: https://github.com/click-contrib/click-man
[click-man documentation]: https://github.com/click-contrib/click-man#automatic-man-page-installation-with-setuptools-and-pip
[a2p]: https://github.com/python/cpython/blob/master/Tools/scripts/win_add2path.py