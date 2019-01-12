import dataread
import tensorflow as tf
import numpy as np

def bin2dec(arr):
    result = 0
    for i in range(arr.shape[0]):
        result+=arr[i] * 2 ** (arr.shape[0] - 1 - i)
    return result

#lst=[1,0,1,1,0,1,1,0]
#print(bin2dec(np.asarray(lst)))
inputlist = dataread.input('learn')
outputlist = dataread.output('learn')
print()

input_dim = inputlist.shape[1]
output_dim = outputlist.shape[1]

x = tf.placeholder(tf.float32, [None, input_dim])
W = tf.Variable(tf.random_normal([input_dim,output_dim]))
b = tf.Variable(tf.random_normal([output_dim]))

y_ = tf.placeholder("float", [None,output_dim])

# ================================================================
# main model
# ================================================================
y = tf.nn.softmax(tf.matmul(x,W) + b)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.0004).minimize(cross_entropy)
# ================================================================

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# test set
inputtest = dataread.input('validate')
outputtest = dataread.output('validate')

num = 400001
for i in range(num):
    sess.run(train_step, feed_dict={x: inputlist, y_: outputlist})
    if i % 10000 == 0:
        print(i / num)
        yargmax = sess.run(tf.argmax(y,1),feed_dict={x:inputtest})
        yargmax_correct = sess.run(tf.argmax(y_,1),feed_dict={y_:outputtest})
        print(yargmax)
        print(yargmax_correct)
        print(sess.run(b))
        print(sess.run(cross_entropy,feed_dict={x: inputtest, y_: outputtest}))
        cnt = 0
        abserror = 0
        for i in range(50):
            abserror+=np.abs(yargmax[i] - yargmax_correct[i])
            if yargmax[i] == yargmax_correct[i]:
                cnt+=1
        print(cnt)
        print(abserror)
        print()
        #yargmax = sess.run(tf.argmax(y,1),feed_dict={x:inputtest})
        #correct = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
        #accuracy = tf.reduce_mean(tf.cast(correct, "float"))
        #print(accuracy.eval(feed_dict={x: inputtest, y_: outputtest}))
#print(inputtest)
#yraw = sess.run(y,feed_dict={x:inputtest})
#print(yraw)

# best: 37 correct 14 abserror (rate=0.0004)
# final: 36 correct 17 abserror then nan...nan
print()
