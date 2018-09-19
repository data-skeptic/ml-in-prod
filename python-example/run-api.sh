docker run -i -t -a STDOUT \
	-p 9988:9988 \
	-e API_PORT=9988 \
	-e USER=$(cat creds.txt | awk '{print $1}') \
	-e PASSWORD=$(cat creds.txt | awk '{print $2}') \
	-e AWS_ACCESS_KEY=$(cat creds.txt | awk '{print $3}') \
	-e AWS_SECRET_KEY=$(cat creds.txt | awk '{print $4}') \
	-e S3_BUCKET=$(cat creds.txt | awk '{print $5}') \
	-e MODE=API \
	$(cat latest.txt)
