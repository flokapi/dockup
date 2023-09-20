# Dockup

Dockup is a command line interface tool which allows to easily publish applications at a given path through docker containers and nginx.

A Dockup package is a compressed file containing:

- the content you want to publish: python script, HTML file, ...

- the `dockup.yml` configuration file which contains the following info

    - `name` of the package, must be the same name as the archive containing it
    - `path` at which the package will be accessible. For example `/app1` for `website.com/app1` 

    - `type` of the package. For example, `website`, `flet` application

- optional: `Dockerfile` and `nginx.conf` in case customization is needed



When you publish a Dockup package, the tool will do the following things automatically for you:

- Docker compose stop
- Extract the package archive in the Dockup app folder
- If necessary, build the nginx configuration
- If necessary, build the docker file
- Rebuild the docker compose file
- Dockup compose build and up



The nginx reverse proxy used by Dockup is also installed as Dockup package. This makes it convenient to configure and update the reverse proxy, for example to configure HTTPS on your server.



### Installation

First of all install the docker engine: https://docs.docker.com/engine/install/

Then install Dockup as a pip package

```
pip3 install dockup
```



### Usage

Install the proxy Package

- given that your reverse proxy package is located in your current working directory
- you can prepare the reverse proxy package according to you needs:
    - [reverse_proxy_http](https://github.com/flokapi/dockup/tree/main/example_packages/reverse_proxy_http) is an example of simple HTTP proxy (not configured for HTTPS)
- you can also specify the package as an archive if it is present in you working directory.

```
python3 -m dockup installproxy reverse_proxy_http
```



Publish a package

- you can also specify the package as an archive if it is present in your working directory.

```
pyhton3 -m dockup install flet_app1
```



To remove a package

```
python3 -m dockup uninstall flet_app1
```



