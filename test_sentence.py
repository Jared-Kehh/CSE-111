from sentence import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["A", "One", "The"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["Some", "Many", "The"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    single_noun_words = ["boy", "phone", "child"]

    for i in range(4):

        word_noun = get_noun(1)

        assert word_noun in single_noun_words
    
    plural_noun_words = ["men", "dragons", "hens"]

    for i in range(4):

        word_noun = get_noun(2)

        assert word_noun in plural_noun_words

def test_get_verb():

    more_verb_words = ["sings", "dances", "flies"]

    for i in range(4):

        word_verb = get_verb(1, "present")
        
        assert word_verb in more_verb_words

    single_verb_words = ["jump", "run", "walk", "tackle"]

    for i in range(4):

        word_verb = get_verb(2, "present")
        
        assert word_verb in single_verb_words
    
    future_verb_words = ["will sing", "will run", "will jump"]

    for i in range(4):

        word_verb = get_verb(2, "future")

        assert word_verb in future_verb_words
    
def test_get_preposition():
    preposition_words = ["over", "behind", "around", "in"]

    word_preposition = get_preposition()

    assert word_preposition in preposition_words


def test_get_prepositional_phrase():
    single_prepositional_phrase = ["the car", "one child", "a computer"]

    for i in range(4):
        word_prepositional_phrase = get_prepositional_phrase(1)

        assert word_prepositional_phrase in single_prepositional_phrase
    
    many_prepositional_phrase = ["many kids", "several cats", "some tables"]

    for i in range(4):
        word_prepositional_phrase = get_prepositional_phrase(2)
        
        assert word_prepositional_phrase in many_prepositional_phrase

def test_get_adjective():
    adjective = ["pretty", "ugly", "excited", "happy"]

    word_adjective = get_adjective()

    assert word_adjective in adjective

def test_get_adverb():
    adverb = ["loudly", "quitely", "happily", "quickly"]

    word_adverb = get_adverb()

    assert word_adverb in adverb


pytest.main(["-v", "--tb=line", "-rN", __file__])