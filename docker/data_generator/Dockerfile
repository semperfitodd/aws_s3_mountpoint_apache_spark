# Start from a base Ubuntu image
FROM ubuntu:latest

# Set environment variables
ENV AWS_PROFILE=<AWS_PROFILE>
ENV DEBEZIUM_VERSION=noninteractive

# Set the S3 bucket name from the terraform output
ENV S3_BUCKET=<BUCKET_NAME>
ENV MOUNT_PATH=/mount_s3

RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    apt-get update && \
    apt-get install -y awscli wget python3 fuse libfuse2 && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    wget https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.deb && \
    dpkg -i mount-s3.deb && \
    apt clean && \
    mkdir $MOUNT_PATH && \
    rm -rf /var/lib/apt/lists/* /mount-s3.deb

COPY data_generator.py /data_generator.py

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
