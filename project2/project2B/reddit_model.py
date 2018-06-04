from __future__ import print_function
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import udf, col
from pyspark.sql.types import LongType, StringType, ArrayType
from pyspark.ml.feature import CountVectorizer

# IMPORT OTHER MODULES HERE
from cleantext import sanitize
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import BinaryClassificationEvaluator

def train_process(pos, neg):
    # Initialize two logistic regression models.
    # Replace labelCol with the column containing the label, and featuresCol with the column containing the features.
    poslr = LogisticRegression(labelCol="poslabel", featuresCol="features", maxIter=10)
    neglr = LogisticRegression(labelCol="neglabel", featuresCol="features", maxIter=10)
    # This is a binary classifier so we need an evaluator that knows how to deal with binary classifiers.
    posEvaluator = BinaryClassificationEvaluator()
    negEvaluator = BinaryClassificationEvaluator()
    # There are a few parameters associated with logistic regression. We do not know what they are a priori.
    # We do a grid search to find the best parameters. We can replace [1.0] with a list of values to try.
    # We will assume the parameter is 1.0. Grid search takes forever.
    posParamGrid = ParamGridBuilder().addGrid(poslr.regParam, [1.0]).build()
    negParamGrid = ParamGridBuilder().addGrid(neglr.regParam, [1.0]).build()
    # We initialize a 5 fold cross-validation pipeline.
    posCrossval = CrossValidator(
        estimator=poslr,
        evaluator=posEvaluator,
        estimatorParamMaps=posParamGrid,
        numFolds=5)
    negCrossval = CrossValidator(
        estimator=neglr,
        evaluator=negEvaluator,
        estimatorParamMaps=negParamGrid,
        numFolds=5)
    # Although crossvalidation creates its own train/test sets for
    # tuning, we still need a labeled test set, because it is not
    # accessible from the crossvalidator (argh!)
    # Split the data 50/50
    posTrain, posTest = pos.randomSplit([0.5, 0.5])
    negTrain, negTest = neg.randomSplit([0.5, 0.5])
    # Train the models
    print("Training positive classifier...")
    posModel = posCrossval.fit(posTrain)
    print("Training negative classifier...")
    negModel = negCrossval.fit(negTrain)

    # Once we train the models, we don't want to do it again. We can save the models and load them again later.
    posModel.save("www/pos.model")
    negModel.save("www/neg.model")




def main(context):
    """Main function takes a Spark SQL context."""
    # YOUR CODE HERE
    # YOU MAY ADD OTHER FUNCTIONS AS NEEDED

    # Task 1:
    df_com = sqlContext.read.json("/home/cs143/data/comments-minimal.json.bz2")
    df_sub = sqlContext.read.json("/home/cs143/data/submissions.json.bz2")
    df_lab = sqlContext.read.csv("labeled_data.csv", header=True, inferSchema=True)


    # save data
    """
    df_com.write.parquet("/home/cs143/data/comments-minimal.parquet")
    df_sub.write.parquet("/home/cs143/data/submissions.parquet")
    df_lab.write.parquet("/home/cs143/data/labeled_data.parquet")

    df_com = sqlContext.read.parquet("/home/cs143/data/comments-minimal.parquet")
    df_sub = sqlContext.read.parquet("/home/cs143/data/submissions.parquet")
    df_lab = sqlContext.read.parquet("/home/cs143/data/labeled_data.parquet")
    """
    

    # Task 2:
    df_lab.createOrReplaceTempView('view_lab')
    df_com = df_com.where('id IN (SELECT Input_id FROM view_lab)')
    # df_com.describe().show()
    
    # Task 4 & 5:
    sanitize_udf = udf(sanitize, ArrayType(StringType()))
    df_sanitize = df_com.select("id", sanitize_udf(col("body")).alias("comments"))
    #df_sanitize.show()

    # save data
    """
    df_sanitize.write.parquet("/home/cs143/data/sanitize.parquet")
    df_sanitize = sqlContext.read.parquet("/home/cs143/data/sanitize.parquet")
    """

    # Task 6A

    cv = CountVectorizer(inputCol="comments", outputCol="features", binary=True, minDF=5.0)
    model = cv.fit(df_sanitize)

    df_cv = model.transform(df_sanitize)
    df_cv.show()

    # save data
    """
    df_cv.write.parquet("/home/cs143/data/CountVectorizer.parquet")
    df_cv = sqlContext.read.parquet("/home/cs143/data/CountVectorizer.parquet")
    """


    # Task 6B

    df_cv.createOrReplaceTempView('view_cv')
    df_poslabel = sqlContext.sql('SELECT Input_id, IF(labeldjt = 1, 1, 0) AS label FROM view_lab')
    df_poslabel.createOrReplaceTempView('view_poslab')
    df_pos = sqlContext.sql('SELECT id, features, view_poslab.label AS label FROM view_cv INNER JOIN view_poslab ON view_poslab.Input_id = view_cv.id')

    df_neglabel = sqlContext.sql('SELECT Input_id, IF(labeldjt = -1, 1, 0) AS label FROM view_lab')
    df_neglabel.createOrReplaceTempView('view_neglab')
    df_neg = sqlContext.sql('SELECT id, features, view_neglab.label AS label FROM view_cv INNER JOIN view_neglab ON view_neglab.Input_id = view_cv.id')

    # Task 7
    train_process(df_pos, df_neg)




if __name__ == "__main__":
    conf = SparkConf().setAppName("CS143 Project 2B")
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    sc.addPyFile("cleantext.py")
    main(sqlContext)
