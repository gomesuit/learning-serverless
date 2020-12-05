deploy:
	nodenv exec npx pipenv run sls deploy -v

remove:
	nodenv exec npx pipenv run sls remove -v

login-test:
	nodenv exec npx pipenv run sls invoke local -f login --path sample.json

role-test:
	nodenv exec npx pipenv run sls invoke local -f role
