import helpers

class Classifier:

    def __init__(self, positive_corpus, negative_corpus):
        self.positive_corpus = positive_corpus
        self.negative_corpus = negative_corpus
        self.total_probability = 0
        self.inverse_total_probability = 0
        self.tolerance = 0.05

    def classify(self, text):
        stop_words = helpers.get_stop_words()

        for word in text.split(" "):
            if word.lower() in stop_words:
                continue
            positive_matches = self.positive_corpus.token_count(word)
            negative_matches = self.negative_corpus.token_count(word)
            positive_total = self.positive_corpus.total_tokens
            negative_total = self.negative_corpus.total_tokens
            # print word
            # print "========="
            probability = self.calculate_probability(positive_matches, positive_total, negative_matches, negative_total)
            self.record_probability(probability)

        final_probability = self.combine_probabilities()

        return {"sentiment": self.compute_sentiment(final_probability), "probability": final_probability}

    def calculate_probability(self, positive_matches, positive_total, negative_matches, negative_total):
        # print "pos_mat ", positive_matches, ", pos_tot: ", positive_total, ", neg_mat: ", negative_matches, "neg_tot: ", negative_total
        total = positive_matches + negative_matches
        positive_ratio = positive_matches / float(positive_total)
        negative_ratio = negative_matches / float(negative_total)
        probability = positive_ratio / (positive_ratio + negative_ratio) if positive_ratio + negative_ratio != 0 else 0
        print "total: ", total, ", positive_ratio: ", positive_ratio, ", negative_ratio: ", negative_ratio, ", prob: ", probability
        # print ((unknown_word_strength * unknown_word_probability) + (total * probability)) / (unknown_word_strength + total)
        # print "========================================================================================"
        return ((total * probability) + 1) / (total + 2)

    def record_probability(self, probability):
        if probability is None:
            return
        self.total_probability = probability if self.total_probability == 0 else self.total_probability * probability
        self.inverse_total_probability = (1 - probability) if self.inverse_total_probability == 0 else self.inverse_total_probability * (1 - probability)

    def combine_probabilities(self):
        if self.total_probability == 0:
            return 0.5
        return self.total_probability / (self.total_probability + self.inverse_total_probability)

    def compute_sentiment(self, probability):
        if probability < (0.5):
            return "Negative"
        if probability > (0.5):
            return "Positive"
        return "Neutral"