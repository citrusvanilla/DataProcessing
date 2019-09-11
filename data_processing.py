import boto3
from boto3.dynamodb.types import TypeDeserializer

from overview import *
from resolvers import *


def deserialize(data):
  """
  Helper function to parse the DynamoDB serialization.
  
  Args:
    data: DynamoDB unmarshalled data.
  
  Returns:
    {}: unmarshalled python dict
  """
  serializer = TypeDeserializer()

  # Check for list type.
  if isinstance(data, list):
    return [deserialize(v) for v in data]

  # Check for object type.
  if isinstance(data, dict):
    try: 
      return serializer.deserialize(data)
    except TypeError:
      return { k : deserialize(v) for k, v in data.items() }
  else:
    return data


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

  # To go from low-level format to python
  boto3.resource('dynamodb')
  deserializer = boto3.dynamodb.types.TypeDeserializer()

  print(event)
  # getItem api call, pass in params
  response = client.get_item(
    TableName = "GraphQLData",
    Key = {
      'AccessID': {
          'S': event['AccessID']
      }
    }
  )

  # Extract data from the response.
  data = deserialize(response['Item']['Data'])

  # Process data.
  processedData: dict = {
    'overview': get_overview_data(data),
    'resolvers': get_resolvers_data(data)
  }
  
  # Return
  return processedData

