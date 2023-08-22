# AWS S3 mountpoint with Apache Spark

This proof of concept (POC) demonstrates a powerful integration between Terraform, Docker, and AWS S3. It automates the creation of a private and encrypted S3 bucket, the generation of random CSV files, and processing those files using Apache Spark within a Docker container.

The solution leverages the new AWS S3 mountpoint functionality, allowing for efficient handling of vast amounts of data without the need for transferring it.

## File Structure
```
├── README.md
├── docker
│   ├── build.sh
│   ├── data_generator
│   │   ├── Dockerfile
│   │   ├── data_generator.py
│   │   └── entrypoint.sh
│   └── spark_ingestion
│       ├── Dockerfile
│       ├── entrypoint.sh
│       └── spark_ingestion.py
├── images
└── terraform
    ├── backend.tf
    ├── outputs.tf
    ├── plan.out
    ├── s3.tf
    ├── variables.tf
    └── versions.tf
```

## Prerequisites
- Terraform
- Docker
- AWS Account
- AWS CLI

## Instructions

### Step 1: Terraform Setup
Navigate to the terraform directory and initialize Terraform.
```bash
cd terraform

terraform init
terraform plan -out=plan.out
terraform apply plan.out
```
After applying the plan, you will receive the bucket name as output. Make sure to update the bucket name in both Dockerfiles.

![terraform_apply.png](images%2Fterraform_apply.png)

### Step 2: Docker Configuration
Update the `ENV AWS_PROFILE` in both Dockerfiles. This sets the profile from the mounted AWS credentials file to be used automatically when running AWS CLI commands.

### Step 3: Docker Build & Run
Navigate to the docker directory and run the `build.sh` script. This script builds the Docker images, runs them in detached mode, and then tails the logs from the Spark Docker image.
```bash
cd ../docker

./build.sh
```

![docker_build.png](images%2Fdocker_build.png)

This takes about 5 minutes and goes directly into  tailing the spark container's logs.

### Step 4: Validation
Monitor the logs and verify the creation of random CSV files every 5 seconds in the S3 bucket, along with the processing done by Apache Spark.

![logs.gif](images%2Flogs.gif)

## Features
- **Terraform Automation:** Automates the provisioning of an S3 bucket.
- **Data Generation:** A Docker container that creates random CSV files and uploads them to the S3 bucket.
- **Data Processing:** Another Docker container equipped with Apache Spark, processing the CSV files from the S3 bucket.
- **AWS S3 Integration:** Utilizes AWS S3 mountpoint for efficient data handling.

This POC demonstrates a scalable and efficient solution for managing and processing large datasets using the synergy of Terraform, Docker, Apache Spark, and AWS S3. It can be a significant stepping stone for more extensive data processing applications.
