

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        original_sorted = sorted(self.word)
        matches = []

        for word in word_list:
            if word.lower() != self.word and sorted(word.lower()) == original_sorted:
                matches.append(word)

        return matches
