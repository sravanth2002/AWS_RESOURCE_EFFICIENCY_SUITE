# AWS_RESOURCE_EFFICIENCY_SUITE

## Overview
**AWS_RESOURCE_EFFICIENCY_SUITE** is a suite of tools designed to optimize AWS resources, particularly focusing on EC2 and EBS. This application aims to analyze resource usage, suggest optimizations, and automate certain efficiency improvements.

## Features
- **EC2 Optimizations**: Analyze and optimize EC2 instances based on utilization.
- **EBS Efficiency**: Manage and optimize EBS volumes.
- **Lambda Automation**: Uses AWS Lambda functions for automation tasks, ensuring efficient resource management.

## File Structure
- **`constants.py`**: Defines configuration constants used across the suite.
- **`ebs.py`**: Handles EBS volume management and optimization.
- **`ec2_optimizer.py`**: Contains logic to analyze and optimize EC2 instances.
- **`lambda_function.py`**: AWS Lambda function definitions for handling automation processes.
- **`main.py`**: Main script to execute the suite and manage AWS resource optimization.
- **`run.sh`**: Shell script for initializing and executing the suite.

## Prerequisites
- **Python 3.9**: Ensure Python 3.9 and above is installed.
- **AWS SDK (boto3)**: Install the AWS SDK using:
  ```bash
  pip install boto3
  ```
- **AWS IAM Permissions:** Required permissions to access EC2, EBS, and Lambda resources.

## Setup and Installation
1. Clone the repository
    ``` bash
    git clone https://code.experian.local/scm/expngblhackfy25q3/aws-resource-efficiency-suite.git
    ```
    ``` bash
    cd aws-resource-efficiency-suite
    ```
2. Install dependencies:
    ``` bash
    pip install -r requirements.txt
    ```
3. Configure AWS credentials using `aws configure` or set them using `gimme-aws-creds`.

## Usage
- To run the suite, execute the main script:
    ``` bash
    sh run.sh
    ```
- Provide your inputs in the tkinter

## Configuration
- Customize any necessary parameters in `constants.py` to using the tkinter UI.


