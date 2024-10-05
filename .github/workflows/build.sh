docker build -t earth-invader .
docker tag earth-invader soulsender/earth-invader:latest
docker push soulsender/earth-invader:latest