from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
from six.moves import cPickle
import language_check
from utils import TextLoader
from model import Model

import sys

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

def partition(prime, save_dir):

    #Sample is timestep (don't change)
    #Pick is weight method (don't change)
    #save_dir is model directory to store checkpointed models (don't change)
    #prime is words to start with
    #n is number of words to generate
    sample = 1
    pick = 1
    n = 200

    with open(os.path.join(save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(save_dir, 'words_vocab.pkl'), 'rb') as f:
        words, vocab = cPickle.load(f)
    model = Model(saved_args, True)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            output = model.sample(sess, words, vocab, n, prime, sample, pick)
            tool = language_check.LanguageTool('en-US')
            matches = tool.check(output)
            return language_check.correct(output, matches)

print(partition(sys.argv[1], sys.argv[2]))