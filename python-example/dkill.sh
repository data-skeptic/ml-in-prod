docker ps
docker kill $(docker ps | grep example-api | awk '{print $1}')
echo "========================================================================"
docker ps