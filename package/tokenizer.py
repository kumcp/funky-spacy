

class Tokenizer():

    def __init__(self):

        self.cache = {
            "hello": "hi"
        }

    def tokenize_sentence(self, sentence="", lang="en", delimiter=" "):
        """Function that tokenize a sentence and return a known common list.

        Keyword Arguments:
            sentence {str} -- sentence to be tokenized (default: {""})
            lang {str} -- Language code (default: {"en"})

        Raises:
            ValueError -- Error raise when parameters are not in correct type

        Returns:
            Array -- An array of string as token in sentence
        """

        if not isinstance(sentence, str):
            raise ValueError(str)

        if not isinstance(lang, str):
            raise ValueError("lang is expect to be %s" % (str))

        result_tokens = []

        for word in sentence.split(delimiter):

            lower_word = str.lower(word)

            if lower_word in self.cache:
                result_tokens.append(self.cache[lower_word])
            else:
                subtokens = self.tokenize_word(lower_word)
                result_tokens.append(lower_word)
                self.cache[lower_word] = subtokens

        return result_tokens

    def tokenize_word(self, word):
        return word


a = Tokenizer()
print(a.tokenize_sentence("Hello World", "en"))
