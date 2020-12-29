## short description

   What if you could specify WHAT a system should look like and another tool
   took care of making that possible so you don't know HOW and can focus on just 
   WHAT outcome is needed. That's what Ansible can do for you. 

## long description

   Dining out is convenient because you decide **WHAT** to eat, and someone 
   else makes it for you. You don’t need to know **HOW** the sausage is made--literally--so long as the sausage is good!

   Unfortunately, all too often we are making our own meals instead of letting 
   tools (chefs) help us out. That is when it comes to our own work and probably
   for many people when they get home too! This course can help with the former
   more than the latter, but perhaps it can give you some ideas for both! 

   Ansible is a popular choice for IT automation because it allows you to 
   concisely specify a desired state and then it does the heavy lifting to make
   that state a reality. And, it works on every level of IT automation from the 
   network, to provisioning machines, to builds and it is especially known for configuration management of both systems and apps!

   Ansible is highly extensible and is comprised of a ginormous amount of core 
   and community content to jumpstart just about any configuration you can 
   imagine.

   It's time to move beyond just manually configuring servers. Beyond writing 
   confusing scripts. Beyond a mess of servers that consume all of your time 
   to keep in a desired state of configuration.

   So, I'll ask you, what if you could specify a desired state and let Ansible
   take care of bringing your machines into said desired state of configuration? Regardless how machines are setup, with Ansible you can specify WHAT and it 
   will take care of the rest to figure out HOW to make your WHAT a reality. 
   
   This eliminates inspecting the state of environments and determining what 
   commands to call to reconfigure them. It spares you of needing to be an 
   expert of every platform/tool/framework you manage. Let's face it, 
   you have bigger fish to fry! 

   So, in this course, Getting Started with Ansible, you will learn 
   foundational knowledge to quickly and reliably configure machines. 

   First, you will learn how to install Ansible and use the ansible Ad-hoc 
   command line tool to execute one off (often idempotent) modules 
   in Ansible to configure single, low level aspects of a system by describing
   a desired state. 

   Next, you will discover how playbooks allow you to invoke multiple modules
   via tasks with the `ansible-playbook` command line tool to configure your
   local machine. 

   Then, you'll see how to use `ansible-playbook` with inventories to configure
   multiple machines, both local and remote. You'll see how to use vagrant with 
   Ansible to spin up a local, VM lab environment so you can configure them with ansible-playbook. Giving you a chance to simulate configuring multiple 
   managed nodes with Ansible all on a local machine. No network of machines 
   needed unless you want that!

   Between core, community and your own modules, as well as plugins and other 
   aspects of the modularity of Ansible, it quickly becomes apparent that it is
   not possible to know everything about Ansible in a single life time 
   and part of that is due to Ansible's broad support for a plethora of 
   systems/tools many of which you will never need to use. So next you'll learn 
   how to learn what you need to know, when you need to know it so you don't 
   spend your entire life learning and instead can get something done from the 
   get-go. 

   Next, SSH is common for configuring systems so naturally it is used by 
   default in Ansible for remote configurations. In this module you'll see more 
   connection approaches beyond SSH. For example, the local connection plugin to
   bypass SSH when configuring a local machine. Or, `winrm` for configuring 
   Windows machines. Or, the docker connection plugin to configure docker 
   containers. And you'll see how we can invert Ansible's default push model 
   with the `ansible-pull` command. 

   Finally, you'll learn about reuse via 
   (Ansible's Galaxy site)[galaxy.ansible.com] and corresponding ansible-galaxy 
   command. You'll also briefly learn about the newly released Collections 
   format contrasted with the historic Role format. Both of which afford 
   learning and reuse opportunities beyond just what comes out of the box when 
   installing Ansible.  

   By the end of this course you'll know how to start using Ansible in your own 
   work to reduce risk and maximize rewards. And how to evolve your 
   understanding of Ansible.  



