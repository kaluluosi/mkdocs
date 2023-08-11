# 发行说明

---

## 升级

要升级到最新版的MkDocs，请使用pip：

```bash
pip install -U mkdocs
```

您可以使用`mkdocs --version`确定您当前安装的版本：

```console
$ mkdocs --version
mkdocs, version 1.5.0 from /path/to/mkdocs (Python 3.10)
```

## 维护团队

MkDocs团队的现任和过去成员。

* [@tomchristie](https://github.com/tomchristie/)
* [@d0ugal](https://github.com/d0ugal/)
* [@waylan](https://github.com/waylan/)
* [@oprypin](https://github.com/oprypin/)
* [@ultrabug](https://github.com/ultrabug/)


## 1.5.2版本（2023-08-02）

* Bugfix（1.5.0中的回归）：恢复'--no-livereload'功能。(#3320)

* Bugfix(1.5.0中的回归)：新的页面标题检测有时会无法删除锚链接-修复。(#3325)

* 部分恢复1.5版本API：`extra_javascript`项将再次大多数是字符串，只有在使用额外的`script`功能时才是`ExtraStringValue`（此时插件应自由追加字符到`config.extra_javascript`，但在读取值时，它们仍然必须确保将其读为`str(value)`，以防它是一个`ExtraScriptValue`项目。查询属性（如`.type`）之前，您需要首先检查`isinstance`。静态类型检查将指导您。(#3324)
 
有关提交记录，请参见[提交记录](https://github.com/mkdocs/mkdocs/compare/1.5.1...1.5.2)。


## 版本1.5.1（2023-07-28）

* Bugfix（1.5.0中的回归）：即使使用了破坏性的更改，也可以将`ExtraScriptValue`视为路径。这使得某些插件仍然可以正常工作。

* Bugfix（1.5.0中的回归）：对于具有3个冲突文件的特殊设置（例如`index.html`，`index.md`和`README.md`），防止出现错误。(#3314)

请参见[提交记录](https://github.com/mkdocs/mkdocs/compare/1.5.0...1.5.1)。


## 版本1.5.0（2023-07-26）

### 新命令`mkdocs get-deps`

此命令猜测MkDocs网站所需的Python依赖项以进行构建。它会打印需要安装的PyPI包。您在终端中可以与安装命令直接组合使用，如下所示：

```bash
pip install $(mkdocs get-deps)
```

它的想法是，在运行此命令后，您可以直接跟进“mkdocs build”，而不需要考虑安装哪些依赖项。

它的工作方式是通过扫描`mkdocs.yml`以查找`themes:`，`plugins:`和`markdown_extensions:`项，并基于已知项目的一个大型列表进行反向查找（目录，请参见下文）。

当然，您可以使用一个“virtualenv”与这样的命令。还要注意的是，对于需要稳定性的环境（例如CI），直接以这种方式安装依赖项不是非常可靠的方法，因为它排除了依赖项固定。

该命令允许覆盖使用的配置文件（而不是当前目录中的`mkdocs.yml`）以及使用的项目目录。请参见[`mk## 版本 1.4.0 (2022-12-17)

### 添加的功能

#### 为配置文件添加 JSON Schema 验证

MkDocs 现在支持对配置文件使用 JSON Schema 进行验证。这可以通过一个新的 `config_schemas` 选项来进行配置。有关如何设置选项和编写验证模式的更多信息，请参见[文档页面](../user-guide/configuration.md#config-schemas)。

这个功能目前仅支持对以下类型的验证：

* 字符串
* 布尔
* 整数
* 浮点数
* 对象
* 数组

但不支持自定义验证器或嵌套。

有关如何编写验证模式的更多信息，请参见 [JSON Schema 文档](https://json-schema.org/).

#### 新的 `SubConfig` 类型

新添加了一个名为 `SubConfig` 的类型，它允许在嵌套配置中进行严格的值验证。具体看 [example](../dev-guide/plugins.md#examples-of-config-definitions).

#### 配置选项的其他更改

现在`URL`的默认值是`None`而不是`''`，这仍然可以通过 `if config.some_url` 等方式检查真实性 (#2962)。

`FilesystemObject` 不再是抽象类型，可以直接使用，表示“文件或目录” ，可选的存在性检查 (#2938) 。

Bug 修正:
 - 修复 `SubConfig`, `ConfigItems`, `MarkdownExtensions` 将值泄漏到不同的实例中 (#2916, #2290)。
 - `SubConfig` 抛出正确类型的验证错误，而不是跟踪调用栈 (#2938)。
 - 修复 `config_options.Deprecated(moved_to)` 中的点分隔重定向 (#2963)。

调整处理`ConfigOption.default`的方法(#2938) 。

弃用的配置选项类：`ConfigItems` (#2983), `OptionallyRequired` (#2962), `RepoURL` (#2927) 。

### 主题更新

* "MkDocs" 主题的注意事项样式 (#2981):
    * 更新颜色以增加对比度
    * 还将注意事项样式应用到 `<details>` 标记，以支持提供它的 Markdown 扩展（ [pymdownx.details](https://facelessuser.github.io/pymdown-extensions/extensions/details/), [callouts](https://oprypin.github.io/markdown-callouts/#collapsible-blocks)）

* 内置主题现在还支持以下语言：
    * 俄语 (#2976)
    * 土耳其语（土耳其）(#2946)
    * 乌克兰语 (#2980)

### 将来的兼容性

*`extra_css:` 和 `extra_javascript:` 如传递了反斜线`\`，将会发出警告 (#2930, #2984)。

* 将 `DeprecationWarning` 作为 INFO 消息显示。(#2907)
  如果你使用的任何插件或扩展依赖于已弃用的库的功能，则它有可能在不久的将来出现故障。插件开发人员应及时解决这些问题。

# MkDocs更新内容

## 版本1.0(2019-05-19)

### 重大改变

#### Navigation items和pages中的URLs现在应该使用url模板过滤器

以前MkDocs会神奇地返回一个相对于当前页面的主页URL。现在取消了这种“神奇”的操作，应该使用[url]模板过滤器：

```django
<a href = "{{ nav.homepage.url | url }}">{{ config.site_name }}</a>
```

此更改适用于任何导航项目和页面，以及`page.next_page` 和 `page.previous_page`属性。目前， `extra_javascript` 和 `extra_css`变量仍然像以前一样工作(不用`url`模板过滤器），但已弃用，并且对应的配置值(`config.extra_javascript` 和 `config.extra_css`）应该使用此过滤器。

```django
{% for path in config.extra_css %}
    <link href="{{ path|url }}" rel="stylesheet">
{% endfor %}
```

请注意，导航现在可以包括指向外部网站的链接。显然，不应该对这些项附加`base_url`。但是，`url`模板过滤器足够聪明，可以识别URL不是相对的并且不改变它。因此，所有导航项都可以传递给过滤器，并且只有需要的那些项会被更改。

#### 基于路径的配置现在相对于配置文件而不是当前工作目录。

以前，各种配置选项中的所有相对路径都是相对于当前工作目录解析的。现在，它们相对于配置文件进行解析。由于文档一直鼓励从包含配置文件的目录(项目根目录)运行各种MkDocs命令，所以这个更改不会影响大多数用户。然而，这将使实现自动化构建或以其他方式从不同的位置运行命令变得更加容易。

只需使用`-f/--config-file`选项并将其指向配置文件：

```sh
mkdocs build --config-file /path/to/my/config/file.yml
```

与以前一样，如果没有指定文件，则MkDocs会在当前工作目录中查找名为`mkdocs.yml`的文件。

#### 添加对YAML元数据的支持

以前，MkDocs只支持MultiMarkdown风格的元数据，这种元数据无法识别不同的数据类型，而且相当有限。现在，MkDocs还支持Markdown文档中的YAML风格元数据。MkDocs依靠定界符(`---`或`...`)的存在或不存在来确定正在使用YAML风格元数据还是MultiMarkdown风格元数据。

以前，MkDocs会在定界符之间识别MultiMarkdown风格的元数据。现在，如果检测到定界符，但定界符之间的内容不是有效的YAML元数据，MkDocs将不会尝试将内容解析为MultiMarkdown风格的元数据。因此，MultiMarkdown的风格元数据不能包括定界符。详情请参见[MultiMarkdown风格元数据文档]。

在版本0.17之前，MkDocs将所有元数据值作为字符串列表返回(即使单行也会返回一个字符串列表)。在0.17版本中，该行为已更改为将每个值作为单个字符串返回(多行将被连接)，这可能对一些用户有所限制(请参见#1471)。然而，YAML风格元数据支持“安全”的YAML数据类型的全部范围。因此，建议任何复杂的元数据都使用YAML风格(详情请参见[YAML风格元数据文档]）。事实### 版本0.13.0

#### 全新的命令行交互界面

MkDocs的命令行接口已被重新编写，使用了Python库[Click]。这意味着MkDocs现在有了一个更易于使用且输出更好的帮助文档的界面。

这个改变部分不再向后兼容。尽管以前没有被记录，但可以将任何配置选项传递给不同的命令，现在只有一个较小的子集可以被传递到命令中。使用`mkdocs --help`和`mkdocs build --help`，以查看完整的命令和可用参数。

[Click]: https://click.palletsprojects.com/

#### 支持额外的HTML和XML文件

像[extra_javascript]和 [extra_css]配置选项一样，现在添加了一个名为[extra_templates]的新选项。这将自动填充项目文档目录中的任何`.html`或`.xml`文件。

用户可以放置静态HTML和XML文件，并将它们复制过去，或者还可以使用Jinja2语法，并利用[全局变量]。

默认情况下，MkDocs将使用这种方法创建文档的站点地图。

[extra_javascript]: ../user-guide/configuration.md#extra_javascript
[extra_css]: ../user-guide/configuration.md#extra_css
[extra_templates]: ../user-guide/configuration.md#extra_templates
[global variables]: ../dev-guide/themes.md#global-context

### 版本0.13.0中的其他变更和添加

* 添加对[Markdown扩展配置选项]的支持。(#435)
* MkDocs现在提供Python [wheels]。(#486)
* 仅在主页上包括构建日期和MkDocs版本。(#490)
* 为文档生成站点地图。(#436)
* 在配置中添加一个更清晰的定义嵌套页面的方法。(#482)
* 添加额外的配置选项，用于将任意变量传递给模板。(#510)
* 为`mkdocs serve`添加`--no-livereload`选项，以获得简单的开发服务器。(#511)
* 将版权信息适配到所有主题中。(#549)
* 支持自定义提交信息的`mkdocs gh-deploy`。(#516)
* 已解决问题：修复了与名为index.md的markdown文件位于同一目录中的媒体链接问题(#535)
* 已解决问题：修复了Unicode文件名的错误(#542)

[extra config]: ../user-guide/configuration.md#extra
[Markdown extension configuration options]: ../user-guide/configuration.md#markdown_extensions
[wheels]: https://pythonwheels.com/

## 版本0.12.2（2015-04-22）

* 已解决问题：修复了如果某些子标题丢失但其他子标题在页面配置中提供，则会出现错误的回归。(#464)

## 版本0.12.1（2015-04-14）

* 已解决问题：修复了在某些浏览器上目录中的表不可点击的CSS错误。

## 版本0.12.0（2015-04-14）

* 在CLI输出中显示当前的MkDocs版本。(#258)
* 在使用gh-deploy时检查CNAME文件。(#285)
* 在所有主题的导航栏上添加主页。(#271)
* 添加本地链接检查的严格模式。(#279)
* 为所有主题添加Google Analytics支持。(#333)
* 在ReadTheDocs和MkDocs主题输出中添加构建日期和MkDocs版本。(#382)
* 在所有主题中标准化代码高亮并添加缺少的语言。(#387)
* 添加了一个verbose标志(-v)，以显示更多与构建有关的详细信息。(#147)
* 添加了在部署到GitHub时指定远程分支的选项。这允许在个人和repo网站上部署到GitHub Pages。(#354)
* 在ReadTheDocs主题HTML中添加了favicon支持。(#422)
* 在编辑文件时自动刷新浏览器。(#163)
* 已解决问题：不要在代码块中重写网址。(#240)
* 已解决问题：不要在从“docs_dir”复制媒体时复制点文件。(#254)
* 已解决问题：修复了ReadTheDocs主题中表的呈现问题。(#106)
* 已解决问题：为所有bootstrap主题添加底部填充。(#255)
* 已解决问题：修复了Markdown页面嵌套和自动页面配置的问题。(#276)
* 已解决问题：修复了GitHub企业版URL解析错误的问题。(#284)
* 已解决问题：如果mkdocs.yml完全为空，则不会发生错误。(#288)
* 已解决问题：修复了URL和Markdown文件问题的一些相关问题。(#292)
* 已解决问题：即使找不到页面，也不要停止构建，继续处理其他页面。(#150)
* 已解决问题：从页面标题中删除site_name，这需要手动添加。(#299)
* 已解决问题：修复了内容目录截断Markdown时的问题。(#294)
* 已解决问题：修复了BitBucket的主机名。(#339)
* 已解决问题：确保所有链接都以斜杠结尾。(#344)
* 已解决问题：修复了ReadTheDocs主题中的repo链接。(#365)
* 已解决问题：包含本地jQuery以避免在离线使用MkDocs时出现问题。(#143)
* 已解决问题：不允许docs_dir在site_dir或反之亦然。(#384)
* 已解决问题：在ReadTheDocs主题中删除内联CSS。(#393)
* 已解决问题：因处理属性的顺序而导致的子标题问题。(#395)
* 已解决问题：当主题不存在时，在实时重新加载期间不要出现错误。(#373)
* 已解决问题：解决Meta扩展不一定存在时的问题。(#398)
* 已解决问题：换行较长的内联代码，否则它们将跑出屏幕。(#313)
* 已解决问题：删除HTML分析正则表达式并使用HTMLParser解析以解决包含代码的标题问题。(#367)
* 已解决问题：修复了将锚点滚动到导航栏下而导致标题被隐藏的问题。(#7)
* 已解决问题：在bootswatch主题的HTML表中添加更好的CSS类。(#295)
* 已解决问题：使用特定的配置文件与`mkdocs serve`一起使用时不会出错。(#341)
* 已解决问题：不要使用`mkdocs new`命令覆盖index.md文件。(#412)
* 已解决问题：从ReadTheDocs主题中删除代码中的粗体和斜体。(#411)
* 已解决问题：在MkDocs主题中显示图像内联。(#415)
* 已解决问题：修复了ReadTheDocs主题中no-highlight的问题。(#319)
* 已解决问题：使用`mkdocs build -clean`时不要删除隐藏文件。(#346)
* 已解决问题：不要阻止Python>= 2.7上较新版本的Python-markdown。(#376)
* 已解决问题：在跨平台打开文件时解决编码问题。(#428)

## 版本0.11.1（2014-11-20）

* 已解决问题：修复了ReadTheDocs主题中代码高亮的CSS换行问题。(#233)

## 版本0.11.0（2014-11-18）

* 如果当前主题存在404.html文件，则渲染该文件。（#194）
* 已解决问题：在MkDocs和ReadTheDocs主题中修复了长的导航栏，表格渲染和代码高亮的问题。(#225)
* 已解决问题：修复了google_analytics代码的问题。(#219)
* 已解决问题：从软件包tar中删除`__pycache__`文件。(#196)
* 已解决问题：修复了指向当前页面锚点的Markdown链接的问题。(#197)
* 已解决问题：只将`prettyprint well` CSS类添加到所有HTML中，而不是添加到所有主题中。(#183)
* 已解决问题：在ReadTheDocs主题中显示章节标题。(#175)
* 在watchdog中使用轮询观察程序，以便在没有inotify的文件系统上实现重建。(#184)
* 改善了一般配置相关错误的错误输出。(#176)

## 版本0.10.0（2014-10-29）

* 增加了对Python 3.3和3.4的支持。(#103)
* 使用配置设置“markdown_extensions”进行可配置的Python-Markdown扩展。(#74)
* 添加了`mkdocs json`命令，以将呈现的文档输出为json文件。(#128)
* 为构建、json和gh-deploy命令添加了`--clean`开关，以从输出目录中删除Stale文件。(#157)
* 支持多个主题目录，以允许替换单个模板而不是复制全部主题。(#129)
* 已解决问题：修复了在readthedocs主题中的’<ul>‘呈现问题。(#171)
* 已解决问题：在较小的显示器上改善readthedocs主题。(＃168)
* 已解决问题：放松了必需的Python软件包版本以避免冲突。(#104)
* 已解决问题：修复了使用某些配置时呈现目录的问题。(#146)
* 已解决问题：修复了子页面中嵌入图像的路径问题。(#138)
* 已解决问题：修复了`use_directory_urls`配置行为。(#63)
* 已解决问题：在所有主题中支持`extra_javascript`和`extra_css’。(#90)
* 已解决问题：修复了处理Windows下的路径的问题。(#121)
* 已解决问题：修复了在readthedocs主题中生成菜单的问题。(#110)
* 已解决问题：在Windows下正确处理mkdocs命令创建。(＃122)
* 已解决问题：正确处理外部的`extra_javascript`和`extra_css’。(#92)
* 已解决问题：支持了图标。(#87)