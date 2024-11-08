#!/bin/bash

# Run main.py and wait for it to finish
python3 main.py

# After main.py completes, proceed with zipping the specific files
# Define the folder containing the files
FOLDER="."

# Create the zip file including only the specific files
zip -r archive_name.zip "lambda_function.py" "ec2_optimizer.py" "ebs.py" "constants.py"