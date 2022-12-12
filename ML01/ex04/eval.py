class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum([coef * len(word) for coef, word in zip(coefs, words)])

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum([coef * len(word) for i, coef in enumerate(coefs) for word in words[i]])

# https://pynative.com/python-static-method/