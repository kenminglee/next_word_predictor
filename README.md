### Usage
To try this out, please use a GET command on the following url: 
```
http://ec2-54-145-55-94.compute-1.amazonaws.com/getNextWord/<Enter your word or sentence here>
```
<Enter your word or sentence here> can be replaced with any words/sentences. We can add "%20" in between words to act as spacing.

For example, if we want to send "hello world" to the next word predictor, we can enter the following url in any browser
```
http://ec2-54-145-55-94.compute-1.amazonaws.com/getNextWord/hello%20world
```

### Deployment 
``` bash
git clone 
cd deploy
docker . -t=an_image
docker run -d --restart always -p 80:80 -e WORKERS_PER_CORE="0.5" an_image:latest
```
