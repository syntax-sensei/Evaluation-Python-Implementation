students = [
    {"name": "Alice", "marks": [80, 75, 90]},
    {"name": "Bob", "marks": [70, 60, 65]},
    {"name": "Charlie", "marks": [95, 85, 100]},
    {"name": "David", "marks": [60, 70, 80]},
]


def mapping(info):
    category = {
        "A": {d["name"] for d in info if sum(d["marks"]) / len(d["marks"]) >= 85},
        "B": {d["name"] for d in info if 70 <= sum(d["marks"]) / len(d["marks"]) < 85},
        "C": {d["name"] for d in info if sum(d["marks"]) / len(d["marks"]) < 70},
    }

    return category


print(mapping(students))
