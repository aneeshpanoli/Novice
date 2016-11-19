######---topanoli@gmail.com-----Scrabble helper------with an
#option to find meaning..see random_letter_word for evolution

#imp:1------------------------------------------------------------
from PyDictionary import PyDictionary
dictionary = PyDictionary()
#imp:2---------------------------------------------------
from itertools import permutations
#imp:3-----------------------
from operator import itemgetter
#imp-------------
import sys
#func:1-----------------------------------------------------------------
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

#func:2 meaning-----------------------------------------------------------------
#Figures meaning from pydict. statement loops without sys.exit
def meaning():
    word = raw_input("Enter the word: ")
    meaning = dictionary.meaning(word)
    print meaning
    sys.exit()

#func:3------------------------------------------------
#generates permutation combintaions based on the word length
def permus():
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
        None
    return word_permus

#mod:1-----------------
#calls meaning or permutation func based on user input
selection = raw_input("Enter  1 for meaning or 2 for words: ")
selection = int(selection)
if selection == 2:
    word = raw_input("Enter upto 8 random letters: ")
    word = one_chr(word)
    word_all = list(word)
    permus()

elif selection == 1:
    meaning()
else:
    selection = raw_input("Enter  1 for meaning or 2 for words: ")

#mod:2--------------------------
#Joins letters and create actual words and collects in word = ""
words = ""
for i in permus():
    words = ''.join(i) + " " + words
ready_word = words.split(" ")
#ready_word = list(ready_word)
del ready_word[-1]
#mod:3-------------------------------------------------
#Check in deictionary word list for possible matches
with open("dic_words.txt")as dic_words:
    dic_data = dic_words.read()
dic_data = dic_data.split('\n')
words_found = list(set(dic_data).intersection(ready_word))
words_output = ', ' .join(words_found)
words_output = words_output.upper()
if words_output == "":
    print "No words found!"
else:
    print "Possible words are: " + words_output


#================================end of code===================================
