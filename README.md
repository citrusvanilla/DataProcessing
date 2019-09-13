# Data Processing
Python3 scripts for processing raw data.

## How to use these files
The entrypoint for the processing is in the data_processing.py file.  This file must be in the 'DataProcessing' directory of the AWS lambda Python 3 environment, viewable using the AWS Lambda console.  The individual data processing files (i.e. 'overview.py', 'resolvers.py', ...) must be in the same directory, on the same level as the 'data_processing.py' file.

![file org in AWS lambda console](https://i.imgur.com/GAG0cHI.png)

Updates to these files can simply be copied and pasted into the Python 3 environment in the AWS console.  For larger changes, follow the guidelines in the console for zipping and uploading to AWS Lambda.

## Testing
The data processing routine is unit tested using the built-in 'unittest' module.  To test sample data sets, replace 'test_data.json' and enter the command 'python3 tests.py -v' in the command line.
