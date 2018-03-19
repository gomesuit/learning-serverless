# build

```
mvn package shade:shade
```

# デプロイ
```
sls deploy -v
```

# ローカル実行
```
sls invoke local -f hello --data '{"keyword":"Template:今日は何の日", "header":""}'
```

# 実行
```
sls invoke -f hello --data '{"keyword":"Template:今日は何の日", "header":""}'
```

# ログ
```
sls logs -f hello -t
```

# 削除
```
sls remove -v
```
