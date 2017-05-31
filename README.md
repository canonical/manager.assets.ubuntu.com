# Assets manager

An admin web frontend for managing the [assets-server](https://github.com/canonical-websites/assets.ubuntu.com).

## Local development

First, you need to know the URL of instance of the [assets server](https://github.com/canonical-websites/assets.ubuntu.com) you wish to connect to, and an authorisation key for connecting to it.

### Running the server

The simplest way to run the site locally is to first [install Docker](https://docs.docker.com/engine/installation/) (on Linux you may need to [add your user to the `docker` group](https://docs.docker.com/engine/installation/linux/linux-postinstall/)), and then use the `./run` script.

The first time you run it, the script will ask you to choose a URL for the server, and an authorisation key. E.g.:

``` bash
$ ./run
Enter the URL for the assets webservice (e.g. https://assets.staging.ubuntu.com, or http://localhost:8018):
https://assets.staging.ubuntu.com
Enter the authentication token for the assets webservice:
xxxxxxxxxxx
```

These settings will be stored in the `.local-env` file, and read from there.

Once the containers are setup, you can visit <http://127.0.0.1:8018> in your browser to see the web frontend for controlling the assets service.

### Building CSS

For working on [Sass files](_sass), you may want to dynamically watch for changes to rebuild the CSS whenever something changes.

To setup the watcher, open a new terminal window and run:

``` bash
./run watch
```

---

The champion for this project is [nottrobin](https://github.com/nottrobin).
