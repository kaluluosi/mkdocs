# MkDocs插件

安装、使用和创建MkDocs插件指南

---

## 安装插件

在使用插件之前，必须在系统上安装它。如果您正在使用MkDocs自带的插件，则在安装MkDocs时已经安装了它。但是，要安装第三方插件，需要确定适当的软件包名称并使用 `pip` 安装它：

```bash
pip install mkdocs-foo-plugin
```

插件安装成功后，它就可以使用了。它只需要在配置文件中[启用](#using-plugins)，[Catalog]仓库提供了大量可以安装和使用的插件的排名列表。

## 使用插件

[`plugins`][config]配置选项应包含一个构建站点时要使用的插件列表。每个“插件”都必须是分配给插件的字符串名称（请参阅给定插件的文档以确定其“名称”）。在此列出的插件必须已经[安装](#installing-plugins)。

```yaml
plugins:
  - search
```

某些插件可以提供自己的配置选项。如果您想设置任何配置选项，那么您可以嵌套一个键/值映射（`选项名称：选项值`），该插件支持给定插件的任何选项。请注意，插件名称必须跟随冒号（`:`），然后在新行上，选项名称和值必须缩进并用冒号分隔。如果您想为单个插件定义多个选项，每个选项必须在单独的行上定义。

```yaml
plugins:
  - search:
      lang: en
      foo: bar
```

有关特定插件可用的配置选项的信息，请参见该插件的文档。

要获取默认插件列表以及如何覆盖它们的列表，请参见[配置][config]文档。

## 开发插件

与MkDocs一样，插件必须用Python编写。通常期望每个插件都被分发为单独的Python模块，尽管可以在同一模块中定义多个插件。至少，MkDocs插件必须包括一个[BasePlugin]子类和一个指向它的[entry point]。

### BasePlugin

一个`mkdocs.plugins.BasePlugin`子类应该定义插件的行为。该类通常由在构建过程中特定事件上执行的操作以及插件的配置方案组成。

所有`BasePlugin`子类都包含以下属性：

#### config_scheme

配置验证实例的元组。每个条目都必须由一个二元组组成，在该二元组中第一个项目是配置选项的字符串名称，第二个项目是`mkdocs.config.config_options.BaseConfigOption`或其任何子类的实例。

例如，以下`config_scheme`定义了三个配置选项：`foo`，它接受一个字符串；`bar`，它接受一个整数；以及`baz`，它接受一个布尔值。

```python
class MyPlugin(mkdocs.plugins.BasePlugin):
    config_scheme = (
        ('foo', mkdocs.config.config_options.Type(str, default='a default value')),
        ('bar', mkdocs.config.config_options.Type(int, default=0)),
        ('baz', mkdocs.config.config_options.Type(bool, default=True))
    )
```

> NEW: **在1.4版本中新增：**
>
> ##### 子类化“Config”以指定配置模式
>
> 要获得类型安全功能，请在仅针对MkDocs 1.4+时定义配置模式作为类：
>
> ```python
> class MyPluginConfig(mkdocs.config.base.Config):
>     foo = mkdocs.config.config_options.Type(str, default='a default value')
>     bar = mkdocs.config.config_options.Type(int, default=0)
>     baz = mkdocs.config.config_options.Type(bool, default=True)
>
> class MyPlugin(mkdocs.plugins.BasePlugin[MyPluginConfig]):
>     ...
> ```
##### 配置定义示例

>! 例如：
>
> ```python
> from mkdocs.config import base, config_options as c
>
> class _ValidationOptions(base.Config):
>     enabled = c.Type(bool, default=True)
>     verbose = c.Type(bool, default=False)
>     skip_checks = c.ListOfItems(c.Choice(('foo', 'bar', 'baz')), default=[])
>
> class MyPluginConfig(base.Config):
>     definition_file = c.File(exists=True)  # required
>     checksum_file = c.Optional(c.File(exists=True))  # 可选，但如果指定则必须存在
>     validation = c.SubConfig(_ValidationOptions)
> ```
>
> 从用户的角度来看，`SubConfig`类似于类型为 `dict` 的数据，只要键值存在，就视为有效，它可以保留完整的验证功能：您定义了所有有效的键以及每个值应满足的要求。

> `ListOfItems`类似于类型为 `list` 的数据，但我们定义了每一个值必须遵循的约束。

> 这将接受以下配置：
>
> ```yaml
> my_plugin:
>   definition_file: configs/test.ini  # 相对于 mkdocs.yml
>   validation:
>     enabled: !ENV [CI, false]
>     verbose: true
>     skip_checks:
>       - foo
>       - baz
> ```
>）如果不符合限制或在 `config_scheme` 中未定义，则用户提供的任何设置都将引发`mkdocs.config.base.ValidationError`

#### config

一个字典，其中包含插件的配置选项，它将在`load_config`方法在配置验证完成后填充中。使用此属性访问用户提供的选项。

```python
def on_pre_build(self, config, **kwargs):
    if self.config['baz']:
        # 在这里实现“baz”功能...
```

> NEW: **在1.4版本中新增：**
>
> ### 安全的基于属性的访问
>
> 要获得类型安全功能，请仅针对MkDocs 1.4+以属性方式使用选项：

```python
def on_pre_build(self, config: MkDocsConfig, **kwargs):
    if self.config.baz:
        print(self.config.bar ** 2)  # OK，`int ** 2` 是有效的
```

所有`BasePlugin`子类都包含以下方法：

#### load_config(options)

从选项字典中加载配置。返回`(errors, warnings)`元组。MkDocs在配置验证期间会调用此方法，因此插件不需要调用它。

#### on_&lt;event_name&gt;()

为特定[事件]定义行为的可选方法。插件应在这些方法中定义其行为。将 `<event_name>` 替换为实际事件名称。例如，`预构建`事件将在`on_pre_build`方法中定义。

大多数事件接受一个位置参数和各种关键字参数。通常期望位置参数由插件修改（或替换），并返回。如果未返回任何内容（该方法返回`None`），则使用原始，未修改的对象。关键字参数仅是提供上下文和/或提供可能用于确定应如何修改位置参数的数据。最好使用`**kwargs`接受关键字参数。如果在MkDocs的将来版本中向事件提供了其他关键字，则无需修改插件。

例如，以下事件将向主题配置添加一个附加的`static_template`：

```python
class MyPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        config['theme'].static_templates.add('my_template.html')
        return config
```

> NEW: **在1.4版本中新增：**
>
> 要获得类型安全功能，请仅针对MkDocs 1.4+操作属性：

```python
class MyPlugin(BasePlugin):
    def on_config(self, config: MkDocsConfig):
        config.theme.static_templates.add('my_template.html')
        return config
```

### 事件

有三种类型的事件：[全局事件]，[页面事件]和[模板事件]。

<details class="card">
  <summary>
    查看所有插件事件之间的关系图表
  </summary>
  <div class="card-body">
    <ul>
      <li>事件本身显示为黄色，显示其参数。
      <li>箭头显示每个事件的参数和输出的流动。
          有时它们没有被省略。
      <li>事件按时间顺序从上到下排序。
      <li>点状线出现在从全局事件到特定页面事件的分裂处。
      <li>单击事件的标题以跳转到其说明。
    </ul>
--8<-- "docs/img/plugin-events.svg"
  </div>
</details>
<br>

#### 一次性事件

一次性事件每个`mkdocs`调用运行一次。它们与[全局事件](#global-events)唯一不同的情况是对于`mkdocs serve`，全局事件会运行多次 - 每个*构建*一次。

##### on_startup

::: mkdocs.plugins.BasePlugin.on_startup
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_shutdown

::: mkdocs.plugins.BasePlugin.on_shutdown
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_serve

::: mkdocs.plugins.BasePlugin.on_serve
    options:
        show_root_heading: false
        show_root_toc_entry: false

#### 全局事件

全局事件在构建过程的开始或结束时调用一次。在这些事件中进行的任何更改都将对整个站点产生全局影响。

##### on_config

::: mkdocs.plugins.BasePlugin.on_config
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_pre_build

::: mkdocs.plugins.BasePlugin.on_pre_build
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_files

::: mkdocs.plugins.BasePlugin.on_files
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_nav

::: mkdocs.plugins.BasePlugin.on_nav
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_env

::: mkdocs.plugins.BasePlugin.on_env
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_post_build

::: mkdocs.plugins.BasePlugin.on_post_build
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_build_error

::: mkdocs.plugins.BasePlugin.on_build_error
    options:
        show_root_heading: false
        show_root_toc_entry: false

#### 模板事件

模板事件为每个非页面模板调用一次。每个模板事件将为在[extra_templates]配置设置中定义的任何模板以及主题中定义的任何[static_templates]调用。所有模板事件都在[env]事件之后，并在任何[页面事件]之前调用。

##### on_pre_template

::: mkdocs.plugins.BasePlugin.on_pre_template
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_template_context

::: mkdocs.plugins.BasePlugin.on_template_context
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_post_template

::: mkdocs.plugins.BasePlugin.on_post_template
    options:
        show_root_heading: false
        show_root_toc_entry: false

#### 页面事件

每个页面事件针对站点中包含的每个Markdown页面调用一次。所有
[页面事件]都是在[post_template]事件之后，在[post_build]事件之前调用。

##### on_pre_page

::: mkdocs.plugins.BasePlugin.on_pre_page
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_read_source

::: mkdocs.plugins.BasePlugin.on_page_read_source
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_markdown

::: mkdocs.plugins.BasePlugin.on_page_markdown
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_content

::: mkdocs.plugins.BasePlugin.on_page_content
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_page_context

::: mkdocs.plugins.BasePlugin.on_page_context
    options:
        show_root_heading: false
        show_root_toc_entry: false

##### on_post_page

::: mkdocs.plugins.BasePlugin.on_post_page
    options:
        show_root_heading: false
        show_root_toc_entry: false

### 事件优先级

对于每个事件类型，插件的相应方法按照它们在`plugins` [config]中的出现顺序进行调用。

自MkDocs 1.4以来，插件可以选择为其事件设置优先级值。具有更高优先级的事件首先被调用。没有选择优先级的事件默认为 0。具有相同优先级的事件按照它们在config中出现的顺序排序。

#### ::: mkdocs.plugins.event_priority

### 处理错误

MkDocs定义了四种错误类型：

#### ::: mkdocs.exceptions.MkDocsException

#### ::: mkdocs.exceptions.ConfigurationError

#### ::: mkdocs.exceptions.BuildError

#### ::: mkdocs.exceptions.PluginError

意外和未捕获的例外会中断构建过程并生成典型的Python回溯，这对于调试您的代码非常有用。然而，用户通常会觉得追踪太复杂，经常会错过有用的错误消息。因此，MkDocs会捕获上述任何一种错误，检索错误消息，并立即退出并显示有用的消息。

因此，您可能需要在插件中捕获任何异常并引发一个`PluginError`，传入自己的自定义消息，以便构建过程被中止并显示有用的消息。

对于例如：

```python
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin


class MyPlugin(BasePlugin):
    def on_post_page(self, output, page, config, **kwargs):
        try:
            # 可能引发KeyError的代码
            ...
        except KeyError as error:
            raise PluginError(str(error))

    def on_build_error(self, error, **kwargs):
        # 进行清理的一些代码
        ...
```

### 插件日志记录

MkDocs提供了一个`get_plugin_logger`函数，返回可用于记录消息的记录器。

#### ::: mkdocs.plugins.get_plugin_logger

### 入口点

插件需要打包为Python库（与MkDocs分开在PyPI上分发），并且需要通过setuptools `entry_points`向每个Plugin注册。将以下内容添加到您的`setup.py`脚本中：

```python
entry_points={
    'mkdocs.plugins': [
        'pluginname = path.to.some_plugin:SomePluginClass',
    ]
}
```

`pluginname`将是用户使用的名称（在配置文件中），而`path.to.some_plugin:SomePluginClass`将是可导入插件本身，其中`SomePluginClass`是定义插件行为的[BasePlugin]的子类。自然，可以在同一模块中定义多个Plugin类。只需将每个定义为独立的入口点即可。

```python
entry_points={
    'mkdocs.plugins': [
        'featureA = path.to.my_plugins:PluginA',
        'featureB = path.to.my_plugins:PluginB'
    ]
}
```

注意，注册插件不会激活它。用户仍然需要通过配置告诉MkDocs使用它。

### 发布插件

应将软件包发布在[PyPI]上，然后将其添加到[Catalog]以供发现。强烈建议插件具有唯一的插件名称（entry point名称）。

[BasePlugin]:#baseplugin
[config]: ../user-guide/configuration.md#plugins
[entry point]: #entry-point
[env]: #on_env
[events]: #events
[extra_templates]: ../user-guide/configuration.md#extra_templates
[Global Events]: #global-events
[Page Events]: #page-events
[post_build]: #on_post_build
[post_template]: #on_post_template
[static_templates]: ../user-guide/configuration.md#static_templates
[Template Events]: #template-events
[catalog]: https://github.com/mkdocs/catalog