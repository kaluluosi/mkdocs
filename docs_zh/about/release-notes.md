# 发布说明

---

## 升级

要将MkDocs升级到最新版本，请使用pip：

```bash
pip install -U mkdocs
```

您可以使用`mkdocs --version`确定当前已安装的版本：

```console
$ mkdocs --version
mkdocs, version 1.5.0 from /path/to/mkdocs (Python 3.10)
```

## 维护团队

MkDocs团队的当前和过去成员。

* [@tomchristie](https://github.com/tomchristie/)
* [@d0ugal](https://github.com/d0ugal/)
* [@waylan](https://github.com/waylan/)
* [@oprypin](https://github.com/oprypin/)
* [@ultrabug](https://github.com/ultrabug/)

## 版本 1.5.2 (2023-08-02)

* 修复错误（1.5.0中的回归）：恢复`--no-livereload`的功能。 (#3320)

* 修复错误（1.5.0中的回归）：新页面标题检测有时无法删除锚链接-修复该问题。 (#3325)

* 部分恢复1.5版本之前的API：`extra_javascript`项目将再次大多为字符串，仅在使用额外的“script”功能时才有时为`ExtraStringValue`（当然，plugins可以自由附加字符串到`config.extra_javascript`，但读取值时，他们必须仍然确保将其读取为`str(value)`，以防它是`ExtraScriptValue`类型。对于查询诸如`.type`之类的属性，您需要首先检查 `isinstance`。静态类型检查将引导您在其中。 (#3324)

请参见[提交日志](https://github.com/mkdocs/mkdocs/compare/1.5.1...1.5.2) 。

## 版本 1.5.1 (2023-07-28)

*   修复错误（1.5.0中的回归）：使得`ExtraScriptValue`可以看作是路径。这样一些插件仍可以工作，尽管有破坏性变化。

*   修复错误（1.5.0中的回归）：防止特殊设置中出现3个冲突文件（如`index.html`、`index.md`和`README.md`）时出错(#3314)。

请参见[提交日志](https://github.com/mkdocs/mkdocs/compare/1.5.0...1.5.1)。

## 版本 1.5.0 (2023-07-26)

### 新命令 `mkdocs get-deps`

该命令猜测一个MkDocs网站构建所需的Python依赖项。它只是打印需要安装的PyPI软件包。在终端中，它可以与安装命令直接组合使用，如下所示：

```bash
pip install $(mkdocs get-deps)
```

它的思想是在运行此命令后，您可以直接跟进`mkdocs build`，它几乎总是可以“正常工作”，而无需考虑哪些依赖项需要安装。

它的工作原理是扫描`mkdocs.yml`的`themes：`，`plugins：`和`markdown_extensions：`项，并基于一个已知项目列表（目录，请参见下文）进行反向查找。

当然，您可以使用带有这样的命令的“虚拟环境”。此外，请注意，对于需要稳定性的环境（例如CI），直接以这种方式安装## 版本 1.4.0 (2022-09-11)

### 大的变化

#### 支持配置定义预校验

现在可以使用配置定义和类型信息预先校验字典的数据类型。

请参阅 [文档 ](../dev-guide/plugins.md#examples-of-config-definitions) 中的示例。
 
#### 配置选项的其他更改

- `URL` 的默认值现在为 `None` 而不是 `''`。您仍然可以使用相同的方式检查它是否为真值-`if config.some_url:`（# 2962）
- `FilesystemObject` 不再是抽象的，可以直接使用，表示“文件或目录”并可选地检查存在（# 2938）

Bug 修复:

* 修正了 `SubConfig`、`ConfigItems`、`MarkdownExtensions` 在不同实例之间不泄漏值的问题（#2916, #2290）
* `SubConfig` 在没有堆栈跟踪的情况下抛出正确类型的验证错误（#2938）
* 修正了在 `config_options.Deprecated(moved_to)` 中的点分重定向 (#2963)

微调用于处理 `ConfigOption.default` 的逻辑 (#2938)

弃用的配置选项类: `ConfigItems` (#2983), `OptionallyRequired` (#2962), `RepoURL` (#2927)

### 主题更新

*“MkDocs”主题中警告的样式 (#2981):
    * 更新颜色以增加对比度
    * 将警告样式应用于 `<details>` 标签，以支持提供它的 Markdown 扩展([pymdownx.details](https://facelessuser.github.io/pymdown-extensions/extensions/details/)，[callouts](https://oprypin.github.io/markdown-callouts/#collapsible-blocks))

*内置主题现在还支持以下语言:
    * 俄语(#2976)
    * 土耳其语(土耳其)(#2946)
    * 乌克兰语(#2980)

### 未来的兼容性

* `extra_css:` 和 `extra_javascript:` 现在会发出警告，如果再它们中传递了反斜杠`\`。(#2930, #2984)
* 将 `DeprecationWarning` 作为 INFO 消息显示. (#2907)
    如果您使用的任何插件或扩展程序依赖于其他库的弃用功能，则有潜在的风险，在不久的将来可能会出现问题。插件开发人员应及时解决这些问题。
* 从 Python 3.10 开始避免依赖 `importlib_metadata`. (#2959)
* 不再支持 Python 3.6 (#2948)

#### 与公共 api 不兼容的更改

* `mkdocs.utils`:
    * `create_media_urls` 和 `normalize_url` 现在会发出警告，如果在其中传递反斜杠`\`。(#2930)
    * `is_markdown_file# MkDocs 1.0 发布说明

主要更新内容如下：

## 改变了历史的 URL 模式

以前，MkDocs 会神奇地返回一个主页的 URL，该 URL 是相对于当前页面的。现在已经去掉了这个“魔法”，应使用 [url] 模板过滤器：

```django
<a href="{{ nav.homepage.url|url }}">{{ config.site_name }}</a>
```

这个更改适用于所有导航项和页面，以及 `page.next_page` 和 `page.previous_page` 属性。目前，`extra_javascript` 和 `extra_css` 变量仍然像以前一样工作（没有 `url` 模板过滤器），但已经过时，应该使用相应的配置值（`config.extra_javascript` 和 `config.extra_css`）使用该过滤器代替。

```django
{% for path in config.extra_css %}
    <link href="{{ path|url }}" rel="stylesheet">
{% endfor %}
```

需要注意的是，导航现在可以包括指向外部站点的链接。显然，`base_url` 不应该添加到这些项中。但是，`url` 模板过滤器足够聪明，能够识别 URL 是否为绝对值，并且不会更改它。因此，所有导航项都可以传递到该过滤器，只有需要更改的项才会更改。

```django
{% for nav_item in nav %}
    <a href="{{ nav_item.url|url }}">{{ nav_item.title }}</a>
{% endfor %}
```

[base_url]: ../dev-guide/themes.md#base_url
[url]: ../dev-guide/themes.md#url

#### 基于路径的设置相对于配置文件（#543）

以前，各种配置选项中的任何相对路径都会相对于当前工作目录进行解析。它们现在相对于配置文件进行解析。由于文档一直鼓励从包含配置文件的目录（项目根目录）运行各种 MkDocs 命令，因此此更改不会影响大多数用户。但是，它将使实现自动化构建或以其他方式从位置运行命令变得更容易，而不是项目根目录。

只需使用 `-f/--config-file` 选项，指向配置文件即可：

```sh
mkdocs build --config-file /path/to/my/config/file.yml
```

与以前一样，如果没有指定文件，则 MkDocs 将在当前工作目录中查找名为 `mkdocs.yml` 的文件。

#### 添加对 YAML 元数据的支持（#1542）

以前，MkDocs 仅支持 MultiMarkdown 样式的元数据，该样式不识别不同的数据类型，且非常有限制。现在，MkDocs 还支持 Markdown 文档中的 YAML 样式元数据。MkDocs 依赖于限定符号（`---` 或 `...`）的存在或不存在来确定是否使用了 YAML 样式的元数据或 MultiMarkdown 样式的元数据。

以前，MkDocs 必须识别位于限制符之间的 MultiMarkdown 样式元数据。现在，如果检测到分隔符，但分隔符之间的内容不是有效的 YAML 元数据，则 MkDocs 不会尝试将内容解析为 MultiMarkdown 样式元数据。因此，MultiMarkdown 的样式元数据不得包括分隔符。详细信息请参见[MultiMarkdown 样式的元数据文档]。

在 0.17 版本之前，MkDocs 返回的所有元数据值都是字符串列表（即使单行也会返回一个字符串列表）。#### 新命令行界面

现在，MkDocs的命令行界面已经使用Python库[Click]进行了重写。这意味着MkDocs现在具有更易于使用的界面和更好的帮助输出。

这种变化在某种程度上是不兼容的，因为虽然未记录，但以前可以将任何配置选项传递给不同的命令。现在，只有一小部分配置选项可以传递给命令。要查看完整的命令和可用参数，请使用`mkdocs --help`和`mkdocs build --help`。

[Click]：https://click.palletsprojects.com/

#### 支持额外的HTML和XML文件

像[extra_javascript]和[extra_css]配置选项一样，在项目文档目录中添加了一个名为[extra_templates]的新选项。这将自动填充任何项目文档目录中的`.html`或`.xml`文件。

用户可以放置静态HTML和XML文件，它们将被复制，或者他们还可以使用Jinja2语法并利用[全局变量]。

默认情况下，MkDocs将使用这种方法创建站点地图。

[extra_javascript]：../user-guide/configuration.md#extra_javascript

[extra_css]：../user-guide/configuration.md#extra_css

[extra_templates]：../user-guide/configuration.md#extra_templates

[global variables]：../dev-guide/themes.md#global-context

### 版本0.13.0的其他更改和添加

* 添加支持[Markdown扩展配置选项]。(#435)
* MkDocs现在发行Python[Wheels]。(#486)
* 只在主页上包括构建日期和MkDocs版本。(#490)
* 为文档构建生成站点地图。(#436)
* 提供更清晰的方式在配置中定义嵌套页面。(#482)
* 为向模板传递任意变量添加了一个[额外的配置]选项。(#510)
* 在mkdocs serve中添加了`--no-livereload`，以获得更简单的开发服务器。(#511)
* 在所有主题中添加版权显示支持(#549)
* 支持在`mkdocs gh-deploy`中使用自定义提交消息(#516)
* Bugfix：修复了链接到同一目录中名为index.md的markdown文件中的媒体的问题(#535)
* Bugfix：修复了与Unicode文件名有关的错误(#542)。

[额外配置]：../user-guide/configuration.md#extra

[Markdown扩展配置选项]：../user-guide/configuration.md#markdown_extensions

[Wheels]：https://pythonwheels.com/

## 版本0.12.2（2015-04-22）

* Bugfix：修复了如果某些子标题丢失但其他子标题在页面配置中提供，则会出现错误的回归问题。 (#464)

## Version 0.12.1 (2015-04-14)

* Bugfix：修复了在某些浏览器上目录中的表无法点击的CSS bug。

## 版本0.12.0（2015-04-14）

* 在CLI输出中显示当前的MkDocs版本。 (#258)
* 在使用gh-deploy时检查CNAME文件。 (#285)
* 在所有主题上将主页添加回导航中。(#271)
* 为本地链接检查添加了一个严格的模式。(#279)
* 在所有主题中添加了Google Analytics支持。 (#333)
* 在ReadTheDocs和MkDocs主题输出中添加了构建日期和MkDocs版本。(#382)
* 在所有主题中标准化语法高亮，并添加缺少的语言。(#387)
* 添加了一个详细的标志`-v`，可以显示有关构建的更多详细信息。(#147)
* 在将文件部署到GitHub时添加了指定远程分支的选项。这使个人和repo站点都可以在GitHub上的页面上部署。（＃354）
* 向ReadTheDocs主题HTML添加了favicon支持。(#422)
* 当文件被编辑时自动刷新浏览器。(#163)
* Bugfix：永远不要在代码块中重新编写URL。(#240)
* Bugfix：将点文件从docs_dir拷贝到site_dir中时，请勿拷贝它们。 (#254)
* Bugfix：修复了在ReadTheDocs主题中渲染表格的问题。(#106)
* Bugfix：向所有引导主题添加底部填充。(#255)
* Bugfix：修复了嵌套Markdown页面和自动页面配置的一些问题。(#276)
* Bugfix：修复了GitHub企业中的URL解析错误。 (#284)
* Bugfix：如果mkdocs.yml完全为空，则不要发生错误。 (#288)
* Bugfix：修复了与相对URL和Markdown文件相关的一些问题。 (#292)
* Bugfix：如果找不到页面，不要停止构建，请继续进行其他页面的构建。 (#150)
* Bugfix：从页面标题中删除site_name，这需要手动添加。(#299)
* Bugfix：修复了目录在裁剪Markdown时存在的问题。 (#294)
* Bugfix：修复了BitBucket的主机名。 (#339)
* Bugfix：确保所有链接都以斜杠结尾。(#344)
* Bugfix：修复ReadTheDocs主题中的repo链接。(#365)
* Bugfix：包含本地jQuery以避免在离线使用MkDocs时出现问题。(#143)
* Bugfix：不允许`docs_dir`在`site_dir`中，反之亦然。(#384)
* Bugfix：从ReadTheDocs主题中删除行内CSS。 (#393)
* Bugfix：由于处理页面配置的顺序，修复了与子标题相关的一些问题。(#395)
* Bugfix：在没有主题的情况下实时重新加载时不要出错。(#373)
* Bugfix：解决Meta扩展在可能不存在时的一些问题。(#398)
* Bugfix：合理包装长的内联代码，否则它们将超出屏幕。 (#313)
* Bugfix：通过HTMLParser解析HTML来删除HTML解析正则表达式，并解决包含代码的标题问题。 (#367)
* Bugfix：修复滚动锚定引起的标题在导航下被隐藏的问题。 (#7)
* Bugfix：在bootswatch主题的HTML表格中添加更好的CSS类。(#295)
* Bugfix：使用`mkdocs serve`并传递特定的配置文件时不要出现错误。(#341)
* Bugfix：不要使用`mkdocs new`命令覆盖index.md文件。 (#412)
* Bugfix：从ReadTheDocs主题的代码中删除粗体和斜体。 (#411)
* Bugfix：在MkDocs主题中显示行内图像。 (#415)
* Bugfix：修复了在ReadTheDocs主题中无高亮的问题。(#319)
* Bugfix：使用`mkdocs build --clean`不要删除隐藏文件。 (#346)
* Bugfix：在Python> = 2.7中不要阻止Python-markdown的新版本。 (#376)
* Bugfix：修复了跨平台打开文件时的编码问题。 (#428)

## 版本0.11.1（2014-11-20）

* Bugfix：修复了在ReadTheDocs主题中代码高亮中出现缠绕问题的问题。 (#233)

## 版本0.11.0（2014-11-18）

* 如果当前主题支持，渲染404.html文件。 (#194)
* Bugfix：在MkDocs和ReadTheDocs主体中修复了长导航栏、表格渲染和代码高亮的问题。 (#225)
* Bugfix：修复了google_analytics代码的问题。(#219)
* Bugfix：从tar包中删除`__pycache__`。 (#196)
* Bugfix：修复了渲染带有锚点的markdown链接的问题。 (#197)
* Bugfix：不要将`prettyprint well` CSS类添加到所有HTML中，只在MkDocs主题中添加它。 (#183)
* Bugfix：在ReadTheDocs主题中显示章节标题。 (#175)
* Bugfix：在没有inotify的文件系统上使用轮询观察器使重建工作。 (#184)
* Bugfix：改进常见配置相关错误的错误输出。 (#176)

## 版本0.10.0（2014-10-29）

* 添加对Python 3.3和3.4的支持。(#103)
* 通过config设置`markdown_extensions`，可以配置Python-Markdown扩展。(#74)
* 添加`mkdocs json`命令，将您的呈现的文档作为json文件输出。 (#128)
* 添加`--clean`切换到`build`，`json`和`gh-deploy`命令以从输出目录中删除陈旧文件。 (#157)
* 支持多个主题目录，以允许替换单个模板而不是复制整个主题。 (#129)
* Bugfix：在ReadTheDocs主题中修复了`<ul>`的渲染。 (#171)
* Bugfix：在较小的显示器上改进了ReadTheDocs主题。 (#168)
* Bugfix：放宽需要的python软件包版本以避免冲突。 (#104)
* Bugfix：修复了带有某些配置的目录的渲染表。 (#146)
* Bugfix：修复了在子页面中嵌入图像的路径问题。 (#138)
* Bugfix：修复了`use_directory_urls`配置的行为。 (#63)
* Bugfix：在所有主题中支持`extra_javascript`和`extra_css`。 (#90)
* Bugfix：修复了在Windows下处理路径的问题。 (#121)
* Bugfix：修复了readthedocs主题中Menu生成的问题。 (#110)
* Bugfix：修复了在Windows下创建MkDocs命令的问题。 (#122)
* Bugfix：正确处理外部的`extra_javascript`和`extra_css`。 (#92)
* Bugfix：修复了favicon支持。 (#87)