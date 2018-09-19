docker run -d \
	-p 8888:8888 \
	-p 9988:9988 \
	-e API_PORT=9988 \
	-e JUPYTER_PORT=8888 \
	-e USER=$(cat creds.txt | awk '{print $1}') \
	-e PASSWORD=$(cat creds.txt | awk '{print $2}') \
	-e AWS_ACCESS_KEY=$(cat creds.txt | awk '{print $3}') \
	-e AWS_SECRET_KEY=$(cat creds.txt | awk '{print $4}') \
	-e S3_BUCKET=$(cat creds.txt | awk '{print $5}') \
	-e MODE=DEV \
	-v "$(pwd)":/files \
	$(cat latest.txt) > current_container_id.txt
cat current_container_id.txt | awk '{print $1}' | cut -c-12
sleep 1
docker exec $(cat current_container_id.txt | awk '{print $1}' | cut -c-12) jupyter notebook list | awk '{print $1}' | tail -1 > running.txt
cat running.txt
open $(cat running.txt)
