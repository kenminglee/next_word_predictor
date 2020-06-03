from flask import Flask
import numpy as np
from tensorflow import keras
import tensorflow_hub as hub
import tensorflow as tf
from tensorflow.python.keras import backend as K

model = keras.models.load_model('/app/next_word_predictor')
vocab_arr = np.load('/app/vocab_arr.npy') 
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
  
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello!'

@app.route('/getNextWord/<sent>')
def getNextWord(sent):
  return vocab_arr[np.argmax(model.predict(embed([sent]).numpy())[-1])]

# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=80, debug=False)

