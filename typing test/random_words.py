import re
import random
class random_words:
    @staticmethod
    def get_easy_sentance(size):
        word_file = "easy_words.txt"
        #opens easy word.txt
        WORDS = open(word_file).read().splitlines()
        sentence = ""
        space = " "

        i = 0
        while i < (size):
            #chooses a random easy word
            word = random.choice(WORDS)
            #uses regex to clean the word beacause the corpus was very large and some of the words where numbers symbols etc
            if re.search('^[a-z]', word):
                pass
            else:
                continue
            if i == 0:
                # ands the word to the sent with no space since its the last one
                sentence = sentence + word
            else:
                # ands word to sent with space
                sentence = sentence + space + word
            i+=1 

        return sentence

    @staticmethod
    #same as easy just no regex since the corpus was a lot smaller
    def get_hard_sentance(size):
        word_file = "words.txt"
        WORDS = open(word_file).read().splitlines()
        sentence = ""
        space = " "

        for i in range(size):
            word = random.choice(WORDS)
            if i == 0:
                sentence = sentence + word
            else:
                sentence = sentence + space + word

        return sentence



