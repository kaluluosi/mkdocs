# 撰写你的文档

如何布局和编写Markdown源文件。

---

## 文件布局

您的文档源应以常规Markdown文件的形式编写（参见
[使用Markdown编写](#使用markdown编写)），并将其放置在
[文档目录](configuration.md#docs_dir)中。默认情况下，该目录
将命名为`docs`，并将存在于您的项目顶层，与
`mkdocs.yml`配置文件并称。

您可以创建的最简单的项目将如下所示：

```text
mkdocs.yml
docs/
    index.md
```

按惯例，您的项目主页应命名为`index.md`（参见 [主页](#主页) 以下的详细信息）。任何以下任何文件扩展名都可能用于您的Markdown源文件：`markdown`，`mdown`，`mkdn`，`mkd`，`md`。无论任何设置， 任何包含在您的文档目录中的Markdown文件都将在构建站点时呈现。

注意：
以点（例如：`.foo.md`或`.bar/baz.md`）开头的名称的文件和目录将被MkDocs忽略。这可以通过[`exclude_docs`配置](configuration.md#exclude_docs)进行覆盖。

如果需要，您还可以创建多页文档，方法是创建几个Markdown
文件：

```text
mkdocs.yml
docs/
    index.md
    about.md
    license.md
```

您使用的文件布局决定了用于生成的URL
页面。在上面的布局中，将为以下URL生成页面：

```text
/
/about/
/license/
```

如果更适合您的文档布局，还可以在嵌套目录中包含Markdown文件。

```text
docs/
    index.md
    user-guide/getting-started.md
    user-guide/configuration-options.md
    license.md
```

嵌套目录中的源文件将导致页面生成嵌套URL，例如：

```text
/
/user-guide/getting-started/
/user-guide/configuration-options/
/license/
```

文档目录中未标识为Markdown文件（通过其文件扩展名）的任何文件都将被MkDocs复制到构建站点中，不经处理。详情请参阅[如何链接到图像和媒体](#链接到图像和媒体)。

### 主页

默认情况下，请求目录时，大多数Web服务器会返回一个索引文件（通常命名为`index.html`）包含在该目录中（如果存在）。因此，在上面的所有示例中，主页均已命名为`index.md`，当构建站点时，MkDocs将其呈现为`index.html`。

许多仓库托管站点通过在浏览目录内容时显示README文件的内容来提供特殊处理。因此，MkDocs允许您将主页命名为`README.md`而不是`index.md`。这样，当用户浏览源代码时，代码库主机可以显示该目录的索引页，因为它是README文件。然而，当MkDocs呈现您的站点时，该文件将被重命名为`index.html`，以便服务器将其作为正确的索引文件服务。

如果在同一个目录中发现`index.md`文件和`README.md`文件，则使用`index.md`文件，忽略`README.md`文件。

### 配置页面和导航

`mkdocs.yml`文件中的 [nav](configuration.md#nav) 配置设置定义可包含在全局站点导航菜单中的页面以及该菜单的结构。如果未提供，则导航将通过发现文档中的所有Markdown文件自动生成。自动创建的导航配置将始终按文件名的字母数字顺序排序（除了索引文件始终在子部分中列在第一位除外）。如果要按不同的顺序对导航菜单进行排序，则需要手动定义导航配置。

最小化的导航配置可能如下所示：

```yaml
nav:
  - 'index.md'
  - 'about.md'
```

导航配置中的所有路径都必须相对于`docs_dir`配置选项。如果该选项设置为默认值`docs`，则上面配置的源文件将位于`docs/index.md`和`docs/about.md`。

上述示例将导致创建两个顶级导航项，并从Markdown文件或（如果在文件中未定义标题）从文件名中推断其标题。要在`nav`设置中覆盖标题，请在文件名之前添加一个标题。

```yaml
nav:
  - 主页：'index.md'
  - 关于我们：'about.md'
```

请注意，如果在导航中为页面定义了标题，则将在整个站点中使用该页面的标题，并覆盖页面本身定义的任何标题。

可以通过将相关页面放在标题下面来创建导航子部分。例如：

```YAML
nav:
  - 'index.md'
  - '用户指南':
    - '编写文档': 'writing-your-docs.md'
    - '风格说明': 'styling-your-docs.md'
  - '关于':
    - '许可证': 'license.md'
    - '发布说明': 'release-notes.md'
```

通过上面的配置，我们有三个顶层项：“主页”，“用户指南”和“关于”。 “主页”是指向站点主页的链接。在“用户指南”下列出了两个页面：“编写文档”和“风格说明”。“关于”下面列出了两个页面：“许可证”和“发布说明”。

请注意，一个部分不能分配给一个页面。部分仅是子页面和子部分。您可以嵌套部分，但是请注意，不要通过过于复杂的嵌套使用户难以通过网站导航。虽然部分可以映射您的目录结构，但它们不必如此。

任何未在导航配置中列出的页面仍将呈现并包含在构建站点中，但它们不会链接到全局导航，并且不包括`previous`和`next`链接。这些页面将“隐藏”，除非您直接链接到它们。

## 使用Markdown编写

MkDocs页面必须使用[Markdown][md]编写，这是一种轻量级标记语言，可产生易于阅读，易于编写的纯文本文档，可以以可预测的方式转换为有效的HTML文档。

MkDocs使用[Python-Markdown]库将Markdown文档呈现为HTML。Python-Markdown几乎完全符合[参考实现][md]，尽管有少许的[差异]。

除了适用于所有Markdown实现的基本Markdown [语法]之外，MkDocs还包括支持使用Python-Markdown [扩展]来扩展Markdown语法的支持。有关启用扩展的详细信息，请参见MkDocs的 [markdown_extensions] 配置设置。

MkDocs默认包含一些扩展，如下所示。

[Python-Markdown]: https://python-markdown.github.io/
[md]: https://daringfireball.net/projects/markdown/
[differences]: https://python-markdown.github.io/#differences
[syntax]: https://daringfireball.net/projects/markdown/syntax
[extensions]: https://python-markdown.github.io/extensions/
[markdown_extensions]: configuration.md#markdown_extensions

### 内部链接

MkDocs允许您使用常规Markdown [链接]将您的文档链接起来。但是，按照下面的格式为MkDocs格式化这些链接也有一些额外的好处。

[links]: https://daringfireball.net/projects/markdown/syntax#link

#### 链接页面

在文档之间链接时，可以使用常规的Markdown [链接][链接]语法，包括您要链接到的Markdown文档的*相对路径*。

```markdown
请参阅[项目许可证](license.md)以了解更多详细信息。
```

当MkDocs构建运行时，这些Markdown链接将自动转换为恰当的HTML超链接以链接到合适的HTML页面。

警告：
不官方支持使用绝对路径进行链接。MkDocs将相对路径调整为始终相对于页面。绝对路径完全不被修改。这意味着使用绝对路径的链接在本地环境中可能不会有任何问题，但在将其部署到生产服务器上后可能会出现问题。

如果目标文档位于另一个目录中，则需要确保在链接中包含任何相对目录路径。

```markdown
请参阅[项目许可证](../about/license.md)以了解更多详细信息。
```

MkDocs使用[toc]扩展程序为您的Markdown文档生成标头的ID。
通过使用锚点链接，可以使用该ID链接到目标文档中的某个部分。
生成的HTML将正确转换链接的路径部分，并保留锚字符部分。

```markdown
请参阅[项目许可证](about.md#许可证)以了解更多详细信息。
```

请注意，标识符是从标头的文本创建的。所有文本都转换为
小写，并且任何不允许的字符，包括空格，都转换为划线。接续横线然后简化成单个横线。

toc扩展提供了一些配置设置，您可以在`mkdocs.yml`配置文件中设置它们以更改默认行为：

* **`permalink`**

在每个标题末尾生成永久链接。默认值：`False`。

如果设置为True，则使用段落符号（&para;或`&para;`）作为链接文本。如果设置为字符串，则提供的字符串将用作链接文本。例如，要代替哈希符号(`#`)使用，执行以下操作：

```yaml
markdown_extensions:
  - toc:
      permalink: "#"
```

* **`baselevel`**

标头的基础级别。默认值：`1`。

此设置允许自动调整标题级别以适应HTML模板的层次结构。例如，如果Markdown文本不应包含高于2级的标头(`<h2>`)，则执行以下操作：

```yaml
markdown_extensions:
  - toc:
      baselevel: 2
```

然后，文档中的任何标头都会增加1。例如，标题“#Header”在HTML输出中将呈现为第2级标题(`<h2>`)

* **`separator`**

单词分隔符。默认值：`-`。

此字符代替生成的ID中的空格。如果您喜欢下划线，那就执行以下操作

```yaml
markdown_extensions:
  - toc:
      separator: "_"
```

请注意，如果要定义多个上述设置，则必须在“配置”下对其进行设置
单个`toc`条目在`markdown_extensions`配置选项中。


```yml
markdown_extensions:
  - toc:
      permalink: "#"
      baselevel: 2
      separator: "_"
```

[toc]: https://python-markdown.github.io/extensions/toc/

#### 链接图像和媒体

以及Markdown源文件，您可以在文档中包含其他文件类型，这些文件在生成文档站点时会复制过去。这些文件可能包括图像和其他媒体。

例如，如果您的项目文档需要包含[GitHub Pages CNAME文件]和以PNG格式的截图图像，则您的文件布局可能如下：

```text
mkdocs.yml
docs/
    CNAME
    index.md
    about.md
    license.md
    img/
        screenshot.png
```

要在文档源文件中包含图像，请使用任何常规Markdown图像语法：

```Markdown
蛋糕索引器是一个崭新的项目，用于索引小糕点。

！[截图](img/screenshot.png)

*上：正在进行中的蛋糕索引器*
```

当您构建文档时，您的图像将嵌入其中，并且如果您使用Markdown编辑器编辑文档，则应该预览。

[GitHub Pages CNAME文件]: https://help.github.com/articles/using-a-custom-domain-with-github-pages/

#### 从原始HTML链接

Markdown允许文档作者回退到原始的HTML，当Markdown语法无法满足作者的需求时。MkDocs在此方面不受限制。但是，由于Markdown解析器忽略所有原始HTML，因此MkDocs无法验证或转换包含在原始HTML中的链接。当在原始HTML中包含内部链接时，您将需要手动格式化该链接，以适合呈现文档。

### 元数据

MkDocs包括对YAML和MultiMarkdown样式元数据（通常称为front-matter）的支持。元数据由Markdown文档开头定义的一系列关键字和值组成，这些关键字和值在通过Python-Markdown处理之前从文档中剥离。关键字/值对由MkDocs传递给页面模板。因此，如果主题包括支持，则键的任何值都可以在页面上显示或用于控制页面呈现。有关支持的键可能性的信息，请参阅主题的文档。

除了在模板中显示信息之外，MkDocs还支持一些预定义元数据键，这些键可以更改MkDocs对该特定页面的行为。支持以下键：

* **`template`**

    当前页面使用的模板。

    默认情况下，MkDocs使用主题的`main.html`模板来呈现Markdown页面。您可以使用`template`元数据键为该特定页面定义不同的模板文件。模板文件必须在主题环境的路径中可用。

* **`title`**

    用于文档的“标题”。

    MkDocs将尝试通过以下方式确定文档的标题：

    1.  在文档的[导航](configuration.md#nav)配置设置中定义的标题。

    2.  在文档的`title`元数据键中定义的标题。

    3.  文档正文的第一行