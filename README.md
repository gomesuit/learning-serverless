
# get start
```
npm install
pip install -r requirements.txt
pip install -g serverless
# aws アクセスキー設定
aws configure
```

# 環境変数の設定
```
# line bot アクセストークン
export ACCESS_TOKEN=XXXXXXXXXXXXXX
```

# テンプレートの作成
```
./node_modules/.bin/sls create --template aws-nodejs --name hello
```

# デプロイ
```
sls deploy -v
```

# 実行
```
sls invoke -f hello
```

# 確認
```
curl -X GET https://xxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/dev/hello
```

# 削除
```
sls remove -v
```
