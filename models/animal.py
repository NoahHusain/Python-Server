class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, species, status, location_id = 0, customer_id = 0):
        self.id = id
        self.name = name
        self.species = species
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id