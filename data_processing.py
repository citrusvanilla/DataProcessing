import boto3

from modes import overview
from modes import resolvers


def lambda_handler(event: dict, context: dict) -> dict:
    """
    Main handler for the DataProcessing lambda.

      Makes connection to dynamoDB.
      Passes API key as event to dynamo and returns raw data.
      Processes raw data and returns to calling context.

    Args:
      event:         dict containing API key.
      context:       dict containing calling context info.
    
    Returns:
      processedData: dict containing processed data
    """
    # Make a connection to dynamodb service with boto3.
    client = boto3.client('dynamodb')

    # getItem api call, pass in params
    response = client.get_item(
        TableName = "UserData",
        Key = {
            'UserID': {
                'S': event['UserID']
            }
        }
    )

    # Extract data from the response.
    data = response

    # Process data.
    processedData: dict = {
      'overview': overview.get_overview_data(data),
      'resolvers': resolvers.get_resolvers_data(data)
    }
    
    # Return
    return processedData

