# 配置

指南到所有可用的配置设置。

---

## 介绍

项目设置默认使用名为`mkdocs.yml`的项目目录中的YAML配置文件进行配置。您可以通过使用`-f`/`--config-file`选项指定另一个路径(参见 `mkdocs build --help`)来指定它。

作为最小要求，此配置文件必须包含`sitename`。所有其他设置都是可选的。

## 项目信息

### site_name

这是一个**必需的设置**，应该是一个用作项目文档的主要标题的字符串。例如：

```yaml
site_name: Marshmallow Generator
```

在呈现主题时，此设置将作为`site_name`上下文变量传递。

### site_url

设置站点的规范化URL。这将在每个HTML页面的`head`部分中添加具有`canonical` URL的`link`标记。如果MkDocs站点的“根”将在域的子目录内，则必须在设置中包括该子目录(`https://example.com/foo/` )。

此设置还用于`mkdocs server`:服务器将装入从URL的路径组件中获取的路径，例如`some/page.md`将被服务于`http://127.0.0.1:8000/foo/some/page/`以模拟预期的远程布局。

**default**: `null`

### repo_url

当设置时，在每个页面上提供与您的存储库(GitHub、Bitbucket、GitLab等)的链接。

```yaml
repo_url: https://github.com/example/repository/
```

**default**: `null`

### repo_name

当设置时，在每个页面上提供与您的存储库链接的名称。

**default**: `'GitHub'`，`'Bitbucket'`或`'GitLab'`，如果`repo_url`与这些域匹配，则为主机名，否则为`repo_url`。

### edit_uri

当直接查看页面时从基本`repo_url`到文档目录的路径，考虑到存储库主机的特殊情况(例如 GitHub、Bitbucket 等)、分支和文档目录本身。MkDocs将连接`repo_url`和`edit_uri`，并附加页面的输入路径。

当设置时，并且如果您的主题支持它，则提供直接链接到您的源存储库中的页面。这使得更容易找到和编辑页面的源。如果未设置`repo_url`，则忽略此选项。在某些主题上，设置此选项可能导致使用编辑链接而不是存储库链接。其他主题可能会同时显示两个链接。

`edit_uri`支持查询('?' )和片段('#') 字符。对于使用查询或片段访问文件的存储库主机，`edit_uri`可以设置如下。(注意 URI 中的 `?` 和 `#`。)

```yaml
# Query string example
edit_uri: '?query=root/path/docs/'
```

```yaml
# Hash fragment example
edit_uri: '#root/path/docs/'
```

对于其他存储库主机，只需指定到文档目录的相对路径即可。

```yaml
# Query string example
edit_uri: root/path/docs/
```

例如，具有此配置：

```yaml
repo_url: https://example.com/project/repo
edit_uri: blob/main/docs/
```

意味着名为'foo/bar.md'的页面将其编辑链接导向: 

<https://example.com/project/repo/blob/main/docs/foo/bar.md>

`edit_uri`实际上可以是绝对 URL，而不一定是相对于`repo_url`的URL，因此可以实现同样的结果：

```yaml
edit_uri: https://example.com/project/repo/blob/main/docs/
```

请参阅 [edit_uri_template](#edit_uri_template) 以获得更大的灵活性。

> 注意：
>
> 在一些已知的主机(具体来说是GitHub、Bitbucket和GitLab)，`edit_uri`是从'repo_url'派生的，无需手动设置。只需定义一个`repo_url`就会自动填充`edit_uri`配置设置。
>
> 例如，对于托管在GitHub或GitLab上的存储库，`edit_uri`将自动设置为`edit/master/docs/` (注意`edit`路径和`master` 分支)。
>
> 对于托管在Bitbucket上的存储库，等效的`edit_uri`将自动设置为`src/default/docs/`(注意`src`路径和`default`分支)。
>
> 要使用与默认值(例如不同的分支)不同的URI，只需将`edit_uri`设置为您想要的字符串即可。如果不想在页面上显示任何“编辑URL链接”，则将`edit_uri`设置为空字符串以禁用自动设置。

*注意：在 GitHub 和 GitLab 上，默认的“编辑”路径(`edit/master/docs/`)会打开在线编辑器。此功能要求用户具有并登录到 GitHub/GitLab 帐户。否则，用户将被重定向到一个登录/注册页面。或者，使用“blob”路径(`blob/master/docs/`)来打开只读视# 配置选项

与MkDocs一起使用的配置文件是一个标准的YAML文件。他们用来控制你的站点是如何生成和呈现的。这个部分列举了可用的配置选项，并说明了它们的含义。

大多数配置选项都可以按照默认值工作。然而，你最好至少定义 `site_name` 和 `pages` 选项，如下所述。

## site_name

类似于网站的标题。通常，它会在每个页面的标题标签中使用。除了界面之外，还用于生成站点的默认元描述标签。

```yaml
site_name: 'MkLorum - A Dummy Project'
```

## site_url

你的站点的网址。这将被用于生成Canonical URL标签并允许搜索引擎和其他工具正确索引站点的页面。

> 注意：尽管这是强制要求的选项，但可以使用`mkdocs serve`开发服务器启动站点，而不必定义此选项。

```yaml
site_url: https://example.com/my-docs/
```

注意尾斜线的存在。使用尾部斜线保证易于维护和真正的网络路径相同。

## pages

pages是一个有序列表，在此列表中定义的页面将被编译到您的站点中。我们建议您使用此选项指定目录树上的所有文件。如果您只编写单个文件，则该文件名可能会议出你的预期,仅适用于单页项目。

`pages`支持简单的`filename`字符串语法和高度可配置选项`dict`语法。请注意，在文件名字符串特定场景下，顶层文件夹的特殊的`.`和`*`字符，但是在使用字典语法时，这些字符将被解释为普通字符。您可以将基本的文件名字符串语法与易于定制的字典语法结合使用，例如，为文件夹结构指定文件名称，并使用字典选项来指定每个页面的标题和元数据。

`pages`中任何一个字段的标题和元数据都可以由`mkdocs.yml`中全局定义的`extra`字段中的任何内容继承。格式化的页面文档字符串必须是一个由8个空格或两个tab字符缩进的字符串。以下是`pages`的示例配置：

```yaml
pages:
    - 'Home': 'index.md'
    - 'Introducing MkDocs':
        - 'Introduction': 'intro.md'
        - 'Features': 'features.md'
        - 'Contribute': 'contributing.md'
    - 'Installing MkDocs':
        - 'Installation': 'install.md'
        - 'Windows': 'windows.md'
        - 'macOS': 'macos.md'
        - 'Linux': 'linux.md'
    - 'Commands':
        - 'New': 'new.md'
        - 'Build': 'build.md'
        - 'Serve': 'serve.md'
    - 'Customizing'
        - 'Configuration': 'config.md'
        - 'Custom Themes': 'custom-themes.md'
        - 'Extensions': 'extensions.md'
    - 'About':
        - 'License': 'license.md'
        - 'Release Notes': 'release-notes.md'
```

## nav

`nav`是一个顶级选项，用于完全控制导航条的树结构。`nav`的值是一个有序的层次结构列表，可以通过简单的字符串语法或高度可配置的字典语法指定。


以下是一个使用字符串语法的示例`nav`配置示例：

```yaml
nav:
    - 'Home': 'index.md'
    - 'User Guide':
        - 'Writing your docs': 'writing-your-docs.md'
        - 'Styling your docs': 'customizing-your-theme.md'
        - 'MKDocs Configuration': 'mkdocs.yml'
        - 'Commands': 'commands.md'
    - 'About MKDocs':
        - 'License': 'LICENSE'
        - 'Release Notes': 'release-notes.md'
```

以下是一个使用字典语法的示例`nav`配置示例：

```yaml
nav:
    - Home: index.md
    - section1:
        - page1:
            - "Page One - Subpage A": page1/subpage-a.md
            - "Page One - Subpage B": page1/subpage-b.md
        - Some Page: some-page.md
    - section2:
        - page2: page2.md
        - Another Page:
            url: another-page.md
    - custom site name/title:
        - page 3: page3.md
```

这种例子`nav`给出了字典语法的一些方面。

- 当页面只有文件名时，可以将它们用字符串语法指定
- 当页面需要名称和url时，必须采用字典语法。
- 如果想给列表节点指定名称而不是提取节点名称或文件名，那么必须使用字典语法。

## theme

您所选择的Mkdocs主题。如果主题有配置选项，提供一个字典。以下是一个具有默认值的字典`theme`配置示例。

```yaml
theme:
    name: 'mkdocs'
    custom_dir: null
    css: null
    extra:
        google_analytics:
            - 'UA-00000000-1'
```

有关如何选择和使用Mkdocs主题的详细信息，请参见 [选择您的主题](choosing-your-theme.md)。

### 快速设置

有时，个别属性与基本主题风格无关。出于这个原因，每个Mkdocs主题都有一个捷径列表上的属性`theme.common`。

这样，一些属性可以在每个主题上简单地指定一次，以确保在（可能）使用不同的主题时拥有一致的体验。以下是一个具有默认值的字典`theme.common`配置示例：

```yaml
theme:
  name: readthedocs
  custom_dir: null
  logo: null
  styles:
    - null
  favicon: null
  google_analytics: null
  include_search_page: null
  search_index_only: null
  search_disable_footer: null
  extra:
    github_repo: null
    twitter_username: null
    canonical_url: null
    ga_ua: null
    donation_text: null
    markdown_extensions:
      - admonition
      - codehilite
      - pymdownx.details
```

### theme_dir

一个路径，指向包含自定义主题模板和静态文件的目录。您可以设置整个主题或覆盖特定'templates' / 'static' / 'custom_css' / 'custom_js'文件的路径。

```yaml
theme_dir: null            # 无自定义主题
theme_dir: my_theme        # 包含完整的主题的目录
theme_dir:
    templates: my_templates
    static: my_static
    custom_css: my/custom.css
    custom_js: my/custom.js
```

### extra_css

CSS文件的路径或URL，将被添加到每个页面中。在优化您的CSS之前，请务必使用[Mkdocs缓存](caching.md)以提高性能。

```yaml
extra_css:
    - css/extra.css
    - https://example.com/font.css
    - '//cdn.domain.com/extra.css'
```

请注意，从默认主题中删除的不同导航或页脚元素可以使用来删除。

### highlightjs

选择默认的语法高亮库。MkDocs支持使用Pygments或Highlight.js。默认情况下，选择Highlight.js，如果不能按预期运行，建议尝试它是否与Pygments一起运行。

```yaml
highlightjs: true
```

pygments主题可以通过[YAML缩写名称](https://pygments.org/docs/styles/#creating-own-styles)或通过Pygments风格的CSS文件名来指定。

```yaml
highlightjs:
    style: monokai
```

pygments还允许指定具有额外选项的样式。

```yaml
highlightjs:
    style:
        name: monokai
        background: '#f00'
```

### markdown_extensions

MkDocs使用Python Markdown [pymkd]和扩展[pymdk-extensions]来解析markdown，并且需要将标准Markdown语法扩展到mkdocs。

```yaml
markdown_extensions:
    - pymdownx.superfences
    - pymdownx.details
    - pymdownx.tilde
```

大多数通过[pymdk-extensions]提供，建议适量使用以避免MkDocs构建的性能下降。

使用字符串名称而不是对象。在一些情况下，对象也可以工作。有关详细信息，请参见[pymdk-extensions]。

_注：更改此选项后，必须重建搜索索引_

### markdown_extensions_configs

这个选项允许你向markdown扩展传递从字典映射类名到配置对象的一列表。这个选项中的字典被解释为一个`{class_name: config_dict}`键值对的列表。

```yaml
markdown_extensions_configs:
  - pymdownx.magiclink:
      repo_url_shortener: True

  - pymdownx.extra:
      link_attrs:
        rel: ['nofollow', 'external']
        target: '_blank'
```

### mdx_configs

此选项允许向mkdocs的Python Markdown扩展传递从扩展明细到配置映射的字典。使用此选项，可以自定义使用标准markdown库进行语法解析的私有特性。

```yaml
mdx_configs:
    footnotes:
        BACKLINK_LABEL: '↩'
```

### extra

在主题模板中具有不同格式的meta选项。有关详细信息可以在主题的文档中找到。在上面的示例中，`readthedocs`主题使用该`extra`字段来提供一个值以`include_search_page`选项。

```yaml
theme:
    name: 'readthedocs'
    custom_dir: null
    css: null
    extra:
        google_analytics: 'UA-00000000-1'
```

在上面的示例中，Google Analytics跟踪仪将在生成的页面上激活。

### search

一个包含各种选项的字典，用于控制是否启用搜索，搜索框的选项，搜索过程中每个条目要索引的内容以及用于生成搜索索引的Lunr.js包的配置。搜索选项大而强大，下面对一些高级选项进行了描述。请参见[搜索选项](#search-options)进行配置。

```yaml
search:
    index_only: false
    lang: ['en']
    min_search_length: 3
    per_page: 10
    search_title_only: false
    separator: '[\s\-\.]+'
```

注意：在搜索中使用非默认的选择性功能如图像涉及到旧版的Lunr.js和未维护的额外插件。此执行不推荐，且很少支持。

### security

此选项为使用MkDocs留下的后门提供额外的安全配置，目前只有一个选项。默认情况下，仅允许在本地(127.0.0.1/localhost)的回送地址上运行`mkdocs serve`，以防止任何人都发现你的站点。

```yaml
security:
    localhost_only: true
```

> 注意：使用`0.0.0.0`或任何其他不慎放弃的IP地址启动的服务器的安全性完全由操作系统和网络架构决定。请仅在本地开发环境中使用这种方法。

## 插件

MkDocs插件是为MkDocs实现定义自己的自定义功能的Python包。请参见[插件](../dev-guide/plugins.md)了解有关编写自己的插件的更多信息。

MkDocs包括一些使用常用功能的插件，以及所有其他插件都支持。默认插件位于名为“mkdocs_internal”的包中。以下列出并描述了MkDocs支持的所有默认插件和选项。

### [搜索插件](../plugins/search/)

搜索插件为MkDocs生成了一个搜索索引，允许通过站点搜索页面并在返回的结果上轻松导航。此外，一些与搜索相关的选项可以在主配置文件中进行配置。

```yaml
plugins:
    - search
```

#### 搜索选项

当启用搜索插件时，可以通过搜索配置选项来自定义搜索行为。以下是搜索选项的详细列表：

##### **index_only**

一个布尔选项，用于根据需要决定搜索项中包含哪些页面。

如果设置了`index_only`，则只索引位于search_index目录中的页面。这个目录是通过搜索配置来定义的。

```yaml
plugins:
  - search:
      index_only: true
```

**default**: `True`

##### **search_title_only**

一个布尔选项，用于确定MkDocs搜索是否仅在页面标题中搜索内容。

```yaml
plugins:
  - search:
      search_title_only: true
```

默认情况下，MkDocs会在页面标题、段落和标题级别的文本中查找搜索词。在大多数情况下，将所有文本包括在搜索中会导致更佳的搜索结果。但是，在特定的用例下，搜索标题和页脚注释之类的内容可能更重要。

**default**: `False`

##### **separator**

一个正则表达式，用于定义单词之间的分隔符。在生成搜索索引时，MkDocs使用此分隔符将单词从页面文本中提取到搜索索引中。您也可以根据需要提供一个正则表达式字符串。

```yaml
plugins:
  - search:
      separator: '[\s\-\.]+'
```

**default**: `'[\s\-]+'`

##### **min_search_length**

一个整数值，用于定义搜索查询的最小长度。默认情况下，忽略长度小于3个字符的搜索结果，因为使用较短的搜索术语的搜索结果质量较低。但是，对于某些用例（例如关于可以生成对'MQ'进行搜索的消息队列的文档），最好设置“较短”的限制。

```yaml
plugins:
  - search:
      min_search_length: 2
```

**default**: 3

##### **lang**

使用它们的[ISO 639-1]语言代码，A包含要在构建搜索索引时使用的语言列表。使用[Lunr Languages]，支持以下语言：

* ar: 阿拉伯语
* da: 丹麦语
* nl: 荷兰语
* en: 英语
* fi: 芬兰语
* fr: 法语
* de: 德语
* hu: 匈牙利语
* it: 意大利语
* ja: 日语
* no: 挪威语
* pt: 葡萄牙语
* ro: 罗马尼亚语
* ru: 俄语
* es: 西班牙语
* sv: 瑞典语
* th: 泰语
* tr: 土耳其语
* vi: 越南语

可以[贡献更多的语言]。

警告：
虽然搜索支持同时使用多种语言，但最好不要添加其他语言，除非你真的需要它们。每个附加语言都会增加带宽需求并使用更多的浏览器资源。通常，最好将每个MkDocs实例保留在单个语言上。

注意：
Lunr Languages目前不包括对汉语或其他亚洲语言的支持。但是，一些用户报告了使用Japanese所产生的不错的结果。

**default**: 如果设置，则为`theme.locale`的值，否则为`[en]`。

##### **prebuild_index**

可选地生成所有页面的预构建索引，这提供了一些大型站点的性能改进。在启用之前，请确认您正在使用一个明确支持使用预构建索引的主题（内置主题）。设置为`true`启用。

警告：
此选项要求安装[Node.js]并且在系统路径上使用`node命令。如果`node' 的调用由于任何原因而失败，则会发出警告并且继续无中断地构建。当构建时使用`--strict`标志会导致此类失败引发错误而不是警告。

请注意：
在较小的站点上，不推荐使用预构建索引，因为它会显著增加带宽需求，对您的用户几乎没有感知到的提高性能。但是，对于较大的站点（数百页），带宽增加相对较小，您的用户将注意到搜索性能的显著提高。

**default**: `False`

##### **indexing**

配置搜索索引器在构建索引时将使用什么策略的选项。如果您的项目规模很大且索引占用了大量磁盘空间，则此属性特别有用。

```yaml
plugins:
  - search:
      indexing: 'full'
```

###### 选项

| 选项  | Description |
| ----- | ----------- |
| full  | 索引页面的标题，范围标题和完整文本。|
| sections | 索引页面的标题和范围标题。|
| titles | 仅索引页面的标题。  |

**default**: `full`

### 特殊的YAML标记

### 环境变量

在大多数情况下，配置选项的值是直接在配置文件中设置的。但是，作为一种选择，配置选项的值可以设置为环境变量的值，使用`!ENV`标记。例如，要将`site_name`选项的值设置为变量`SITE_NAME`的值，YAML文件可能包含以下内容：

```yaml
site_name: !ENV SITE_NAME
```

如果未定义环境变量，则会为配置设置分配一个空值（或Python中的“None”）。可以定义默认值作为列表中的最后一个值。如下所示：

```yaml
site_name: !ENV [SITE_NAME, 'My default site name']
```

也可以使用多个后备变量。注意，最后一个值不是环境变量，但必须是没有定义的默认值。

```yaml
site_name: !ENV [SITE_NAME, OTHER_NAME, 'My default site name']
```

简单类型在环境变量中定义，如字符串，布尔值，整数，浮点，日期戳和空值会像在YAML文件中定义一样解析，这意味着该值将被转换为适当的类型。但是，复杂类型（如列表和键/值对）无法在单个环境变量中定义。

有关详细信息，请参见[pyyaml_env_tag]项目。

### 相对于当前文件或站点的路径

NEW：**1.5版中的新功能。**

某些Markdown扩展程序可以从当前正在处理的Markdown文件的路径或仅限于当前站点的根路径受益。为此，可以在配置文件的大多数上下文内使用特殊标记`!relative`，尽管已知的使用案例仅在使用[markdown_extensions]中。 示例可能的值是：

```yaml
- !relative  # 相对于当前Markdown文件的目录
- !relative $docs_dir  # docs_dir的路径
- !relative $config_dir  # 包含主mkdocs.yml的目录的路径
- !relative $config_dir/some/child/dir  # 子目录的一些子目录根目录
```

（在这里，`$docs_dir`和`$config_dir`目前是*唯一*认可的特殊前缀名称。）

例子：

```yaml
markdown_extensions:
  - pymdownx.snippets:
      base_path: !relative  # 相对于当前Markdown文件
```

这允许[pymdownx.snippets]扩展从当前Markdown文件相对包括文件，否则它就不知道。

> 注意：甚至对于默认情况，任何扩展的基本路径都是*当前工作目录*，尽管假设它是*mkdocs.yml*的*目录*。因此，即使您不希望这些路径间关系是相对的，以改进默认行为，也应始终使用此成语：
> 
> ```yaml
> markdown_extensions:
>   - pymdownx.snippets:
>       base_path: !relative $config_dir  # 相对于具有mkdocs.yml的根目录
> ```

## 配置继承

通常，单个文件将保存整个站点的配置。然而，一些组织可能会维护多个站点，它们在所有站点之间共享通用配置。而不是为每个站点单独维护配置，可以将通用配置选项定义为父配置文件，每个站点的主配置文件都会继承该父配置文件。

要定义配置文件的父级，请将`INHERIT`（全部大写）键设置为父文件的路径。该路径必须相对于主文件