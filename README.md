Assets manager
===

An admin web frontend for managing the [assets-server](/canonicalltd/assets-server).

Setting the server location
---

You'll need to have an instance of the [assets-server](/canonicalltd/assets-server) running for this manager to pair with. By default, the manager will look for the server at <http://localhost:8012>. You can change this in two ways.

By changing the default in `settings.py`:

``` python
# assets_server/settings.py

DEFAULT_SERVER_URL = 'https://assets.example.com'
```

Or by setting the `WEBSERVICE_URL` environment variable:

``` bash
# Start the development server with an environment variable

$ WEBSERVICE_URL='https://assets.example.com' make develop
```

Credentials for the assets-server
---

You also need to create an authorization token for the assets-manager:

``` bash
# This sets a random token in assets_manager/settings.py
# And prints it out
$ make auth-token
Authorization token (in assets_manager/settings.py):
0338588d93c845e387cd4ec8b1aee55c 
```

and add this token to the assets-server using its `create-token.sh` script:

``` bash
cd assets-server-directory
scripts/create-token.sh 0338588d93c845e387cd4ec8b1aee55c manager
```

Local development
---

Once you've setup the server credentials, here how to get the manager working locally:

### System packages

``` bash
sudo apt-get install python-dev python-pip
sudo pip install vex
```

### Python environment

You need to setup your python environment, which you can either do manually
if you know how (from `requirements/dev.txt`) or use the make target:

``` bash
$ make setup  # Sets up a new environment in the `env` folder
```

### Run the development server

``` bash
$ make develop  # Starts the dev server on port 8011
````

Or you can run on a different port as follows:

``` bash
$ PORT=8765 make develop
```

