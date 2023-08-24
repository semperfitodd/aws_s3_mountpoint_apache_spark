# Start from a base Ubuntu image
FROM ubuntu:latest

# Set environment variables
ENV AWS_PROFILE=<AWS_PROFILE>
ENV DEBEZIUM_VERSION=noninteractive
ENV SPARK_VERSION=3.4.1

# Set the S3 bucket name from the terraform output
ENV S3_BUCKET=<BUCKET_NAME>
ENV MOUNT_PATH=/mount_s3

# Install system dependencies
RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    apt-get update && \
    apt-get install -y tzdata wget fuse libfuse2 awscli openjdk-8-jdk python3 python3-pip && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    wget https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.deb && \
    dpkg -i mount-s3.deb && \
    apt clean && \
    mkdir $MOUNT_PATH && \
    rm -rf /var/lib/apt/lists/* /mount-s3.deb && \
    pip3 install pyspark

# Install Spark
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
    tar -xzf spark-${SPARK_VERSION}-bin-hadoop3.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop3 /opt/spark && \
    rm spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Add the file "files/data_generator.py" to the container
COPY spark_ingestion.py /spark_ingestion.py

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Set permissions for entrypoint script
RUN chmod +x /entrypoint.sh

# Set the entrypoint script to run when the container starts
ENTRYPOINT ["/entrypoint.sh"]
