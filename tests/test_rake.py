import pytest

from src.nlp_rake import get_cooccurrence_graph, get_degrees, get_frequencies, get_ranked_phrases
from src.nlp_rake import split_to_tokens, split_tokens_to_phrases

from cases_for_test import Case
from cases_for_test import ENGLISH_WORDS_STOPLIST
from cases_for_test import COOCCURRENCE_TEST_CASES, DEGREES_TEST_CASES, FREQUENCIES_TEST_CASES
from cases_for_test import PHRASES_TEST_CASES, RANKED_TEST_CASES, TOKENS_TEST_CASES


@pytest.mark.parametrize(
    'data, expected',
    [
        ('OSX 13.0', ['OSX', '13.0']),
        ('a b c', ['a', 'b', 'c']),
        (
                'John    said "Hey!" (and some other words.)',
                ['John', 'said', '"', 'Hey', '!', '"', '(', 'and', 'some', 'other', 'words', '.', ')']
        ),
        ('A  and   B.  ', ['A', 'and', 'B', '.']),
        ('(Hey...)', ['(', 'Hey', '.', '.', '.', ')']),
    ]
)
def test_split_to_tokens_simple(data, expected) -> None:
    assert split_to_tokens(data) == expected


@pytest.mark.parametrize('case', TOKENS_TEST_CASES, ids=lambda c: c.name)
def test_split_to_tokens(case: Case) -> None:
    tokens = split_to_tokens(case.data)
    for i, token in enumerate(tokens):
        assert token == case.expected[i], f'Mismatch at token #{i}: {token}'
    assert len(tokens) == len(case.expected), 'Wrong number of tokens'


@pytest.mark.parametrize(
    'tokens, stoplist, expected',
    [
        (
                ['Mary', 'and', 'John', ',', 'some', 'words', '(', 'and', 'other', 'words', ')'],
                ['and', ',', '.', '(', ')'],
                ['Mary', 'John', 'some words', 'other words']
        ),
        (['a', 'b'], [], ['a b']),
    ]
)
def test_split_tokens_to_phrases_simple(tokens, stoplist, expected) -> None:
    assert split_tokens_to_phrases(tokens=tokens, stoplist=stoplist) == expected


@pytest.mark.parametrize('case', PHRASES_TEST_CASES, ids=lambda c: c.name)
def test_split_tokens_to_phrases(case: Case) -> None:
    tokens = split_to_tokens(case.data)
    phrases = split_tokens_to_phrases(tokens, stoplist=ENGLISH_WORDS_STOPLIST)
    for i, phrase in enumerate(phrases):
        assert phrase == case.expected[i], f'Mismatch at phrase #{i}: {phrase}'
    assert len(phrases) == len(case.expected), 'Wrong number of phrases'


@pytest.mark.parametrize('case', COOCCURRENCE_TEST_CASES, ids=lambda c: c.name)
def test_get_cooccurrence_graph(case: Case) -> None:
    tokens = split_to_tokens(case.data)
    phrases = split_tokens_to_phrases(tokens, stoplist=ENGLISH_WORDS_STOPLIST)
    cooccurrence_result = get_cooccurrence_graph(phrases)
    for key in cooccurrence_result:
        assert cooccurrence_result[key] == case.expected[key], f'Mismatch at token {key}'
    assert len(cooccurrence_result) == len(case.expected), 'Wrong number of tokens'


@pytest.mark.parametrize('case', DEGREES_TEST_CASES, ids=lambda c: c.name)
def test_get_degrees(case: Case) -> None:
    tokens = split_to_tokens(case.data)
    phrases = split_tokens_to_phrases(tokens, stoplist=ENGLISH_WORDS_STOPLIST)
    cooccurrence = get_cooccurrence_graph(phrases)
    degrees_result = get_degrees(cooccurrence)
    for key in degrees_result:
        assert degrees_result[key] == case.expected[key], f'Mismatch at token {key}'
    assert len(degrees_result) == len(case.expected), 'Wrong number of tokens'


@pytest.mark.parametrize('case', FREQUENCIES_TEST_CASES, ids=lambda c: c.name)
def test_get_frequencies(case: Case) -> None:
    tokens = split_to_tokens(case.data)
    phrases = split_tokens_to_phrases(tokens, stoplist=ENGLISH_WORDS_STOPLIST)
    cooccurrence = get_cooccurrence_graph(phrases)
    degrees_result = get_frequencies(cooccurrence)
    for key in degrees_result:
        assert degrees_result[key] == case.expected[key], f'Mismatch at token {key}'
    assert len(degrees_result) == len(case.expected), 'Wrong number of tokens'


@pytest.mark.parametrize('case', RANKED_TEST_CASES, ids=lambda c: c.name)
def test_get_ranked_phrases(case: Case) -> None:
    tokens = split_to_tokens(case.data)
    phrases = split_tokens_to_phrases(tokens, stoplist=ENGLISH_WORDS_STOPLIST)
    cooccurrence = get_cooccurrence_graph(phrases)
    degrees = get_degrees(cooccurrence)
    frequencies = get_frequencies(cooccurrence)
    ranked_result = get_ranked_phrases(phrases, degrees=degrees, frequencies=frequencies)
    for i, phrase in enumerate(ranked_result):
        assert phrase[0] == case.expected[i][0], f'Mismatch at phrase #{i}: {phrase[0]}'
        assert phrase[1] == case.expected[i][1], \
            f'Wrong score {phrase[1]} at phrase #{i}: {phrase[0]}'
    assert len(ranked_result) == len(case.expected), 'Wrong number of phrases'
