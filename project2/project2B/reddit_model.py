from __future__ import print_function
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import udf, col,from_unixtime, sum, count 
from pyspark.sql.types import LongType, StringType, ArrayType,IntegerType,DateType
from pyspark.ml.feature import CountVectorizer

# IMPORT OTHER MODULES HERE
from cleantext import sanitize
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder,CrossValidatorModel
from pyspark.ml.evaluation import BinaryClassificationEvaluator

def train_process(pos, neg):
    # Initialize two logistic regression models.
    # Replace labelCol with the column containing the label, and featuresCol with the column containing the features.
    poslr = LogisticRegression(labelCol="label", featuresCol="features", maxIter=10)
    neglr = LogisticRegression(labelCol="label", featuresCol="features", maxIter=10)
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
    
    # df_com.write.parquet("/home/cs143/data/comments-minimal.parquet")
    # df_sub.write.parquet("/home/cs143/data/submissions.parquet")
    # df_lab.write.parquet("/home/cs143/data/labeled_data.parquet")
    
    
    
    # df_com = sqlContext.read.parquet("/home/cs143/data/comments-minimal.parquet")
    # df_sub = sqlContext.read.parquet("/home/cs143/data/submissions.parquet")
    # df_lab = sqlContext.read.parquet("/home/cs143/data/labeled_data.parquet")
    
    

    # Task 2:
    df_lab.createOrReplaceTempView('view_lab')
    df_com = df_com.where('id IN (SELECT Input_id FROM view_lab)')
    # # df_com.describe().show()
    
    # # Task 4 & 5:
    sanitize_udf = udf(sanitize, ArrayType(StringType()))
    df_sanitize = df_com.select("id", sanitize_udf(col("body")).alias("comments"))
    #df_sanitize.show()

    # # save data
    # """
    # df_sanitize.write.parquet("/home/cs143/data/sanitize.parquet")
    # df_sanitize = sqlContext.read.parquet("/home/cs143/data/sanitize.parquet")
    # """

    # # Task 6A

    cv = CountVectorizer(inputCol="comments", outputCol="features", binary=True, minDF=5.0)
    model = cv.fit(df_sanitize)

    df_cv = model.transform(df_sanitize)
    # df_cv.show()

    # save data
    """
    df_cv.write.parquet("/home/cs143/data/CountVectorizer.parquet")
    df_cv = sqlContext.read.parquet("/home/cs143/data/CountVectorizer.parquet")
    """


    # # Task 6B

    df_cv.createOrReplaceTempView('view_cv')
    df_poslabel = sqlContext.sql('SELECT Input_id, IF(labeldjt = 1, 1, 0) AS label FROM view_lab')
    df_poslabel.createOrReplaceTempView('view_poslab')
    df_pos = sqlContext.sql('SELECT id, features, view_poslab.label AS label FROM view_cv INNER JOIN view_poslab ON view_poslab.Input_id = view_cv.id')

    df_neglabel = sqlContext.sql('SELECT Input_id, IF(labeldjt = -1, 1, 0) AS label FROM view_lab')
    df_neglabel.createOrReplaceTempView('view_neglab')
    df_neg = sqlContext.sql('SELECT id, features, view_neglab.label AS label FROM view_cv INNER JOIN view_neglab ON view_neglab.Input_id = view_cv.id')

    # Task 7
    df_pos.write.parquet("home/cs143/data/pos.parquet")
    df_neg.write.parquet("home/cs143/data/neg.parquet")
    train_process(df_pos, df_neg)

    # Task 8
    idtype_udf = udf(idtype, StringType())
    df_com_full = df_com.select("id",idtype_udf(col("link_id")).alias("link_id"),"body","created_utc","author_flair_text")
    # df_com_full.write.parquet("/home/cs143/data/comfull.parquet")
    # df_com_full = sqlContext.read.parquet("/home/cs143/data/comfull.parquet").sample(False, 0.01, None)
    # df_com_full.show()

    df_sub_full = df_sub.select(col("id").alias("sub_id"), "title")
    # df_sub_full = sqlContext.read.parquet("/home/cs143/data/subfull.parquet").sample(False, 0.01, None)
    # df_sub_full.show()
    # df_sub_full.write.parquet("/home/cs143/data/subfull.parquet")


    df_full = df_com_full.join(df_sub_full, df_com_full.link_id == df_sub_full.sub_id, 'inner')
    df_full = df_full.select(col('id'), col('link_id'), col('created_utc'), col('body'), col('author_flair_text'), col('title'))
    # df_full.show()
    # df_full.write.parquet("/home/cs143/data/full.parquet")
    # df_full.show()

    # Task 9
    df_full = df_full.where("body not like '&gt%'")
    df_full = df_full.where("body not like '%/s%'")
    # df_full.show()


    df_full_sanitize = df_full.select("id", sanitize_udf(col("body")).alias("comments"),col('link_id'), col('created_utc'),col('author_flair_text'), col('title'))
    # df_full_sanitize.show()


    df_cv_full = model.transform(df_full_sanitize)
    # df_cv_full.show()

    posModel = CrossValidatorModel.load("www/pos.model")
    negModel = CrossValidatorModel.load("www/neg.model")
    posResult = posModel.transform(df_cv_full)
    negResult = negModel.transform(df_cv_full)

    # posResult.show()
    # negResult.show()
    # posResult.write.parquet("/home/cs143/data/posResult.parquet")
    # negResult.write.parquet("/home/cs143/data/negResult.parquet")
    # posResult = sqlContext.read.parquet("/home/cs143/data/posResult.parquet")
    # negResult = sqlContext.read.parquet("/home/cs143/data/negResult.parquet")

  
    posthreshold_udf = udf(set_pos_threshold,IntegerType())
    negthreshold_udf = udf(set_neg_threshold,IntegerType())


    posResult = posResult.select("id",posthreshold_udf(col('probability')).alias("probability"),col('link_id'),col('created_utc'),col('author_flair_text'), col('title'))
    negResult = negResult.select("id",negthreshold_udf(col('probability')).alias("probability"), col('link_id'), col('created_utc'),col('author_flair_text'), col('title'))

    # Task 10
    num_rows = posResult.count()
    num_pos =  posResult.filter(posResult.probability == 1).count()
    num_neg =  negResult.filter(negResult.probability == 1).count()
    print('percentage of positive %f'%(num_pos / num_rows))
    print('Percentage of negative %f'%(num_neg / num_rows))

    sub_pos_pct = posResult.groupBy('link_id','title').agg((sum('probability') / count('probability')).alias('pos_pct'))
    sub_neg_pct = negResult.groupBy('link_id','title').agg((sum('probability') / count('probability')).alias('neg_pct'))

    time_pos_pct = posResult.groupBy('created_utc').agg((sum('probability') / count('probability')).alias('pos_pct'))
    time_neg_pct = negResult.groupBy('created_utc').agg((sum('probability') / count('probability')).alias('neg_pct'))

    time_pos_pct = time_pos_pct.select(from_unixtime(col('created_utc')).alias('time'),'pos_pct').show()
    time_neg_pct = time_neg_pct.select(from_unixtime(col('created_utc')).alias('time'),'neg_pct').show()






def idtype(id):
    return id[3:]
def set_pos_threshold(p):
    if p[1]>0.2:
        return 1
    else:
        return 0

def set_neg_threshold(p):
    if p[1]>0.25:
        return 1
    else:
        return 0






if __name__ == "__main__":
    conf = SparkConf().setAppName("CS143 Project 2B")
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    sc.addPyFile("cleantext.py")
    main(sqlContext)
