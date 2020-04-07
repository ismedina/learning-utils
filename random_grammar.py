from learning_utils import random_grammar
from colorama import init
init()


if __name__ == "__main__":
    file = 'grammar.md'
    N = 4 # number of grammar resources to use
    random_grammar(file, N)


