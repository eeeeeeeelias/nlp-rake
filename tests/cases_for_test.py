from collections import namedtuple

from data_for_tests import DIOPHANTINE_ABSTRACT, HVV8_KS_ABSTRACT
from data_for_tests import DIOPHANTINE_COOCCURRENCE_EXPECTED, HVV8_KS_COOCCURRENCE_EXPECTED
from data_for_tests import DIOPHANTINE_DEGREES_EXPECTED, HVV8_KS_DEGREES_EXPECTED
from data_for_tests import DIOPHANTINE_FREQUENCIES_EXPECTED, HVV8_KS_FREQUENCIES_EXPECTED
from data_for_tests import DIOPHANTINE_PHRASES_EXPECTED, HVV8_KS_PHRASES_EXPECTED
from data_for_tests import DIOPHANTINE_RANKED_EXPECTED, HVV8_KS_RANKED_EXPECTED
from data_for_tests import DIOPHANTINE_TOKENS_EXPECTED, HVV8_KS_TOKENS_EXPECTED


Case = namedtuple('Case', ['data', 'expected', 'name'])


ENGLISH_WORDS_STOPLIST = [
    '(', ')', 'and', 'of', 'the', 'amongst', 'with', 'from', 'after', 'its', 'it', 'at', 'is',
    'this', ',', '.', 'be', 'in', 'that', 'an', 'other', 'than', 'also', 'are', 'may', 'suggests',
    'all', 'where', 'most', 'against', 'more', 'have', 'been', 'several', 'as', 'before',
    'although', 'yet', 'likely', 'rather', 'over', 'a', 'for', 'can', 'these', 'considered',
    'used', 'types', 'given', 'precedes',
]


TOKENS_TEST_CASES = [
    Case(data=HVV8_KS_ABSTRACT, expected=HVV8_KS_TOKENS_EXPECTED, name='hhv8-ks'),
    Case(data=DIOPHANTINE_ABSTRACT, expected=DIOPHANTINE_TOKENS_EXPECTED, name='diophantine'),
]


PHRASES_TEST_CASES = [
    Case(data=HVV8_KS_ABSTRACT, expected=HVV8_KS_PHRASES_EXPECTED, name='hhv8-ks'),
    Case(data=DIOPHANTINE_ABSTRACT, expected=DIOPHANTINE_PHRASES_EXPECTED, name='diophantine'),
]


COOCCURRENCE_TEST_CASES = [
    Case(data=HVV8_KS_ABSTRACT, expected=HVV8_KS_COOCCURRENCE_EXPECTED, name='hhv8-ks'),
    Case(data=DIOPHANTINE_ABSTRACT, expected=DIOPHANTINE_COOCCURRENCE_EXPECTED, name='diophantine'),
]


DEGREES_TEST_CASES = [
    Case(data=HVV8_KS_ABSTRACT, expected=HVV8_KS_DEGREES_EXPECTED, name='hhv8-ks'),
    Case(data=DIOPHANTINE_ABSTRACT, expected=DIOPHANTINE_DEGREES_EXPECTED, name='diophantine'),
]


FREQUENCIES_TEST_CASES = [
    Case(data=HVV8_KS_ABSTRACT, expected=HVV8_KS_FREQUENCIES_EXPECTED, name='hhv8-ks'),
    Case(data=DIOPHANTINE_ABSTRACT, expected=DIOPHANTINE_FREQUENCIES_EXPECTED, name='diophantine'),
]


RANKED_TEST_CASES = [
    Case(data=HVV8_KS_ABSTRACT, expected=HVV8_KS_RANKED_EXPECTED, name='hhv8-ks'),
    Case(data=DIOPHANTINE_ABSTRACT, expected=DIOPHANTINE_RANKED_EXPECTED, name='diophantine'),
]
