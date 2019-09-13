import unittest
import json

from data_processing import *
from overview import *

# Declare a test json file.
TEST_FILE = './test_data.json'

# Load in the test data.
with open(TEST_FILE) as test_data:
    data = json.load(test_data)


#######################################################################


class TestOverviewModeDataprocessing(unittest.TestCase):
  """
  Test Case for Overview Mode Data Processing.
  Test Fixture is parsed local test_data.json file.

  Checks the following:

    test_get_summary:        test for overview.get_summary
    test_get_requests:       test for overview.get_requests
    test_get_responses:      test for overview.get_responses
    test_get_resolvers:      test for overview.get_resolvers
    test_get_overview_data:  test for overview.get_overview_data
  """
  # Set up our test fixture by loading in the test data.
  def setUp(self):
    self.data = data


  # Test the Overview/Summary data processin functiong.
  def test_get_summary(self):
    # Init the summary data.
    testReturn = get_summary(self.data)

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict)) 

    # Test for keys in dict.
    self.assertTrue('numTotalRequests' in testReturn)

    # Test for value type on keys.
    keyval_types = {
      'numTotalRequests': int
    }
    self.assertTrue(
      all([type(value) == keyval_types[key]
           for key, value
           in testReturn.items()])
    )

    # Test for conditional non-empty result.
    self.assertTrue(len(testReturn) > 0
                    if 'Query' in self.data
                    else len(testReturn) == 0)

    # Clean up.
    del testReturn
  

  # Test the Overview/Requests data processing function.
  def test_get_requests(self):
    # Init requests data.
    testReturn = get_requests(self.data)

    # Define expected key/vals types.
    keyval_types = {
      'times': list,
      'rpm': list,
    }

    should_be_sorted = ['times']

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict)) 

    # Test for keys in dict.
    self.assertTrue(all([i in testReturn
                         for i in keyval_types.keys()]))

    # Test for value type on keys.
    self.assertTrue(
      all([type(value) == keyval_types[key]
           for key, value
           in testReturn.items()])
    )

    # Test for conditional non-empty results.
    self.assertTrue(
      all([len(y) > 0 if len(self.data['Query']) > 0 else len(y) == 0
           for x,y in testReturn.items()])
    )

    # Test for sorted keys.
    self.assertTrue(
      all([sorted(testReturn[x]) == testReturn[x]
           for x in should_be_sorted])
    )

    # Clean-up.
    del testReturn


  # Test the Overview/Response data processing function.
  def test_get_responses(self):
    # Init requests data.
    testReturn = get_responses(self.data)

    # Define expected key/vals types.
    keyval_types = {
      'ave': float,
      'count': int,
      'times': list,
      '90': list,
    }
    should_be_sorted = ['times']

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict)) 

    # Test for keys in dict.
    self.assertTrue(all([i in testReturn
                         for i in keyval_types.keys()]))

    # Test for value type on keys.
    self.assertTrue(
      all([type(value) == keyval_types[key]
           for key, value
           in testReturn.items()])
    )

    # Test for conditional non-empty list results.
    self.assertTrue(
       len(testReturn['times']) > 0
       if len(self.data['Query']) > 0
       else len(testReturn['times']) == 0
    )
    self.assertTrue(
       len(testReturn['90']) > 0
       if len(self.data['Query']) > 0
       else len(testReturn['90']) == 0
    )

    # Test for sorted keys.
    self.assertTrue(
      all([sorted(testReturn[x]) == testReturn[x]
           for x in should_be_sorted])
    )

    # Clean-up.
    del testReturn


  # Test the Overview/Resolvers data processing function.
  def test_get_resolvers(self):
    # Init requests data.
    testReturn = get_resolvers(self.data)

    # Define expected key/vals types.
    keyval_types = {
      'times':    list,
      'aveSpeed': list,
    }
    should_be_sorted = ['times']

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict)) 

    # Test for keys in dict.
    self.assertTrue(all([i in testReturn
                         for i in keyval_types.keys()]))

    # Test for value type on keys.
    self.assertTrue(
      all([type(value) == keyval_types[key]
           for key, value
           in testReturn.items()])
    )

    # Test for conditional non-empty results.
    self.assertTrue(
      all([len(y) > 0 if len(self.data['Query']) > 0 else len(y) == 0
           for x,y in testReturn.items()])
    )

    # Test for sorted keys.
    self.assertTrue(
      all([sorted(testReturn[x]) == testReturn[x]
           for x in should_be_sorted])
    )

    # Clean-up.
    del testReturn
 

  # Test for Overview/Overview_Data data processing function
  def test_get_overview_data(self):
    # Init overview data.
    testReturn = get_overview_data(self.data)

    # Define expected key/vals types.
    keyval_types = {
      'summary':   dict,
      'requests':  dict,
      'response':  dict,
      'resolvers': dict
    }

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict)) 

    # Test for keys in dict.
    self.assertTrue(all([i in testReturn
                         for i in keyval_types.keys()]))

    # Clean-up.
    del testReturn


  # Clean-up.
  def tearDown(self):
    del self.data


class TestResolversModeDataprocessing(unittest.TestCase):
  """
  Test Case for Resolvers Mode Data Processing.
  Test Fixture is parsed local test_data.json file.

  Checks the following:

    test_get_invocationcounts:   test for resolvers.get_invocationcounts
    test_get_aveexecutiontimes:  test for resolvers.get_aveexecutiontimes
    test_get_resolvers_data:     test for resolvers.get_resolvers_data
  """
  # Set up our test fixture by loading in the test data.
  def setUp(self):
    self.data = data


  # Test the Resolvers/InvocationCounts data processing function.
  def test_get_invocationcounts(self):
    # Init the summary data.
    testReturn = get_invocationcounts(self.data)

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict))

    # Test for non-zero length count.
    self.assertTrue(
      len(testReturn) > 0
      if len(self.data['Query']) > 0
      else len(testReturn) == 0
    )

    # Test for type on return data.
    self.assertTrue(all([type(testReturn[i]) == int for i in testReturn]))

    # Test for non-zero data on return data.
    self.assertTrue(all([testReturn[i] > 0 for i in testReturn]))

    # Clean-up.
    del testReturn


  # Test the Resolvers/AveExecutionTimes data processing function.
  def test_get_aveexecutiontimes(self):
    # Init the summary data.
    testReturn = get_aveexecutiontimes(self.data)

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict))

    # Test for non-zero length count.
    self.assertTrue(
      len(testReturn) > 0
      if len(self.data['Query']) > 0
      else len(testReturn) == 0
    )

    # Test for type on return data.
    self.assertTrue(
      all([type(testReturn[i]) == float for i in testReturn])
    )

    # Test for non-zero data on return data.
    self.assertTrue(
      all([testReturn[i] >= 0 for i in testReturn])
    )

    # Clean-up.
    del testReturn


  # Test the Resolvers/InvocationCounts data processing function.
  def test_get_resolvers_data(self):
    # Init the summary data.
    testReturn = get_resolvers_data(self.data)

    # Declare expected types.
    keyval_types = {
      'invocationCounts': dict,
      'executionTimes': dict,
      'averageTime': float
    }

    # Test for return type.
    self.assertTrue(isinstance(testReturn, dict))

    # Test for non-zero length count.
    self.assertTrue(
      [len(testReturn[i]) > 0
       if len(self.data['Query']) > 0
       else len(testReturn[i]) == 0
       for i in ["invocationCounts", "executionTimes"]]
    )

    # Test for type on return data.
    self.assertTrue(
      all([type(testReturn[i]) == keyval_types[i] for i in testReturn])
    )

    # Test for non-zero data on average time.
    self.assertTrue(
      testReturn['averageTime'] > 0
    )

    # Clean-up.
    del testReturn


if __name__ == '__main__':
   unittest.main()

