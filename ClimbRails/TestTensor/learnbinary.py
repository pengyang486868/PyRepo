import dataread
import tensorflow as tf


inputlist = dataread.input('learn')
outputlist = dataread.output('learn')
print()

x = tf.placeholder(tf.float32, [None, 8])
W = tf.Variable(tf.zeros([8,23]))
b = tf.Variable(tf.zeros([23]))

y = tf.nn.softmax(tf.matmul(x,W) + b)

y_ = tf.placeholder("float", [None,23])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1000001):
    #batch_xs, batch_ys = mnist.train.next_batch(100)
    #sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
    sess.run(train_step, feed_dict={x: inputlist, y_: outputlist})
    if i % 20000 == 0:
        print(i, sess.run(W), sess.run(b))


