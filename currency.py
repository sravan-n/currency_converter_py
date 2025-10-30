"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Sravan Kumar Nuthalapati
Date:   10/28/2025
"""

import introcs

APIKEY = 'sK7fFU3F8eGfcJA9679KDrnbcpmpcASn3CpLfRF2fTYe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, ' ') >= 1, repr(s) + ' has no space in it'

    # Find the index of the first space in the string
    pos = introcs.find_str(s, ' ')
    # Compute the substring from the start to first space
    result = s[:pos]
    # Return the result
    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, ' ') >= 1, repr(s) + ' has no space in it'

    # Find the index of the first space in the string
    pos = introcs.find_str(s, ' ')
    # Compute the substring after the first space
    result = s[pos+1:]
    # Return the result
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a 
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """

    assert type(s) == str, repr(s) + ' is not a string'
    assert introcs.count_str(s, '"') >= 2, repr(s) + 'should have 2 double quotes inside'

    # Find postion of first double quote
    pos1 = introcs.find_str(s, '"')
    # Find position of second double quote
    pos2 = introcs.find_str(s, '"', pos1+1)
    # Compute the substring between position 1 and 2
    result = s[pos1+1:pos2]
    # Retun the substring
    return result