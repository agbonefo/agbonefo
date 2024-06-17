#!/usr/bin/python3

#2024-06-17

def main():
    # Print "Hello, world!"
    print("Hello, world!")

    # List of transport companies in Edo State
    edo_transport_companies = [
        "God Is Good Motors (GIGM)",
        "ABC Motors",
        "GUO Transport",
        "Autostar Travels",
        "Chisco Transport Limited",
        "The Young Shall Grow Motors",
        "Ifesinachi Transport Limited",
        "Cross Country Limited",
        "Peace Mass Transit (PMT)",
        "Bonny Way Motors Nig. Ltd"
    ]

    # Sort the list alphabetically
    edo_transport_companies.sort()

    # Print the sorted names
    for company in edo_transport_companies:
        print(company)

if __name__ == "__main__":
    main()
