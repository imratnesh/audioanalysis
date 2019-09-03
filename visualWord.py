# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector
import numpy as np 
import gensim

#url = "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"

model = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format("../GoogleNews-vectors-negative300.bin.gz",
                                                                     binary=True, limit=5000)

# Visualize word2vec embeddings in tensorboard
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

# ### Load the saved word2vec model
#
# fname = "w2v_model"
# model = gensim.models.keyedvectors.KeyedVectors.load('w2v_model')
# model = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(fname, unicode_errors='ignore', binary=True)

max_size = len(model.vocab)-1
print(max_size, model.vector_size)
w2v = np.zeros((max_size,model.vector_size))

with open("./tensorboard1/metadata.tsv", 'w+') as file_metadata:
    file_metadata.write('Index\tLabel\n')
    for i,word in enumerate(model.index2word[:max_size]):
        w2v[i] = model.wv[word]
        print(i)
        file_metadata.write(str(i)+'\t'+word+'\n')

sess = tf.InteractiveSession()
#Let us create a 2D tensor called embedding that holds our embeddings.
with tf.device("/cpu:0"):
    embedding = tf.Variable(w2v, trainable=False, name='embedding')

tf.global_variables_initializer().run()

path = 'tensorboard1'

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
