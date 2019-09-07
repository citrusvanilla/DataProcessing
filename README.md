# Data Processing
Python3 scripts for processing raw data.

## How to use these files
The entrypoint for the processing is in the data_processing.py file.  This file must be in the 'DataProcessing' directory of the AWS lambda Python 3 environment, viewable using the AWS Lambda console.  The individual data processing files (i.e. 'modes/overview.py', 'modes/resolvers.py', ...) must be in the 'modes' directory, on the same level as the 'data_processing.py' file.

Updates to these files can simply be copied and pasted into the Python 3 environment in the AWS console.  For larger changes, follow the guidelines in the console for zipping and uploading to AWS Lambda.
