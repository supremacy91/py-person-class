class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)
    for person in people:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]
    return person_list
