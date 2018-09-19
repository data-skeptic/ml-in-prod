#!/bin/sh

aws lambda invoke \
	--invocation-type RequestResponse \
	--function-name=example-service \
	--region=us-east-1 \
	--log-type Tail \
	--payload '{"bucket": "ml-in-prod", "s3key": "examples/example1.json"}' \
	outputfile.txt > log.txt

cat log.txt | jq '.LogResult' | tr -d '"' | base64 --decode

cat outputfile.txt

rm outputfile.txt
rm log.txt