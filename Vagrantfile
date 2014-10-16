# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = '2'
Vagrant.require_version ">= 1.5.0"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box      = 'casualjim/trusty-vagrant'
  #config.vm.box_url  = 'http://files.vagrantup.com/trusty64.box'

  config.vm.hostname = 'koomus'
  
  config.vm.network :private_network, ip: '172.16.0.33'
  
  config.vm.network "forwarded_port", guest: 5000, host: 5017
  config.vm.network "forwarded_port", guest: 1234, host: 1236

  config.ssh.forward_agent = true

  config.vm.synced_folder "./dev", "/opt/dev", create: true

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--ioapic", "on"]
    vb.customize ['modifyvm', :id, '--memory', 6144]
    vb.customize ["modifyvm", :id, "--cpus", "2"] 
  end

  config.vm.provision "ansible" do |ansible|
    ansible.limit = 'all'
    ansible.playbook       = 'ansible/setup.yml'
    ansible.inventory_path = 'hosts'
    ansible.verbose        = 'vvvv'
  end

end
