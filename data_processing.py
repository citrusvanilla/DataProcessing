import typing
import json
from modes import overview
from modes import resolvers


with open("data.json", "r") as read_file:
  data = json.load(read_file)

def get_overview_data(data: dict) -> dict:
  """
  Process data for overview component.

  Args:
    data: input data as a dictionary.

  Returns:
    p_dic: processed data as a dictionary.
  """
  # Init processed data dictionary.
  p_dic: dict = {
    'summary': overview.get_summary(data),
    'requests': overview.get_requests(data),
    'response': overview.get_responses(data),
    'resolvers': overview.get_resolvers(data)
  }

  # Return processed data.
  return p_dic


def get_resolvers_data(data: dict) -> dict:
  """
  Processes data for resolvers mode.

  Args:
    data: a dictionary of data for processing.

  Returns:
    p_dic: a dictionary of component-level data.
  """

  # Init processed data dictionary.
  p_dic: dict = {
    "invocationCounts": resolvers.get_invocationcounts(data),
    "executionTimes": resolvers.get_aveexecutiontimes(data),
  }

  # Stick some averages data on p_dic.
  total_count = sum([p_dic['invocationCounts'][x]
                     for x in p_dic['invocationCounts']])
  sum_ave = \
    sum([p_dic['executionTimes'][x] * p_dic['invocationCounts'][x]
         for x in p_dic['invocationCounts']])
  p_dic['averageTime'] = sum_ave / total_count

  # Return the processed data.
  return p_dic


# Process the data.

def main(data: dict) -> None:

  processedData: dict = {
    'overview': get_overview_data(data),
    'resolvers': get_resolvers_data(data)
  }

  file_object = open('processed_data.json', 'w')

  # Save dict data into the JSON file.
  json.dump(processedData, file_object)

  return



#print(processedData)

if __name__ == "__main__":
  main(data)
