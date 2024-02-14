# NetPoint Installation

This section of the documentation discusses installing and configuring the NetPoint application itself.

## Install System Packages

Begin by installing all system packages required by NetPoint and its dependencies.

!!! warning "Python 3.8 or later required"
    NetPoint requires Python 3.8, 3.9, 3.10 or 3.11.

=== "Ubuntu"

    ```no-highlight
    sudo apt install -y python3 python3-pip python3-venv python3-dev build-essential libxml2-dev libxslt1-dev libffi-dev libpq-dev libssl-dev zlib1g-dev
    ```

=== "CentOS"

    ```no-highlight
    sudo yum install -y gcc libxml2-devel libxslt-devel libffi-devel libpq-devel openssl-devel redhat-rpm-config
    ```

Before continuing, check that your installed Python version is at least 3.8:

```no-highlight
python3 -V
```

## Download NetPoint

This documentation provides two options for installing NetPoint: from a downloadable archive, or from the git repository. Installing from a package (option A below) requires manually fetching and extracting the archive for every future update, whereas installation via git (option B) allows for seamless upgrades by re-pulling the `master` branch.

### Option A: Download a Release Archive

Download the [latest stable release](https://github.com/khulnasoft/netpoint/releases) from GitHub as a tarball or ZIP archive and extract it to your desired path. In this example, we'll use `/opt/netpoint` as the NetPoint root.

```no-highlight
sudo wget https://github.com/khulnasoft/netpoint/archive/refs/tags/vX.Y.Z.tar.gz
sudo tar -xzf vX.Y.Z.tar.gz -C /opt
sudo ln -s /opt/netpoint-X.Y.Z/ /opt/netpoint
```

!!! note
    It is recommended to install NetPoint in a directory named for its version number. For example, NetPoint v3.0.0 would be installed into `/opt/netpoint-3.0.0`, and a symlink from `/opt/netpoint/` would point to this location. (You can verify this configuration with the command `ls -l /opt | grep netpoint`.) This allows for future releases to be installed in parallel without interrupting the current installation. When changing to the new release, only the symlink needs to be updated.

### Option B: Clone the Git Repository

Create the base directory for the NetPoint installation. For this guide, we'll use `/opt/netpoint`.

```no-highlight
sudo mkdir -p /opt/netpoint/
cd /opt/netpoint/
```

If `git` is not already installed, install it:

=== "Ubuntu"

    ```no-highlight
    sudo apt install -y git
    ```

=== "CentOS"

    ```no-highlight
    sudo yum install -y git
    ```

Next, clone the **master** branch of the NetPoint GitHub repository into the current directory. (This branch always holds the current stable release.)

```no-highlight
sudo git clone -b master --depth 1 https://github.com/khulnasoft/netpoint.git .
```

!!! note
    The `git clone` command above utilizes a "shallow clone" to retrieve only the most recent commit. If you need to download the entire history, omit the `--depth 1` argument.

The `git clone` command should generate output similar to the following:

```
Cloning into '.'...
remote: Enumerating objects: 996, done.
remote: Counting objects: 100% (996/996), done.
remote: Compressing objects: 100% (935/935), done.
remote: Total 996 (delta 148), reused 386 (delta 34), pack-reused 0
Receiving objects: 100% (996/996), 4.26 MiB | 9.81 MiB/s, done.
Resolving deltas: 100% (148/148), done.
```

!!! note
    Installation via git also allows you to easily try out different versions of NetPoint. To check out a [specific NetPoint release](https://github.com/khulnasoft/netpoint/releases), use the `git checkout` command with the desired release tag. For example, `git checkout v3.0.8`.

## Create the NetPoint System User

Create a system user account named `netpoint`. We'll configure the WSGI and HTTP services to run under this account. We'll also assign this user ownership of the media directory. This ensures that NetPoint will be able to save uploaded files.

=== "Ubuntu"

    ```
    sudo adduser --system --group netpoint
    sudo chown --recursive netpoint /opt/netpoint/netpoint/media/
    sudo chown --recursive netpoint /opt/netpoint/netpoint/reports/
    sudo chown --recursive netpoint /opt/netpoint/netpoint/scripts/
    ```

=== "CentOS"

    ```
    sudo groupadd --system netpoint
    sudo adduser --system -g netpoint netpoint
    sudo chown --recursive netpoint /opt/netpoint/netpoint/media/
    sudo chown --recursive netpoint /opt/netpoint/netpoint/reports/
    sudo chown --recursive netpoint /opt/netpoint/netpoint/scripts/
    ```

## Configuration

Move into the NetPoint configuration directory and make a copy of `configuration_example.py` named `configuration.py`. This file will hold all of your local configuration parameters.

```no-highlight
cd /opt/netpoint/netpoint/netpoint/
sudo cp configuration_example.py configuration.py
```

Open `configuration.py` with your preferred editor to begin configuring NetPoint. NetPoint offers [many configuration parameters](../configuration/index.md), but only the following four are required for new installations:

* `ALLOWED_HOSTS`
* `DATABASE`
* `REDIS`
* `SECRET_KEY`

### ALLOWED_HOSTS

This is a list of the valid hostnames and IP addresses by which this server can be reached. You must specify at least one name or IP address. (Note that this does not restrict the locations from which NetPoint may be accessed: It is merely for [HTTP host header validation](https://docs.djangoproject.com/en/3.0/topics/security/#host-headers-virtual-hosting).)

```python
ALLOWED_HOSTS = ['netpoint.example.com', '192.0.2.123']
```

If you are not yet sure what the domain name and/or IP address of the NetPoint installation will be, you can set this to a wildcard (asterisk) to allow all host values:

```python
ALLOWED_HOSTS = ['*']
```

### DATABASE

This parameter holds the database configuration details. You must define the username and password used when you configured PostgreSQL. If the service is running on a remote host, update the `HOST` and `PORT` parameters accordingly. See the [configuration documentation](../configuration/required-parameters.md#database) for more detail on individual parameters.

```python
DATABASE = {
    'NAME': 'netpoint',               # Database name
    'USER': 'netpoint',               # PostgreSQL username
    'PASSWORD': 'J5brHrAXFLQSif0K', # PostgreSQL password
    'HOST': 'localhost',            # Database server
    'PORT': '',                     # Database port (leave blank for default)
    'CONN_MAX_AGE': 300,            # Max database connection age (seconds)
}
```

### REDIS

Redis is a in-memory key-value store used by NetPoint for caching and background task queuing. Redis typically requires minimal configuration; the values below should suffice for most installations. See the [configuration documentation](../configuration/required-parameters.md#redis) for more detail on individual parameters.

Note that NetPoint requires the specification of two separate Redis databases: `tasks` and `caching`. These may both be provided by the same Redis service, however each should have a unique numeric database ID.

```python
REDIS = {
    'tasks': {
        'HOST': 'localhost',      # Redis server
        'PORT': 6379,             # Redis port
        'PASSWORD': '',           # Redis password (optional)
        'DATABASE': 0,            # Database ID
        'SSL': False,             # Use SSL (optional)
    },
    'caching': {
        'HOST': 'localhost',
        'PORT': 6379,
        'PASSWORD': '',
        'DATABASE': 1,            # Unique ID for second database
        'SSL': False,
    }
}
```

### SECRET_KEY

This parameter must be assigned a randomly-generated key employed as a salt for hashing and related cryptographic functions. (Note, however, that it is _never_ directly used in the encryption of secret data.) This key must be unique to this installation and is recommended to be at least 50 characters long. It should not be shared outside the local system.

A simple Python script named `generate_secret_key.py` is provided in the parent directory to assist in generating a suitable key:

```no-highlight
python3 ../generate_secret_key.py
```

!!! warning "SECRET_KEY values must match"
    In the case of a highly available installation with multiple web servers, `SECRET_KEY` must be identical among all servers in order to maintain a persistent user session state.

When you have finished modifying the configuration, remember to save the file.

## Optional Requirements

All Python packages required by NetPoint are listed in `requirements.txt` and will be installed automatically. NetPoint also supports some optional packages. If desired, these packages must be listed in `local_requirements.txt` within the NetPoint root directory.

### Remote File Storage

By default, NetPoint will use the local filesystem to store uploaded files. To use a remote filesystem, install the [`django-storages`](https://django-storages.readthedocs.io/en/stable/) library and configure your [desired storage backend](../configuration/system.md#storage_backend) in `configuration.py`.

```no-highlight
sudo sh -c "echo 'django-storages' >> /opt/netpoint/local_requirements.txt"
```

### Remote Data Sources

NetPoint supports integration with several remote data sources via configurable backends. Each of these requires the installation of one or more additional libraries.

* Amazon S3: [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* Git: [`dulwich`](https://www.dulwich.io/)

For example, to enable the Amazon S3 backend, add `boto3` to your local requirements file:

```no-highlight
sudo sh -c "echo 'boto3' >> /opt/netpoint/local_requirements.txt"
```

!!! info
    These packages were previously required in NetPoint v3.5 but now are optional.

### Sentry Integration

NetPoint may be configured to send error reports to [Sentry](../administration/error-reporting.md) for analysis. This integration requires installation of the `sentry-sdk` Python library.

```no-highlight
sudo sh -c "echo 'sentry-sdk' >> /opt/netpoint/local_requirements.txt"
```

!!! info
    Sentry integration was previously included by default in NetPoint v3.6 but is now optional.

## Run the Upgrade Script

Once NetPoint has been configured, we're ready to proceed with the actual installation. We'll run the packaged upgrade script (`upgrade.sh`) to perform the following actions:

* Create a Python virtual environment
* Installs all required Python packages
* Run database schema migrations
* Builds the documentation locally (for offline use)
* Aggregate static resource files on disk

!!! warning
    If you still have a Python virtual environment active from a previous installation step, disable it now by running the `deactivate` command. This will avoid errors on systems where `sudo` has been configured to preserve the user's current environment.

```no-highlight
sudo /opt/netpoint/upgrade.sh
```

Note that **Python 3.8 or later is required** for NetPoint v3.2 and later releases. If the default Python installation on your server is set to a lesser version,  pass the path to the supported installation as an environment variable named `PYTHON`. (Note that the environment variable must be passed _after_ the `sudo` command.)

```no-highlight
sudo PYTHON=/usr/bin/python3.8 /opt/netpoint/upgrade.sh
```

!!! note
    Upon completion, the upgrade script may warn that no existing virtual environment was detected. As this is a new installation, this warning can be safely ignored.

## Create a Super User

NetPoint does not come with any predefined user accounts. You'll need to create a super user (administrative account) to be able to log into NetPoint. First, enter the Python virtual environment created by the upgrade script:

```no-highlight
source /opt/netpoint/venv/bin/activate
```

Once the virtual environment has been activated, you should notice the string `(venv)` prepended to your console prompt.

Next, we'll create a superuser account using the `createsuperuser` Django management command (via `manage.py`). Specifying an email address for the user is not required, but be sure to use a very strong password.

```no-highlight
cd /opt/netpoint/netpoint
python3 manage.py createsuperuser
```

## Schedule the Housekeeping Task

NetPoint includes a `housekeeping` management command that handles some recurring cleanup tasks, such as clearing out old sessions and expired change records. Although this command may be run manually, it is recommended to configure a scheduled job using the system's `cron` daemon or a similar utility.

A shell script which invokes this command is included at `contrib/netpoint-housekeeping.sh`. It can be copied to or linked from your system's daily cron task directory, or included within the crontab directly. (If installing NetPoint into a nonstandard path, be sure to update the system paths within this script first.)

```shell
sudo ln -s /opt/netpoint/contrib/netpoint-housekeeping.sh /etc/cron.daily/netpoint-housekeeping
```

See the [housekeeping documentation](../administration/housekeeping.md) for further details.

## Test the Application

At this point, we should be able to run NetPoint's development server for testing. We can check by starting a development instance locally.

!!! tip
    Check that the Python virtual environment is still active before attempting to run the server.

```no-highlight
python3 manage.py runserver 0.0.0.0:8000 --insecure
```

If successful, you should see output similar to the following:

```no-highlight
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 30, 2021 - 18:02:23
Django version 3.2.6, using settings 'netpoint.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Next, connect to the name or IP of the server (as defined in `ALLOWED_HOSTS`) on port 8000; for example, <http://127.0.0.1:8000/>. You should be greeted with the NetPoint home page. Try logging in using the username and password specified when creating a superuser.

!!! note
    By default RHEL based distros will likely block your testing attempts with firewalld. The development server port can be opened with `firewall-cmd` (add `--permanent` if you want the rule to survive server restarts):

    ```no-highlight
    firewall-cmd --zone=public --add-port=8000/tcp
    ```

!!! danger "Not for production use"
    The development server is for development and testing purposes only. It is neither performant nor secure enough for production use. **Do not use it in production.**

!!! warning
    If the test service does not run, or you cannot reach the NetPoint home page, something has gone wrong. Do not proceed with the rest of this guide until the installation has been corrected.

Type `Ctrl+c` to stop the development server.