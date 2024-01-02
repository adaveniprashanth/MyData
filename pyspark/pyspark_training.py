from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *

# for  pyspark install reference --> https://www.youtube.com/watch?v=6Cn_Gb0RMG8
# for reference --> https://www.datacamp.com/tutorial/pyspark-tutorial-getting-started-with-pyspark

if 0:
    # Stop the existing SparkContext if it exists
    if 'spark' in locals() and spark is not None:
        spark.stop()


if 0:
    # import pyspark
    sc = SparkContext()
    nums = sc.parallelize([1, 2, 3, 4])
    print(nums.take(5))


if 0:
    if 'spark' not in locals() :
        spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","10g").getOrCreate()
    df = spark.read.csv('datacamp_ecommerce.csv',header=True,escape="\"")
    df.show(5,0)
    print(df.count())

# create dataframe manually
if 0:
    # Method 1  --> using list of tuples
    df = spark.createDataFrame(data=[(1, 1), (2, 2), (3, 3), (4, 4)], schema=['id', 'data'])
    # df.show()

    # Method 2 --> using list of dictionaries
    data = [{'id': 1, 'name': 'a'}, {'id': 2, 'name': 'b'}]
    df1 = spark.createDataFrame(data=data)
    df1.show()

    # Method 3 -- by proving the schema for the dtaframe
    # provinding the schema details for dataframe i.e like creating the table
    schema = StructType([StructField(name="id", dataType=IntegerType()),
                         StructField(name="data", dataType=StringType())])

    data = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]  # inserting data in table
    # df2=spark.createDataFrame(data=data,schema=schema) #creating the dataframe
    # df2.show()
    # df2.printSchema()