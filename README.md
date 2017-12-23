# Ansible action_plugin which call's module example

In this example action_plugin call's custom docker_module

## Build with

* [Architect's library](https://github.com/sbeliakou/ansible-examples) - Ansible examples
* [Docker lib](https://github.com/docker/docker-py) - Executes docker commands from python
* [Modules and Action Plugins example](https://terryhowe.wordpress.com/2016/05/03/ansible-2-0-modules-and-action-plugins/) - Modules live in the library directory and action plugins in action_plugin

### Prerequisites

```
$ python -V
```
```
$ sudo yum install -y python-pip
```
```
$ pip install ansible
```
```
$ pip install docker 
```
```
$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```
```
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```
```
$ sudo yum install docker-ce
```

## Examples how to use this modules

First check your docker images

```
$ docker images
```

Then run the ansible-playbook

```
$ ansible-playbook docker.yml -vv
```

To specify another image, go to docker.yml and change image_name variable (by default it is "spotify/alpine")

## Acknowledgments

* Many thanks to this book: "Implementing DevOps with Ansible 2 Jonathan McAllister July 2017"
