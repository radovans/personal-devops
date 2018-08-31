# Personal project- devops part
### Prerequisties
Vagrant - https://www.vagrantup.com/ - version 2.1.4
Oracle VM Virtualbox - https://www.virtualbox.org - version 5.2.18
Docker Toolbox for Windows - https://docs.docker.com/toolbox/overview/

### Technologies
- vagrant
- ansible
- gitlab

### Installation guide
Start vagrant and connect to mgmt node
```sh
$ vagrant up
$ vagrant ssh mgmt
```

Save ssh key of servers into known_hosts to remove ask pass, generate ssh key and install it on hosts. Password is **vagrant**
```sh
$ ssh-keyscan lb1 db1 web1 web2 elk gitlab >> .ssh/known_hosts
$ ssh-keygen -t rsa -b 2048
$ ansible-playbook bin/ssh-addkey.yml --ask-pass
```

Run ansible-playbook to configure gitlab
```sh
$ ansible-playbook role-gitlab.yml
```

After installation is succeeded just open browser and type
```sh
http://10.0.15.11:80/
```

You need to change initial password for **root** user.
