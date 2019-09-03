# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
import numpy as np 
import gensim
import clean


from gensim.models import word2vec
sentences = [
  "That movie was absolutely awful",
  "The acting was a bit lacking",
  "The film was creative and surprising",
  "Absolutely fantastic!"
]
# Visualize word2vec embeddings in tensorboard
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

#for sent in sentences:
#    sentences.append(sent.split())
sentences = clean.getSentence()     

#print('khl',a)
model = word2vec.Word2Vec(sentences, min_count=1)

max_size = len(model.wv.vocab)-1
print(max_size, model.vector_size)
w2v = np.zeros((max_size,model.wv.vector_size))

with open("./tensorboard3/metadata.tsv", 'w+') as file_metadata:
    file_metadata.write('Index\tLabel\n')
    for i,word in enumerate(model.wv.index2word[:max_size]):
        print(i,word)
        w2v[i] = model.wv[word]
        file_metadata.write(str(i)+'\t'+word+'\n')

sess = tf.InteractiveSession()
#Let us create a 2D tensor called embedding that holds our embeddings.
with tf.device("/cpu:0"):
    embedding = tf.Variable(w2v, trainable=False, name='embedding')

tf.global_variables_initializer().run()

path = 'tensorboard3'

saver = tf.train.Saver()
# using file writer, we can save our summaries and events to our event file.
writer = tf.summary.FileWriter(path, sess.graph)

# adding into projector
config = projector.ProjectorConfig()
embed = config.embeddings.add()
embed.tensor_name = 'embedding'
embed.metadata_path = 'metadata.tsv'

# Specify the width and height of a single thumbnail.
projector.visualize_embeddings(writer, config)

saver.save(sess, path+'/model.ckpt', global_step=max_size)
