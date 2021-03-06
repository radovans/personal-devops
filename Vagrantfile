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

  # create development server
  config.vm.define :dev do |development_config|
      development_config.vm.box = "ubuntu/trusty64"
      development_config.vm.hostname = "dev"
      development_config.vm.network :private_network, ip: "10.0.15.11"
      development_config.vm.provider "virtualbox" do |vb|
        vb.memory = "4096"
      end
  end

  # create hosts
  (1..2).each do |i|
      config.vm.define "web#{i}" do |host_config|
          host_config.vm.box = "ubuntu/trusty64"
          host_config.vm.hostname = "host#{i}"
          host_config.vm.network :private_network, ip: "10.0.15.2#{i}"
          host_config.vm.network "forwarded_port", guest: 80, host: "808#{i}"
          host_config.vm.provider "virtualbox" do |vb|
            vb.memory = "256"
          end
      end
  end

  # create load balancer
  config.vm.define :haproxy do |haproxy_config|
      haproxy_config.vm.box = "ubuntu/trusty64"
      haproxy_config.vm.hostname = "haproxy"
      haproxy_config.vm.network :private_network, ip: "10.0.15.12"
      haproxy_config.vm.network "forwarded_port", guest: 80, host: 8080
      haproxy_config.vm.provider "virtualbox" do |vb|
        vb.memory = "256"
     end
  end

  # create elk server
  config.vm.define :elk do |elk_config|
      elk_config.vm.box = "ubuntu/trusty64"
      elk_config.vm.hostname = "elk"
      elk_config.vm.network :private_network, ip: "10.0.15.13"
      elk_config.vm.provider "virtualbox" do |vb|
        vb.memory = "4096"
      end
  end

end