"""
Module containing utilities for RAKE algorithm.
"""
import string

from typing import Dict, List, Set, Tuple

PUNCTUATION = string.punctuation.replace('\'', '')  # Do not use apostrophe as a delimiter

ENGLISH_WORDS_STOPLIST: List[str] = [
    '(', ')', 'and', 'of', 'the', 'amongst', 'with', 'from', 'after', 'its', 'it', 'at', 'is',
    'this', ',', '.', 'be', 'in', 'that', 'an', 'other', 'than', 'also', 'are', 'may', 'suggests',
    'all', 'where', 'most', 'against', 'more', 'have', 'been', 'several', 'as', 'before',
    'although', 'yet', 'likely', 'rather', 'over', 'a', 'for', 'can', 'these', 'considered',
    'used', 'types', 'given', 'precedes',
]


def split_to_tokens(text: str) -> List[str]:
    """
    Split text string to tokens.

    Behavior is similar to str.split(),
    but empty lines are omitted and punctuation marks are separated from word.

    Example:
    split_to_tokens('John     said "Hey!" (and some other words.)') ->
    -> ['John', 'said', '"', 'Hey', '!', '"', '(', 'and', 'some', 'other', 'words', '.', ')']
    """
    result = []
    for item in text.split():
        while item[0] in PUNCTUATION:
            result.append(item[0])
            item = item[1:]
        for i in range(len(item)):
            if item[-i - 1] not in PUNCTUATION:
                break
        if i == 0:
            result.append(item)
        else:
            result.append(item[:-i])
            result.extend(item[-i:])
    return [item for item in result if item]


def split_tokens_to_phrases(tokens: List[str], stoplist: List[str] = None) -> List[str]:
    """
    Merge tokens into phrases, delimited by items from stoplist.

    Phrase is a sequence of token that has the following properties:
    - phrase contains 1 or more tokens
    - tokens from phrase go in a row
    - phrase does not contain delimiters from stoplist
    - either the previous (not in a phrase) token belongs to stop list or it is the beginning of tokens list
    - either the next (not in a phrase) token belongs to stop list or it is the end of tokens list

    Example:
    split_tokens_to_phrases(
        tokens=["Mary", "and", "John", ",", "some", "words", "(", "and", "other", "words", ")"],
        stoplist=["and", ",", ".", "(", ")"]) ->
    -> ["Mary", "John", "some words", "other words"]
    """
    if stoplist is None:
        stoplist = ENGLISH_WORDS_STOPLIST
    stoplist += list(PUNCTUATION)

    current_phrase: List[str] = []
    all_phrases: List[str] = []
    stoplist_set: Set[str] = {stopword.lower() for stopword in stoplist}
    for token in tokens:
        if token.lower() in stoplist_set:
            if current_phrase:
                all_phrases.append(" ".join(current_phrase))
            current_phrase = []
        else:
            current_phrase.append(token)
    if current_phrase:
        all_phrases.append(" ".join(current_phrase))
    return all_phrases


def get_cooccurrence_graph(phrases: List[str]) -> Dict[str, Dict[str, int]]:
    """
    Get graph that stores cooccurence of tokens in phrases.

    Matrix is stored as dict,
    where key is token, value is dict (key is second token, value is number of cooccurrence).

    Example:
    get_occurrence_graph(["Mary", "John", "some words", "other words"]) -> {
        'mary': {'mary': 1},
        'john': {'john': 1},
        'some': {'some': 1, 'words': 1},
        'words': {'some': 1, 'words': 2, 'other': 1},
        'other': {'other': 1, 'words': 1}
    }
    """
    graph: Dict[str, Dict[str, int]] = {}
    for phrase in phrases:
        for first_token in phrase.lower().split():
            for second_token in phrase.lower().split():
                if first_token not in graph:
                    graph[first_token] = {}
                graph[first_token][second_token] = graph[first_token].get(second_token, 0) + 1
    return graph


def get_degrees(cooccurrence_graph: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    """
    Get degrees for all tokens by cooccurrence graph.

    Result is stored as dict,
    where key is token, value is degree (sum of lengths of phrases that contain the token).

    Example:
    get_degrees(
        {
            'mary': {'mary': 1},
            'john': {'john': 1},
            'some': {'some': 1, 'words': 1},
            'words': {'some': 1, 'words': 2, 'other': 1},
            'other': {'other': 1, 'words': 1}
        }
    ) -> {'mary': 1, 'john': 1, 'some': 2, 'words': 4, 'other': 2}
    """
    return {token: sum(cooccurrence_graph[token].values()) for token in cooccurrence_graph}


def get_frequencies(cooccurrence_graph: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    """
    Get frequencies for all tokens by cooccurrence graph.

    Result is stored as dict,
    where key is token, value is frequency (number of times the token occurs).

    Example:
    get_frequencies(
        {
            'mary': {'mary': 1},
            'john': {'john': 1},
            'some': {'some': 1, 'words': 1},
            'words': {'some': 1, 'words': 2, 'other': 1},
            'other': {'other': 1, 'words': 1}
        }
    ) -> {'mary': 1, 'john': 1, 'some': 1, 'words': 2, 'other': 1}
    """
    return {token: cooccurrence_graph[token][token] for token in cooccurrence_graph}


def get_ranked_phrases(phrases: List[str], *,
                       degrees: Dict[str, int],
                       frequencies: Dict[str, int]) -> List[Tuple[str, float]]:
    """
    Get RAKE measure for every phrase.

    Result is stored as list of tuples, every tuple contains of phrase and its RAKE measure.

    Items are sorted non-ascending by RAKE measure, than alphabetically by phrase.
    """
    processed_phrases: Set[str] = set()
    ranked_phrases: List[Tuple[str, float]] = []
    for phrase in phrases:
        lowered_phrase = phrase.lower()
        if lowered_phrase in processed_phrases:
            continue
        score: float = sum(degrees[token] / frequencies[token] for token in lowered_phrase.split())
        ranked_phrases.append((lowered_phrase, round(score, 2)))
        processed_phrases.add(lowered_phrase)
    # Sort by score than by phrase alphabetically.
    ranked_phrases.sort(key=lambda item: (-item[1], item[0]))
    return ranked_phrases


def rake_text(text: str) -> List[Tuple[str, float]]:
    """
    Get RAKE measure for every phrase in text string.

    Result is stored as list of tuples, every tuple contains of phrase and its RAKE measure.

    Items are sorted non-ascending by RAKE measure, than alphabetically by phrase.
    """
    tokens: List[str] = split_to_tokens(text)
    phrases: List[str] = split_tokens_to_phrases(tokens)
    cooccurrence: Dict[str, Dict[str, int]] = get_cooccurrence_graph(phrases)
    degrees: Dict[str, int] = get_degrees(cooccurrence)
    frequencies: Dict[str, int] = get_frequencies(cooccurrence)
    ranked_result: List[Tuple[str, float]] = get_ranked_phrases(phrases, degrees=degrees, frequencies=frequencies)
    return ranked_result
