# Data Backends

[Data sources](../../models/core/datasource.md) can be defined to reference data which exists on systems of record outside NetPoint, such as a git repository or Amazon S3 bucket. Plugins can register their own backend classes to introduce support for additional resource types. This is done by subclassing NetPoint's `DataBackend` class.

```python title="data_backends.py"
from netpoint.data_backends import DataBackend

class MyDataBackend(DataBackend):
    name = 'mybackend'
    label = 'My Backend'
    ...
```

To register one or more data backends with NetPoint, define a list named `backends` at the end of this file:

```python title="data_backends.py"
backends = [MyDataBackend]
```

!!! tip
    The path to the list of search indexes can be modified by setting `data_backends` in the PluginConfig instance.

::: netpoint.data_backends.DataBackend
