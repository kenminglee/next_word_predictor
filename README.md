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
git clone https://github.com/leeming99/next_word_predictor.git
cd deploy
docker . -t=an_image
docker run -d --restart always -p 80:80 -e WORKERS_PER_CORE="0.5" an_image:latest
```

### Improvements:
- Use larger training dataset (the current dataset used only has a corpus of 2000+ words)
- Use a better model (LSTM? GRU?)
- Fine-tuning a pretrained model like GPT2? (Currently most pretrained models use their own word embeddings so using it with Universal Sentence Embedding is out of the question)
