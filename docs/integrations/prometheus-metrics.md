# Prometheus Metrics

NetPoint supports optionally exposing native Prometheus metrics from the application. [Prometheus](https://prometheus.io/) is a popular time series metric platform used for monitoring.

NetPoint exposes metrics at the `/metrics` HTTP endpoint, e.g. `https://netpoint.local/metrics`. Metric exposition can be toggled with the `METRICS_ENABLED` configuration setting. Metrics are not exposed by default.

## Metric Types

NetPoint makes use of the [django-prometheus](https://github.com/korfuri/django-prometheus) library to export a number of different types of metrics, including:

- Per model insert, update, and delete counters
- Per view request counters
- Per view request latency histograms
- Request body size histograms
- Response body size histograms
- Response code counters
- Database connection, execution, and error counters
- Cache hit, miss, and invalidation counters
- Django middleware latency histograms
- Other Django related metadata metrics

For the exhaustive list of exposed metrics, visit the `/metrics` endpoint on your NetPoint instance.

## Multi Processing Notes

When deploying NetPoint in a multiprocess manner (e.g. running multiple Gunicorn workers) the Prometheus client library requires the use of a shared directory to collect metrics from all worker processes. To configure this, first create or designate a local directory to which the worker processes have read and write access, and then configure your WSGI service (e.g. Gunicorn) to define this path as the `prometheus_multiproc_dir` environment variable.

!!! warning
    If having accurate long-term metrics in a multiprocess environment is crucial to your deployment, it's recommended you use the `uwsgi` library instead of `gunicorn`. The issue lies in the way `gunicorn` tracks worker processes (vs `uwsgi`) which helps manage the metrics files created by the above configurations. If you're using NetPoint with gunicorn in a containerized environment following the one-process-per-container methodology, then you will likely not need to change to `uwsgi`. More details can be found in  [issue #3779](https://github.com/khulnasoft/netpoint/issues/3779#issuecomment-590547562).
