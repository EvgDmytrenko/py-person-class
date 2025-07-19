class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people]

    for person_dict in people:
        wife_key = person_dict.get("wife")
        husband_key = person_dict.get("husband")
        if wife_key is not None:
            Person.people[person_dict["name"]].wife = Person.people[wife_key]
        if husband_key is not None:
            Person.people[person_dict["name"]].husband = (
                Person.people)[husband_key]

    return person_list
