# example for visuals in course and also for people to follow along

# copy gitconfig file using ansible ad-hoc
ansible -m copy -a "src=master.gitconfig dest=~/.gitconfig" localhost

# dry run to see if anything would be changed
ansible -m copy -a "src=master.gitconfig dest=~/.gitconfig" --check localhost

# dry run with diff of changes
ansible -m copy -a "src=master.gitconfig dest=~/.gitconfig" --check --diff localhost

# apply changes and show diff of what was changed
ansible -m copy -a "src=master.gitconfig dest=~/.gitconfig" --diff localhost
