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
sls invoke local -f hello
```

# 実行
```
sls invoke -f hello
```

# ログ
```
sls logs -f hello -t
```

# 削除
```
sls remove -v
```