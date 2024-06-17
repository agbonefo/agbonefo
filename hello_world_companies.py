def print_motto_companies():
  """Prints a Hello World message and a sorted list of motto companies in Edo State, Nigeria"""
  # Print Hello World message 2024-06-17
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

# Run the function
print_motto_companies()
