from __future__ import print_function
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

# IMPORT OTHER MODULES HERE


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


if __name__ == "__main__":
    conf = SparkConf().setAppName("CS143 Project 2B")
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    sc.addPyFile("cleantext.py")
    main(sqlContext)
