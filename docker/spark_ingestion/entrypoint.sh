#!/bin/bash

# Automatically mount the S3 bucket
mount-s3 $S3_BUCKET $MOUNT_PATH

# Run the data_generator.py script
exec python3 /spark_ingestion.py
