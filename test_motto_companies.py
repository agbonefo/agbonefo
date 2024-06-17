
from io import StringIO
import sys
import unittest

def print_motto_companies():
  """Prints a Hello World message and a sorted list of motto companies in Edo State, Nigeria"""
  # Print Hello World message
  print("Hello World!")

  # Sample list of motto companies in Edo State, Nigeria
  motto_companies = [
      "Godwin Ize-Iyamu Motors",
      "Ekons Transport",
      "A.A.A. Motors",
      "Young Shall Grow Motors",
      "Ehigabus",
      "Iyeagbe Motors",
      "Peace Mass Transit",
      "AY RoadRunners",
      "Onitsha South East Transport Company",
      "Edo Line"
  ]

  # Sort the list of companies alphabetically
  motto_companies.sort()

  # Print the sorted list of companies
  print("Motto Companies in Edo State, Nigeria:")
  for company in motto_companies:
    print(company)

class TestMottoCompanies(unittest.TestCase):

  def test_hello_world_message(self):
    # Test if "Hello World!" is printed
    captured_output = StringIO()  # Capture output for testing
    sys.stdout = captured_output
    print_motto_companies()
    sys.stdout = sys.__stdout__  # Restore original stdout
    self.assertIn("Hello World!", captured_output.getvalue())

  def test_sorted_companies(self):
    # Test if the list of companies is sorted alphabetically
    expected_companies = sorted([
      "Godwin Ize-Iyamu Motors",
      "Ekons Transport",
      "A.A.A. Motors",
      "Young Shall Grow Motors",
      "Ehigabus",
      "Iyeagbe Motors",
      "Peace Mass Transit",
      "AY RoadRunners",
      "Onitsha South East Transport Company",
      "Edo Line"
    ])
    print_motto_companies()  # Run the function to sort the list

    motto_companies = [
      "Godwin Ize-Iyamu Motors",
      "Ekons Transport",
      "A.A.A. Motors",
      "Young Shall Grow Motors",
      "Ehigabus",
      "Iyeagbe Motors",
      "Peace Mass Transit",
      "AY RoadRunners",
      "Onitsha South East Transport Company",
      "Edo Line"
    ]
 

    self.assertEqual(motto_companies, expected_companies)
    #henry
    #assert(motto_companies == expected_companies, "Names are not sorted correctly")

if __name__ == "__main__":
  unittest.main()

