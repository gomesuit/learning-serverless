
# getting started
```
pyenv install $(cat .python-version)
nodebrew install-binary v7.10.0
npm install
pip install -r requirements.txt
# aws アクセスキー設定
aws configure
```

# 環境変数の設定
```
# line bot アクセストークン
export ACCESS_TOKEN=XXXXXXXXXXXXXX
```

# デプロイ
```
sls deploy -v
```

# ローカル実行
```
sls invoke local -f hello
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
