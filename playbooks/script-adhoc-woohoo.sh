# Here's an example script analogy 
# of scripting ansible ad-hoc calls 
# to understand the purpose of playbooks.

# Ensure ~/.gitconfig is basaed on my master.gitconfig
ansible -m copy -a "src=../adhoc/master.gitconfig dest=~/.gitconfig" localhost

# Ensure `bat` is installed
# - A `cat` replacement for syntax highlighting!
# - IMHO the best highlighter, or at least the best I've found so far :)
ansible -m homebrew -a "name=bat state=latest" localhost

# Ensure `jq` is installed
# - CLI tool for working with json data! 
# - prettify, format, mutate, select subsets, etc
ansible -m homebrew -a "name=jq state=latest" localhost
