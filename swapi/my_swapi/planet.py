

class Planet:

    def __init__(self, planet_obj):
        for key, value in planet_obj.json().items():
            setattr(self, key, value)
