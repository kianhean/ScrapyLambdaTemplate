# Scrapy Crawler on AWS Lambda

## Init

### Start Scrapy Project

```bash
pipenv --three

pipenv shell

pipenv install scrapy

```

### Install Serverless

```bash
npm install -g serverless

sls plugin install -n serverless-python-requirements
```

### Deploy

```bash
sls deploy
```

### Invoke

```bash
sls invoke -f crawler -l
```
