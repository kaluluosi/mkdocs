# 开发主题

创建和分发自定义主题的指南。

---

注意:
如果你正在寻找现有的第三方主题，它们在[社区Wiki]页面和[MkDocs项目目录][catalog]中列出。如果你想分享你创建的主题，你应该在那里列出它。

在创建新主题时，你可以按照本指南中的步骤从头开始创建，也可以下载 `mkdocs-basic-theme` 作为一个基本，但完整的主题，其中包含所有所需的样板文件。你可以在[ GitHub上][基本主题]找到此基本主题。它包含了详细的注释来描述不同的功能及其用法。

[社区Wiki]：https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes
[目录]：https://github.com/mkdocs/catalog#-theming
[基本主题]：https://github.com/mkdocs/mkdocs-basic-theme

## 创建自定义主题

自定义主题所需的最少要求是 `main.html` [Jinja2
template] 文件，它位于不是[docs_dir]的子目录中。在 `mkdocs.yml` 中，将 [`theme.custom_dir`][custom_dir]
选项设置为包含 `main.html` 的目录路径。路径应该相对于配置文件。例如，给定这个示例项目布局：

```text
mkdocs.yml
docs/
    index.md
    about.md
custom_theme/
    main.html
    ...
```

... 你应该在 `mkdocs.yml` 中包含以下设置，以使用自定义主题目录：

```yaml
theme:
  name: null
  custom_dir: 'custom_theme/'
```

> 注意：
> 通常，在构建你自己的自定义主题时，主题.[name]
> 配置设置应设为 `null`。然而，如果
> theme.[custom_dir] 配置值与现有主题结合使用，则可以使用 theme.[custom_dir] 来替换内置主题中的特定部分。例如，对于上面的布局，如果你设置
> `name: "mkdocs"`，则主题.[custom_dir] 中的 `main.html` 文件将替换内置主题中同名的文件，但除此之外 `mkdocs` 主题将保持不变。如果你想对现有主题进行微调，这非常有用。
>
> 关于更具体的信息，请参阅[自定义主题]。
<!-- -->
> 警告：
> 主题的[配置]定义在 `mkdocs_theme.yml` 文件中载入并非来自 `theme.custom_dir`。当 `theme.custom_dir` 中存在整个主题，并且设置 `theme.name` 为 `null` 时，整个主题配置必须在 `mkdocs.yml` 文件中的 [theme] 配置选项中定义。
>
> 然而，当主题 [打包] 用于分发并使用 `theme.name` 配置选项加载时，将需要一个 `mkdocs_theme.yml` 文件作为主题。

[自定义主题]：../user-guide/customizing-your-theme.md#using-the-theme-custom_dir
[custom_dir]: ../user-guide/configuration.md#custom_dir
[name## 支持主题本地化/翻译

虽然内置主题提供了模板本地化/翻译的支持，但自定义主题和第三方主题可能选择不提供此功能。但无论如何，在“theme”配置选项的[`locale`]（#locale）设置始终存在，并被其他部分依赖。因此，建议所有第三方主题使用相同的设置来指定语言，而不考虑它们用于翻译的系统。这样，用户无论选择哪个主题，都会体验到一致的行为。

翻译管理的方法取决于主题开发人员。但是，如果主题开发人员选择使用内置主题使用的相同机制，则以下部分概述如何启用并利用MkDocs使用的相同命令。

[本地化/翻译]:../user-guide/localizing-your-theme.md

### 使用本地化/翻译命令

警告：因为**[pybabel]未默认安装**，大多数用户不会安装pybabel，因此主题开发人员和/或翻译者应确保已安装必要的依赖关系（使用`pip install mkdocs [i18n]`），以便命令可供使用。

翻译命令应从您的主题的工作树根目录调用。

有关MkDocs用于翻译内置主题的工作流程的概述，请参见Contributing Guide的相应[部分]和[翻译指南]。

[pybabel]: https://babel.pocoo.org/en/latest/setup.html
[部分]：../about/contributing.md#submitting-changes-to-the-builtin-themes
[翻译指南]：翻译.md

### 示例自定义主题本地化/翻译工作流程

>注意：如果您的主题继承自已提供翻译目录的现有主题，则在MkDocs构建期间，您的主题的翻译将与父主题的翻译合并。
>这意味着您只需要专注于添加的翻译。但是，您仍将从父主题的翻译中获益。同时，您可以覆盖父主题的任何翻译！

假设您正在自己的[mkdocs-basic-theme]分支上工作，并希望为其添加翻译。

通过在您的HTML源中使用`{% trans％}`和` {% endtrans％}`将文本包装在模板中进行编辑：：

```diff
--- a/basic_theme/base.html
+++ b/basic_theme/base.html
@@ -88,7 +88,7 @@

 <body>

-  <h1>This is an example theme for MkDocs.</h1>
+  <h1>{% trans %}This is an example theme for MkDocs.{% endtrans %}</h1>

   <p>
     It is designed to be read by looking at the theme HTML which is heavily
```

然后，像往常一样遵循[Translation Guide]来运行您的翻译。

### 打包翻译与主题

虽然由`extract_messages`命令创建的Portable Object Template（`pot`）文件和由`init_catalog`和`update_catalog`命令创建的Portable Object（`po`）文件适用于创建和编辑翻译，但它们不直接被MkDocs使用，也不需要在主题的打包版本中包含在内。当MkDocs使用翻译构建网站时，它仅使用指定语言环境的二进制`mo`文件（s）。因此，在[打包主题]时，请确保在“wheels”中包含它，使用`MANIFEST.in`文件或其他方式。

然后，在构建Python程序包之前，您将希望通过为每个区域设置运行`compile_catalog`命令来确保每个区域设置的二进制`mo`文件是最新的。 MkDocs希望将二进制`mo`文件位于`locales/<locale>/LC_MESSAGES/messages.mo`，`compile_catalog`命令为您自动执行此操作。有关详细信息，请参见[测试主题翻译]。

注：
如我们的[Translation Guide]所述，MkDocs项目选择将`pot`和`po`文件包含在我们的代码存储库中，但不包括`mo`文件。这要求我们在打包新版本之前始终运行`compile_catalog`，而不管是否对翻译进行了任何更改。但是，您可以选择自己的代替工作流程主题。最少，您需要确保在每个版本中在正确的位置包括最新的`mo`文件。但是，如果选择这样做，您可以使用其他过程生成这些`mo`文件。

[打包主题]：＃打包主题
[测试主题翻译]：翻译.md#测试主题翻译