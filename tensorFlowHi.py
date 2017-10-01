#python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # This line of code prevents the warning of "compilation" etc to junk the output that matters

import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
