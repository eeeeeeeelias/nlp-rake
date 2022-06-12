# nlp-rake

![Python >= 3.6](https://img.shields.io/badge/python->=3.6-blue)
![License MIT](https://img.shields.io/badge/license-MIT-green)
![cov: 100%](https://img.shields.io/badge/codecov-100%25-brightgreen)

A Python package that implements RAKE algorithm for keyword extraction.

Rapid Automatic Keyword Extraction (RAKE) algorithm is [proposed](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents) by Stuart Rose, Dave Engel, Nick Cramer, Wendy Cowley.
## Installation
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps nlp-rake-eeeeeeeelias
```

## Quick usage
```
    from nlp_rake import rake_text

    text = 'Compatibility of systems of...'
    ranked_result = rake_text(text)
    # [
    #     ('minimal generating sets', 8.67),
    #     ('linear diophantine equations', 8.5),
    #     ('minimal supporting set', 7.67),
    #     ...
    # ]
```

## Advanced usage
```
    import nlp_rake

    text = 'Compatibility of systems of...'

    tokens = nlp_rake.split_to_tokens(text)
    phrases = nlp_rake.split_tokens_to_phrases(
        tokens, stoplist=nlp_rake.ENGLISH_WORDS_STOPLIST
    )
    cooccurrence = nlp_rake.get_cooccurrence_graph(phrases)
    degrees = nlp_rake.get_degrees(cooccurrence)
    frequencies = nlp_rake.get_frequencies(cooccurrence)
    ranked_result = nlp_rake.get_ranked_phrases(
        phrases, degrees=degrees, frequencies=frequencies
    )
    # [
    #     ('minimal generating sets', 8.67),
    #     ('linear diophantine equations', 8.5),
    #     ('minimal supporting set', 7.67),
    #     ...
    # ]
```