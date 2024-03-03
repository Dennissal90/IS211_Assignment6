import pytest
from conversions import *

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(-273.15) == 0
    assert celsius_to_kelvin(100) == 373.15

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(-40) == -40
    assert fahrenheit_to_celsius(212) == 100

def test_fahrenheit_to_kelvin():
    assert fahrenheit_to_kelvin(32) == 273.15
    assert fahrenheit_to_kelvin(-40) == 233.15
    assert fahrenheit_to_kelvin(212) == 373.15

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0
    assert kelvin_to_celsius(0) == -273.15
    assert kelvin_to_celsius(373.15) == 100

def test_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(273.15) == 32
    assert kelvin_to_fahrenheit(233.15) == -40
    assert kelvin_to_fahrenheit(373.15) == 212
