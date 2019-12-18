#!/usr/bin/env python
# NOTE: this file must be executable `chmod +x centos.py`
	# challenge: make this file not executable and see what `ansible-inventory --list` prints

# Great docs on how to build an inventory script
# albeit an inventory plugin is preferrable
# https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html
# https://docs.ansible.com/ansible/latest/user_guide/intro_dynamic_inventory.html
import json

# must print a json dictionary, otherwise you'll get an error:
#   " needs to be a json dict"
inventory = {
    # more about meta here https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html#id16
    "_meta": {
        "hostvars": {}
    },
    "centos": {"hosts": []}
}

# programatically add hosts to inventory to show scripting benefits
# challenge: increase range & Vagrantfile VMs to see how we can dynamically add more targets
# challenge: port ubuntu static inventory to script too
# challenge: port centos.py script (this file) back into static inventory 
for i in range(2):
    inventory["_meta"]["hostvars"]["centos2{:d}".format(i)] = {
        "ansible_host": "192.168.50.2{:d}".format(i),
        "ansible_private_key_file": ".vagrant/machines/centos2{:d}/virtualbox/private_key".format(i)
    }
    inventory["centos"]["hosts"].append("centos2{:d}".format(i))

inventory_string = json.dumps(inventory, 4)

print inventory_string
