
class StarShip:

    def __init__(self, star_ship_obj):
        for key, value in star_ship_obj.json().items():
            setattr(self, key, value)
