# Personal project- devops part
### Prerequisties
- Vagrant - https://www.vagrantup.com/ - version 2.1.4
- Oracle VM Virtualbox - https://www.virtualbox.org - version 5.2.18
- Docker Toolbox for Windows - https://docs.docker.com/toolbox/overview/

### Technologies
- vagrant
- ansible
- gitlab
- docker

### Installation guide
Start vagrant and connect to mgmt node
```sh
vagrant up
vagrant ssh mgmt
```

Save ssh key of servers into known_hosts to remove ask pass, generate ssh key and install it on hosts.
```sh
ssh-keyscan dev host1 host2 haproxy elk >> .ssh/known_hosts
ssh-keygen -t rsa -b 2048 -f /home/vagrant/.ssh/id_rsa -q -N ""
ansible-playbook bin/ssh-addkey.yml -e "ansible_ssh_pass=vagrant"
```

-------------------------
GITLAB
-------------------------

Run ansible-playbook to configure gitlab
```sh
ansible-playbook role-gitlab.yml
```

After installation is succeeded just open browser and change initial password for **root** user.
```sh
http://10.0.15.11:80/
```

Connect to dev server and register runner and supply registration-token from `http://10.0.15.11:80/admin/runners`
```sh
ssh dev
sudo gitlab-runner register \
    --non-interactive \
    --url "http://10.0.15.11/" \
    --registration-token "QmfN9xbAPJoQhLRNitNx" \
    --executor "docker" \
    --docker-image alpine:latest \
    --description "docker-runner" \
    --tag-list "docker,alpine" \
    --run-untagged \
    --locked="false"
```

-------------------------
WEB, HAPROXY
-------------------------

Run ansible-playbook to configure web sites on hosts and haproxy.
```sh
ansible-playbook role-site.yml
```

Sites are directly available at `http://10.0.15.21/` and `http://10.0.15.22/`. If you want to go trough load balancer you need to visit `http://localhost:8080/`
HAProxy is available at `http://localhost:8080/haproxy?stats`.

-------------------------
ELK STACK - ElasticSearch, Logstash, Kibana
-------------------------

Run elk playbook to install ELK stack on elk server and configure Filebeat on hosts.
```sh
ansible-playbook role-elk.yml
```

Kibana will be available at `http://10.0.15.13:5601/`. You will need to configure index pattern as `filebeat-*`