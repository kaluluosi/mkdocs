# 编写你的文档

如何编写和布局Markdown源文件。 

## 文件布局

您的文档源应该编写为常规的Markdown文件(参见[Markdown的编写](#markdown编写)以下)，并放置在[文档目录](configuration.md #docs_dir)中。默认情况下，此目录的名称将为 `docs`，并将存在于项目的顶层，与 `mkdocs.yml` 配置文件并列。你可以创建一个最简单的项目，它看起来像这样: 

```text
mkdocs.yml
docs/
     index.md
```

按照惯例，您的项目主页应该命名为 `index.md`(详情请参阅[索引页](#索引页)以下)。以下任何文件扩展名都可以用于Markdown源文件: `markdown`, `mdown`, `mkdn`, `mkd`, `md`。文档目录中包括的所有Markdown文件都将在构建的站点中呈现，无论任何设置。注意:所有以点开始的文件和目录(例如: `.foo.md` 或 `.bar/baz.md`)都将被MkDocs忽略。这可以通过[`exclude_docs`配置](configuration.md# exclude_docs)来覆盖。您还可以创建多页文档，创建多个Markdown文件:

```text
mkdocs.yml
docs/
    index.md
    about.md
    license.md
```

您使用的文件布局决定了用于生成的页面的URL。在上述布局中，页面将生成以下URL: 

```text
/
/about/
/license/
```

如果符合您的文档布局，您还可以在嵌套目录中包含Markdown文件。 

```text
docs/
     index.md
     user-guide/getting-started.md
     user-guide/configuration-options.md
     license.md
```

嵌套目录中的源文件将引起生成具有嵌套URL的页面，例如: 

```text
/
/user-guide/getting-started/
/user-guide/configuration-options/
/license/
```

在[文档目录](configuration.md#docs_dir)中未识别为Markdown文件(通过它们的文件扩展名)的任何文件都将由MkDocs无修改地复制到构建的站点中。有关详细信息，请参见[如何链接到图像和视频](#链接到图像和视频)以下。 

### 索引页面

当请求目录时，通常，大多数Web服务器都会返回该目录中包含的索引文件(通常命名为`index.html`), 如果有索引文件存在。由于这个原因，上述示例中的主页被命名为 `index.md`，当构建站点时，MkDocs将其呈现为 `index.html`。许多代码库托管站点通过显示 README 文件的内容来提供特殊功能。因此，MkDocs允许您将您的索引页命名为 `README.md` 而不是 `index.md`。这样，当用户浏览您的源代码时，库主机可以将该目录的索引页面显示为README文件。但是，当MkDocs呈现您的站点时，该文件将被重命名为 `index.html`，以使服务器将其作为适当的索引文件提供服务。如果在同一目录中找到了 `index.md` 文件和 `README.md` 文件，则使用 `index.md` 文件并忽略 `README.md` 文件。 

### 配置页面和导航

[`mkdocs.yml`](configuration.md)文件中的[导航配置](configuration.md#nav)设置定义了包括在全局站点导航菜单中的页面以及该菜单的结构。如果没有提供，则导航将通过发现文档目录中的所有Markdown文件自动创建。自动创建的导航配置始终按文件名按字母数字排序(子部分中的索引文件始终列在第一位)。如果您希望手动定义导航菜单，则需要手动定义导航配置。 

最简配置文件看起来像这样: 

```yaml
nav:
  - 'index.md'
  - 'about.md'
```

导航配置中的所有路径都必须相对于`docs_dir`配置选项。如果该选项设置为默认值 `docs`，则上述配置的源文件将位于 `docs/index.md` 和 `docs/about.md`。上面的示例将生成两个导航项目，并从Markdown文件的内容中推断其标题，如果文件本身未定义标题，那么就从文件名中推断。要在`nav`设置中覆盖标题，请在文件名之前添加一个标题。 

```yaml
nav:
  - Home: 'index.md'
  - About: 'about.md'
```

请注意，如果为页面在导航中定义了标题，则该标题将在整个站点中用于该页面，并将覆盖页面本身内定义的任何标题。导航子部分可以通过在一个部分标题下列出相关页面而创建。例如: 

```yaml
nav:
  - Home: 'index.md'
  - 'User Guide':
    - 'Writing your docs': 'writing-your-docs.md'
    - 'Styling your docs': 'styling-your-docs.md'
  - About:
    - 'License': 'license.md'
    - 'Release Notes': 'release-notes.md'
```

使用上述配置，我们有三个顶级项目: "Home"、 "User Guide" 和 "About"。"Home"是站点主页的链接。在 "User Guide" 部分下列出了两个页面: "编写您的文档" 和 "修饰您的文档"。在 "关于" 部分下再列出两个页面: "许可"和"发行说明"。请注意，一个部分不能有一个页面分配给它。段只用于存储子页面和子部分。您可以深度嵌套部分的页眉，但要小心不要通过过于复杂地嵌套使您的用户在站点导航中难以导航。虽然部分可能反映您的目录结构，但它们不必这样。未在导航配置中列出的任何页面仍将被呈现并包含在构建的站点中，但它们将不会从全局导航中链接，并且不会包含在 `previous` 和 `next` 链接中。除非直接进行链接，否则这些页面将被“隐藏”。 

## Markdown编写

MkDocs页面必须使用[Markdown][md]方式编写，这是一种轻量级标记语言，可产生易于阅读、易于编写的普通文本文档，这些文档可以以可预测的方式转换为有效的HTML文档。MkDocs使用[Python-Markdown]库将Markdown文档呈现为HTML。Python-Markdown几乎完全符合[参考实现][md]，尽管存在一些非常小的[差异]。除了所有Markdown实现中都常见的基本Markdown[语法]之外，MkDocs还包括扩展了Python-Markdown[扩展]的Markdown syntax。有关如何启用扩展的详细信息，请参阅MkDocs的[markdown_extensions]配置设置。默认情况下，MkDocs包括一些扩展，如下所示。 

[Python-Markdown]: https://python-markdown.github.io/
[md]: https://daringfireball.net/projects/markdown/
[差异]: https://python-markdown.github.io/#differences
[语法]: https://daringfireball.net/projects/markdown/syntax
[扩展]: https://python-markdown.github.io/extensions/
[markdown_extensions]: configuration.md#markdown_extensions

### 内部链接

MkDocs允许您使用常规的Markdown[链接]交互链接文档。然而，特别为MkDocs格式化这些链接有一些附加的好处，如下所述。 

[链接]: https://daringfireball.net/projects/markdown/syntax#link

#### 链接到页面

在文档中链接页面时，只需使用常规的Markdown[链接][links]语法，包括您想要链接到Markdown文档的*相对路径*。 

```markdown
请参见项目许可证以了解更多详细信息。[许可证](license.md)
```

当MkDocs进行构建时，这些Markdown链接将自动转换为适当HTML页面上的HTML超链接。警告: 使用绝对路径进行链接不受官方支持。相对路径由MkDocs进行调整，以确保它们始终相对于页面的目录。绝对路径不进行任何修改。这意味着您使用绝对路径的链接在本地环境中可能工作正常，但一旦将其部署到生产服务器上，它们可能会中断。如果目标文档文件在另一个目录中，您需要确保在链接中包含任何相对目录路径。 

```markdown
请参见项目许可证以获得更多详细信息。[许可证](../about/license.md)
```

[toc]扩展用于生成Markdown文档中每个标题的ID。您可以使用该ID通过锚链接链接到目标文档中的部分。生成的HTML会正确地转换链接的路径部分，并保留锚定部分不变。 

```markdown
请参见项目许可证了解更多详情。[关于](about.md#license)
```

请注意，ID由标头的文本创建。所有文本都转换为小写，并且任何不允许的字符(包括空格)都转换为破折号。连续破折号然后缩短为单个破折号。 

[toc]: https://python-markdown.github.io/extensions/toc/

#### 链接到图像和视频

除了Markdown源文件，您还可以在文档中包括其他文件类型，这些文件在生成文档站点时将被复制。这些文件可能包括图像和其他媒体。例如，如果您的项目文档需要包括[GitHub Pages CNAME文件]和PNG格式的截图图像，那么您的文件布局可能如下所示: 

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

要在文档源文件中包含图像，请使用任何常规的Markdown图像语法: 

```markdown
杯子检索器是一个用于索引小蛋糕的时髦新项目。![screenshot](img/screenshot.png)

*上述: 杯子检索器正在进行中*
```

构建文档时，您的图像现在将被嵌入，并且如果在Markdown编辑器中使用文档，则还应显示预览。 

[GitHub Pages CNAME文件]: https://help.github.com/articles/using-a-custom-domain-with-github-pages/

#### 从原始HTML进行链接

Markdown允许文档作者在Markdown语法不符合作者需求时回退以使用原始HTML。MkDocs在这方面不对Markdown设置任何限制。但是，由于Markdown解析器忽略所有原始HTML，因此MkDocs无法验证或转换包含在原始HTML中的链接。在原始HTML中包含内部链接时，您需要手动为呈现的文档格式化链接。 

### 元数据

MkDocs包括对YAML和MultiMarkdown样式元数据(通常称为正文)的支持。metadata由Markdown文档开头的一系列关键字和值组成，在被Python-Markdown处理之前从文档中剥离。关键字/值对由MkDocs传递给页面模板。因此，如果主题包括支持，那么键的任何值都可以在页面上显示或用于控制页面呈现。有关受支持的密钥的信息，请参阅您的主题文档，如果有的话。除了在模板中显示信息外，MkDocs还支持一些预定义的元数据键，这些键可以更改MkDocs的行为，使其特定页面更具体。支持以下键: 

*   **`template`**
    
    当前页面使用的模板。默认情况下，MkDocs使用主题的 `main.html` 模板来呈现Markdown页面。可以使用`template`元数据键为特定页面定义不同的模板文件。模板文件必须在主题环境定义的路径中可用。*   **`title`**
    
    用于文档中使用的“title”。MkDocs将尝试按以下方式确定文档的标题:
    
    1.在文档的 [nav] 配置设置中定义的标题。2.在一个文档的 `title` 元数据键中定义的标题。3.文档正文中的第一行的1级Markdown标题。(*自MkDocs 1.5起支持[Setext-style] headers。*)4.文档的文件名。
    
    在为页面找到标题后，MkDoc不再继续检查上述列表中的任何其他源。[Setext-style]: https://daringfireball.net/projects/markdown/syntax#header

对于MultiMarkdown样式的正文，Meta-data由包裹在YAML风格的元素的[YAML]键值对组成，以标记元数据的开头。文档的第一行必须是`---`。元数据在包含结束分割符(也就是`---`或`...`之一的)的第一行上结束。限制符之间的内容解析为[YAML]。 

```text
---
title: My Document
summary: A brief description of my document.authors:
    - Waylan Limberg
    - Tom Christie
date: 2018-07-10
some_url: https://example.com
---
This is the first paragraph of the document.
```

[YAML]: https://yaml.org
[nav]: configuration.md#nav

### 表

[tables]扩展为Markdown添加了一种基本的表格语法，该语法在多个实现中广受欢迎。语法非常简单，通常仅适用于简单的表格数据。一个简单的表格如下所示: 

```markdown
第一标题 |第二标题 |第三标题
------------ | ------------- | ------------
内容单元格 |内容单元格  |内容单元格
内容单元格 |内容单元格  |内容单元格
```

如果您愿意，可以在每行之前和之后添加管道: 

```markdown
| 第一标题 | 第二标题 | 第三标题 |
| ------------ | ------------- | ------------ |
| 内容单元格 | 内容单元格 | 内容单元格 |
| 内容单元格 | 内容单元格 | 内容单元格 |
```

通过将冒