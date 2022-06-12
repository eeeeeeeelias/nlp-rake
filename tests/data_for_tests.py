# LINEAR DIOPHANTINE EQUATIONS ARTICLE

# Article: https://link.springer.com/article/10.1023/A:1015531813214
DIOPHANTINE_ABSTRACT = """
Compatibility of systems of linear constraints over the set of natural numbers.
Criteria of compatibility of a system of linear Diophantine equations, strict inequations,
and nonstrict inequations are considered.
Upper bounds for components of a minimal set of solutions and algorithms of construction
of minimal generating sets of solutions for all types of systems are given.
These criteria and the corresponding algorithms for constructing a minimal supporting set
of solutions can be used in solving all the considered types of systems and systems.
"""

DIOPHANTINE_TOKENS_EXPECTED = [
    'Compatibility', 'of', 'systems', 'of', 'linear', 'constraints', 'over', 'the', 'set', 'of',
    'natural', 'numbers', '.', 'Criteria', 'of', 'compatibility', 'of', 'a', 'system', 'of',
    'linear', 'Diophantine', 'equations', ',', 'strict', 'inequations', ',', 'and', 'nonstrict',
    'inequations', 'are', 'considered', '.', 'Upper', 'bounds', 'for', 'components', 'of', 'a',
    'minimal', 'set', 'of', 'solutions', 'and', 'algorithms', 'of', 'construction', 'of',
    'minimal', 'generating', 'sets', 'of', 'solutions', 'for', 'all', 'types', 'of', 'systems',
    'are', 'given', '.', 'These', 'criteria', 'and', 'the', 'corresponding', 'algorithms', 'for',
    'constructing', 'a', 'minimal', 'supporting', 'set', 'of', 'solutions', 'can', 'be', 'used',
    'in', 'solving', 'all', 'the', 'considered', 'types', 'of', 'systems', 'and', 'systems', '.'
]

DIOPHANTINE_PHRASES_EXPECTED = [
    'Compatibility', 'systems', 'linear constraints', 'set', 'natural numbers', 'Criteria',
    'compatibility', 'system', 'linear Diophantine equations', 'strict inequations',
    'nonstrict inequations', 'Upper bounds', 'components', 'minimal set', 'solutions',
    'algorithms', 'construction', 'minimal generating sets', 'solutions', 'systems',
    'criteria', 'corresponding algorithms', 'constructing', 'minimal supporting set',
    'solutions', 'solving', 'systems', 'systems'
]

DIOPHANTINE_COOCCURRENCE_EXPECTED = {
    'algorithms': {'algorithms': 2, 'corresponding': 1},
    'bounds': {'bounds': 1, 'upper': 1},
    'compatibility': {'compatibility': 2},
    'components': {'components': 1},
    'constraints': {'constraints': 1, 'linear': 1},
    'constructing': {'constructing': 1},
    'construction': {'construction': 1},
    'corresponding': {'algorithms': 1, 'corresponding': 1},
    'criteria': {'criteria': 2},
    'diophantine': {'diophantine': 1, 'equations': 1, 'linear': 1},
    'equations': {'diophantine': 1, 'equations': 1, 'linear': 1},
    'generating': {'generating': 1, 'minimal': 1, 'sets': 1},
    'inequations': {'inequations': 2, 'nonstrict': 1, 'strict': 1},
    'linear': {'constraints': 1, 'diophantine': 1, 'equations': 1, 'linear': 2},
    'minimal': {
        'generating': 1,
        'minimal': 3,
        'set': 2,
        'sets': 1,
        'supporting': 1
    },
    'natural': {'natural': 1, 'numbers': 1},
    'nonstrict': {'inequations': 1, 'nonstrict': 1},
    'numbers': {'natural': 1, 'numbers': 1},
    'set': {'minimal': 2, 'set': 3, 'supporting': 1},
    'sets': {'generating': 1, 'minimal': 1, 'sets': 1},
    'solutions': {'solutions': 3},
    'solving': {'solving': 1},
    'strict': {'inequations': 1, 'strict': 1},
    'supporting': {'minimal': 1, 'set': 1, 'supporting': 1},
    'system': {'system': 1},
    'systems': {'systems': 4},
    'upper': {'bounds': 1, 'upper': 1}
}

DIOPHANTINE_DEGREES_EXPECTED = {
    'compatibility': 2, 'systems': 4, 'linear': 5, 'constraints': 2, 'set': 6, 'natural': 2,
    'numbers': 2, 'criteria': 2, 'system': 1, 'diophantine': 3, 'equations': 3, 'strict': 2,
    'inequations': 4, 'nonstrict': 2, 'upper': 2, 'bounds': 2, 'components': 1, 'minimal': 8,
    'solutions': 3, 'algorithms': 3, 'construction': 1, 'generating': 3, 'sets': 3,
    'corresponding': 2, 'constructing': 1, 'supporting': 3, 'solving': 1
}

DIOPHANTINE_FREQUENCIES_EXPECTED = {
    'compatibility': 2, 'systems': 4, 'linear': 2, 'constraints': 1, 'set': 3, 'natural': 1,
    'numbers': 1, 'criteria': 2, 'system': 1, 'diophantine': 1, 'equations': 1, 'strict': 1,
    'inequations': 2, 'nonstrict': 1, 'upper': 1, 'bounds': 1, 'components': 1, 'minimal': 3,
    'solutions': 3, 'algorithms': 2, 'construction': 1, 'generating': 1, 'sets': 1,
    'corresponding': 1, 'constructing': 1, 'supporting': 1, 'solving': 1
}

DIOPHANTINE_RANKED_EXPECTED = [
    ('minimal generating sets', 8.67), ('linear diophantine equations', 8.5),
    ('minimal supporting set', 7.67), ('minimal set', 4.67), ('linear constraints', 4.5),
    ('natural numbers', 4.0), ('nonstrict inequations', 4.0), ('strict inequations', 4.0),
    ('upper bounds', 4.0), ('corresponding algorithms', 3.5), ('set', 2.0), ('algorithms', 1.5),
    ('compatibility', 1.0), ('components', 1.0), ('constructing', 1.0), ('construction', 1.0),
    ('criteria', 1.0), ('solutions', 1.0), ('solving', 1.0), ('system', 1.0), ('systems', 1.0)
]


# HHV-8 KS ARTICLE

# Article: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8616388/
HVV8_KS_ABSTRACT = """
The epidemiology of Kaposi's sarcoma (KS) amongst North American and Northern European patients
with AIDS suggests that an infectious agent other than HIV is involved in its pathogenesis.
Several lines of evidence indicate that human herpesvirus 8 (HHV-8),
also termed Kaposi's sarcoma associated herpesvirus, is the sought after agent.
DNA of HHV-8 is invariably found in all forms of KS where the virus is present
 in the KS spindle cell.
 In contrast, HHV-8 DNA is not regularly detected in most other malignancies.
Antibodies against HHV-8 are more frequently found in groups at risk of KS,
and HHV-8 seroconversion precedes KS development.
Several HHV-8 genes have been identified that exhibit transforming potential
 in cell culture systems. In addition, the virus encodes and induces several cytokines
  and angiogenic factors. This is of particular interest as models of KS pathogenesis developed
   before the discovery of HHV-8 emphasized the importance of inflammatory cytokines.
   Although the expression pattern of viral genes in KS is not certain yet,
   it appears likely that the pathogenetic role of HHV-8 in KS may be rather complex and
   differs from other virus-induced malignancies. 1999 Academic Press.
"""

HVV8_KS_TOKENS_EXPECTED = [
    'The', 'epidemiology', 'of', 'Kaposi\'s', 'sarcoma', '(', 'KS', ')', 'amongst', 'North',
    'American', 'and', 'Northern', 'European', 'patients', 'with', 'AIDS', 'suggests', 'that',
    'an', 'infectious', 'agent', 'other', 'than', 'HIV', 'is', 'involved', 'in', 'its',
    'pathogenesis', '.', 'Several', 'lines', 'of', 'evidence', 'indicate', 'that', 'human',
    'herpesvirus', '8', '(', 'HHV-8', ')', ',', 'also', 'termed', 'Kaposi\'s', 'sarcoma',
    'associated', 'herpesvirus', ',', 'is', 'the', 'sought', 'after', 'agent', '.', 'DNA',
    'of', 'HHV-8', 'is', 'invariably', 'found', 'in', 'all', 'forms', 'of', 'KS', 'where',
    'the', 'virus', 'is', 'present', 'in', 'the', 'KS', 'spindle', 'cell', '.', 'In',
    'contrast', ',', 'HHV-8', 'DNA', 'is', 'not', 'regularly', 'detected', 'in', 'most',
    'other', 'malignancies', '.', 'Antibodies', 'against', 'HHV-8', 'are', 'more',
    'frequently', 'found', 'in', 'groups', 'at', 'risk', 'of', 'KS', ',', 'and', 'HHV-8',
    'seroconversion', 'precedes', 'KS', 'development', '.', 'Several', 'HHV-8', 'genes',
    'have', 'been', 'identified', 'that', 'exhibit', 'transforming', 'potential', 'in',
    'cell', 'culture', 'systems', '.', 'In', 'addition', ',', 'the', 'virus', 'encodes',
    'and', 'induces', 'several', 'cytokines', 'and', 'angiogenic', 'factors', '.', 'This',
    'is', 'of', 'particular', 'interest', 'as', 'models', 'of', 'KS', 'pathogenesis',
    'developed', 'before', 'the', 'discovery', 'of', 'HHV-8', 'emphasized', 'the',
    'importance', 'of', 'inflammatory', 'cytokines', '.', 'Although', 'the', 'expression',
    'pattern', 'of', 'viral', 'genes', 'in', 'KS', 'is', 'not', 'certain', 'yet', ',', 'it',
    'appears', 'likely', 'that', 'the', 'pathogenetic', 'role', 'of', 'HHV-8', 'in', 'KS',
    'may', 'be', 'rather', 'complex', 'and', 'differs', 'from', 'other', 'virus-induced',
    'malignancies', '.', '1999', 'Academic', 'Press', '.'
]

HVV8_KS_PHRASES_EXPECTED = [
    'epidemiology', 'Kaposi\'s sarcoma', 'KS', 'North American', 'Northern European patients',
    'AIDS', 'infectious agent', 'HIV', 'involved', 'pathogenesis', 'lines',
    'evidence indicate', 'human herpesvirus 8', 'HHV-8',
    'termed Kaposi\'s sarcoma associated herpesvirus', 'sought', 'agent', 'DNA', 'HHV-8',
    'invariably found', 'forms', 'KS', 'virus', 'present', 'KS spindle cell', 'contrast',
    'HHV-8 DNA', 'not regularly detected', 'malignancies', 'Antibodies', 'HHV-8',
    'frequently found', 'groups', 'risk', 'KS', 'HHV-8 seroconversion', 'KS development',
    'HHV-8 genes', 'identified', 'exhibit transforming potential', 'cell culture systems',
    'addition', 'virus encodes', 'induces', 'cytokines', 'angiogenic factors',
    'particular interest', 'models', 'KS pathogenesis developed', 'discovery',
    'HHV-8 emphasized', 'importance', 'inflammatory cytokines', 'expression pattern',
    'viral genes', 'KS', 'not certain', 'appears', 'pathogenetic role', 'HHV-8', 'KS',
    'complex', 'differs', 'virus-induced malignancies', '1999 Academic Press'
]

HVV8_KS_COOCCURRENCE_EXPECTED = {
    '1999': {'1999': 1, 'academic': 1, 'press': 1},
    '8': {'8': 1, 'herpesvirus': 1, 'human': 1},
    'academic': {'1999': 1, 'academic': 1, 'press': 1},
    'addition': {'addition': 1},
    'agent': {'agent': 2, 'infectious': 1},
    'aids': {'aids': 1},
    'american': {'american': 1, 'north': 1},
    'angiogenic': {'angiogenic': 1, 'factors': 1},
    'antibodies': {'antibodies': 1},
    'appears': {'appears': 1},
    'associated': {
        'associated': 1,
        'herpesvirus': 1,
        'kaposi\'s': 1,
        'sarcoma': 1,
        'termed': 1
    },
    'cell': {'cell': 2, 'culture': 1, 'ks': 1, 'spindle': 1, 'systems': 1},
    'certain': {'certain': 1, 'not': 1},
    'complex': {'complex': 1},
    'contrast': {'contrast': 1},
    'culture': {'cell': 1, 'culture': 1, 'systems': 1},
    'cytokines': {'cytokines': 2, 'inflammatory': 1},
    'detected': {'detected': 1, 'not': 1, 'regularly': 1},
    'developed': {'developed': 1, 'ks': 1, 'pathogenesis': 1},
    'development': {
        'development': 1,
        'ks': 1,
    },
    'differs': {'differs': 1},
    'discovery': {'discovery': 1},
    'dna': {'dna': 2, 'hhv-8': 1},
    'emphasized': {'emphasized': 1, 'hhv-8': 1},
    'encodes': {'encodes': 1, 'virus': 1},
    'epidemiology': {'epidemiology': 1},
    'european': {'european': 1, 'northern': 1, 'patients': 1},
    'evidence': {'evidence': 1, 'indicate': 1},
    'exhibit': {'exhibit': 1, 'potential': 1, 'transforming': 1},
    'expression': {'expression': 1, 'pattern': 1},
    'factors': {'angiogenic': 1, 'factors': 1},
    'forms': {'forms': 1},
    'found': {'found': 2, 'frequently': 1, 'invariably': 1},
    'frequently': {'found': 1, 'frequently': 1},
    'genes': {'genes': 2, 'hhv-8': 1, 'viral': 1},
    'groups': {'groups': 1},
    'herpesvirus': {
        '8': 1,
        'associated': 1,
        'herpesvirus': 2,
        'human': 1,
        'kaposi\'s': 1,
        'sarcoma': 1,
        'termed': 1
    },
    'hhv-8': {
        'dna': 1,
        'emphasized': 1,
        'genes': 1,
        'hhv-8': 8,
        'seroconversion': 1
    },
    'hiv': {'hiv': 1},
    'human': {'8': 1, 'herpesvirus': 1, 'human': 1},
    'identified': {'identified': 1},
    'importance': {'importance': 1},
    'indicate': {'evidence': 1, 'indicate': 1},
    'induces': {'induces': 1},
    'infectious': {'agent': 1, 'infectious': 1},
    'inflammatory': {'cytokines': 1, 'inflammatory': 1},
    'interest': {'interest': 1, 'particular': 1},
    'invariably': {'found': 1, 'invariably': 1},
    'involved': {'involved': 1},
    'kaposi\'s': {
        'associated': 1,
        'herpesvirus': 1,
        'kaposi\'s': 2,
        'sarcoma': 2,
        'termed': 1
    },
    'ks': {
        'cell': 1,
        'developed': 1,
        'development': 1,
        'ks': 8,
        'pathogenesis': 1,
        'spindle': 1
    },
    'lines': {'lines': 1},
    'malignancies': {'malignancies': 2, 'virus-induced': 1},
    'models': {'models': 1},
    'north': {'american': 1, 'north': 1},
    'northern': {'european': 1, 'northern': 1, 'patients': 1},
    'not': {'certain': 1, 'detected': 1, 'not': 2, 'regularly': 1},
    'particular': {'interest': 1, 'particular': 1},
    'pathogenesis': {'developed': 1, 'ks': 1, 'pathogenesis': 2},
    'pathogenetic': {'pathogenetic': 1, 'role': 1},
    'patients': {'european': 1, 'northern': 1, 'patients': 1},
    'pattern': {'expression': 1, 'pattern': 1},
    'potential': {'exhibit': 1, 'potential': 1, 'transforming': 1},
    'present': {'present': 1},
    'press': {'1999': 1, 'academic': 1, 'press': 1},
    'regularly': {'detected': 1, 'not': 1, 'regularly': 1},
    'risk': {'risk': 1},
    'role': {'pathogenetic': 1, 'role': 1},
    'sarcoma': {
        'associated': 1,
        'herpesvirus': 1,
        'kaposi\'s': 2,
        'sarcoma': 2,
        'termed': 1
    },
    'seroconversion': {
        'hhv-8': 1,
        'seroconversion': 1
    },
    'sought': {'sought': 1},
    'spindle': {'cell': 1, 'ks': 1, 'spindle': 1},
    'systems': {'cell': 1, 'culture': 1, 'systems': 1},
    'termed': {
        'associated': 1,
        'herpesvirus': 1,
        'kaposi\'s': 1,
        'sarcoma': 1,
        'termed': 1
    },
    'transforming': {'exhibit': 1, 'potential': 1, 'transforming': 1},
    'viral': {'genes': 1, 'viral': 1},
    'virus': {'encodes': 1, 'virus': 2},
    'virus-induced': {'malignancies': 1, 'virus-induced': 1}
}

HVV8_KS_DEGREES_EXPECTED = {
    'epidemiology': 1, 'kaposi\'s': 7, 'sarcoma': 7, 'ks': 13, 'north': 2, 'american': 2,
    'northern': 3, 'european': 3, 'patients': 3, 'aids': 1, 'infectious': 2, 'agent': 3, 'hiv': 1,
    'involved': 1, 'pathogenesis': 4, 'lines': 1, 'evidence': 2, 'indicate': 2, 'human': 3,
    'herpesvirus': 8, '8': 3, 'hhv-8': 12, 'termed': 5, 'associated': 5, 'sought': 1, 'dna': 3,
    'invariably': 2, 'found': 4, 'forms': 1, 'virus': 3, 'present': 1, 'spindle': 3, 'cell': 6,
    'contrast': 1, 'not': 5, 'regularly': 3, 'detected': 3, 'malignancies': 3, 'antibodies': 1,
    'frequently': 2, 'groups': 1, 'risk': 1, 'seroconversion': 2, 'development': 2,
    'genes': 4, 'identified': 1, 'exhibit': 3, 'transforming': 3, 'potential': 3, 'culture': 3,
    'systems': 3, 'addition': 1, 'encodes': 2, 'induces': 1, 'cytokines': 3, 'angiogenic': 2,
    'factors': 2, 'particular': 2, 'interest': 2, 'models': 1, 'developed': 3, 'discovery': 1,
    'emphasized': 2, 'importance': 1, 'inflammatory': 2, 'expression': 2, 'pattern': 2, 'viral': 2,
    'certain': 2, 'appears': 1, 'pathogenetic': 2, 'role': 2, 'complex': 1, 'differs': 1,
    'virus-induced': 2, '1999': 3, 'academic': 3, 'press': 3
}

HVV8_KS_FREQUENCIES_EXPECTED = {
    'epidemiology': 1, 'kaposi\'s': 2, 'sarcoma': 2, 'ks': 8, 'north': 1, 'american': 1,
    'northern': 1, 'european': 1, 'patients': 1, 'aids': 1, 'infectious': 1, 'agent': 2, 'hiv': 1,
    'involved': 1, 'pathogenesis': 2, 'lines': 1, 'evidence': 1, 'indicate': 1, 'human': 1,
    'herpesvirus': 2, '8': 1, 'hhv-8': 8, 'termed': 1, 'associated': 1, 'sought': 1, 'dna': 2,
    'invariably': 1, 'found': 2, 'forms': 1, 'virus': 2, 'present': 1, 'spindle': 1, 'cell': 2,
    'contrast': 1, 'not': 2, 'regularly': 1, 'detected': 1, 'malignancies': 2, 'antibodies': 1,
    'frequently': 1, 'groups': 1, 'risk': 1, 'seroconversion': 1, 'development': 1,
    'genes': 2, 'identified': 1, 'exhibit': 1, 'transforming': 1, 'potential': 1, 'culture': 1,
    'systems': 1, 'addition': 1, 'encodes': 1, 'induces': 1, 'cytokines': 2, 'angiogenic': 1,
    'factors': 1, 'particular': 1, 'interest': 1, 'models': 1, 'developed': 1, 'discovery': 1,
    'emphasized': 1, 'importance': 1, 'inflammatory': 1, 'expression': 1, 'pattern': 1,
    'viral': 1, 'certain': 1, 'appears': 1, 'pathogenetic': 1, 'role': 1, 'complex': 1,
    'differs': 1, 'virus-induced': 1, '1999': 1, 'academic': 1, 'press': 1
}


HVV8_KS_RANKED_EXPECTED = [
    ('termed kaposi\'s sarcoma associated herpesvirus', 21.0), ('human herpesvirus 8', 10.0),
    ('1999 academic press', 9.0), ('cell culture systems', 9.0),
    ('exhibit transforming potential', 9.0), ('northern european patients', 9.0),
    ('not regularly detected', 8.5), ('ks spindle cell', 7.62), ('kaposi\'s sarcoma', 7.0),
    ('ks pathogenesis developed', 6.62), ('not certain', 4.5), ('angiogenic factors', 4.0),
    ('evidence indicate', 4.0), ('expression pattern', 4.0), ('frequently found', 4.0),
    ('invariably found', 4.0), ('north american', 4.0), ('particular interest', 4.0),
    ('pathogenetic role', 4.0), ('viral genes', 4.0), ('ks development', 3.62),
    ('hhv-8 emphasized', 3.5), ('hhv-8 genes', 3.5), ('hhv-8 seroconversion', 3.5),
    ('infectious agent', 3.5), ('inflammatory cytokines', 3.5), ('virus encodes', 3.5),
    ('virus-induced malignancies', 3.5), ('hhv-8 dna', 3.0), ('pathogenesis', 2.0), ('ks', 1.62),
    ('agent', 1.5), ('cytokines', 1.5), ('dna', 1.5), ('hhv-8', 1.5), ('malignancies', 1.5),
    ('virus', 1.5), ('addition', 1.0), ('aids', 1.0), ('antibodies', 1.0), ('appears', 1.0),
    ('complex', 1.0), ('contrast', 1.0), ('differs', 1.0), ('discovery', 1.0),
    ('epidemiology', 1.0), ('forms', 1.0), ('groups', 1.0), ('hiv', 1.0), ('identified', 1.0),
    ('importance', 1.0), ('induces', 1.0), ('involved', 1.0), ('lines', 1.0), ('models', 1.0),
    ('present', 1.0), ('risk', 1.0), ('sought', 1.0)
]
