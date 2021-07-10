from pyspark.sql import SparkSession

from minsait.ttaa.datio.engine.Transformer import Transformer

if __name__ == '__main__':
    spark: SparkSession = SparkSession \
        .builder \
        .master(SPARK_) \
        .getOrCreate()
    transformer = Transformer(spark)
