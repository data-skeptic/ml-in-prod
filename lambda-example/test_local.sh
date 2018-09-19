export USER=$(cat creds.txt | awk '{print $1}')
export PASSWORD=$(cat creds.txt | awk '{print $2}')
export AWS_ACCESS_KEY=$(cat creds.txt | awk '{print $3}')
export AWS_SECRET_KEY=$(cat creds.txt | awk '{print $4}')
export S3_BUCKET=$(cat creds.txt | awk '{print $5}')
python3 lambda_function.py
