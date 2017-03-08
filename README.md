Assets manager
===

An admin web frontend for managing the [assets-server](https://github.com/ubuntudesign/assets-server).


Server setup
---

You'll need to have the [assets-server](https://github.com/ubuntudesign/assets-server) running for this manager to pair with.

By default, the manager will look for the server at <http://localhost:8012>. You can change this by setting the `WEBSERVICE_URL` environment variable.

The manager will also need a token to authenticate with the server's API. This can be set using the `AUTH_TOKEN` environment variable. 

Local development
---

How to run the manager locally:

``` bash
make setup                                          # Install dependencies
export AUTH_TOKEN=0338588d93c845e387cd4ec8b1aee55c  # Register an auth token for the server
export WEBSERVICE_URL=https://my-assets-server.com  # Where to find the assets-server (default: http://localhost:8012)
make develop                                        # Start the development server on port 8011
```

---

The champion for this project is [nottrobin](https://github.com/nottrobin).
