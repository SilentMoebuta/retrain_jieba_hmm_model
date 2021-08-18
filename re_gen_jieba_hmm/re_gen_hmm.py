import math
import json

# 读取自己准备好的词典，用词典里的数据进行统计
# 词典的格式和标准的jieba词典的格式相同 都是 “词语 词频 词性”
with open('jieba_userdict.txt', 'r', encoding='utf-8') as handle:
    text = handle.readlines()


def func(x):
    # 可以对词频做一些调整，因为用例里的词频相差太大所以用了log来缩小差距
    return int(math.log(x, 2))*10



def res_merge(ab):
    ab = sorted(ab, key=lambda x: x[0], reverse=True)
    res = [ab[0]]
    for i in range(1, len(ab)):
        if res[-1][0] == ab[i][0]:
            res[-1][1] += ab[i][1]
        else:
            res.append(ab[i])
    return res

# 用例中的结尾都是n因此按照' n\n'来做了strip，实际上不一定是n
text = [x.strip(' n\n').split(' ') for x in text]
word = []
for x in text:
    if len(x[0]) <= 4:
        word.append(x)
tk = [x[0] for x in word]
# print(tk[:5])
tv = [func(int(x[1])) for x in word]
# print(tv[:5])
B, M, E, S = [], [], [], []
for i in range(len(tk)):
    if len(tk[i]) == 1:
        S.append([tk[i], tv[i]])
    elif len(tk[i]) == 2:
        B.append([tk[i][0], tv[i]])
        E.append([tk[i][1], tv[i]])
    elif len(tk[i]) == 3:
        B.append([tk[i][0], tv[i]])
        M.append([tk[i][1], tv[i]])
        E.append([tk[i][2], tv[i]])
    else:
        B.append([tk[i][0], tv[i]])
        M.append([tk[i][1], tv[i]])
        M.append([tk[i][2], tv[i]])
        E.append([tk[i][3], tv[i]])
B = res_merge(B)
M = res_merge(M)
E = res_merge(E)
S = res_merge(S)
bs = sum([x[1] for x in B])
ms = sum([x[1] for x in M])
es = sum([x[1] for x in E])
ss = sum([x[1] for x in S])
B = [[x[0], round(math.log(x[1]/bs, 2.828), 6)] for x in B]
M = [[x[0], round(math.log(x[1]/ms, 2.828), 6)] for x in M]
E = [[x[0], round(math.log(x[1]/es, 2.828), 6)] for x in E]
S = [[x[0], round(math.log(x[1]/ss, 2.828), 6)] for x in S]

B = dict(zip([json.dumps(x[0]) for x in B], [x[1] for x in B]))
M = dict(zip([json.dumps(x[0]) for x in M], [x[1] for x in M]))
E = dict(zip([json.dumps(x[0]) for x in E], [x[1] for x in E]))
S = dict(zip([json.dumps(x[0]) for x in S], [x[1] for x in S]))
P = {'B':B,'M':M,'E':E,'S':S}
# print(B.get('天'), len(B), bs)
# print(M.get('天'), len(M), ms)
# print(E.get('天'), len(E), es)
# print(S.get('天'), len(S), ss)
# print(P.get('E'))


with open('prob_emit.py', 'w', encoding='utf8') as f:
    f.write("from __future__ import unicode_literals")
    f.write('\n\n')

    f.write("P={'B': {\n")
    for k in P['B'].keys():
        f.write(str(k)+': '+ str(P['B'][k]) + ',\n')
    f.write("},\n")
    f.write("'M': {\n")
    for k in P['M'].keys():
        f.write(str(k)+': '+ str(P['M'][k]) + ',\n')
    f.write("},\n")
    f.write("'E': {\n")
    for k in P['E'].keys():
        f.write(str(k)+': '+ str(P['E'][k]) + ',\n')
    f.write("},\n")
    f.write("'S': {\n")
    for k in P['S'].keys():
        f.write(str(k)+': '+ str(P['S'][k]) + ',\n')
    f.write("},\n")
    f.write("}\n")
