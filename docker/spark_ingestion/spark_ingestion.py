import os
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType
from pyspark.sql.functions import window, avg

# Get the mount path from the environment variable
mount_path = os.getenv('MOUNT_PATH', '/mount_s3')

spark = SparkSession.builder \
    .appName("Real-Time Analytics") \
    .getOrCreate()

# Define the schema of the dataset
schema = StructType() \
    .add("timestamp", StringType()) \
    .add("value", IntegerType())

# Read the CSV files as a streaming dataframe
streamingDF = spark \
    .readStream \
    .option("sep", ",") \
    .option("header", "true") \
    .schema(schema) \
    .csv(mount_path) # Use the MOUNT_PATH environment variable

# Debug code to print a sample of the data
streamingDF.writeStream.outputMode("append").format("console").start().awaitTermination()

# Aggregate data to calculate average value in a window of time
windowedAggregates = streamingDF \
    .groupBy(
        window(streamingDF.timestamp, "10 seconds"),
        streamingDF.value) \
    .agg(avg("value").alias("average_value"))

# Start the query to print the results on the console
query = windowedAggregates \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
