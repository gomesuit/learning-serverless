#!/bin/bash

# install nodejs
curl -L git.io/nodebrew | perl - setup
echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> .bash_profile
source ~/.bash_profile
nodebrew install-binary v6.9.5
nodebrew use v6.9.5

