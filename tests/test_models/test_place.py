#!/usr/bin/python3

"""Test case for place """

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Base model Test """

    def __init__(self, *args, **kwargs):
        """initials """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Self"""
        dev_n = self.value()
        self.assertEqual(type(dev_n.city_id), str)

    def test_user_id(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.user_id), str)

    def test_name(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.name), str)

    def test_description(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.description), str)

    def test_number_rooms(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.max_guest), int)

    def test_price_by_night(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.price_by_night), int)

    def test_latitude(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.latitude), float)

    def test_longitude(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.latitude), float)

    def test_amenity_ids(self):
        """ """
        dev_n = self.value()
        self.assertEqual(type(dev_n.amenity_ids), list)
