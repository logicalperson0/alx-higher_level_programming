#!/usr/bin/python3
""" Module for test Base class """
import unittest
from unittest import mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id"""
        ins = Base()
        self.assertEqual(ins.id, 1)

    def test_for_when_id_1(self):
        """Test for id 1"""
        ins = Base(1)
        self.assertEqual(ins.id, 1)

    def test_id_nb_objects(self):
        """Test for id conti"""
        ins = Base()
        ins2 = Base()
        ins4 = Base(None)
        ins3 = Base()

        self.assertEqual(ins.id, 1)
        self.assertEqual(ins2.id, 2)
        self.assertEqual(ins4.id, 3)
        self.assertEqual(ins3.id, 4)

    def test_id_mix(self):
        """Test by mixing num and -ve"""
        ins = Base()
        ins2 = Base(-1024)
        ins3 = Base()
        ins4 = Base(333)

        self.assertEqual(ins.id, 1)
        self.assertEqual(ins2.id, -1024)
        self.assertEqual(ins3.id, 2)
        self.assertEqual(ins4.id, 333)

    def test_string_id(self):
        """Test string"""
        ins = Base('Alx School')
        self.assertEqual(ins.id, 'Alx School')

    def test_more_args_id(self):
        """test errors"""
        with self.assertRaises(TypeError):
            new = Base(30, 55)

    def test_attrs(self):
        """Test for private attributes """
        ins = Base()
        with self.assertRaises(AttributeError):
            ins.__nb_objects

    def test_for_empty(self):
        ins = []
        insa = Base.to_json_string(ins)
        self.assertEqual(insa, '[]')

    def test_save_to_file(self):
        """Test save to file"""
        Square.save_to_file(None)
        ins = "[]\n"
        with open("Square.json", "r") as di:
            with mock.patch('sys.stdout', new=StringIO()) as insa:
                print(di.read())
                self.assertEqual(insa.getvalue(), ins)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as di:
            self.assertEqual(di.read(), "[]")

    def test_ins(self):
        ins = Base()
        self.assertEqual(type(ins), Base)
        self.assertTrue(isinstance(ins, Base))
