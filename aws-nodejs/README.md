# ローカル実行
```
sls invoke local -f hello -d "$(jo hoge=fuga)"
```

# デプロイ時にステージを切り替える
```
sls deploy -s <stage> -f hello -v
```
