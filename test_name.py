from names import make_full_name, \
    extract_family_name, extract_given_name
from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Jared", "Keh") == "Keh; Jared"
    assert make_full_name("Emily", "Keh") == "Keh; Emily"
    assert make_full_name("Brandon", "Lewis") == "Lewis; Brandon"
    

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Keh; Jared") == "Keh"
    assert extract_family_name("Keh; Emily") == "Keh"
    assert extract_family_name("Lewis; Brandon") == "Lewis"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Keh; Jared") == "Jared"
    assert extract_given_name("Keh; Emily") == "Emily"
    assert extract_given_name("Lewis; Brandon") == "Brandon"



pytest.main(["-v", "--tb=line", "-rN", __file__])