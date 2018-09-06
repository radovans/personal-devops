# Personal project- devops part
### Prerequisties
- Vagrant - https://www.vagrantup.com/ - version 2.1.4
- Oracle VM Virtualbox - https://www.virtualbox.org - version 5.2.18
- Docker Toolbox for Windows - https://docs.docker.com/toolbox/overview/

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

Save ssh key of servers into known_hosts to remove ask pass, generate ssh key and install it on hosts.
```sh
$ ssh-keyscan gitlab >> .ssh/known_hosts
$ ssh-keygen -t rsa -b 2048 -f /home/vagrant/.ssh/id_rsa -q -N ""
$ ansible-playbook bin/ssh-addkey.yml -e "ansible_ssh_pass=vagrant"
```

-------------------------
GITLAB
-------------------------

Connect to mgmt host and run ansible-playbook to configure gitlab
```sh
$ vagrant ssh mgmt
$ ansible-playbook role-gitlab.yml
```

After installation is succeeded just open browser and change initial password for **root** user.
```sh
http://10.0.15.11:80/
```

Connect to gitlab server and register runner and supply registration-token from `http://10.0.15.11:80/admin/runners`
```sh
$ ssh gitlab
$ sudo gitlab-runner register \
    --non-interactive \
    --url "http://10.0.15.11/" \
    --registration-token "QmfN9xbAPJoQhLRNitNx" \
    --executor "docker" \
    --docker-image alpine:latest \
    --description "docker-runner" \
    --tag-list "docker,alpine" \
    --run-untagged \
    --locked="false" \
```