
class Person:

    def __init__(self, person_obj):
        for key, value in person_obj.json().items():
            setattr(self, key, value)
