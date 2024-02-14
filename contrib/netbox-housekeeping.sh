#!/bin/sh
# This shell script invokes NetPoint's housekeeping management command, which
# intended to be run nightly. This script can be copied into your system's
# daily cron directory (e.g. /etc/cron.daily), or referenced directly from
# within the cron configuration file.
#
# If NetPoint has been installed into a nonstandard location, update the paths
# below.
/opt/netpoint/venv/bin/python /opt/netpoint/netpoint/manage.py housekeeping
