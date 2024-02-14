# Error Reporting

## Sentry

### Enabling Error Reporting

NetPoint supports native integration with [Sentry](https://sentry.io/) for automatic error reporting. To enable this functionality, set `SENTRY_ENABLED` to True and define your unique [data source name (DSN)](https://docs.sentry.io/product/sentry-basics/concepts/dsn-explainer/) in `configuration.py`.

```python
SENTRY_ENABLED = True
SENTRY_DSN = "https://examplePublicKey@o0.ingest.sentry.io/0"
```

Setting `SENTRY_ENABLED` to False will disable the Sentry integration.

### Assigning Tags

You can optionally attach one or more arbitrary tags to the outgoing error reports if desired by setting the `SENTRY_TAGS` parameter:

```python
SENTRY_TAGS = {
    "custom.foo": "123",
    "custom.bar": "abc",
}
```

!!! warning "Reserved tag prefixes"
    Avoid using any tag names which begin with `netpoint.`, as this prefix is reserved by the NetPoint application.

### Testing

Once the configuration has been saved, restart the NetPoint service.

To test Sentry operation, try generating a 404 (page not found) error by navigating to an invalid URL, such as `https://netpoint/404-error-testing`. (Be sure that debug mode has been disabled.) After receiving a 404 response from the NetPoint server, you should see the issue appear shortly in Sentry.
