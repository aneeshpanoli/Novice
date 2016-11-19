######---topanoli@gmail.com-----Scrabble helper------improved

#imp:1------------------------------------------------------------
from PyDictionary import PyDictionary
dictionary = PyDictionary()
#imp:2---------------------------------------------------
from itertools import permutations
#imp:3-----------------------
from operator import itemgetter
#mod:1-----------------------------------------------------------------
#gets called by mod:2 when user enters more than one character
# prompts for a letter
def one_chr(string):
    while True:
        len(string) < 1 or string == '' or string == ' ' or len(string) > 8
        if len(string) < 1 or string == '' or string == ' ' or len(string) > 8:
            string = raw_input("Try again, enter upto 8 random letters: ")
##continue asks the while loop to go on
            continue
        else:
            return string
##break stops the while loop
            break

#mod:2-------------------------------------------------------------------
#ask user for random letters prints a list
word = raw_input("Enter upto 8 random letters: ")
word = one_chr(word)
word_all = list(word)

#mod:3---------------------------------------------------------------
#generates all possible permutaitons for the elements in the list
#for permutation in itertools.permutations(word_l):
#def shuffle_lets (int):
if len(word_all) == 2:
    word_permus = list(permutations(word_all, 2))
elif len(word_all) == 3:
    word_permus = list(permutations(word_all, 2)) + \
                            list(permutations(word_all, 3))
elif len(word_all) == 4:
    word_permus = list(permutations(word_all, 2)) + \
        list(permutations(word_all, 3)) + list(permutations(word_all, 4))
elif len(word_all) == 5:
    word_permus = list(permutations(word_all, 2)) + \
        list(permutations(word_all, 3)) + list(permutations(word_all, 4)) \
        + list(permutations(word_all, 5))
elif len(word_all) == 6:
    word_permus = list(permutations(word_all, 2)) + \
        list(permutations(word_all, 3)) + list(permutations(word_all, 4)) \
        + list(permutations(word_all, 5)) + list(permutations(word_all, 6))
elif len(word_all) == 7:
    word_permus = list(permutations(word_all, 2)) + \
        list(permutations(word_all, 3)) + list(permutations(word_all, 4)) \
        + list(permutations(word_all, 5)) + list(permutations(word_all, 6)) \
        + list(permutations(word_all, 7))
elif len(word_all) == 8:
    word_permus = list(permutations(word_all, 2)) + \
        list(permutations(word_all, 3)) + list(permutations(word_all, 4)) \
        + list(permutations(word_all, 5)) + list(permutations(word_all, 6)) \
        + list(permutations(word_all, 7)) + list(permutations(word_all, 8))
else:
    print "Not enough letters!"

## here words creates an empty string to collect the data from for loop
##this is such a neat trick
words = ""
for i in word_permus:
    words = ''.join(i) + " " + words
ready_word = words.split(" ")
#ready_word = list(ready_word)
del ready_word[-1]

#mod4------------------------------------------------

with open("dic_words.txt")as dic_words:
    dic_data = dic_words.read()

dic_data = dic_data.split('\n')
words_found = list(set(dic_data).intersection(ready_word))
words_output = ', ' .join(words_found)
words_output = words_output.upper()
if words_output == " ":
    print "No words found!"
else:
    print "Possible words are: " + words_output


# for w in words_found:
#     print (dictionary.meaning(w))
