import os
import warnings
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import hmmlearn.hmm as hl#隐马尔科夫模型

 #梅尔频率倒谱系数算法

warnings.filterwarnings('ignore',
                        category=DeprecationWarning)
np.seterr(all='ignore')

#搜索语音位置 转换路径
def search_speeches(directory, speeches):
    directory = os.path.normpath(directory)
    #路径的合法化 统一 比如： 斜杠
    for entry in os.listdir(directory): #列出目录
        label = directory[
            directory.rfind(os.path.sep) + 1:]
            # 从后往前找 os.path.sep是目录的分隔符  各个系统不一样
        #.../.../apple/apple01找到apple目录 
        path = os.path.join(directory, entry)
        #目录和条目合在一起
        if os.path.isdir(path):#会不会是个目录
            search_speeches(path, speeches)#递归
        elif os.path.isfile(
                path) and path.endswith('.wav'):
        #判断是不是wav文件
            if label not in speeches:
                speeches[label] = []
            speeches[label].append(path)


train_speeches = {}
search_speeches('./speeches/training',
                train_speeches)
# print(speeches)
train_x, train_y = [], []#训练列表 输入x 输出y
for label, filenames in train_speeches.items():
    mfccs = np.array([])
    for filename in filenames:#把每个wav文件读出
        sample_rate, sigs = wf.read(filename)#采样率 和信号数组
        mfcc = sf.mfcc(sigs, sample_rate)#梅尔频率倒谱系数
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
        # print(mfcc.shape)#二维数组对应单词
    train_x.append(mfccs)
    train_y.append(label)

#创建训练模型 
models = {}#每个单词有个模型
for mfccs, label in zip(train_x, train_y):#联合查询
    model = hl.GaussianHMM(n_components=4,
                           covariance_type='diag', n_iter=1000)
# n_components=4 随机状态 学习效果的变化  
# covariance_type 评估相似度 协方差类型 相关性矩阵 对角线上的值
#n_iter 迭代次数
    models[label] = model.fit(mfccs)
#训练 训练模型 和标签放在一起：
#比如apple对应apple的模型 马尔科夫生成模型

#测试数据
test_speeches = {}
search_speeches('./speeches/testing',
                test_speeches)
test_x, test_y = [], []
for label, filenames in test_speeches.items():
    mfccs = np.array([])
    for filename in filenames:
        sample_rate, sigs = wf.read(filename)
        mfcc = sf.mfcc(sigs, sample_rate)
        if len(mfccs) == 0:
            mfccs = mfcc
        else:
            mfccs = np.append(mfccs, mfcc, axis=0)
    test_x.append(mfccs)
    test_y.append(label)
pred_test_y = []
for mfccs in test_x:
    best_score, best_label = None, None
    for label, model in models.items():
        score = model.score(mfccs)
        if (best_score is None) or (
                best_score < score):
            best_score, best_label = score, label
    pred_test_y.append(best_label)
print(test_y)
print(pred_test_y)
