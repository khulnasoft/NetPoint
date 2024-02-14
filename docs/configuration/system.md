# System Parameters

## BASE_PATH

Default: None

The base URL path to use when accessing NetPoint. Do not include the scheme or domain name. For example, if installed at https://example.com/netpoint/, set:

```python
BASE_PATH = 'netpoint/'
```

---

## DEFAULT_LANGUAGE

Default: `en-us` (US English)

Defines the default preferred language/locale for requests that do not specify one. This is used to alter e.g. the display of dates and numbers to fit the user's locale. See [this list](http://www.i18nguy.com/unicode/language-identifiers.html) of standard language codes. (This parameter maps to Django's [`LANGUAGE_CODE`](https://docs.djangoproject.com/en/stable/ref/settings/#language-code) internal setting.)

!!! note
    Altering this parameter will *not* change the language used in NetPoint. We hope to provide translation support in a future NetPoint release.

---

## DOCS_ROOT

Default: `$INSTALL_ROOT/docs/`

The filesystem path to NetPoint's documentation. This is used when presenting context-sensitive documentation in the web UI. By default, this will be the `docs/` directory within the root NetPoint installation path. (Set this to `None` to disable the embedded documentation.)

---

## EMAIL

In order to send email, NetPoint needs an email server configured. The following items can be defined within the `EMAIL` configuration parameter:

* `SERVER` - Hostname or IP address of the email server (use `localhost` if running locally)
* `PORT` - TCP port to use for the connection (default: `25`)
* `USERNAME` - Username with which to authenticate
* `PASSWORD` - Password with which to authenticate
* `USE_SSL` - Use SSL when connecting to the server (default: `False`)
* `USE_TLS` - Use TLS when connecting to the server (default: `False`)
* `SSL_CERTFILE` - Path to the PEM-formatted SSL certificate file (optional)
* `SSL_KEYFILE` - Path to the PEM-formatted SSL private key file (optional)
* `TIMEOUT` - Amount of time to wait for a connection, in seconds (default: `10`)
* `FROM_EMAIL` - Sender address for emails sent by NetPoint

!!! note
    The `USE_SSL` and `USE_TLS` parameters are mutually exclusive.

Email is sent from NetPoint only for critical events or if configured for [logging](#logging). If you would like to test the email server configuration, Django provides a convenient [send_mail()](https://docs.djangoproject.com/en/stable/topics/email/#send-mail) function accessible within the NetPoint shell:

```no-highlight
# python ./manage.py nbshell
>>> from django.core.mail import send_mail
>>> send_mail(
  'Test Email Subject',
  'Test Email Body',
  'noreply-netpoint@example.com',
  ['users@example.com'],
  fail_silently=False
)
```

---

## ENABLE_LOCALIZATION

Default: False

Determines if localization features are enabled or not. This should only be enabled for development or testing purposes as netpoint is not yet fully localized. Turning this on will localize numeric and date formats (overriding any configured [system defaults](./date-time.md#date-and-time-formatting)) based on the browser locale as well as translate certain strings from third party modules.

---

## HTTP_PROXIES

Default: None

A dictionary of HTTP proxies to use for outbound requests originating from NetPoint (e.g. when sending webhook requests). Proxies should be specified by schema (HTTP and HTTPS) as per the [Python requests library documentation](https://requests.readthedocs.io/en/latest/user/advanced/#proxies). For example:

```python
HTTP_PROXIES = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}
```

---

## INTERNAL_IPS

Default: `('127.0.0.1', '::1')`

A list of IP addresses recognized as internal to the system, used to control the display of debugging output. For
example, the debugging toolbar will be viewable only when a client is accessing NetPoint from one of the listed IP
addresses (and [`DEBUG`](#debug) is true).

---

## JINJA2_FILTERS

Default: `{}`

A dictionary of custom jinja2 filters with the key being the filter name and the value being a callable. For more information see the [Jinja2 documentation](https://jinja.palletsprojects.com/en/3.1.x/api/#custom-filters). For example:

```python
def uppercase(x):
    return str(x).upper()

JINJA2_FILTERS = {
    'uppercase': uppercase,
}
```

---

## LOGGING

By default, all messages of INFO severity or higher will be logged to the console. Additionally, if [`DEBUG`](#debug) is False and email access has been configured, ERROR and CRITICAL messages will be emailed to the users defined in [`ADMINS`](#admins).

The Django framework on which NetPoint runs allows for the customization of logging format and destination. Please consult the [Django logging documentation](https://docs.djangoproject.com/en/stable/topics/logging/) for more information on configuring this setting. Below is an example which will write all INFO and higher messages to a local file:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/netpoint.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },
}
```

### Available Loggers

* `netpoint.<app>.<model>` - Generic form for model-specific log messages
* `netpoint.auth.*` - Authentication events
* `netpoint.api.views.*` - Views which handle business logic for the REST API
* `netpoint.reports.*` - Report execution (`module.name`)
* `netpoint.scripts.*` - Custom script execution (`module.name`)
* `netpoint.views.*` - Views which handle business logic for the web UI

---

## MEDIA_ROOT

Default: $INSTALL_ROOT/netpoint/media/

The file path to the location where media files (such as image attachments) are stored. By default, this is the `netpoint/media/` directory within the base NetPoint installation path.

---

## REPORTS_ROOT

Default: `$INSTALL_ROOT/netpoint/reports/`

The file path to the location where [custom reports](../customization/reports.md) will be kept. By default, this is the `netpoint/reports/` directory within the base NetPoint installation path.

---

## SCRIPTS_ROOT

Default: `$INSTALL_ROOT/netpoint/scripts/`

The file path to the location where [custom scripts](../customization/custom-scripts.md) will be kept. By default, this is the `netpoint/scripts/` directory within the base NetPoint installation path.

---

## SEARCH_BACKEND

Default: `'netpoint.search.backends.CachedValueSearchBackend'`

The dotted path to the desired search backend class. `CachedValueSearchBackend` is currently the only search backend provided in NetPoint, however this setting can be used to enable a custom backend. 

---

## STORAGE_BACKEND

Default: None (local storage)

The backend storage engine for handling uploaded files (e.g. image attachments). NetPoint supports integration with the [`django-storages`](https://django-storages.readthedocs.io/en/stable/) package, which provides backends for several popular file storage services. If not configured, local filesystem storage will be used.

The configuration parameters for the specified storage backend are defined under the `STORAGE_CONFIG` setting.

---

## STORAGE_CONFIG

Default: Empty

A dictionary of configuration parameters for the storage backend configured as `STORAGE_BACKEND`. The specific parameters to be used here are specific to each backend; see the [`django-storages` documentation](https://django-storages.readthedocs.io/en/stable/) for more detail.

If `STORAGE_BACKEND` is not defined, this setting will be ignored.

---
