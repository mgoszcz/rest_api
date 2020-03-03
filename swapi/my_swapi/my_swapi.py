import requests

from my_swapi.film import Film
from my_swapi.person import Person
from my_swapi.planet import Planet
from my_swapi.species import Species
from my_swapi.star_ship import StarShip
from my_swapi.vehicle import Vehicle


class SWApi:
    """
    SWAPI handling
    """
    def __init__(self):
        self._planets = list()
        self._films = list()
        self._people = list()
        self._species = list()
        self._starships = list()
        self._vehicles = list()
        # self.initialize_planets()

    def _initialize_objects(self, object_name, object_class, attribute):
        print('Initialize {}'.format(object_name))
        objects = requests.get('http://swapi.co/api/{}'.format(object_name))
        print('Objects found: {}'.format(objects.json()['count']))
        for i in range(1, objects.json()['count'] + 1):
            print('Initializing {} object'.format(i))
            obj = requests.get('http://swapi.co/api/{}/{}'.format(object_name ,i))
            attribute.append(object_class(obj))

    @property
    def planets(self):
        if not self._planets:
            self._initialize_objects('planets', Planet, self._planets)
        return self._planets

    @property
    def films(self):
        if not self._films:
            self._initialize_objects('films', Film, self._films)
        return self._films

    @property
    def people(self):
        if not self._people:
            self._initialize_objects('people', Person, self._people)
        return self._people

    @property
    def species(self):
        if not self._species:
            self._initialize_objects('species', Species, self._species)
        return self._species

    @property
    def star_ships(self):
        if not self._starships:
            self._initialize_objects('starships', StarShip, self._starships)
        return self._starships

    @property
    def vehicles(self):
        if not self._vehicles:
            self._initialize_objects('vehicles', Vehicle, self._vehicles)
        return self._vehicles
