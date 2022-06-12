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
    Функция работает почти как метод str.split(), с некоторыми особенностями:
    - пустые строки не остаются в итоговом списке
    - знаки препинания в начале и в конце слова (все, кроме апострофа) отделяются от слова

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
    Функция получает на вход список токенов tokens и список разделителей stoplist,
    а возвращает список фраз.
    Фраза -- такой набор токенов, что
    - фраза содержит несколько токенов (>0), идущих в списке tokens подряд
    - фраза не содержит разделителей
    - перед фразой стоит разделитель из stoplist или начало списка tokens
    - после фразы стоит разделитель из stoplist или конец списка tokens

    Если простыми словами, нужно сложить слова в словосочетаниями,
    а границами этих словосочетаний являются элементы stoplist
    Example:
    split_tokens_to_phrases(
        tokens=["Mary", "and", "John", ",", "some", "words", "(", "and", "other", "words", ")"],
        stoplist=["and", ",", ".", "(", ")"]) ->
    -> ["Mary", "John", "some words", "other words"]
    """
    if stoplist is None:
        stoplist = ENGLISH_WORDS_STOPLIST

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
    Функция принимает список фраз и возвращает таблицу совместной встречаемости в виде словаря,
    где ключом является токен, а значением -- словарём
    (в этом внутреннем словаре ключ -- токен, а значение -- встречаемость).

    Пример: смотрите тесты!
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
    Функция принимает таблицу встречаемости и для каждого токена возвращает его СТЕПЕНЬ:
    сумму длин фраз, в которых встречается этот токен.

    Пример: смотрите тесты!
    """
    return {token: sum(cooccurrence_graph[token].values()) for token in cooccurrence_graph}


def get_frequencies(cooccurrence_graph: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    """
    Функция принимает таблицу встречаемости и для каждого токена возвращает его ЧАСТОТУ:
    количество раз, которое этот токен встречается.

    Пример: смотрите тесты!
    """
    return {token: cooccurrence_graph[token][token] for token in cooccurrence_graph}


def get_ranked_phrases(phrases: List[str], *,
                       degrees: Dict[str, int],
                       frequencies: Dict[str, int]) -> List[Tuple[str, float]]:
    """
    Функция принимает список фраз, степени и частоты токенов.
    Функция возвращает список кортежей, где каждый кортеж -- фраза и её score.
    Score должен быть округлен до 2 знаков после запятой.
    Элементы списка упорядочены по убыванию score,
    при равенстве score -- в алфавитном порядке по фразе.
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
    tokens: List[str] = split_to_tokens(text)
    phrases: List[str] = split_tokens_to_phrases(tokens, stoplist=ENGLISH_WORDS_STOPLIST)
    cooccurrence: Dict[str, Dict[str, int]] = get_cooccurrence_graph(phrases)
    degrees: Dict[str, int] = get_degrees(cooccurrence)
    frequencies: Dict[str, int] = get_frequencies(cooccurrence)
    ranked_result: List[Tuple[str, float]] = get_ranked_phrases(phrases, degrees=degrees, frequencies=frequencies)
    return ranked_result
