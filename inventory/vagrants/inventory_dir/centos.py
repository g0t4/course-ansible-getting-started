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
            "centos20": {
                "ansible_host": "192.168.50.20",
                "ansible_private_key_file": ".vagrant/machines/centos20/virtualbox/private_key"
            },
            "centos21": {
                "ansible_host": "192.168.50.21",
                "ansible_private_key_file": ".vagrant/machines/centos21/virtualbox/private_key"
            }
        }
    },
    "centos": {
        "hosts": [
            "centos20",
            "centos21"
        ]
    }
}

inventory_string = json.dumps(inventory,  4)

print inventory_string
