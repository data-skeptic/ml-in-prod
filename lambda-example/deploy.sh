#!/bin/sh

zip -9 venv.zip *.py
aws s3 cp venv.zip s3://ml-in-prod/example-service.zip

aws lambda update-function-code \
	--function-name=example-service \
	--region=us-east-1 \
	--s3-bucket ml-in-prod \
	--s3-key example-service.zip

aws lambda update-function-configuration \
	--function-name example-service \
	--region=us-east-1 \
	--environment "Variables={db_host=myhost,db_user=myuser,db_password=blah}"

