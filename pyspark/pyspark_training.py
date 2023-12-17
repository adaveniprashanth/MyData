from pyspark.sql import SparkSession


# Stop the existing SparkContext if it exists
if 'spark' in locals() and spark is not None:
    spark.stop()
if 0:
    spark = SparkSession.builder.appName("Datacamp Pyspark Tutorial").config("spark.memory.offHeap.enabled","true").config("spark.memory.offHeap.size","10g").getOrCreate()
    df = spark.read.csv('datacamp_ecommerce.csv',header=True,escape="\"")
    print(df.show(5,0))

    df.count()

# not working
if 0:
    from pyspark.sql import SparkSession

    # spark = SparkSession.builder.appName("PythonVersionCheck").getOrCreate()

    # python_version = spark._jconf.get("spark.pyspark.python")
    # print(f"Using Python version: {python_version}")
if 0:
    from pyspark import SparkContext
    from pyspark.sql import SparkSession
    # for  pyspark install reference --> https://www.youtube.com/watch?v=6Cn_Gb0RMG8
    # for reference --> https://www.datacamp.com/tutorial/pyspark-tutorial-getting-started-with-pyspark

    # Create a new SparkContext
    spark = SparkSession.builder.appName("YourAppName").getOrCreate()

if 0:
    # import pyspark
    from pyspark import SparkContext

    sc = SparkContext()
    nums = sc.parallelize([1, 2, 3, 4])
    print(nums.take(5))