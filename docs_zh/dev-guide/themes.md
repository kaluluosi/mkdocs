# 开发主题

创建和发布自定义主题的指南。

---

注意:
如果你正在寻找现有的第三方主题，它们在[社区wiki]页面和[MkDocs项目目录][catalog]中列出。如果你想分享你创建的主题，应该在那里列出它。

当创建一个新的主题时，你可以跟随这个指南中的步骤从头开始创建，或者你可以下载`mkdocs-basic-theme`作为一个基本的、完整的主题，其中包含了所有所需的样板文件。**你可以在[GitHub][基础主题]上找到这个基础主题**。它在代码中包含了对不同功能及其用法的详细注释。

[社区wiki]: https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[catalog]: https://github.com/mkdocs/catalog#-theming
[基础主题]: https://github.com/mkdocs/mkdocs-basic-theme

## 创建自定义主题

自定义主题所需的最少要求是一个称为 `main.html` 的[Jinja2 模板]文件，它位于文档目录[docs_dir]的子目录之外。在 `mkdocs.yml` 中，将[`theme.custom_dir`] 配置选项设置为包含 `main.html` 的目录的路径。路径应该是相对于配置文件而言的。例如，给定以下示例项目布局：

```text
mkdocs.yml
docs/
    index.md
    about.md
custom_theme/
    main.html
    ...
```

…你需要在 `mkdocs.yml` 中包含以下设置来使用自定义主题目录：

```yaml
theme:
  name: null
  custom_dir: 'custom_theme/'
```

> 注意：
> 通常，在构建你自己的自定义主题时，`theme.[name]` 配置设置将被设置为 `null`。但是，如果将 `theme.[custom_dir]` 配置值与现有主题一起使用，则可以使用 `theme.[custom_dir]` 来替换内置主题的特定部分。例如，对于以上布局，如果设置 `name: "mkdocs" `，那么主题中的 `main.html` 文件将替换 `mkdocs` 主题中相应的同名文件，但除此之外， `mkdocs` 主题保持不变。如果你想对现有主题进行小的调整，这一点非常有用。
> 
> 有关更具体的信息，请参见[自定义你的主题]。
<!-- -->
> 警告：
> 主题的 [配置] 在 `mkdocs_theme.yml` 文件中定义，而这个文件并不是从 `theme.custom_dir` 加载的。当整个主题存在于 `theme.custom_dir` 中，且 `theme.name` 设置为 `null` 时，主题的整个配置必须在 `mkdocs.yml` 文件中的 [theme] 配置选项中定义。然而，当一个主题被[## 支持主题本地化/翻译

虽然内置主题提供模板的[本地化/翻译]支持，但自定义主题和第三方主题可能选择不支持。无论如何，`theme`配置选项的 [`locale`](#locale) 设置始终存在，其他部分依赖于它。因此，建议所有第三方主题使用相同的设置来指定语言，而不管它们用于翻译的系统如何。这样一来，无论用户选择哪个主题，他们都会体验到一致的行为。

管理翻译的方法由主题开发人员决定。但是，如果主题开发人员选择使用内置主题使用的相同机制，则下面的部分概述了如何启用和利用MkDocs使用的相同命令。

[本地化/翻译]：../user-guide/localizing-your-theme.md

### 使用本地化/翻译命令

警告：由于默认情况下未安装[pybabel]，大多数用户将不会安装pybabel，因此主题开发人员和/或翻译员应确保已安装必要的依赖项（使用`pip install mkdocs [i18n] `），以便命令可用于使用。

应从主题工作树的根目录中调用翻译命令。

有关MkDocs如何翻译内置主题的工作流概述，请参阅相应的[部分] 贡献指南 和 [翻译指南]。

[pybabel]：https：//babel.pocoo.org/en/latest/setup.html
[section]：../about/contributing.md#submitting-changes-to-the-builtin-themes
[Translation Guide]：translations.md

### 示例自定义主题本地化/翻译工作流程

> 注意：如果您的主题继承自已提供翻译目录的现有主题，则在MkDocs构建期间，您的主题的翻译将与父级主题的翻译合并。
> 这意味着您只需要关注添加的翻译。
> 但是，您仍将从父主题的翻译中受益。同时，您还可以覆盖父主题的任何翻译！

假设您正在使用自己的[mkdocs-basic-theme] 的 fork 并希望向其中添加翻译。

通过将HTML源中的文本包装在以下内容中的 ` {% trans %} ` 和 ` {% endtrans %} `，编辑模板：

```diff
--- a/basic_theme/base.html
+++ b/basic_theme/base.html
@@ -88,7 +88,7 @@

 <body>

-  <h1>This is an example theme for MkDocs.</h1>
+  <h1>{% trans %}This is an example theme for MkDocs. {% endtrans %}</h1>

   <p>
     It is designed to be read by looking at the theme HTML which is heavily
```

然后，像往常一样遵循翻译指南即可。

### 与主题一起打包翻译

虽然`extract_messages`命令创建的[可移植对象模板](`pot file`) 文件和`init_catalog`和`update_catalog`命令创建的[Portable Object (`po`) file]是用于创建和编辑翻译的有用的,但MkDocs没有直接使用它们，因此不需要在主题的打包版本中包含它们。当MkDocs使用翻译构建站点时，它只使用指定语言环境的二进制`mo`文件。因此，在[打包主题]时，请确保将其包含在"wheels"中，使用`MANIFEST.in`文件或其他方式。

然后，在构建Python包之前，您将希望确保每个语言环境的二进制 `mo`文件都是最新的，方法是为每个语言环境运行`compile_catalog`命令。MkDocs期望二进制`mo`文件位于`locales/<locale>/LC_MESSAGES/messages.mo`，`compile_catalog`命令会自动完成此任务。有关详细信息，请参阅[测试主题翻译]。

注意：
如我们的[翻译指南]中所述，MkDocs项目选择在代码存储库中包括“pot”和“po”文件，但不包括`mo`文件。这需要我们始终在打包新版本之前运行`compile_catalog`，无论是否对翻译进行了任何更改。但是，您可以选择主题的替代工作流程。最低限度，您需要确保每个版本包括正确位置的最新的`mo`文件。但是，如果您选择这样做，可以使用不同的进程生成这些`mo`文件。。

[可移植对象模板]：((`pot file`))
[Portable Object (`po`) file]：((`po`))
[打包主题]：#packing-themes
[测试主题翻译]：translations.md#testing-theme-translations