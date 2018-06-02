from __future__ import print_function
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import re
import string
import argparse
from pyspark.sql.functions import udf, col
from pyspark.sql.types import LongType, StringType, ArrayType

# IMPORT OTHER MODULES HERE
def sanitize1(test):
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    
    # remove url as [some text](http://ucla.edu)
    text = re.sub(r'\[.*?\]\((https?|ftp):\/\/(-\.)?([^\s/?\.#-]+\.?)+(\/[^\s]*)?\)','',text)
    text = re.sub (r'(https?|ftp):\/\/(-\.)?([^\s/?\.#-]+\.?)+(\/[^\s]*)?','',text)
    text = re.sub (r'\[.*?\]\(.*?\)','',text)
   
    text_list1 = text.split(" ")
    text_list1 = list(filter(None, text_list1))

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
            if text_cur[l] in string.punctuation and text_cur[l] != '$':
                if text_cur[l] in punctuation_allowed:
                    text_new_left.append(text_cur[l])
                l += 1
            else:
                break

        # parse the right part
        text_new_right = list()
        while l <= r:
            if text_cur[r] in string.punctuation and text_cur[r] != '$':
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
    
    # parsed_text
    parsed_text1 = [item.lower() for item in text_list2]
    parsed_text = ' '.join(e for e in parsed_text1)

    # Unigrams
    unigrams1 = []
    for i in range(len(parsed_text1)):
        if parsed_text1[i] not in string.punctuation:
            unigrams1.append(parsed_text1[i])
    unigrams = ' '.join(f for f in unigrams1)

    # Bigrams
    bigrams1 = []
    for i in range(len(parsed_text1) - 1):
        if parsed_text1[i] not in punctuation_allowed and parsed_text1[i + 1] not in punctuation_allowed:
            bigrams1.append(parsed_text1[i] + "_" + parsed_text1[i + 1])
    bigrams = ' '.join(e for e in bigrams1)

    # Trigrams
    trigrams1 = []
    for i in range(len(parsed_text1) - 2):
        if parsed_text1[i] not in punctuation_allowed and parsed_text1[i + 1] not in punctuation_allowed and parsed_text1[i + 2] not in punctuation_allowed:
            trigrams1.append(parsed_text1[i] + "_" + parsed_text1[i + 1] + "_" + parsed_text1[i + 2])
    trigrams = ' '.join(e for e in trigrams1)
    
    comments = []
    comments = unigrams1 + bigrams1 + trigrams1
    #comm = ' '.join(str(e) for e in comments)
    return comments


def main(context):
    """Main function takes a Spark SQL context."""
    # YOUR CODE HERE
    # YOU MAY ADD OTHER FUNCTIONS AS NEEDED

    # Task 1:
    df_com = sqlContext.read.json("comments-minimal.json.bz2")
    df_sub = sqlContext.read.json("submissions.json.bz2")
    df_lab = sqlContext.read.csv("labeled_data.csv", header=True, inferSchema=True)

    # Task 2:
    df_lab.createOrReplaceTempView('view_lab')
    df_com = df_com.where('id IN (SELECT Input_id FROM view_lab)')
    # df_com.describe().show()
    
    # Task 4 & 5:
    sanitize_udf = udf(sanitize1, ArrayType(StringType()))
    df_sanitize = df_com.select("id", sanitize_udf(col("body")).alias("comments"))
    #df_sanitize.show()


if __name__ == "__main__":
    conf = SparkConf().setAppName("CS143 Project 2B")
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    sc.addPyFile("cleantext.py")
    main(sqlContext)
