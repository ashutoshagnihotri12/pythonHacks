#python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # This line of code prevents the warning of "compilation" etc to junk the output that matters


# The central unit of data in TensorFlow is the tensor. A tensor consits of a set of primitive values shaped into an array of any number of dimensions.
# Importing statements for TensorFlow programs. This gives Python access to all of TensorFlow's classes, methods, and symbols.
import tensorflow as tf

hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()	# This line of code creates a Session Object.
print(sess.run(hello))

# Creating Computational Graph. A computational graph consists of nodes. Each node takes zero or more tensors as inputs and produces a tensor as an output. A constant node takes in no inputs and it outputs a value it stores internally.

node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)
print(sess.run([node1, node2]))

node3 = tf.add(node1, node2)
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b # + provides a shortcut for tf.add(a, b)
print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node,{a: [1, 3], b: [2, 4]}))

add_and_triple = adder_node * 3.
print(sess.run(add_and_triple,{a: 3, b: 4.5}))

W = tf.Variable([3.]. dtype=tf.float32)
b = tf.Variable([-3.], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b
init = tf.global_variables_initializer()
sess.run(init)















