# GraphQL API

## Defining the Schema Class

A plugin can extend NetPoint's GraphQL API by registering its own schema class. By default, NetPoint will attempt to import `graphql.schema` from the plugin, if it exists. This path can be overridden by defining `graphql_schema` on the PluginConfig instance as the dotted path to the desired Python class. This class must be a subclass of `graphene.ObjectType`.

### Example

```python
# graphql.py
import graphene
from netpoint.graphql.types import NetPointObjectType
from netpoint.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models

class MyModelType(NetPointObjectType):

    class Meta:
        model = models.MyModel
        fields = '__all__'
        filterset_class = filtersets.MyModelFilterSet

class MyQuery(graphene.ObjectType):
    mymodel = ObjectField(MyModelType)
    mymodel_list = ObjectListField(MyModelType)

schema = MyQuery
```

## GraphQL Objects

NetPoint provides two object type classes for use by plugins.

::: netpoint.graphql.types.BaseObjectType
    options:
      members: false

::: netpoint.graphql.types.NetPointObjectType
    options:
      members: false

## GraphQL Fields

NetPoint provides two field classes for use by plugins.

::: netpoint.graphql.fields.ObjectField
    options:
      members: false

::: netpoint.graphql.fields.ObjectListField
    options:
      members: false
