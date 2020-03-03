
class Vehicle:

    def __init__(self, vehicle_obj):
        for key, value in vehicle_obj.json().items():
            setattr(self, key, value)