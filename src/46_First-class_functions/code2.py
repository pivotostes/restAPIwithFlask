from operator import itemgetter


def search(sequence, expected, finder):
    for elemen in sequence:
        if finder(elemen) == expected:
            return elemen
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Bob", "age": 24},
    {"name": "Rolf", "age": 27},
    {"name": "Jen", "age": 30}
]


def get_name_friend(friend: str) -> dict:
    return friend["name"]


print(search(friends, "Bob", get_name_friend))
print(search(friends, "Jen", itemgetter("name")))
