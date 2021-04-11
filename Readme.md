# Config.
Set up of my MacOS computers. 

## Installation.
`git clone --recursive https://github.com/szewczykmira/dotfiles && ruby dotfiles/scripts/update_links.rb && ruby dotfiles/scripts/update_gitconfig.rb`


## Custom aliases etc
For adding options to your zsh config that are specific for given workstation put them in `~/.zshrc_custom`


## Customization
to use VSCode as editor only for some repositories, add 
```sh
export GIT_EDITOR="code --wait"
```
to your `.envrc`

