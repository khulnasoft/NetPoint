# Tables

NetPoint employs the [`django-tables2`](https://django-tables2.readthedocs.io/) library for rendering dynamic object tables. These tables display lists of objects, and can be sorted and filtered by various parameters.

## NetPointTable

To provide additional functionality beyond what is supported by the stock `Table` class in `django-tables2`, NetPoint provides the `NetPointTable` class. This custom table class includes support for:

* User-configurable column display and ordering
* Custom field & custom link columns
* Automatic prefetching of related objects

It also includes several default columns:

* `pk` - A checkbox for selecting the object associated with each table row (where applicable)
* `id` - The object's numeric database ID, as a hyperlink to the object's view (hidden by default)
* `actions` - A dropdown menu presenting object-specific actions available to the user

### Example

```python
# tables.py
import django_tables2 as tables
from netpoint.tables import NetPointTable
from .models import MyModel

class MyModelTable(NetPointTable):
    name = tables.Column(
        linkify=True
    )
    ...

    class Meta(NetPointTable.Meta):
        model = MyModel
        fields = ('pk', 'id', 'name', ...)
        default_columns = ('pk', 'name', ...)
```

### Table Configuration

The NetPointTable class features dynamic configuration to allow users to change their column display and ordering preferences. To configure a table for a specific request, simply call its `configure()` method and pass the current HTTPRequest object. For example:

```python
table = MyModelTable(data=MyModel.objects.all())
table.configure(request)
```

This will automatically apply any user-specific preferences for the table. (If using a generic view provided by NetPoint, table configuration is handled automatically.)

## Columns

The table column classes listed below are supported for use in plugins. These classes can be imported from `netpoint.tables.columns`.

::: netpoint.tables.BooleanColumn
    options:
      members: false

::: netpoint.tables.ChoiceFieldColumn
    options:
      members: false

::: netpoint.tables.ColorColumn
    options:
      members: false

::: netpoint.tables.ColoredLabelColumn
    options:
      members: false

::: netpoint.tables.ContentTypeColumn
    options:
      members: false

::: netpoint.tables.ContentTypesColumn
    options:
      members: false

::: netpoint.tables.MarkdownColumn
    options:
      members: false

::: netpoint.tables.TagColumn
    options:
      members: false

::: netpoint.tables.TemplateColumn
    options:
      members:
        - __init__

## Extending Core Tables

!!! info "This feature was introduced in NetPoint v3.7."

Plugins can register their own custom columns on core tables using the `register_table_column()` utility function. This allows a plugin to attach additional information, such as relationships to its own models, to built-in object lists.

```python
import django_tables2
from django.utils.translation import gettext_lazy as _

from dcim.tables import SiteTable
from utilities.tables import register_table_column

mycol = django_tables2.Column(
    verbose_name=_('My Column'),
    accessor=django_tables2.A('description')
)

register_table_column(mycol, 'foo', SiteTable)
```

You'll typically want to define an accessor identifying the desired model field or relationship when defining a custom column. See the [django-tables2 documentation](https://django-tables2.readthedocs.io/) for more information on creating custom columns.

::: utilities.tables.register_table_column
