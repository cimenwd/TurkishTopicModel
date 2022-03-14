# Örnek Kullanım
# Turkish News 70000 CSV dosyası kullanılır
# "https://www.kaggle.com/suleymancan/turkishnews70000/version/1?select=turkish_news_70000.csv"

import TurkishTopicModel

TurkishTopicModel.Data.read_csv(file="turkish_news_70000.csv",header=0)

TurkishTopicModel.PreProcess.fixUnicode("text", "text1")

dt=TurkishTopicModel.Data.datafrm

TurkishTopicModel.PreProcess.Clean("text1", "text2")

TurkishTopicModel.PreProcess.Data.savePickle()

TurkishTopicModel.PreProcess.Clean("text1", "text2")

TurkishTopicModel.PreProcess.fixChars("text2", "text3")

TurkishTopicModel.PreProcess.correctSpelling("text3", "text4")

TurkishTopicModel.PreProcess.NormalizeWords("text4", "text5")

TurkishTopicModel.PreProcess.MorphologyReplace("text5", "text6", "lemma", "max")

TurkishTopicModel.PreProcess.cleanStops("text6", "text7","nltk")

TurkishTopicModel.PreProcess.Data.savePickle()

"""Create New Corpus"""
TurkishTopicModel.PreProcess.Data.loadPickle()
#Data Transfer from Preprocess to Modeling Class
TurkishTopicModel.transferData()

#Create Corpus
TurkishTopicModel.TopicModel.createCorpus(column="text7")
TurkishTopicModel.PreProcess.Data.datafrm=TurkishTopicModel.TopicModel.datafrm
TurkishTopicModel.PreProcess.Data.savePickle()

#Loading a Corpus
TurkishTopicModel.TopicModel.loadCorpus(column="text7")

##Term Extraction using PMI##
###[Mustafa Kemal ATATÜRK] [Bandırma Vapuru] [İstanbul Üniversitesi]
###Pointwise Mutual Information
cands=TurkishTopicModel.TopicModel.corpus.extract_ngrams(max_len=3, normalized=True,max_cand=1000)
import pandas as pd

candidate=pd.DataFrame(columns=["words","score"])
for cand in cands:
    cd={"words":cand.words,"score":cand.score}
    candidate=candidate.append(cd,ignore_index=True)

##Create LDA Model##
TurkishTopicModel.TopicModel.LDAModel(column="text7",k=50,iteration=500,tw="PMI")

##Print Topic Words##
for i in range(0,TurkishTopicModel.TopicModel.mdl.k):
    print(TurkishTopicModel.TopicModel.mdl.get_topic_words(i))

##PYLdaVis##
TurkishTopicModel.TopicModel.ldavis("text7")

##Infering##
TurkishTopicModel.TopicModel.infer("text7")

##Infering Example ##
article_text=""""Çukur" dizisinde canlandırdığı "Vartolu" karakteriyle milyonların gönlünde taht kuran Erkan Kolçak Köstendil, dizinin sona ermesiyle birlikte Hollanda'ya taşınmıştı. """


import re
import numpy
article_text = re.sub (re.compile (r"[\\][ntrv]"), ' ', article_text)
article_text = re.sub (re.compile (r'[^0-9a-zA-ZçığöüşÇİĞÖÜŞ ]'), ' ', article_text)
while "  " in article_text: article_text = article_text.replace ("  ", " ")
article_text=article_text.lower()
doc=TurkishTopicModel.TopicModel.mdl.make_doc(words=article_text.split(" "))
topic_dist, ll = TurkishTopicModel.TopicModel.mdl.infer (doc)

topic=numpy.argmax(topic_dist)
