"""
Module for processing data for the Overview mode of Goblin Monitor.
"""

import math

#######################################################################

def get_summary(data: dict) -> dict:
  """
  Gets data for the Summary component of the Overview mode.

  Args:
    data: a dictionary of input data
  
  Returns:
    p_dic: a dictionary of output data
  """
  # Init a dictionary to hold output.
  p_dic: dict = {
    'numTotalRequests': 0
  }

  # Iterate through the API entrypoints.
  for entrypoint in data['Query']:
    # Increment total requests by length of entrypoint array.
    p_dic['numTotalRequests'] += len(data['Query'][entrypoint])

  # Return the output dictionary.
  return p_dic


def get_requests(data: dict) -> dict:
  """
  Gets data for the Requests component of the Overview mode.

  Args:
    data: a dictionary of input data
  
  Returns:
    p_dic: a dictionary of output data
  """
  # Init a dicionary to hold output.
  p_dic: dict = {}

  # Init a temp buffer dictionary for processing.
  t_buf: dict = {}

  for entrypoint in data['Query']:
    for req in data['Query'][entrypoint]:
      bin: int = int(math.floor(req['time']/1000)*1000)
      t_buf[bin] = t_buf[bin] + 1 if bin in t_buf else 1
  
  sorted_bins: list = sorted([[i, t_buf[i]] for i in t_buf], 
                             key=lambda x: x[0]) 
  
  p_dic['times'] = [i[0] for i in sorted_bins]
  p_dic['rpm'] = [i[1] for i in sorted_bins]

  return p_dic


def get_responses(data: dict) -> dict:
  """
  Processes data for the Responses component of the Overview mode.

  Args:
    data: input data as a dictionary
  
  Returns:
    p_dic: processed data as a dictionary
  """

  # Init output dict.
  p_dic: dict = {
    'ave': 0.0,
    'count': 0
  }

  # Init a temp buffer.
  t_buf: dict = {
    'counts': {},
    'speed': {}
  }

  # Iterate through API entrypoints.
  for entrypoint in data['Query']:
    for req in data['Query'][entrypoint]:
      bin: int = int(math.floor(req['time']/1000)*1000)
      t_buf['counts'][bin] = t_buf['counts'][bin] + 1 \
                             if bin in t_buf['counts'] else 1
      t_buf['speed'][bin] = (
        ((t_buf['counts'][bin]-1) * (t_buf['speed'][bin]) + req['speed']) /
        t_buf['counts'][bin]
        if bin in t_buf['speed'] else req['speed']
      )

      p_dic['count'] = p_dic['count'] + 1
      p_dic['ave'] = (p_dic['ave'] * (p_dic['count']-1) + req['speed']) \
                      / p_dic['count']

  # Sort the tmp buffer by times.
  sorted_bins: list = sorted([[i, t_buf['speed'][i]] for i in t_buf['speed']], 
                             key=lambda x: x[0]) 
  
  p_dic['times'] = [i[0] for i in sorted_bins]
  p_dic['90'] = [i[1] for i in sorted_bins]

  return p_dic


def get_resolvers(data: dict) -> dict:
  """
  Processes data for the Resolvers component of the Overview mode.

  Args:
    data: input data as a dictionary
  
  Returns:
    p_dic: processed data as a dictionary
  """

  # Init processed data dict.
  p_dic: dict = {}

  # Init a temp buffer dic.
  t_buf: dict = {
    'counts': {},
    'speed': {}
  }

  # Iterate through top-level keys in input data.
  for custom_type in data:
    # Skip the 'query' key.
    if custom_type == 'Query': continue
    # Iterate through custom type resolvers.
    for resolver in data[custom_type]:
      for req in data[custom_type][resolver]:
        bin: int = int(math.floor(req['time']/1000)*1000)
        t_buf['counts'][bin] = t_buf['counts'][bin] + 1 \
                               if bin in t_buf['counts'] else 1
        t_buf['speed'][bin] = (
          ((t_buf['counts'][bin]-1) * (t_buf['speed'][bin]) + req['speed']) /
          t_buf['counts'][bin]
          if bin in t_buf['speed'] else req['speed']
        )

  # Sort the tmp buffer by times.
  sorted_bins: list = sorted([[i, t_buf['speed'][i]] for i in t_buf['speed']], 
                             key=lambda x: x[0]) 
  
  # Write to times and aveSpeeds for those times.
  p_dic['times'] = [i[0] for i in sorted_bins]
  p_dic['aveSpeed'] = [i[1] for i in sorted_bins]

  # Return processed data.
  return p_dic


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
    'summary': get_summary(data),
    'requests': get_requests(data),
    'response': get_responses(data),
    'resolvers': get_resolvers(data)
  }

  # Return processed data.
  return p_dic

