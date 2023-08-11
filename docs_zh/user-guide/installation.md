# 安装MkDocs

一个详细的指南。

---

## 要求

MkDocs需要在您的系统上安装最新版本的 [Python] 和 Python 包管理器 [pip]。

您可以在命令行中检查您是否已经安装了它们：

```console
$ python --version
Python 3.8.2
$ pip --version
pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)
```

如果您已经安装了这些软件包，您可以跳到[安装MkDocs](#安装MkDocs)。

### 安装Python

使用您选择的软件包管理器安装[Python]，或从[python.org]下载适合您系统的安装程序并运行它。

> 注意：
> 如果您正在Windows上安装Python，请确保选中将Python添加到PATH的框（如果安装程序提供这样的选项）（默认情况下通常关闭）。
>
> ![将Python添加到PATH](../img/win-py-install.png)

### 安装pip

如果您使用的是最新版本的Python，Python 包管理器 [pip] 可能已经默认安装。但是，您可能需要将 pip 升级到最新版本：

```bash
pip install --upgrade pip
```

如果您需要第一次安装pip，请下载[get-pip.py]。然后运行以下命令安装它：

```bash
python get-pip.py
```

## 安装MkDocs

使用 pip 安装 `mkdocs` 包：

```bash
pip install mkdocs
```

现在您应该在您的系统上安装了 `mkdocs` 命令。运行 `mkdocs --version` 来检查一切是否正常。

```console
$ mkdocs --version
mkdocs, version 1.2.0 from /usr/local/lib/python3.8/site-packages/mkdocs (Python 3.8)
```

> 注意：
> 如果您希望为MkDocs安装man页，[click-man] 工具可以为您生成并安装它们。只需运行以下两个命令：
>
> ```bash
> pip install click-man
> click-man --target path/to/man/pages mkdocs
> ```
>
> 有关为什么man页不会被pip自动生成和安装的解释，请参见[click-man文档]。
<!-- -->
> 注意：
> 如果您使用的是Windows，上述某些命令可能无法立即起作用。
>
> 一个快速的解决方案可能是在每个Python命令前加上 `python -m`，像这样：
>
> ```bash
> python -m pip install mkdocs
> python -m mkdocs
> ```
>
> 对于更持久的解决方案，您可能需要编辑 `PATH` 环境变量以包括Python安装的 `Scripts` 目录。Python的最新版本包括一个脚本可为您执行此操作。导航到Python安装目录（例如 `C:\Python38\`），打开 `Tools`，然后是 `Scripts` 文件夹，并通过双击运行 `win_add2path.py` 文件。或者，您可以下载此[脚本][a2p]并运行它（`python win_add2path.py`）。

[Python]: https://www.python.org/
[python.org]: https://www.python.org/downloads/
[pip]: https://pip.readthedocs.io/en/stable/installing/
[get-pip.py]: https://bootstrap.pypa.io/get-pip.py
[click-man]: https://github.com/click-contrib/click-man
[click-man文档]: https://github.com/click-contrib/click-man#automatic-man-page-installation-with-setuptools-and-pip
[a2p]: https://github.com/python/cpython/blob/master/Tools/scripts/win_add2path.py