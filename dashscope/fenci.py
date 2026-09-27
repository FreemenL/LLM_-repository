import jieba

chunk = "这是一个基于分词的文本处理工具"

words = jieba.lcut(chunk,cut_all=False)

print('精确分词结果',words)


words = jieba.lcut(chunk,cut_all=True)

print('全模式分词结果',words)

words = jieba.lcut_for_search(chunk)

print('搜索引擎分词结果',words)

# tf  词频 关键词在当前文档出现的次数
# idf 逆文档频率 有多少文档出现过这个关键词

# 1. 一个词在当前文档出现越多 → TF 越高，越重要
# 2. 但是如果这个词在**几乎所有文档都大量出现**（比如：的、是、和），它就没区分价值 → IDF 压低权重


