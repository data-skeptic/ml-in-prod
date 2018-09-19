# Test locally

`./test_local.sh`

# To Build venv.zip, run

```
./build0.sh
```

which does this:

```
docker run -v $(pwd):/outputs -it amazonlinux:2016.09 \
      /bin/bash /outputs/build.sh
```

# Configuration

* Create your own bucket via AWS Console
* `aws s3 cp examples/example1.json s3://ml-in-prod/examples/example1.json`

# To Set Up Lambda Function (first time only)

```
./create_lambda_function.sh
```

# To Deploy

```
./deploy.sh
```

```
./test_lambda.sh
```
