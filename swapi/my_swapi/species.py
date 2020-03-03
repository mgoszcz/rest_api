
class Species:

    def __init__(self, species_obj):
        for key, value in species_obj.json().items():
            setattr(self, key, value)
