# retrain_jieba_hmm_model
re-train the hmm model of jieba to inhance the seg performance.
通过添加用户词典可以提高jieba分词的效果
通过替换hmm模型可以略微提高jieba分词的效果

# 使用
1.运行re_gen_hmm.py，读取user dict的数据，生成新的hmm model文件
2.将生成的prob_emit.py文件替换掉../jieba/finalseg/prob_emit.py文件
3.按照jieba的安装方式进行安装，或者直接放在当前目录中调用

# 效果对比
···
具体结果可见res.xlsx文件
文本：“妙然欧式简约大号无盖素色垃圾桶家用客厅卫生间垃圾筒纸篓”
jieba分词：['妙然', '欧式', '简约', '大', '号', '无盖', '素色', '垃圾桶', '家用', '客厅', '卫生间', '垃圾筒', '纸篓']
jieba分词+用户词典：['妙然', '欧式', '简约', '大号', '无盖', '素色', '垃圾桶', '家用', '客厅', '卫生间', '垃圾筒', '纸篓']
jieba分词+用户词典+hmm模型：['妙然', '欧式简约大号', '无盖', '素色', '垃圾桶', '家用', '客厅', '卫生间', '垃圾筒', '纸篓']
”
···

