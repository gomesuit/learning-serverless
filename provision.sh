#!/bin/bash

# install nodejs
curl -L git.io/nodebrew | perl - setup
echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> .bash_profile
source ~/.bash_profile
nodebrew install-binary v6.9.5
nodebrew use v6.9.5

# install serverless
npm install -g serverless

# install aws-cli
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py
sudo pip install awscli

# aws configure

# install common package
yum install -y vim



#mkdir hello-serverless
#cd hello-serverless
#sls create --template aws-nodejs --name hello
# vim serverless.yml
#sls deploy -v
#sls invoke -f hello
# vim serverless.yml
#sls deploy -v
# curl -X GET https://xxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/hello
#sls remove -v
