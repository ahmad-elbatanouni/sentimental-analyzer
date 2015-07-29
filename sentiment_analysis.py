from sentimental_analysis import Corpus
from sentimental_analysis import Classifier

positive_training_data_path = './data/positive_x'
negative_training_data_path = './data/negative_x'

positive_corpus = Corpus()
negative_corpus = Corpus()

positive_corpus.load_from_directory(positive_training_data_path)
negative_corpus.load_from_directory(negative_training_data_path)

classifier = Classifier(positive_corpus, negative_corpus)

# print classifier.classify("It is sunny today")
print classifier.classify("i'm in love with this thing")


