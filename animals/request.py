ANIMALS = [
    {
        "id": 1,
        "name": "Doodles",
        "species": "dog",
        "customerId": 1,
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Baylee",
        "species": "dog",
        "customerId": 2,
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Snoop",
        "species": "dog",
        "customerId": 3,
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Sky",
        "species": "bird",
        "customerId": 4,
        "locationId": 1
    },
    {
        "id": 5,
        "name": "Porker",
        "species": "pig",
        "customerId": 5,
        "locationId": 2
    },
    {
        "id": 6,
        "name": "Shadow",
        "species": "cat",
        "customerId": 2,
        "locationId": 1
    }
]


def get_all_animals():
    return ANIMALS

# Function with a single parameter


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal
