import tensorflow as tf

# input1 = tf.constant(2)
# input2 = tf.constant(3)
# input3 = tf.constant(4)
#
# mul = tf.multiply(input1,input2)
# add = tf.add(mul,input3)
# with tf.Session() as sess:
#     result = sess.run([mul,add])
#     print(result)

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))
