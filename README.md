To try this out, please use a GET command on the following url: 
```
http://ec2-54-145-55-94.compute-1.amazonaws.com/getNextWord/<Enter your word/sentence here>
```
<Enter your word/sentence here> can be replaced with any words/sentences. We can add "%20" in between words to act as spacing.


Docker command: 
``` bash
cd deploy
docker . -t=an_image
docker run -d --restart always -p 80:80 -e WORKERS_PER_CORE="0.5" an_image:latest
```
