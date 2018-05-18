#!/usr/bin/env python

"""Clean comment text for easier parsing."""

from __future__ import print_function

import re
import string
import argparse

import sys
from optparse import OptionParser
import json
import bz2


__author__ = ""
__email__ = ""

# Some useful data.
_CONTRACTIONS = {
    "tis": "'tis",
    "aint": "ain't",
    "amnt": "amn't",
    "arent": "aren't",
    "cant": "can't",
    "couldve": "could've",
    "couldnt": "couldn't",
    "didnt": "didn't",
    "doesnt": "doesn't",
    "dont": "don't",
    "hadnt": "hadn't",
    "hasnt": "hasn't",
    "havent": "haven't",
    "hed": "he'd",
    "hell": "he'll",
    "hes": "he's",
    "howd": "how'd",
    "howll": "how'll",
    "hows": "how's",
    "id": "i'd",
    "ill": "i'll",
    "im": "i'm",
    "ive": "i've",
    "isnt": "isn't",
    "itd": "it'd",
    "itll": "it'll",
    "its": "it's",
    "mightnt": "mightn't",
    "mightve": "might've",
    "mustnt": "mustn't",
    "mustve": "must've",
    "neednt": "needn't",
    "oclock": "o'clock",
    "ol": "'ol",
    "oughtnt": "oughtn't",
    "shant": "shan't",
    "shed": "she'd",
    "shell": "she'll",
    "shes": "she's",
    "shouldve": "should've",
    "shouldnt": "shouldn't",
    "somebodys": "somebody's",
    "someones": "someone's",
    "somethings": "something's",
    "thatll": "that'll",
    "thats": "that's",
    "thatd": "that'd",
    "thered": "there'd",
    "therere": "there're",
    "theres": "there's",
    "theyd": "they'd",
    "theyll": "they'll",
    "theyre": "they're",
    "theyve": "they've",
    "wasnt": "wasn't",
    "wed": "we'd",
    "wedve": "wed've",
    "well": "we'll",
    "were": "we're",
    "weve": "we've",
    "werent": "weren't",
    "whatd": "what'd",
    "whatll": "what'll",
    "whatre": "what're",
    "whats": "what's",
    "whatve": "what've",
    "whens": "when's",
    "whered": "where'd",
    "wheres": "where's",
    "whereve": "where've",
    "whod": "who'd",
    "whodve": "whod've",
    "wholl": "who'll",
    "whore": "who're",
    "whos": "who's",
    "whove": "who've",
    "whyd": "why'd",
    "whyre": "why're",
    "whys": "why's",
    "wont": "won't",
    "wouldve": "would've",
    "wouldnt": "wouldn't",
    "yall": "y'all",
    "youd": "you'd",
    "youll": "you'll",
    "youre": "you're",
    "youve": "you've"
}

# You may need to write regular expressions.

def sanitize(text):
    """Do parse the text in variable "text" according to the spec, and return
    a LIST containing FOUR strings 
    1. The parsed text.
    2. The unigrams
    3. The bigrams
    4. The trigrams
    """

    # YOUR CODE GOES BELOW:
    # Q1:
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    # Q2:
    # remove url as [some text](http://ucla.edu)
    text = re.sub(r'\[.*\]\(.*\)','',text)

    # Q3:
    text_list1 = text.split(" ")
    text_list1 = list(filter(None, text_list1))

    # Q4 and Q5:
    punctuation_allowed = ['.', '!', '?', ',', ';', ':']
    text_list2 = list()
    while text_list1:

        # initialization
        text_cur = text_list1.pop(0)
        l = 0
        r = len(text_cur) - 1

        # parse the left part
        text_new_left = list()
        while l <= r:
            if text_cur[l] in string.punctuation:
                if text_cur[l] in punctuation_allowed:
                    text_new_left.append(text_cur[l])
                l += 1
            else:
                break

        # parse the right part
        text_new_right = list()
        while l <= r:
            if text_cur[r] in string.punctuation:
                if text_cur[r] in punctuation_allowed:
                    text_new_right.insert(0, text_cur[r])
                r -= 1
            else:
                break

        # parse the middle part
        if l <= r:
            text_new_mid = text_cur[l:r+1]
        else:
            text_new_mid = ""

        # append the result
        text_list2.extend(text_new_left)
        if text_new_mid:
            text_list2.append(text_new_mid)
        text_list2.extend(text_new_right)


    # TODO: following 2 lines are just for demo purposes
    text = " ".join(text_list2)
    return text
    # return [parsed_text, unigrams, bigrams, trigrams]


if __name__ == "__main__":
    # This is the Python main function.
    # You should be able to run
    # python cleantext.py <filename>
    # and this "main" function will open the file,
    # read it line by line, extract the proper value from the JSON,
    # pass to "sanitize" and print the result as a list.

    # YOUR CODE GOES BELOW.

    # python cleantext.py <filename>
    version_msg = "%prog 1.0"
    usage_msg = """%prog [OPTION]... FILE
Text Parsing"""
    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-n",
                      action="store", dest="numlines", default=1,
                      help="do nothing, just for test")
    options, args = parser.parse_args(sys.argv[1:])

    if len(args) != 1:
        parser.error("wrong number of operands:{0}".
            format(len(args)))
    input_file = args[0]

    # read it line by line, extract the proper value from the JSON,
    fo = open(input_file, 'r')
    for line in fo.readlines(): 
        line = line.strip() 
        #text = sanitize(line)
        #print(text)
    fo.close()

    text = "The he'll     lazy   fox, jumps -!sdf--= the \nlazy dog."
    text = sanitize(text)
    print(text)
