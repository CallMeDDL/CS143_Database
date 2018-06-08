from __future__ import print_function
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import udf, col,from_unixtime, sum, count 
from pyspark.sql.types import LongType, StringType, ArrayType,IntegerType,DateType,FloatType
from pyspark.ml.feature import CountVectorizer


# IMPORT OTHER MODULES HERE
from cleantext import sanitize
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder,CrossValidatorModel
from pyspark.ml.evaluation import BinaryClassificationEvaluator


states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',\
          'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', \
          'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', \
          'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', \
          'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',\
          'Pennsylvania', 'Rhode Island', 'South Carolina','South Dakota', 'Tennessee', 'Texas', 'Utah', \
          'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']




def idtype(id):
    return id[3:]




def set_pos_threshold(p):
    if p[1] > 0.2:
        return 1
    else:
        return 0




def set_neg_threshold(p):
    if p[1] > 0.25:
        return 1
    else:
        return 0




def get_prob(p):
    return float(p[1])




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
    posModel.save("./model/pos.model")
    negModel.save("./model/neg.model")




def main(context):

    # ======================== Task 1 & 2 =========================
    # generate and save data
    # df_com = sqlContext.read.json("./data/comments-minimal.json.bz2")
    # df_sub = sqlContext.read.json("./data/submissions.json.bz2")
    # df_lab = sqlContext.read.csv("./data/labeled_data.csv", header=True, inferSchema=True)
    # df_lab.createOrReplaceTempView('view_lab')
    # df_com = df_com.where('id IN (SELECT Input_id FROM view_lab)')
    # df_com.write.parquet("./data/comments_minimal.parquet")
    # df_sub.write.parquet("./data/submissions.parquet")
    # df_lab.write.parquet("./data/labeled_data.parquet")
    

    # load data
    # TODO: should be uncommented
    df_com = sqlContext.read.parquet("./data/comments_minimal.parquet")
    df_sub = sqlContext.read.parquet("./data/submissions.parquet")
    df_lab = sqlContext.read.parquet("./data/labeled_data.parquet")




    # ========================= Task 4 & 5 ========================
    # TODO: should be uncommented
    sanitize_udf = udf(sanitize, ArrayType(StringType()))


    # generate and save data
    # df_sanitize = df_com.select("id", sanitize_udf(col("body")).alias("comments"))
    # df_sanitize.write.parquet("./data/sanitize.parquet")


    # load data
    # TODO: should be uncommented
    df_sanitize = sqlContext.read.parquet("./data/sanitize.parquet")




    # ========================== Task 6A ==========================
    # TODO: should be uncommented
    cv = CountVectorizer(inputCol="comments", outputCol="features", binary=True, minDF=5.0)
    model = cv.fit(df_sanitize)


    # generate and save data
    # df_cv = model.transform(df_sanitize)
    # df_cv.write.parquet("./data/CountVectorizer.parquet")


    # load data
    # df_cv = sqlContext.read.parquet("./data/CountVectorizer.parquet")




    #  ===================== Task 6B & Task 7 =====================
    # generate and save data
    # df_cv.createOrReplaceTempView('view_cv')
    # df_poslabel = sqlContext.sql('SELECT Input_id, IF(labeldjt = 1, 1, 0) AS label FROM view_lab')
    # df_poslabel.createOrReplaceTempView('view_poslab')
    # df_pos = sqlContext.sql('SELECT id, features, view_poslab.label AS label FROM view_cv INNER JOIN view_poslab ON view_poslab.Input_id = view_cv.id')

    # df_neglabel = sqlContext.sql('SELECT Input_id, IF(labeldjt = -1, 1, 0) AS label FROM view_lab')
    # df_neglabel.createOrReplaceTempView('view_neglab')
    # df_neg = sqlContext.sql('SELECT id, features, view_neglab.label AS label FROM view_cv INNER JOIN view_neglab ON view_neglab.Input_id = view_cv.id')

    # df_pos.write.parquet("./data/pos.parquet")
    # df_neg.write.parquet("./data/neg.parquet")


    # load data
    # df_pos = sqlContext.read.parquet("./data/pos.parquet")
    # df_neg = sqlContext.read.parquet("./data/neg.parquet")




    # ========================== Task 7 ===========================
    # train_process(df_pos, df_neg)




    # ========================== Task 8 ===========================
    # TODO: should be uncommented
    idtype_udf = udf(idtype, StringType())


    # generate and save df_com_full
    # TODO: should be uncommented
    df_com_full = df_com.select("id",idtype_udf(col("link_id")).alias("link_id"),"body","created_utc","author_flair_text",col('score').alias('com_score'))
    
    # df_com_full.write.parquet("./data/comfull.parquet")

    # load df_com_full
    # df_com_full = sqlContext.read.parquet("./data/comfull.parquet").sample(False, 0.01, None)


    # generate and save df_sub_full
    # TODO: should be uncommented
    df_sub_full = df_sub.select(col("id").alias("sub_id"), "title",col('score').alias('sub_score'))

    # df_sub_full.write.parquet("./data/subfull.parquet")

    # load df_sub_full
    # df_sub_full = sqlContext.read.parquet("./data/subfull.parquet").sample(False, 0.01, None)


    # generate and save df_full
    # TODO: should be uncommented
    df_full = df_com_full.join(df_sub_full, df_com_full.link_id == df_sub_full.sub_id, 'inner')
    df_full = df_full.select(col('id'), col('link_id'), col('created_utc'), col('body'), col('author_flair_text'), col('title'),col('com_score'),col('sub_score'))
    
    # df_full.write.parquet("./data/full.parquet")

    # load df_full
    # df_full = sqlContext.read.parquet("./data/full.parquet").sample(False, 0.01, None)




    # ========================== Task 9 ===========================
    # TODO: should be uncommented
    df_full = df_full.where("body not like '&gt%'")
    df_full = df_full.where("body not like '%/s%'")
    df_full_sanitize = df_full.select("id", sanitize_udf(col("body")).alias("comments"),col('link_id'), col('created_utc'),col('author_flair_text'), col('title'),col('com_score'),col('sub_score'))
    df_cv_full = model.transform(df_full_sanitize)
    posModel = CrossValidatorModel.load("./model/pos.model")
    negModel = CrossValidatorModel.load("./model/neg.model")
    posthreshold_udf = udf(set_pos_threshold, IntegerType())
    negthreshold_udf = udf(set_neg_threshold, IntegerType())


    # generate and save posResult & negResult
    # TODO: should be uncommented
    posResult = posModel.transform(df_cv_full)
    negResult = negModel.transform(df_cv_full)

    get_prob_udf = udf(get_prob, FloatType())
    posResult_ROC = posResult.select(col("id"), get_prob_udf(col('probability')).alias("probability"))
    negResult_ROC = negResult.select(col("id"), get_prob_udf(col('probability')).alias("probability"))

    posResult_ROC = posResult_ROC.join(df_lab, posResult_ROC.id == df_lab.Input_id, 'inner')
    negResult_ROC = negResult_ROC.join(df_lab, negResult_ROC.id == df_lab.Input_id, 'inner')

    posResult_ROC = posResult_ROC.select(col("id"), col('probability'), col('labeldjt').alias('label'))
    negResult_ROC = negResult_ROC.select(col("id"), col('probability'), col('labeldjt').alias('label'))

    posResult_ROC.show()
    negResult_ROC.show()
    posResult_ROC.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/posResult_ROC.csv")
    negResult_ROC.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/negResult_ROC.csv")


    posResult = posResult.select("id",posthreshold_udf(col('probability')).alias("probability"), col('link_id'),col('created_utc'),col('author_flair_text'), col('title'),col('com_score'),col('sub_score'))
    negResult = negResult.select("id",negthreshold_udf(col('probability')).alias("probability"), col('link_id'), col('created_utc'),col('author_flair_text'), col('title'),col('com_score'),col('sub_score'))
    posResult.write.parquet("./data/posResult.parquet")
    negResult.write.parquet("./data/negResult.parquet")


    # load posResult & negResult
    # posResult = sqlContext.read.parquet("./data/posResult.parquet")
    # negResult = sqlContext.read.parquet("./data/negResult.parquet")
    # posResult.show()
    # negResult.show()




    # ========================== Task 10 ==========================
    # 1 across submission
    sub_pos_pct = posResult.groupBy('title').agg((sum('probability') / count('probability')).alias('pos_pct')).orderBy('title')
    sub_neg_pct = negResult.groupBy('title').agg((sum('probability') / count('probability')).alias('neg_pct')).orderBy('title')

    sub_pos_pct.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/sub_pos_pct.csv")
    sub_neg_pct.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/sub_neg_pct.csv")


    # 2 across time
    time_pos_pct = posResult.groupBy(from_unixtime(col('created_utc')).cast(DateType()).alias('time_pos')).agg((sum('probability') / count('probability')).alias('pos_pct')).orderBy('time_pos')
    time_neg_pct = negResult.groupBy(from_unixtime(col('created_utc')).cast(DateType()).alias('time_neg')).agg((sum('probability') / count('probability')).alias('neg_pct')).orderBy('time_neg')
    time_data = time_pos_pct.join(time_neg_pct, time_pos_pct.time_pos == time_neg_pct.time_neg, 'inner')
    time_data = time_data.select(col('time_pos').alias('date'), col('pos_pct').alias('Positive'), col('neg_pct').alias('Negative'))
    time_data.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/time_data.csv")


    #3 across state
    state_pos_pct = posResult.groupBy('author_flair_text').agg((sum('probability') / count('probability')).alias('pos_pct'))
    state_neg_pct = negResult.groupBy('author_flair_text').agg((sum('probability') / count('probability')).alias('neg_pct'))

    df_state = sqlContext.createDataFrame(states, StringType())

    state_pos_pct = state_pos_pct.join(df_state, state_pos_pct.author_flair_text == df_state.value, 'inner')
    state_pos_pct = state_pos_pct.select(col('author_flair_text').alias('state_pos'), col('pos_pct')).orderBy('state_pos')

    state_neg_pct = state_neg_pct.join(df_state, state_neg_pct.author_flair_text == df_state.value, 'inner')
    state_neg_pct = state_neg_pct.select(col('author_flair_text').alias('state_neg'), col('neg_pct')).orderBy('state_neg')

    state_data = state_pos_pct.join(state_neg_pct, state_pos_pct.state_pos == state_neg_pct.state_neg, 'inner')
    state_data = state_data.select(col('state_pos').alias('state'), col('pos_pct').alias('Positive'), col('neg_pct').alias('Negative'))
    state_data.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/state_data.csv")


    # 4 comment score and submission score
    com_score_pos_pct = posResult.groupBy('com_score').agg((sum('probability') / count('probability')).alias('pos_pct')).orderBy('com_score')
    com_score_neg_pct = negResult.groupBy('com_score').agg((sum('probability') / count('probability')).alias('neg_pct')).orderBy('com_score')
    sub_score_pos_pct = posResult.groupBy('sub_score').agg((sum('probability') / count('probability')).alias('pos_pct')).orderBy('sub_score')
    sub_score_neg_pct = negResult.groupBy('sub_score').agg((sum('probability') / count('probability')).alias('neg_pct')).orderBy('sub_score')

    com_score_pos_pct.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/com_score_pos_pct.csv")
    com_score_neg_pct.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/com_score_neg_pct.csv")
    sub_score_pos_pct.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/sub_score_pos_pct.csv")
    sub_score_neg_pct.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/sub_score_neg_pct.csv")


    # 5 top 10 stories
    top10_sub_pos = posResult.groupBy('title').agg((sum('probability') / count('probability')).alias('pos_pct')).orderBy('title')
    top10_sub_pos = top10_sub_pos.select(col('title').alias('title_pos'), col('pos_pct'))
    top10_sub_pos = top10_sub_pos.join(posResult, top10_sub_pos.title_pos == posResult.title, 'inner')
    top10_sub_pos = top10_sub_pos.select(col('id'), col('title'), col('pos_pct').alias('Positive')).orderBy('pos_pct', ascending=False)
    top10_sub_pos.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/top10_sub_pos.csv")

    top10_sub_neg = negResult.groupBy('title').agg((sum('probability') / count('probability')).alias('neg_pct')).orderBy('title')
    top10_sub_neg = top10_sub_neg.select(col('title').alias('title_neg'), col('neg_pct'))
    top10_sub_neg = top10_sub_neg.join(negResult, top10_sub_neg.title_neg == negResult.title, 'inner')
    top10_sub_neg = top10_sub_neg.select(col('id'), col('title'), col('neg_pct').alias('Negative')).orderBy('neg_pct', ascending=False)
    top10_sub_neg.coalesce(1).write.mode("overwrite").format("com.databricks.spark.csv").option("header", "true").csv("./output/top10_sub_neg.csv")




if __name__ == "__main__":
    conf = SparkConf().setAppName("CS143 Project 2B")
    conf = conf.setMaster("local[*]")
    sc   = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")
    sqlContext = SQLContext(sc)
    sc.addPyFile("cleantext.py")
    main(sqlContext)
