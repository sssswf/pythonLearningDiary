# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:53:12 2018

@author: ASUS
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#MNIST数据集的相关的常数
#输入层的节点数，对于MNIST数据集，这个等于图片的像素
INPUT_NODE = 784
#输出层的节点数，这个等于类别的数目。因为在MNIST数据集中需要区分的是0-9这10个数字。
OUTPUT_NODE = 10
#设置神经网络的参数
#隐藏层节点数，这里只使用一个隐藏层的网络结构作为样例。这个隐藏层有500个节点。
LAYER1_NODE = 500
#一个训练batch中的训练数据个数。数字越小时，训练过程接近随机梯度下降；数据越大时，训练接近梯度下降
BACTH_SIZE = 100
#基础的学习率
LEARNING_RATE_BASE = 0.8
#学习率的衰减率
LEARNING_RATE_DECAY = 0.99
#描述模型复杂度的正则化项在损失函数中的系数
REGULARIZATION_RATE = 0.001
#训练次数
TRAINING_STEPS = 3000
#滑动平均衰减
MOVING_AVERAGE_DECAY = 0.99

#一个辅助函数，给定神经网络的输入和所有参数，计算神经网络的前向传播结果。在这里定义一个ReLU激活函数的三层全链接神经网络。
#通过加入隐藏层实现多层网络结构，通过ReLU激活函数实现去线性化。在这个函数中也支持传入用于计算参数均值的类。这样方便在测试时使用滑动平均模型
def inference(input_tensor,avg_class,weights1,biases1,weights2,biases2):
    #当没有提供滑动平均类是，直接使用参数当前的取值
    if avg_class == None:
        #计算隐藏层的前向传播结果，这里使用了ReLU激活函数
        layer1 = tf.nn.relu(tf.matmul(input_tensor,weights1)+biases1)
        #计算输出层的前向传播结果，因为在计算损失函数时会一并计算softmax函数，所以这里不需要加入激活函数。而且不加入softmax不会影响预测结果。
        #因为预测时使用的是不用于对应节点输出值的相对大小，有没有softmax层对最后的分类结果的计算没有影响。于是在计算整个神经网络的前向传播时
        #可以不加最后的softmax层。
        return tf.matmul(layer1,weights2)+biases2
    #否则，使用滑动平均值
    else:
        #首先使用avg_class.average函数来计算得出变量的滑动平均值。
        #然后再计算相应的神经网络前向传播的结果。
        layer1 = tf.nn.relu(tf.matmul(input_tensor,weights1)+avg_class.average(biases1))
        return tf.matmul(layer1,avg_class.average(weights2))+avg_class.average(biases2)

#定义训练过程
def train(mnist):
    #占位符，定义x，y_变量
    x = tf.placeholder(tf.float32,[None,INPUT_NODE],name = 'x-input')
    y_ = tf.placeholder(tf.float32,[None,OUTPUT_NODE],name = 'y-input')
    #生成隐藏层的参数
    weights1 = tf.Variable(tf.truncated_normal([INPUT_NODE,LAYER1_NODE],stddev = 0.1))
    biases1 = tf.Variable(tf.constant(0.1,shape=[LAYER1_NODE]))
    #生成输出层的参数
    weights2 = tf.Variable(tf.truncated_normal([LAYER1_NODE,OUTPUT_NODE],stddev = 0.1))
    biases2 = tf.Variable(tf.constant(0.1,shape=[OUTPUT_NODE]))
    #计算在当前参数下神经网络前向传播的结果。这里给出的用于计算滑动平均的类为None，所以函数不会使用参数滑动平均
    y = inference(x,None,weights1,biases1,weights2,biases2)
    #定义存储训练的变量。这个变量不需要计算滑动平均，所以这里指定这个变量为不可训练的变量（trainable = False）。在使用TensorFlow训练神经网络时，
    #一般会将代表训练轮数的变量指定为不可训练的参数
    global_step = tf.Variable(0,trainable = False)
    #给定滑动平均衰减率和训练轮数的变量，初始化滑动平均类。
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY,global_step)
    #在所有代表神经网络参数的变量上使用滑动平均，其他的辅助变量(比如global_step)就不需要了。tf.trainable_variables返回的就是图像
    #GraphKeys.TRAINABLE_VARIABLES中的元素。这个集合的元素就是所有没有指定trainable = False的参数
    variable_averages_op = variable_averages.apply(tf.trainable_variables())
    #计算使用了滑动平均之后的前向传播的结果，滑动平均不会改变变量本身的取值，而是会维护一个影子变量来记录其滑动平均值。所以当需要使用这个滑动
    #平均值时，需要明确调用average函数
    average_y = inference(x,variable_averages,weights1,biases1,weights2,biases2)
    #计算交叉熵作为刻画预测值和真实值之间差距的损失函数。函数第一个参数是神经网络不包括softmax层的前向传播结果，第二层是训练数据的正确答案。
    #因为答案是一个长度为10的数组，而该函数是需要提供一个正确答案的数字，所以使用tf.argmax()来得到正确答案对应的类别编号。
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,labels =tf.arg_max(y_,1))
    #计算在当前batch中所有样例的交叉熵的平均值
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    #计算L2正则化的损失函数
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    #一般只计算权重的正则化损失，而不是用偏置项
    regularizaton = regularizer(weights1) +regularizer(weights2)
    #总损失等于交叉熵损失与正则化损失的和
    loss = cross_entropy_mean + regularizaton
    #设置指数衰减的学习率
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,mnist.train.num_examples/BACTH_SIZE,
                                               LEARNING_RATE_DECAY)
    #使用GD梯度下降优化算法优化损失函数
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step = global_step)
    #在训练神经网络模型时，每过一遍数据急需要通过反向传播来更新神经网络的参数，又要更新每一个参数的滑动平均值。为了一次完成操作：
    #tf.control_dependencies()\tf.group()两种机制均能实现
    #train_OP = tf.group(train_step,variable_averages_op)
    with tf.control_dependencies([train_step,variable_averages_op]):
        train_op = tf.no_op(name = 'train')
    #检验使用了滑动均值模型的神经网络前向传播结果是否正确。tf.argmax(average_y,1)计算每一个样例的预测答案。其中average_y是一个batch_size*10的二维
    #数组，每一行表示一个样例的前向传播结果，tf.argmax的第二个参数‘1’表示选取最大值的操作在第一个维度中进行，也就是说，只在每一行选择最大值对应的下标。
    #于是得到的结果是一个长度为batch的一维数组，这个一维数组中的值就表示了每一个样例对应的数字识别的结果。
    #tf.equal()判断两个张量是否相等。
    correct_prediction = tf.equal(tf.arg_max(average_y,1),tf.argmax(y_,1)) 
    #首先讲bool值转化为数值，然后局算平均值
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

    #初始会话，并开始训练过程
    with tf.Session() as sess:
        #将所有的参数变量初始化
        tf.initialize_all_variables().run()
        #验证数据
        validate_feed = {x:mnist.validation.images,y_:mnist.validation.labels}
        #测试数据
        test_feed= {x:mnist.test.images,y_:mnist.test.labels}
        #迭代训练神经网络
        for i in range(TRAINING_STEPS):
            if i%1000 == 0:
                validate_acc = sess.run(accuracy,feed_dict=validate_feed)
                print('循环次数：%d,正确率：%g'%(i,validate_acc))
            #产生这一轮使用的一个batch数据，并运行训练过程
            xs,ys = mnist.train.next_batch(BACTH_SIZE)
            sess.run(train_op,feed_dict = {x:xs,y_:ys})
            '''
            #上述是处理好的batch，不用写循环。
            for i in range(Steps):
                #每次选择batch_size个样本进行训练
                #初始定位为整个数据集batch_size的倍数，且一定是小于dataset_size的数
                start = (i*batch_size)%dataset_size
                #print(start)
                ##结束位置一般是加上一个batch_size，另外如果取到最后一个batch的时候，刚好是最后一个数据集的位置，两者和等于最后位置时，取最后的位置。
                end = min(start+batch_size,dataset_size)
                #通过选取的样本训练神经网络并更新参数
                sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})

                if i%1000==0:
                    #每隔一段时间计算所有数据的交叉熵并输出
                    total_cross_entropy = sess.run(cross_entropy,feed_dict={x:X,y_:Y})
                    print('循环:%d,交叉熵：%g'%(i,total_cross_entropy))
            '''   
        test_acc = sess.run(accuracy,feed_dict=test_feed)
        print('正确率：%g'%test_acc)
#SSS = train(mnist)        
def main(argv = None):
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    train(mnist)

if __name__ == '__main__':
    tf.app.run()
