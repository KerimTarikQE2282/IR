def get_people(name):
    people = [
        {"name": "John", "age": 25},
        {"name": "Alice", "age": 30},
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 40},
        {"name": "Jane", "age": 35}
    ]
    matching_people = [person for person in people if person["name"].lower() == name.lower()]
    return matching_people