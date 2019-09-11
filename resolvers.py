"""
Module for processing data for the Resolvers mode of Goblin Monitor.
"""

#######################################################################

def get_invocationcounts(data: dict) -> dict:
  """
  Processes resolver invocation counts for the invocation counts
  component of the Resolvers mode.

  Args:
    data: input data as a dictionary/object
  
  Returns:
    p_dic: processed data as a dictionary/object
  """

  # Init a dictionary to hold output data.
  p_dic: dict = {}

  # Iterate through the custom type arrays.
  for custom_type in data:
    # Pass over Query.
    if custom_type == "Query": continue
    # Iterate over the custom type resolvers.
    for resolver in data[custom_type]:
      # Stick the custom type + resolver in the output dict with count.
      p_dic[custom_type + ":" + resolver] = \
        len(data[custom_type][resolver])

  # Return the processed data.
  return p_dic


def get_aveexecutiontimes(data: dict) -> dict:
  """
  Processes average execution times for resolvers.

  Args:
    data: input data as a dictionary/object
  
  Returns:
    p_dic: processed data as a dictionary/object
  """

  # Init an object to hold processed data.
  p_dic: dict = {}

  # Iterate through custom types.
  for custom_type in data:
    # If custom type is 'query', continue.
    if custom_type == "Query": continue

    # Iterate through resolvers.
    for resolver in data[custom_type]:
      # Stick average execution time in the p_dic.
      p_dic[custom_type+":"+resolver] = (
        sum([req['speed'] for req in data[custom_type][resolver]]) /
        len(data[custom_type][resolver])
      )
  
  # Return processed data object.
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
    "invocationCounts": get_invocationcounts(data),
    "executionTimes": get_aveexecutiontimes(data),
  }

  # Stick some averages data on p_dic.
  total_count = sum([p_dic['invocationCounts'][x]
                     for x in p_dic['invocationCounts']])
  sum_ave = \
    sum([p_dic['executionTimes'][x] * p_dic['invocationCounts'][x]
         for x in p_dic['invocationCounts']])
  p_dic['averageTime'] = sum_ave / total_count if total_count > 0 else 0.0

  # Return the processed data.
  return p_dic

