import pytest
import re

def test_green_cards():
    balance = 10

    balance += 1
    assert balance == 11

    balance = 10
    balance += 3
    assert balance == 13

    balance = 10
    balance += 5
    assert balance == 15

    balance = 10
    balance += 7
    assert balance == 17


def test_blue_cards():
    balance = 10

    balance -= 2
    assert balance == 8

    balance = 10
    balance -= 4
    assert balance == 6

    balance = 10
    balance -= 6
    assert balance == 4

    balance = 10
    balance -= 8
    assert balance == 2


def test_multiply_card():
    balance = 10
    balance *= 2
    assert balance == 20


def test_divide_card():
    balance = 10

    balance /= 2

    assert balance == 5


def test_plus_special_card():
    draws = 10

    draws -= 1
    draws += 2

    assert draws == 11


def test_minus_special_card():
    draws = 10

    draws -= 1
    draws -= 2

    assert draws == 7


def test_card_regex():
    cards = [
        '+1', '+3', '+5', '+7',
        '-2', '-4', '-6', '-8',
        'x2', '/2', '+2!', '-2!'
    ]

    for card in cards:
        number = re.search(r"([+-x/])(\d)([!]?)", card)

        assert number is not None


def test_deck():
    greenCards = ['+1', '+3', '+5', '+7']
    blueCards = ['-2', '-4', '-6', '-8']
    blackCards = ['x2', '/2', '+2!', '-2!']

    deck = greenCards + blueCards + blackCards

    assert len(deck) == 12