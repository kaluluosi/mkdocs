# MkDocs项目的贡献

这是一个关于向MkDocs项目进行贡献的介绍。

MkDocs项目欢迎并依赖来自开源社区中的开发者和用户的贡献。可以通过多种方式进行贡献，一些例子如下：

- 通过pull request提交代码补丁
- 改进文档
- 报告漏洞和审查补丁

有关可用通信渠道的信息，请参阅我们在GitHub存储库中的[README](https://github.com/mkdocs/mkdocs/blob/master/README.md)文件。

## 行为准则

MkDocs项目代码库、问题跟踪器、聊天室和邮件列表中的每个参与者都应遵循[PyPA行为准则]。

## 报告问题

请提供尽可能多的细节信息。让我们知道您的平台和MkDocs版本。如果问题是视觉上的（例如主题或设计问题），请添加屏幕截图；如果您遇到错误，请包含完整的错误信息和跟踪信息。

## 测试开发版本

如果您要安装和尝试最新版本的MkDocs开发版，可以使用以下命令完成此操作。如果您想提供新功能的反馈或要确认您遇到的错误是否在git主版本中修复，这可能非常有用。强烈建议您在[virtualenv]中执行此操作。

```bash
pip install https://github.com/mkdocs/mkdocs/archive/master.tar.gz
```

## 安装以进行开发

首先，您需要fork并克隆存储库。一旦您有了本地副本，请运行以下命令。强烈建议您在[virtualenv]中执行此操作。

```bash
pip install --editable .
```

这将以开发模式安装MkDocs，其将把“mkdocs”命令绑定到git存储库。

## 运行测试

为了运行测试，建议您使用[Hatch]。

通过运行命令`pip install hatch`使用[pip]安装Hatch。然后，在MkDocs存储库的根目录中运行命令“hatch run all”来运行MkDocs的测试套件。

它将尝试针对我们支持的所有Python版本运行测试。所以如果您缺少某些版本，请不要担心。剩下的
将由[GitHub Actions]在您提交pull request时进行验证。

## 格式化代码

MkDocs代码库中的Python代码使用[Black]和[Isort]进行格式化。您可以使用`hatch run style:format`按照这些工具的要求自动设置代码格式。

## 翻译主题

要将主题本地化为您喜欢的语言，请按照[翻译主题]指南操作。我们欢迎翻译Pull Requests!

## 提交pull request

如果您正在考虑向MkDocs进行大规模代码贡献，请优先提交问题以获取关于这个想法的早期反馈。

一旦您认为代码已准备好进行审查，请将其推送到您的fork并发送pull request。如果是新功能，则可能需要测试和文档才能接受更改。

### 提交对内置主题的更改

在使用`pip install mkdocs [i18n]`安装并启用国际化支持时，如果内置主题遵循 [Jinja的i18n扩展 ]将文本占位符用`{% trans %}`和`{% endtrans %}`标记包裹，则MkDocs允许支持将主题翻译成各种受欢迎语言（称为区域设置）。

每当在主题模板中添加、删除或更改可翻译的文本占位符时，主题的Portable Object Template（`pot`）文件需要通过运行`extract_messages`命令进行更新。要更新内置主题的`pot`文件，请运行以下命令：

```bash
pybabel extract --project=MkDocs --copyright-holder=MkDocs --msgid-bugs-address='https://github.com/mkdocs/mkdocs/issues' --no-wrap --version="$(hatch version)" --mapping-file mkdocs/themes/babel.cfg --output-file mkdocs/themes/mkdocs/messages.pot mkdocs/themes/mkdocs
pybabel extract --project=MkDocs --copyright-holder=MkDocs --msgid-bugs-address='https://github.com/mkdocs/mkdocs/issues' --no-wrap --version="$(hatch version)" --mapping-file mkdocs/themes/babel.cfg --output-file mkdocs/themes/readthedocs/messages.pot mkdocs/themes/readthedocs
```

更新后的`pot`文件应该随附于包含更新模板的PR中。更新的`pot`文件将允许翻译贡献者提出其首选语言所需的翻译。有关详细信息，请参阅[翻译主题]指南。

注意：
贡献者不需要在模板的更改中提供翻译。但是，他们需要包含一个已更新的' pot '文件，以便翻译人员准备就绪。

[virtualenv]:https://virtualenv.pypa.io/en/latest/user_guide.html
[pip]:https://pip.pypa.io/en/stable/
[Hatch]:https://hatch.pypa.io/
[GitHub Actions]:https://docs.github.com/actions
[PyPA行为准则]:https://www.pypa.io/en/latest/code-of-conduct/
[翻译主题]:../dev-guide/translations.md
[Jinja的i18n扩展]:https://jinja.palletsprojects.com/en/latest/extensions/#i18n-extension
[Black]:https://pypi.org/project/black/
[Isort]:https://pypi.org/project/isort/