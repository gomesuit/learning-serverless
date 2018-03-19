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
sls invoke local -f hello -p event.json
```

# 実行
```
sls invoke -f hello -p event.json
```

# ログ
```
sls logs -f hello -t
```

# 削除
```
sls remove -v
```
