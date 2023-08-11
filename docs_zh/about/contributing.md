# MkDocs的贡献

一份贡献MkDocs项目的介绍。

MkDocs项目欢迎并且依赖于开源社区中开发者和用户的贡献。贡献可以通过很多方式进行，以下是一些例子：

- 代码补丁通过pull请求。
- 文档改进
- bug报告和补丁审查

有关可用通信渠道的信息，请参阅我们在GitHub存储库中的[README](https://github.com/mkdocs/mkdocs/blob/master/README.md)文件。

## 行为准则

每个与MkDocs项目的代码库、问题跟踪器、聊天室和邮件列表进行交互的个人都应遵循[PyPA行为准则]。

## 报告问题

请提供尽可能多的细节。告诉我们您的平台和MkDocs版本。如果问题可视化（例如主题或设计问题），请添加截图，如果出现错误，请包括完整的错误和堆栈跟踪。

## 测试开发版本

如果您想安装并尝试最新的MkDocs开发版本，可以使用以下命令。如果您想为新功能提供反馈意见或者想确认您遇到的某个bug是否已经在git master中被修复，那么这可能是有用的。强烈建议您在[virtualenv]内执行此操作。

```bash
pip install https://github.com/mkdocs/mkdocs/archive/master.tar.gz
```

## 开发时的安装

首先，您需要fork并clone存储库。完成本地副本后，运行以下命令。强烈建议您在[virtualenv]中执行此操作。

```bash
pip install --editable .
```

此命令将以开发模式安装MkDocs，将`mkdocs`命令绑定到git存储库。

## 运行测试

请使用[Hatch]运行测试。

通过运行命令`pip install hatch`安装Hatch。然后就可以在MkDocs存储库的根目录下运行`hatch run all`命令来运行MkDocs的测试套件。

它将尝试针对我们支持的所有Python版本运行测试。因此，如果您缺少某些内容，则不用担心。剩下的将在您提交pull请求时由[GitHub Actions]进行验证。

## 格式化代码

MkDocs的代码库中的Python代码是使用[Black]和[Isort]格式化的。您可以使用`hatch run style:format`根据这些工具自动格式化代码。

## 翻译主题

要将一个主题本地化到您喜欢的语言，请按照[翻译主题]指南。我们欢迎翻译Pull请求！

## 提交Pull请求

如果您正在考虑向MkDocs贡献大量的代码，请首先打开一个问题，以便获得关于这个想法的早期反馈。

一旦您认为代码已准备好进行审查，将其推送到您的fork并发送pull请求。如果是新功能，则大多数情况下需要测试和文档才能接受更改。

### 提交内建主题的更改

当使用`i18n`支持（`pip install mkdocs[i18n]`）安装时，MkDocs允许主题支持被翻译成各种语言（称为语言环境），如果它们尊重[Jinja的i18n扩展]，则可以使用“{% trans %}”和“{% endtrans %}”标记将文本占位符包装起来。

每当在主题模板中添加、删除或更改可翻译的文本占位符时，主题的Portable Object Template（pot）文件需要通过运行`extract_messages`命令来更新。要为两个内置主题更新`pot`文件，请运行以下命令：

```bash
pybabel extract --project=MkDocs --copyright-holder=MkDocs --msgid-bugs-address='https://github.com/mkdocs/mkdocs/issues' --no-wrap --version="$(hatch version)" --mapping-file mkdocs/themes/babel.cfg --output-file mkdocs/themes/mkdocs/messages.pot mkdocs/themes/mkdocs
pybabel extract --project=MkDocs --copyright-holder=MkDocs --msgid-bugs-address='https://github.com/mkdocs/mkdocs/issues' --no-wrap --version="$(hatch version)" --mapping-file mkdocs/themes/babel.cfg --output-file mkdocs/themes/readthedocs/messages.pot mkdocs/themes/readthedocs
```

更新后的`pot`文件应包含在具有更新模板的PR中。更新的pot文件将允许翻译员提出所需的翻译语言。详见[翻译主题]指南。

注意:
不要求贡献者在更改主题模板时提供翻译。但是，贡献者需要包括更新的`pot`文件，以便一切都准备好翻译员做他们的工作。

[virtualenv]: https://virtualenv.pypa.io/en/latest/user_guide.html
[pip]: https://pip.pypa.io/en/stable/
[Hatch]: https://hatch.pypa.io/
[GitHub Actions]: https://docs.github.com/actions
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
[翻译主题]: ../dev-guide/translations.md
[Jinja的i18n扩展]: https://jinja.palletsprojects.com/en/latest/extensions/#i18n-extension
[Black]: https://pypi.org/project/black/
[Isort]: https://pypi.org/project/isort/