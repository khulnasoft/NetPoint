from .navigation import *
from .registration import *
from .templates import *
from .utils import *
from netpoint.plugins import PluginConfig


# TODO: Remove in v4.0
warnings.warn(f"{__name__} is deprecated. Import from netpoint.plugins instead.", DeprecationWarning)
