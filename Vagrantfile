# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # we will use the file to define multiple VM's for testing many cases
  # now when we use vagrant up or vagrant ssh we need to specify a 
  # machine name, like vagrant ssh ubuntu14
  # 
  # first ubuntu machines
  config.vm.define "ubuntu14" do |ubuntu14|
    ubuntu.vm.box = "ubuntu/trusty64"
  end
  
  config.vm.define "ubuntu16" do |ubuntu16|
    ubuntu.vm.box = "bento/ubuntu-16.04"
  end

  # now centos boxes
  config.vm.define "centos6" do |centos6|
    centos6.vm.box = "bento/centos6.7"
  end
  
  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "centos/7"
  end
  
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # Give each machine a different port so selenium can test each one
  ubuntu14.vm.network "forwarded_port", guest: 80, host: 8080
  ubuntu16.vm.network "forwarded_port", guest: 80, host: 8081
  centos6.vm.network "forwarded_port", guest: 80, host: 8082
  centos7.vm.network "forwarded_port", guest: 80, host: 8083

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # 
  # the following line tells vagrant to run test.sh on the VM after vagrant up is ran
  # config.vm.provision :shell, path: "test.sh"
end
