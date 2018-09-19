zip -9 venv.zip *.py
aws s3 cp venv.zip s3://ml-in-prod/example-service.zip

aws lambda create-function \
	--function-name=example-service \
	--runtime=python2.7 \
	--role='arn:aws:iam::085318171245:role/tse-api-executor' \
	--handler=lambda_function.lambda_handler \
	--region=us-east-1 \
	--code='{"S3Bucket": "ml-in-prod", "S3Key": "example-service.zip"}'

aws lambda update-function-configuration \
	--function-name example-service \
	--region=us-east-1 \
	--environment "Variables={host=x,port=y,username=z,password=a,database=b}"
