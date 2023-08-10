# 配置

所有可用配置设置的指南。

## 介绍

项目设置默认使用位于项目目录中的YAML配置文件进行配置，命名为 'mkdocs.yml'。您可以使用 '-f'/'--config-file' 选项指定另一个路径（请参见 'mkdocs build --help'）。最少，此配置文件必须包含 'site_name'。所有其他设置均是可选的。

## 项目信息

### site_name

这是一个 **必备设置**，应为一个字符串，用作项目文档的主标题。例如：

```yaml
site_name: Marshmallow Generator
```

在呈现主题时，此设置将作为 'site_name' 上下文变量传递。

### site_url

设置站点的规范 URL。这将在每个 HTML 页面的 'head' 部分添加一个带有规范 URL 的 'link' 标签。如果 MkDocs 站点的 '根' 将处于域的子目录中，请确保在该设置中包括该子目录（例如 `https://example.com/foo/`）。此设置也用于 'mkdocs serve': 服务器将挂载到 URL 的路径组件，例如。'some/page.md' 将从 'http://127.0.0.1:8000/foo/some/page/' 提供，以模仿预期的远程布局。**默认**: `null`。

### repo_url

设置后，提供每个页面中与仓库（GitHub、Bitbucket、GitLab 等）的链接。例如：

```yaml
repo_url: https://github.com/example/repository/
```

**默认**: `null`。

### repo_name

设置后，提供每个页面上与您的仓库链接的名称。**默认**: `'GitHub'`、`'Bitbucket'` 或 `'GitLab'`，如果 `repo_url` 匹配这些域，则提供主机名，否则提供主机名。

### edit_uri

直接查看页面时，从基本 `repo_url` 到文档目录的路径，考虑到仓库主机的特定内容（例如 GitHub、Bitbucket 等）、分支和文档目录本身。MkDocs 连接 `repo_url` 和 `edit_uri`，并附加页面的输入路径。当设置并且您的主题支持时，提供直接链接到源仓库中的页面。这使查找和编辑页面源代码变得更加容易。如果没有设置 `repo_url`，则将忽略此选项。在某些主题上，设置此选项可能会导致一个 "编辑" 链接被用于替换仓库链接。其他主题可能会显示两个链接。`edit_uri` 支持查询 ('?') 和片段 ('#') 字符。对于使用查询或片段访问文件的存储库主机，可以按如下方式设置 `edit_uri`。（请注意 URI 中的 `？` 和 `＃…`）

```yaml
# 查询字符串示例
edit_uri: '?query=root/path/docs/'
```

```yaml
# 数字标签示例
edit_uri: '#root/path/docs/'
```

对于其他与存储库主机，只需指定文档目录的相对路径即可。

```yaml
# 查询字符串示例
edit_uri: roo/path/docs/
```

例如，有了此配置：

```yaml
repo_url: https://example.com/project/repo
edit_uri: blob/main/docs/
```

这意味着名为 'foo/bar.md' 的页面将其编辑链接指向：<https://example.com/project/repo/blob/main/docs/foo/bar.md>

实际上，`edit_uri` 可以是绝对 URL，不一定与 `repo_url` 相对。因此，可以实现相同的结果：

```yaml
edit_uri: https://example.com/project/repo/blob/main/docs/
```

有关更大的灵活性，请参见下面的 [edit_uri_template](#edit_uri_template)。

> 注意：
>
> 在一些已知的主机上（特别是 GitHub、Bitbucket 和 GitLab），'edit_uri' 源自 'repo_url'，并不需要手动设置。只需定义 'repo_url' 将自动填充 'edit_uri' 配置设置。
> 例如，对于 GitHub-或 GitLab-托管的存储库，'edit_uri' 将自动设置为 'edit/master/docs/'（请注意 '编辑' 路径和 '主人' 分支）。
> 对于 Bitbucket-托管的存储库，等效的 'edit_uri' 将自动设置为 'src/default/docs/'（请注意 'src' 路径和 'default' 分支）。
> 要使用与默认值不同的 URI（例如不同的分支），只需将 'edit_uri' 设置为所需的字符串。如果您不想在页面上显示任何 "编辑 URL 链接"，则将 'edit_uri' 设置为空字符串，以禁用自动设置。

警告：在 GitHub 和 GitLab 上，默认的 "edit" 路径（`edit/master/docs/`）将在在线编辑器中打开页面。此功能要求用户有一个 GitHub/GitLab 帐户并已登录。否则，用户将被重定向到登录/注册页面。或者，使用 "blob" 路径（‘blob/master/docs/’）打开只读视图，该视图支持匿名访问。

**默认**: 对于 GitHub 和 GitLab repos，默认为 `edit/master/docs/` 或者 Bitbucket repo 的 ‘src/default/docs/’，如果 `repo_url` 匹配了这些域，则为此设置，否则为 `null`。

### edit_uri_template

[edit_uri](#edit_uri) 更加灵活的变体。下面这两个等价：

```yaml
edit_uri: 'blob/main/docs/'
edit_uri_template: 'blob/main/docs/{path}'
```

（它们也是互斥的-不要指定两者）。从这里开始，您可以更改路径的定位或格式，以防默认附加路径的行为不足。'edit_uri_template' 的内容是普通的 [Python 格式字符串](https://docs.python.org/3/library/string.html#formatstrings)，只有这些字段可用：

- `{path}`，例如。'foo/bar.md'
- `{path_noext}`，例如。'foo/bar'
- 可用转换标志 `!q`，以对字段进行百分比编码：
- `{path!q}`，例如'foo%2Fbar.md'

> ? 注意:  **建议使用的有用配置：**
> 
> - GitHub Wiki：
> （例如。`https://github.com/project/repo/wiki/foo/bar/_edit`）
> ```yaml
> repo_url: 'https://github.com/project/repo/wiki'
> edit_uri_template: '{path_noext}/_edit'
> ```
> 
> - BitBucket 编辑器：
> （例如。`https://bitbucket.org/project/repo/src/master/docs/foo/bar.md?mode=edit`）
> ```yaml
> repo_url: 'https://bitbucket.org/project/repo/'
> edit_uri_template: 'src/master/docs/{path}?mode=edit'
> ```
>
> - GitLab 静态站点编辑器：
> （例如。`https://gitlab.com/project/repo/-/sse/master/docs%2Ffoo%2bar.md`）
> ```yaml
> repo_url: 'https://gitlab.com/project/repo'
> edit_uri_template: '-/sse/master/docs%2F{path!q}'
> ```
> - GitLab Web IDE：
> （例如。https://gitlab.com/-/ide/project/repo/edit/master/-/docs/foo/bar.md）
> ```yaml
> edit_uri_template: 'https://gitlab.com/-/ide/project/repo/edit/master/-/docs/{path}'
> ```

**默认**: `null`。

### site_description

设置站点描述。这将在生成的 HTML header 中添加一个 meta标签。

**默认**: `null`。

### site_author

设置作者名称。这将在生成的 HTML header 中添加一个 meta 标签。

**默认**: `null`。

### 版权

设置包含在文档中的版权信息的主题。**默认**: `null`。

### remote_branch

在使用 `gh-deploy` 部署到 GitHub Pages 时，设置要提交的远程分支。此选项可以在 `gh-deploy` 的命令行选项中被覆盖。

**默认**: `'gh-pages'`。

### remote_name

在使用 `gh-deploy` 部署到 GitHub Pages 时，设置要推送的远程名称。此选项可以在 `gh-deploy` 的命令行选项中被覆盖。**默认**: `'origin'`。

## 文档布局

### nav

此设置用于确定站点的全局导航的格式和布局。最小导航配置可能如下所示：

```yaml
nav:
  - 'index.md'
  - 'about.md'
```

导航配置中的所有路径都必须相对于 [`docs_dir`](#docs_dir) 配置选项。有关详细信息，包括如何创建子部分，请参见有关 [配置页面和导航](https://www.mkdocs.org/user-guide/configuration/#configuring-pages-and-navigation) 的部分。导航项还可以包含指向外部站点的链接。虽然对于内部链接来说，标题是可选的，但对于外部链接是必需的。外部链接可以是完整 URL 或相对 URL。在文件中未找到的任何路径都被认为是外部链接。有关 MkDocs 如何确定文档的页面标题的详细信息，请参见 [元数据](https://www.mkdocs.org/user-guide/writing-your-docs/#metadata) 部分。

```yaml
nav:
  - Introduction: 'index.md'
  - 'about.md'
  - 'Issue Tracker': 'https://example.com/'
```

在上面的示例中，前两个项目指向本地文件，第三个指向外部站点。然而，有时候 MkDocs 站点托管在项目站点的子目录中，您可能希望链接到同一站点的其他部分，而不包括完整域。在这种情况下，您可以使用适当的相对 URL。例如：

```yaml
site_url: https://example.com/foo/

nav:
  - Home: '../'
  - 'User Guide': 'user-guide.md'
  - 'Bug Tracker': '/bugs/'
```

在上面的示例中，使用了两种不同的外部链接样式。首先，注意 `site_url` 表示 MkDocs 站点托管在域的 `/foo/` 子目录中。因此，'Home' 导航项是相对链接，可以向上走一级到服务器根目录，并且有效地指向 `https://example.com/`。'Bug Tracker' 项目使用相对于服务器根的绝对路径，并且有效地指向 `https://example.com/bugs/`。当然，'User Guide' 指向本地 MkDocs 页面。

**默认**: 默认情况下 `nav` 将包含所有发现的 Markdown 文件的按字母数字排序的嵌套列表，这些文件在 `docs_dir` 和其子目录中找到。索引文件将始终排在子部分之前。

### exclude_docs

新 ： **在 1.5 版中推出。**

此配置定义要忽略的文件模式（在[`docs_dir`](#docs_dir)下）以不被加入构建站点中。例如：

```yaml
exclude_docs: |
  api-config.json    # 该名称的文件
  drafts/            # 'drafts' 目录的任何地方
  /requirements.txt  # 顶级 'docs/requirements.txt'。
  *.py               # 任何具有此扩展名的文件，任何地方。
  !/foo/example.py   # 但保留此特定文件。
```

这遵循 [.gitignore 模式格式](https://git-scm.com/docs/gitignore#_pattern_format)。注意， `mkdocs serve`不遵循此设置，而是显示已排除的文档，但带有“DRAFT”标记。要避免此效果，您可以运行 `mkdocs serve --clean`。以下默认值始终被隐式地预先添加-将点文件（和目录）以及顶级 'templates' 目录排除：

```yaml
exclude_docs: |
  .*
  /templates/
```

因此，为了真正从头开始启动此配置，您需要首先说明这些条目的否定版本。否则，例如，可以仅将某些点文件重新加入站点：

```yaml
exclude_docs: |
  !.assets  # 不要排除'.assets'，尽管所有其他 '.*' 都被排除。
```

### not_in_nav

新 ： **在 1.5 版中推出。**

注意：此选项实际上并未从 nav 中排除任何内容。如果要将某些文档包括到站点中，但有意地将其从 nav 中排除，则通常 MkDocs 会发出警告。将这些文件模式（相对于[`docs_dir`](#docs_dir)）添加到 `not_in_nav` 配置中将防止此类警告。例如：

```yaml
nav:
  - Foo: foo.md
  - Bar: bar.md

not_in_nav: |
  /private.md
```

与上一个选项一样，这遵循了 .gitignore 模式格式。注意：将给定文件添加到 [`exclude_docs`](#exclude_docs) 排除优先于并暗示 `not_in_nav`。

### 验证

新 ： **在 1.5 版中推出。**

在验证链接到文档时，配置 MkDocs 的诊断消息的严格程度。这是一个配置树，对于每个配置，值可以是以下三个之一：`warn`，`info`，`ignore`。这些级别分别对应于在发生相应事件时生成相应严重性的记录消息。显然，'warn' 级别旨在在持续测试中使用 `mkdocs build --strict`（其中它将成为错误）。
> 示例：**MkDocs 1.5 中此配置的默认值：**
>
> ```yaml
> validation:
>   nav:
>     omitted_files: info
>     not_found### extra_templates
> ```

在`docs_dir`中设置一个模板列表，以便MkDocs构建。要了解有关编写MkDocs模板的更多信息，请阅读有关[自定义主题]的文档，特别是有关[可用变量]的部分和[extra_css]中的用法示例。**默认值**：`[]`（空列表）。

### extra

一个键值对集合，其中值可以是任何有效的YAML构造，将传递给模板。这使得创建自定义主题非常灵活。例如，如果您正在使用支持显示项目版本的主题，您可以将其传递到主题中，如下所示：

```yaml
extra:
  version: 1.0
```

**默认值**：默认情况下，`extra`将是一个空键值映射。

## 预览控件

### 实时重新加载

### 监视

在运行`mkdocs serve`时确定要监视的附加目录。配置是一个YAML列表。

```yaml
watch:
  - directory_a
  - directory_b
```

允许设置自定义默认值，无需每次调用`mkdocs serve`命令时通过`-w`/`--watch`选项进行传递。

> 注意：
>
> 配置文件中提供的路径是相对于配置文件。通过`-w`/`--watch` CLI参数提供的路径则不是。

### 使用目录URL

此设置控制用于链接到文档内的页面的样式。下表演示了在将`use_directory_urls`设置为`true`或`false`时，在网站上使用的URL的差异。

源文件          | use_directory_urls: true | use_directory_urls: false
--------------- | ------------------------ | ------------------------
index.md        | /                        | /index.html
api-guide.md    | /api-guide/              | /api-guide.html
about/license.md| /about/license/          | /about/license.html

默认样式`use_directory_urls: true`创建了更用户友好的URL，这通常是您想要使用的。备选样式可能在直接从文件系统打开页面时链接保持正确链接上更有用，因为它们创建将直接指向目标*文件*而不是目标*目录*的链接。

**默认值**：`true`

### 严格

确定如何处理警告。设置为`true`时，会在引发警告时停止处理。将其设置为`false`时，会打印警告并继续处理。这也作为一个命令行标志可用：`--strict`。

**默认值**：`false`

### dev_addr

确定运行`mkdocs serve`时使用的地址。必须符合`IP:PORT`的格式。允许设置自定义默认值，无需每次调用`mkdocs serve`命令时通过`--dev-addr`选项进行传递。

**默认值**：`'127.0.0.1:8000'`

另见：[site_url]（#site_url）。

## 格式选项

### markdown_extensions

MkDocs使用[Python Markdown]库将Markdown文件转换为HTML。Python Markdown支持多种[扩展][pymdk-extensions]，这些扩展可定制页面的格式。此设置允许您启用超出MkDocs默认使用的扩展列表（`meta`、`toc`、`tables`和`fenced_code`）的扩展列表。例如，要启用[SmartyPants排版扩展][smarty]，请使用：

```yaml
markdown_extensions:
  - smarty
```

一些扩展提供自己的配置选项。如果您想设置任何配置选项，那么可以嵌套一个每个扩展支持的任何选项的键/值映射（`option_name：option value`）。请参见正在使用的扩展的文档，以确定它们支持哪些选项。例如，要启用（包含的）`toc`扩展中的永久链接，请使用：

```yaml
markdown_extensions:
  - toc:
      permalink: true
```

请注意，冒号（`:`）必须跟随扩展名（`toc`），然后在新行上，选项名称和值必须缩进并用冒号分隔。如果您想为单个扩展定义多个选项，则必须为每个选项定义单独的行：

```yaml
markdown_extensions:
  - toc:
      permalink: true
      separator: "_"
```

为每个扩展添加一个附加项。如果您没有要设置给定扩展的配置选项，则仅省略该扩展的选项：

```yaml
markdown_extensions:
  - smarty
  - toc:
      permalink: true
  - sane_lists
```

> 注意：**动态配置值。**
>
> 为了动态配置扩展，您可以从[环境变量]（＃环境变量）或获取当前呈现的Markdown文件或整个MkDocs网站的路径来获取配置值。在上面的示例中，每个扩展都是列表项（以`-`开头）。作为代替，也可以使用键/值对。但是，在这种情况下，对于未定义选项的扩展，必须提供空值。因此，上面的示例也可以定义为：

```yaml
markdown_extensions:
  smarty: {}
  toc:
    permalink: true
  sane_lists: {}
```

如果要覆盖一些选项，请使用此替代语法。
[inheritance]（＃configuration-inheritance）。

> 注意：**更多扩展。**
>
> Python-Markdown文档提供了一个[扩展列表][exts]，这些扩展可以直接使用。对于给定扩展可用的配置选项列表，请参见该扩展的文档。您还可以安装和使用各种第三方扩展（[Python-Markdown wiki]、[MkDocs项目目录][目录]）。请参阅这些扩展提供的文档以获得安装说明和可用的配置选项。

**默认值**：`[]`（空列表）。

### hooks

**1.4版中的新功能**

用于加载并用作[插件](＃plugins)实例的Python脚本路径列表（相对于`mkdocs.yml`）。例如：

```yaml
hooks:
  - my_hooks.py
```

那么文件* my_hooks.py *可以包含任何[插件事件处理程序](../dev-guide/plugins.md#events)（没有`self`），例如：

```python
def on_page_markdown(markdown，**kwargs):
  return markdown.replace（'a'，'z'）
```

此功能不会启用任何新的功能与[plugins]相比，它只是简化了一次性用途，因此无需像插件一样进行*安装*。请注意，在`mkdocs serve`上，挂钩模块*不会*在每个构建上重新加载。您可能已经在[mkdocs-simple-hooks插件](https://github.com/aklajnert/mkdocs-simple-hooks)中看到过此功能。如果使用标准方法名称，可以直接替换，如下所示：

```diff
-plugins：
-  - mkdocs-simple-hooks：
-      hooks：
-        on_page_markdown：'my_hooks:on_page_markdown'
+钩子：
+  - my_hooks.py
```

### 插件

用于构建站点时使用的[插件（插件）]（＃plugins）的插件列表（可选配备的配置设置）。有关完整详细信息，请参见[Plugins]文档。如果在`mkdocs.yml`配置文件中定义了`plugins`配置设置，则会忽略任何默认值（例如`search`），如果您想继续使用它们，您需要显式地重新启用它们：

```yaml
plugins:
  - search
  - your_other_plugin
```

要为给定的插件定义选项，请使用嵌套的键/值对集合：

```yaml
plugins:
  - search
  - your_other_plugin：
      option1:value
      option2:other value
```

在上面的示例中，每个插件都是列表项（以`-`开头）。作为代替，也可以使用键/值对。但是，在这种情况下，对于未定义选项的插件，必须提供空值。因此，上面的最后一个示例也可以定义为：

```yaml
plugins:
  search: {}
  your_other_plugin：
    option1:value
    option2:other value
```

如果想要完全禁用所有插件，包括任何默认值，请将`plugins`设置为空列表：

```yaml
plugins: []
```

**默认值**：`['search']`（MkDocs附带的“search”插件）。

### Search

MkDocs默认提供一个搜索插件，它使用[lunr.js]作为搜索引擎。可以使用以下配置选项来更改搜索插件的行为：

##### **separator**

在构建索引时匹配单词分隔符使用的正则表达式。默认使用空格和连字符（`-`）。要将点（`.`）添加为单词分隔符，您可以执行以下操作：

```yaml
plugins：
  - 搜索：
      分离器：'[\\ s  -  \\。] +'
```

**默认值**：`'[\\ s  -] +'`

##### **min_search_length**

定义搜索查询的最小长度的整数值。默认情况下，长度小于3个字符的搜索会被忽略，因为短搜索术语的搜索结果质量很差。但是，对于某些用例（例如有关可能会生成对'MQ'的搜索的消息队列的文档），设置较短的限制可能更可取。

```yaml
plugins：
  - 搜索：
      min_search_length：2
```

**默认值**：3

##### **lang**

构建搜索索引时使用的语言列表，由其[ISO 639-1]语言代码标识。使用[Lunr Languages]，支持以下语言：

-用阿拉伯语
-达麦语
-用荷兰语
-英语
-芬兰语
-法语
-德语
-用匈牙利语
-用意大利语
-日本语
-用挪威语
-葡萄牙语
-罗马尼亚语
-俄语
-西班牙语
-瑞典语
-用泰语
-用土耳其语
-越南人

您可以[贡献其他语言]。警告：虽然搜索支持一起使用多种语言，但最好不要添加其他语言，除非确实需要。每种附加语言都会增加显着的带宽要求并使用更多的浏览器资源。通常，最好将每个MkDocs实例保持为单个语言。注意：Lunr Languages当前不包括对中文或其他亚洲语言的支持。但是，一些用户报告使用日语获得了不错的结果。

**默认值**：如果设置了`theme.locale`的值，则为该值，否则为`[en]`。

##### **prebuild_index**

可选地生成所有页面的预构建索引，这为较大的网站提供了一些性能改进。在启用之前，请确认您正在使用的主题显式支持使用预构建索引（内置主题）。设置为`true`以启用。

警告：此选项需要安装[Node.js]和将命令`node`放在系统路径中。如果调用`node`失败，则会发出警告，并且构建将继续无中断。您可以在构建时使用`--strict`标志使此类故障引发错误。注意：在较小的网站上，不建议使用预构建索引，因为这会导致带宽要求显着增加，而对于您的用户而言几乎没有可察觉的改进。但是，对于较大的站点（数百个页面），带宽增加相对较小，用户将注意到搜索性能的显着改进。

**默认值**：`False`

##### **indexing**

使用搜索索引器构建索引时配置所需的策略。该属性在项目规模较大时特别有用，并且索引占用了大量磁盘空间。

```yaml
plugins：
  - 搜索：
      索引：'全文'
```

###### 选项

|选项|说明|
|------|-----------|
|`全部`|对每个页面的标题、部分标题和完整文本进行索引。|
|`section`|对每个页面的标题和章节标题进行索引。|
|`titles`|仅对每个页面的标题进行索引。|

**默认值**：`完全`

## 特殊的YAML标记

### 环境变量

在大多数情况下，配置选项的值直接在配置文件中设置。但是，作为选项，配置选项的值可以使用`!ENV`标记设置为环境变量的值。例如，要将`site_name`选项的值设置为变量`SITE_NAME`的值，则YAML文件可以包含以下内容：

```yaml
site_name: !ENV SITE_NAME
```

如果未定义环境变量，则配置设置将被分配一个`null`（或Python中的`None`）值。可以将默认值定义为列表中的最后一个值。例如：

```yaml
site_name: !ENV [SITE_NAME，'My default site name']
```

也可以使用多个回退变量。请注意，最后一个值不是环境变量，而必须是一个默认值，如果没有指定环境变量，则使用该值。例如：

```yaml
site_name: !ENV [SITE_NAME，OTHER_NAME，'My default site name']
```

在环境变量中定义的简单类型（例如字符串、布尔值、整数、浮点值、日期戳和null）被解析为如果它们在YAML文件中直接定义，则将其解析为相应类型的值。但是，无法在单个环境变量中定义复杂类型，例如列表和键/值对。有关更多详细信息，请参见[pyyaml_env_tag]（https://github.com/waylan/pyyaml-env-tag）项目。

### 相对于当前文件或站点的路径

新的1.5版中提供了一些Markdown扩展可以受益于知道当前正在处理的Markdown文件的路径，或仅与当前网站例如：

```bash
echo '{INHERIT: mkdocs.yml, site_name: "重命名站点"}' | mkdocs build -f -
```

[主题开发者指南]: ../dev-guide/themes.md
[pymdk-扩展]: https://python-markdown.github.io/extensions/
[pymkd]: https://python-markdown.github.io/
[聪明]: https://python-markdown.github.io/extensions/smarty/
[扩展]: https://python-markdown.github.io/extensions/
[Python-Markdown维基]: https://github.com/Python-Markdown/markdown/wiki/Third-Party-Extensions
[目录]: https://github.com/mkdocs/catalog
[配置页面和导航]: writing-your-docs.md#configure-pages-and-navigation
[主题目录]: customizing-your-theme.md#using-the-theme_dir
[选择你的主题]: choosing-your-theme.md
[本地化你的主题]: localizing-your-theme.md
[extra_css]: #extra_css
[插件]: ../dev-guide/plugins.md
[lunr.js]: https://lunrjs.com/
[ISO 639-1]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[Lunr Languages]: https://github.com/MihaiValentin/lunr-languages#lunr-languages-----
[为其它语言做贡献]: https://github.com/MihaiValentin/lunr-languages/blob/master/CONTRIBUTING.md
[Node.js]: https://nodejs.org/
[markdown_extensions]: #markdown_extensions
[nav]: #nav
[继承]: #configuration-inheritance
[pymdownx.snippets]: https://facelessuser.github.io/pymdown-extensions/extensions/snippets/