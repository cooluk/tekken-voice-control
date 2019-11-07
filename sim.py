from gensim import models

koModel = models.fasttext.load_facebook_model('./model/cc.ko.300.bin')



print('나락' in koModel)