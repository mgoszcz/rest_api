
class Film:

    def __init__(self, film_obj):
        for key, value in film_obj.json().items():
            setattr(self, key, value)
