# Ansible Getting Started Course

## Noteworthy Ansible Updates

Here are Ansible Updates since the course (grouped by Ansible release) and including some of the roadmap for what is coming. My notes here are the fastest way for me to get you updates and then I can modify the course as needed. 

### 2.10

- Collections re-org
  - Ansible version 2.10 shifted focus to collections for organization of modules and namespacing (avoiding collisions in multiple implementations)!
    - This is largely an organizational change to how Ansible content can be consumed, packaged and distributed for reuse. 
    - First, there's nothing earthshattering as of 2.10!
      - module names are now namespaced and packaged elsewhere but its transparent as of 2.10 (and likely beyond)
      - you can still refer to non-namespaced module names 
        - see plugin routing here: (a module is one of many types of plugins to ansible):
          - https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html#plugins-in-ansible-builtin
          - code routing table:
            - https://github.com/ansible/ansible/blob/devel/lib/ansible/config/ansible_builtin_runtime.yml
              - This is a great scroll-through resource to see how things map and this is what maps the routing so your 2.9 playbooks just work in 2.10+
    - Second, I address this and my speculations in the course about the future of collections as "sunsetting" roles in many ways or taking over the distribution aspect and roles become a high level way to share content. 
      - Now you can also share playbooks, plugins (modules, etc). This is much more robust and in many ways is a packagization of the core of ansible and the community of modules. And a proper namespacing mechanism that ties into distribution with Ansible Galaxy. 

## Python 2 is sunset

It will take time to move beyond distros and apps that still support 2.X but the 2.X build is EOL'd so that should wrap up quickly, especially given that this EOLing has been a decade or more in the works.

The nice thing is you can forget about 2.X/3.X issues and just move on to using ANsible whereas before the 2.X/3.X could trip you up. This said you can have parallel installs of 3.X versions that can cause trouble but less so than 2.X with the breaking language changes. 