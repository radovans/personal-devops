Vagrant.configure("2") do |config|

  # create mgmt node
  config.vm.define :mgmt do |mgmt_config|
      mgmt_config.vm.box = "ubuntu/trusty64"
      mgmt_config.vm.hostname = "mgmt"
      mgmt_config.vm.network :private_network, ip: "10.0.15.10"
      mgmt_config.vm.provider "virtualbox" do |vb|
        vb.memory = "512"
      end
      mgmt_config.vm.provision :shell, path: "mgmt-start-script.sh"
  end

  # create gitlab server
  config.vm.define :gitlab do |gitlab_config|
      gitlab_config.vm.box = "ubuntu/trusty64"
      gitlab_config.vm.hostname = "gitlab"
      gitlab_config.vm.network :private_network, ip: "10.0.15.11"
      gitlab_config.vm.provider "virtualbox" do |vb|
        vb.memory = "4096"
      end
  end

end