Docker command: 
cd deploy
docker . -t=an_image
docker run -d -p 80:80 -e WORKERS_PER_CORE="0.5" an_image:latest
