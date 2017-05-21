
# serverlessのインストール
```
nodebrew install-binary v7.10.0
npm install -g serverless
```

# テンプレートの作成
```
sls create --template aws-nodejs --name hello

# globalにインストールしない場合、下記
./node_modules/.bin/sls create --template aws-nodejs --name hello
```
