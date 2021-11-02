import np,jieba
import matplotlib.pyplot as plt
import wordcloud as WordCloud
# 自定义类版
class MyWordCloud:
    filePath = ""
    number = 1
    counts = {}
    excludes = []  # 需要排除的词语，例如不是，天气等常见词
    synonym = ()  # 同义词,元组，以该元组最后一个词语作为前面词语的意思

    def __init__(self, path, number, counts={}, excludes=[], synonym=()):
        self.filePath = path
        self.number = number
        self.counts = counts
        self.excludes = excludes
        self.synonym = synonym

    # 使用jieba库进行词频统计
    def count(self):
        txtFile = open(self.filePath, "r").read()
        words = jieba.lcut(txtFile)
        for word in words:
            if len(word) == 1 or len(word) > 4:  # 去除长度为1和大于4的字符
                continue
            for i in range(len(self.synonym)):
                for j in range(len(synonym[i])):
                    if word == synonym[i][j]:
                        word = synonym[i][len(synonym[i]) - 1]
            rword = word
            self.counts[rword] = self.counts.get(rword, 0) + 1  # <class 'int'> 统计词频,0为初值
        # 删除排除词语
        for x in self.excludes:
            del (self.counts[x])

        return self.counts

    # 输出前number词频最高的词语
    def printPreNumberWord(self):
        self.counts = self.count()
        for i in range(15):
            items = list(self.counts.items())
            items.sort(key=lambda x: x[1], reverse=True)  # 降序排序
            word, count = items[i]
            print("{0:<10}{1:<5}".format(word, count))

    # 获取词频最高的前number个词语
    def getPreNumberWord(self, counts=None):
        if (self.counts == None and counts == None):
            counts = self.count()
        else:
            counts = self.counts
        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)  # 降序排序
        wordlist = []
        for i in range(self.number):
            word, count = items[i]
            # print("{0:<10}{1:<5}".format(word, count))  # 输出前N个词频的词语
            wordlist.append(word)  # 把词语word放进一个列表
        return wordlist


if __name__ == '__main__':
    filePath = "./words.txt"
    number = 20
    excludes = []
    synonym = ()
    wl = MyWordCloud(filePath, number=number, excludes=excludes, synonym=synonym)
    wl.printPreNumberWord()