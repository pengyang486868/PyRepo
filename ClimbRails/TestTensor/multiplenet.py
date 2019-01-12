import tensorflow as tf
import numpy as np
import dataread

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


inputlist = dataread.input('learn')
outputlist = dataread.output('learn')
print()

input_dim = inputlist.shape[1]
output_dim = outputlist.shape[1]
hidden_dim1 = 10
hidden_dim2 = 10

x = tf.placeholder(tf.float32, [None, input_dim])
y_ = tf.placeholder(tf.float32, [None, output_dim])


hidden_layer1 = add_layer(x, input_dim, hidden_dim1, activation_function=tf.nn.sigmoid)
hidden_layer2 = add_layer(hidden_layer1, hidden_dim1, hidden_dim2, activation_function=tf.nn.sigmoid)

y = add_layer(hidden_layer2, hidden_dim2, output_dim, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_ - y),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.05).minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# test set
inputtest = dataread.input('validate')
outputtest = dataread.output('validate')

num=400001
for i in range(num):
    sess.run(train_step, feed_dict={x: inputlist, y_: outputlist})
    if i % 10000 == 0:        
        print(i / num)
        yargmax = sess.run(tf.argmax(y,1),feed_dict={x:inputtest})
        yargmax_correct = sess.run(tf.argmax(y_,1),feed_dict={y_:outputtest})
        print(yargmax)
        print(yargmax_correct)
        #print(sess.run(b))
        #print(sess.run(cross_entropy,feed_dict={x: inputtest, y_: outputtest}))
        print(sess.run(loss, feed_dict={x: inputlist, y_: outputlist}))
        cnt = 0
        abserror = 0
        for i in range(50):
            abserror+=np.abs(yargmax[i] - yargmax_correct[i])
            if yargmax[i] == yargmax_correct[i]:
                cnt+=1
        print(cnt)
        print(abserror)
        print()

