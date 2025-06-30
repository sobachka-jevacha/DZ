import pytest
from string_utils import StringUtils

string = StringUtils()

@pytest.mark.positive
def test_capitalize():
    capitalize = StringUtils()
    res = capitalize.capitalize("мария")
    assert res == "Мария"


@pytest.mark.negative
@pytest.mark.parametrize('str,result', [("пАВЕЛ", "ПАВЕЛ"),("сАшА", "САшА"), ("2", "2")])
def test_capitalize_negative(str, result):
    capitalize = StringUtils()
    res = capitalize.capitalize(str)
    assert res == result

@pytest.mark.xfail
@pytest.mark.negative
def test_capitalize():
    capitalize = StringUtils()
    res = capitalize.capitalize(None)
    assert res == None


@pytest.mark.positive
def test_trim():
    Trim = StringUtils()
    res = Trim.trim("  Привет")
    assert res == "Привет"


@pytest.mark.negative
@pytest.mark.parametrize('str, result', [("    ", ""), ("Артур    ", "Артур    "), ("Д м и т р и й", "Д м и т р и й"), ("11", "11")])
def test_trim_negative(str, result):
    Trim = StringUtils()
    res = Trim.trim(str)
    assert res == result


@pytest.mark.positive
def test_contains():
    Contains = StringUtils()
    res = Contains.contains("Москва", "о")
    assert res == True


@pytest.mark.positive
def test_contains():
    Contains = StringUtils()
    res = Contains.contains("Ка зань", " ")
    assert res == True


@pytest.mark.negative
@pytest.mark.parametrize('str, sumbol, result', [("Евгений", "Ф", False),("", "н", False), ("Дарья", "д", False)])
def test_contains_negative(str, sumbol, result):
    Contains = StringUtils()
    res = Contains.contains(str, sumbol)
    assert res == result


@pytest.mark.positive
@pytest.mark.parametrize('str, sumbol, result', [("Скайпро", "С", "кайпро"), ("Скайпро", "про", "Скай"), ("Скайпро", "Скайпро", "")])
def test_delete_symbol(str, sumbol, result):
    Delete_symbol = StringUtils()
    res = Delete_symbol.delete_symbol(str, sumbol)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize('str, sumbol, result', [("Рязань", "р", "Рязань"), ("Волга", "ф", "Волга"), ("Анна-Мария", "-М", "Аннаария")])
def test_delete_symbol_negative(str, sumbol, result):
    Delete_symbol = StringUtils()
    res = Delete_symbol.delete_symbol(str, sumbol)
    assert res == result