#!/bin/bash

# Build the data_generator Docker image
docker build -t data_generator ./data_generator

# Build the spark_ingestion Docker image
docker build -t spark_ingestion ./spark_ingestion

# Run the data_generator container with the specified flags
docker run -d --name data_generator --device /dev/fuse --cap-add SYS_ADMIN -v ~/.aws/credentials:/root/.aws/credentials data_generator

# Run the spark_ingestion container with the specified flags
docker run -d --name spark_ingestion --device /dev/fuse --cap-add SYS_ADMIN -v ~/.aws/credentials:/root/.aws/credentials spark_ingestion

# Show the logs of the spark_ingestion container
docker logs -f spark_ingestion
