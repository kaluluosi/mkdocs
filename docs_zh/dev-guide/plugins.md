# MkDocs插件

安装，使用和创建 MkDocs插件的指南

---

## 安装插件

在使用插件之前，必须将其安装在系统上。如果您使用的是MkDocs自带的插件，则在安装MkDocs时已安装。但是，要安装第三方插件，您需要确定适当的包名称并使用 pip 安装它：

```bash
pip install mkdocs-foo-plugin
```

插件成功安装后即可使用。您只需要在配置文件中[启用](#使用插件)它。 [Catalog]存储库具有大量排名的插件列表，您可以安装并使用这些插件。

## 使用插件

[`plugins`] [config]配置选项应包含要在构建站点时使用的插件列表。每个"插件"都必须是分配给插件的字符串名称（请参阅给定插件的文档以确定其名称）。此处列出的插件必须已经[安装](#安装插件)。

```yaml
plugins:
  - search
```

一些插件可能提供他们自己的配置选项。如果您想设置任何配置选项，则可以嵌套任何给定插件支持的键/值映射（`option_name: option value`）。请注意，必须在插件名称后跟随冒号（`:`），然后在新行上缩进并由冒号隔开选项名称和值。如果您要为单个插件定义多个选项，则必须在单独的行上定义每个选项。

```yaml
plugins:
  - search:
      lang: en
      foo: bar
```

有关特定插件提供的配置选项的信息，请参阅该插件的文档。

有关默认插件列表及如何覆盖它们的信息，请参阅[configuration] [config]文档。

## 开发插件

与MkDocs一样，插件必须以Python编写。通常期望每个插件是作为单独的Python模块分发的，尽管可以在同一模块中定义多个插件。在最少的情况下，MkDocs插件必须包含一个[BasePlugin]子类和指向它的[entry point]。

### BasePlugin

`mkdocs.plugins.BasePlugin`的子类应定义插件的行为。该类通常包含在构建过程中特定事件上执行的操作以及插件的配置方案。

所有的` BasePlugin`子类都包含以下属性：

#### config_scheme

配置验证实例的元组。每个项目都必须包括一个两个项目的元组，其中第一个项目是配置选项的字符串名称，第二个项目是`mkdocs.config.config_options.BaseConfigOption`或其子类的任何实例。

例如，以下`config_scheme`定义了三个配置选项：`foo`，它接受一个字符串; `bar`，它接受一个整数;以及`baz`，它接受一个布尔值。

```python
class MyPlugin(mkdocs.plugins.BasePlugin):
    config_scheme = (
        ('foo', mkdocs.config.config_options.Type(str, default='a default value')),
        ('bar', mkdocs.config.config_options.Type(int, default=0)),
        ('baz', mkdocs.config.config_options.Type(bool, default=True))
    )
```

> 新： **自MkDocs版本1.4起新推出**
>
>##### 子类化`Config`以指定配置模式
>
> 为了获得类型安全性的好处，如果您仅针对MkDocs 1.4+，则请将配置模式定义为类：
>
> ```python
> class MyPluginConfig(mkdocs.config.base.Config):
>     foo = mkdocs.config.config_options.Type(str, default='a default value')
>     bar = mkdocs.config.config_options.Type(int, default=0)
>     baz = mkdocs.config.config_options.Type(bool, default=True)
>
> class MyPlugin(mkdocs.plugins.BasePlugin[MyPluginConfig]):
>     ...
> ```

##### 配置定义示例

>! 示例：
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
>     checksum_file = c.Optional(c.File(exists=True))  # can be None but must exist if specified
>     validation = c.SubConfig(_ValidationOptions)
> ```
>
> 从用户的角度来看，`SubConfig`类似于`Type(dict)`，只是它也保留了完全的验证能力：您定义了所有有效的键以及每个值应该遵守的内容。
>
> `ListOfItems`类似于`Type(list)`，但是我们再次定义了每个值必须遵循的约束。
>
> 这将接受以下配置：
>
> ```yaml
> my_plugin:
>   definition_file:
> relative to mkdocs.ymlconfigs/test.ini  # 4.1
>   validation:
>     enabled: !ENV [CI, false]
>     verbose: true
>     skip_checks:
>       - foo
>       - baz
> ```
<!-- -->
>? 示例：
>
> ```python
> import numbers
> from mkdocs.config import base, config_options as c
>
> class _Rectangle(base.Config):
>     width = c.Type(numbers.Real)  # required
>     height = c.Type(numbers.Real)  # required
>
> class MyPluginConfig(base.Config):
>     add_rectangles = c.ListOfItems(c.SubConfig(_Rectangle))  # required
> ```
>
> 在此示例中，我们定义了一个复杂项列表，并通过将具体的`SubConfig`传递给`ListOfItems`来实现它。
>
> 这将接受以下配置：
>
> ```yaml
> my_plugin:
>   add_rectangles:
>     - width: 5
>       height: 7
>     - width: 12
>       height: 2
> ```

当加载用户的配置时，上述方案将用于验证配置并填充用户未提供的设置的任何默认值。验证类可以是`mkdocs.config.config_options`中提供的任意类或第三方子类，由插件定义。

用户提供的任何设置，如果未通过验证或未在`config_scheme`中定义，则会引发`mkdocs.config.base.ValidationError`。

#### config

插件的配置选项字典，由`load_config`方法在配置验证完成后填充。使用此属性访问用户提供的选项。

```python
def on_pre_build(self, config, **kwargs):
    if self.config['baz']:
        # 在此执行“baz”功能...
```

> 新： **从MkDocs Version 1.4  新增**
>
> ##### 安全的属性访问
>
> 为了获得类型安全性的好处，如果仅针对MkDocs 1.4+，则使用属性访问选项而不是字典访问选项:
>
> ```python
> def on_pre_build(self, config: MkDocsConfig, **kwargs):
>     if self.config.baz:
>         print(self.config.bar ** 2)  # OK, `int ** 2` is valid.
> ```

所有 `BasePlugin`子类都包含以下方法：

#### load_config(options)

从`options`字典中加载配置。返回一个`(errors, warnings)`元组。MkDocs在验证期间调用此方法，插件应该不需要调用它。

#### on_&lt;event_name&gt;()

定义具体[event]的行为的可选方法。插件应该在这些方法中定义它们的行为。将`<event_name>`替换为实际事件的名称。例如，`pre_build`事件将在`on_pre_build`方法中定义。

大多数事件都接受一个位置参数和各种关键字参数。通常期望位置参数将被修改（或替换），然后返回。如果什么都不返回（方法返回`None`），则使用原始的未修改对象。关键字参数仅提供上下文和/或提供可以用于确定如何修改位置参数的数据。最好接受关键字参数作为`**kwargs`。在MkDocs的将来版本中，如果事件提供了其他关键字，则无需更改插件。

例如，以下事件将向主题配置添加额外的静态模板：

```python
class MyPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        config['theme'].static_templates.add('my_template.html')
        return config
```

> 新： **从MkDocs 1.4版本开始新增**
>
> 为了获得类型安全的好处，如果仅针对MkDocs 1.4+，请将配置选项作为属性访问：
>
> ```python
> class MyPlugin(BasePlugin):
>     def on_config(self, config: MkDocsConfig):
>         config.theme.static_templates.add('my_template.html')
>         return config
> ```

### 事件

有三种类型的事件：[全局事件]，[页面事件]和[模板事件]。

<details class="card">
  <summary>
    查看包含所有插件事件关系的图表
  </summary>
  <div class="card-body">
    <ul>
      <li>事件本身显示为黄色，并附有其参数。
      <li>箭头显示每个事件的参数和输出的流动。
          有时会省略。
      <li>事件按时间顺序从上到下排序。
      <li>虚线出现在全局事件到每个页面事件的拆分处。
      <li>单击事件标题可跳转到其描述。
    </ul>
--8<-- "docs/img/plugin-events.svg"
  </div>
</details>
<br>

#### 一次性事件

每次`mkdocs`调用时，一次性事件只运行一次。它们唯一与[全局事件]不同的情况是对于`mkdocs serve`：与这些事件不同，全局事件将多次运行 - 每次*构建*一次。

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

全局事件在构建过程的开始或结束时调用一次。在这些事件中所做的任何更改都会对整个站点产生全局影响。

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

模板事件为每个非页面模板调用一次。每个模板事件都将为在[extra_templates]配置设置中定义的每个模板以及主题中定义的任何[static_templates]调用。所有模板事件都在[env]事件之后，在任何[页面事件]之前调用。

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

页面事件一次为每个包含在站点中的Markdown页面调用一次。所有页面事件都在[post_template]事件之后，并在[post_build]事件之前调用。

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

对于每种事件类型，插件的相应方法按照它们在`plugins`[config]中出现的顺序进行调用。

自MkDocs 1.4以来，插件可以选择为其事件设置优先级值。具有较高优先级的事件将首先被调用。没有选择优先级的事件默认为0。具有相同优先级的事件按照它们在配置中出现的顺序排序。

#### ::: mkdocs.plugins.event_priority

### 处理错误

MkDocs定义了四种错误类型：

#### ::: mkdocs.exceptions.MkDocsException

#### ::: mkdocs.exceptions.ConfigurationError

#### ::: mkdocs.exceptions.BuildError

#### ::: mkdocs.exceptions.PluginError

未预料到和未捕获的异常将中断构建过程并产生典型的Python回溯，这对于调试代码很有用。但是，用户通常会发现回溯难以承受，而且经常会错过有用的错误消息。因此，MkDocs会捕获上述任何错误类型，检索错误消息，并立即退出，仅显示有用的消息。

因此，您可能想要捕获插件中的任何异常并引发`PluginError`，传入自己定制的消息，以便构建过程中止并显示有用的消息。

对于每个异常，都会触发[on_build_error]事件。

例如：

```python
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin


class MyPlugin(BasePlugin):
    def on_post_page(self, output, page, config, **kwargs):
        try:
            # 可能会引发KeyError的代码
            ...
        except KeyError as error:
            raise PluginError(str(error))

    def on_build_error(self, error, **kwargs):
        # 清理一些代码
        ...
```

### 在插件中记录

MkDocs提供了`get_plugin_logger`函数，该函数返回可用于记录消息的记录器。

#### ::: mkdocs.plugins.get_plugin_logger

### 入口点

插件需要打包为Python库（与MkDocs分开在PyPI上分发），并且每个插件必须通过setuptools entry_points 注册为插件。将以下内容添加到您的`setup.py`脚本中：

```python
entry_points={
    'mkdocs.plugins': [
        'pluginname = path.to.some_plugin:SomePluginClass',
    ]
}
```

`pluginname` 将是用户使用的名称（在配置文件中），而`path.to.some_plugin:SomePluginClass` 则为可导入的插件(`from path.to.some_plugin import SomePluginClass`)，其中`SomePluginClass` 是[BasePlugin]的子类，定义了插件行为。自然，同一模块中可能存在多个Plugin类，只需将每个定义为单独的入口点即可。

```python
entry_points={
    'mkdocs.plugins': [
        'featureA = path.to.my_plugins:PluginA',
        'featureB = path.to.my_plugins:PluginB'
    ]
}
```

请注意，注册插件不会激活它