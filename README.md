

# テンプレートの作成
```
sls create --template aws-nodejs --name hello
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
