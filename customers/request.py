CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct"
    },
    {
        "id": 2,
        "name": "Aubrey Husain",
        "address": "1515 Eugene Way"
    },
    {
        "id": 3,
        "name": "Steve Walmsley",
        "address": "2506 Aurora Rd"
    },
    {
        "id": 4,
        "name": "Monica Wright",
        "address": "8353 Borealis Blvd"
    },
    {
        "id": 5,
        "name": "Robin Porter",
        "address": "2352 Blossom St"
    },
    {
        "id": 6,
        "name": "Noah Husain",
        "address": "2606 Parkcrest Way",
        "email": "noahhusain@gmail.com"
    }
]


def get_all_customers():
    return CUSTOMERS

# Function with a single parameter


def get_single_customer(id):
    # Variable to hold the found location, if it exists
    requested_customer = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
