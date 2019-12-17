#!/usr/bin/env python

# Great docs on how to build an inventory script
# albeit an inventory plugin is preferrable
# https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html

import json

# must print a json dictionary, otherwise you'll get an error:
#   " needs to be a json dict"
inventory = {
    "_meta": {
        "hostvars": {

        }
    },
    "centos": {
        "hosts": [
            "centos20",
            "centos21"
        ]
    }
}

for i in range(2):
    inventory["_meta"]["hostvars"]["centos2{:d}".format(i)] = {
        "ansible_host": "192.168.50.2{:d}".format(i),
        "ansible_private_key_file": ".vagrant/machines/centos2{:d}/virtualbox/private_key".format(i)
    }

inventory_string = json.dumps(inventory,  4)

print inventory_string
