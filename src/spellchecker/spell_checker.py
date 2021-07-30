import re
from string import ascii_lowercase
from typing import List, Set, Union


def fetch_words(read_mode: str) -> List[str]:
    """
    Returns the list of words contained in words.txt and BOOKS.txt.

            Parameters:
                    read_mode (str): read mode for the files.

            Returns:
                    (List): List that contains all the words in the files.
    """
    try:
        words_from_dictionary = [word.strip() for word in
                                 open('words.txt', read_mode, encoding="utf-8").readlines()]
        words_from_books = re.findall(r'\w+', open('BOOKS.txt', read_mode, encoding="utf-8").read())
        return words_from_dictionary + words_from_books
    except Exception as e:
        print(f"An error has occurred while reading the files: {e}")


WORDS = fetch_words('r')
ACCENTS_MAP = {"a": "á", "e": "é", "i": "í", "o": "ó", "u": "ú"}
VOWELS = {"a", "e", "i", "o", "u"}
LETTERS = list(ascii_lowercase) + list(ACCENTS_MAP.values()) + ['ñ', 'ü']

WORDS_INDEX = {}

"""
Create a dictionary that counts the occurrences of each word.
"""
for word in WORDS:
    if word not in WORDS_INDEX:
        WORDS_INDEX[word] = 1
    else:
        WORDS_INDEX[word] += 1


def possible_corrections(word: str) -> Union[set, str]:
    """
    This function finds the possible corrections for a word. It checks
    max 2 edits away for a word. If a word max 2 edits away is not found, it
    returns the word given as a parameter.

            Parameters:
                    word (str): The word to check the possible corrections.

            Returns:
                    (Union[set, str]): Set that contains all the possible corrections or
                    the words given as a parameter
    """
    single_word_possible_corrections = filter_real_words([word])
    one_length_edit_possible_corrections = filter_real_words(one_length_edit(word))
    two_length_edit_possible_corrections = filter_real_words(two_length_edit(word))
    no_correction_at_all = word

    if single_word_possible_corrections:
        return single_word_possible_corrections

    elif one_length_edit_possible_corrections:
        return one_length_edit_possible_corrections

    elif two_length_edit_possible_corrections:
        return two_length_edit_possible_corrections

    else:
        return no_correction_at_all


def spell_check_sentence(sentence: str) -> str:
    """
    This function returns the sentence given as a parameter with all the words corrected
    using the words list. First, it splits the sentence into word and strips it. Then,
    for each word, it calculates the possible correction with the max probability of occurrence.

            Parameters:
                    sentence (str): The sentence to be corrected.

            Returns:
                    (str): The sentence corrected
    """
    words_with_punctuation = {}
    words_with_uppercase = {}
    split_sentence = sentence.split()
    correct_uppercase_letter_flag = False
    stripped_sentence = []
    for i in range(len(split_sentence)):
        stripped_word = split_sentence[i].strip()
        last_character = stripped_word[-1]
        first_character_upper = stripped_word[0].isupper()
        if first_character_upper and i == 0:
            words_with_uppercase[i] = True
        elif first_character_upper and not correct_uppercase_letter_flag:
            words_with_uppercase[i] = False
        elif first_character_upper and correct_uppercase_letter_flag:
            words_with_uppercase[i] = True
        if not last_character.isalnum():
            if last_character == ".":
                correct_uppercase_letter_flag = True
            words_with_punctuation[i] = last_character
            stripped_sentence.append(stripped_word[:-1].lower())
        else:
            correct_uppercase_letter_flag = False
            stripped_sentence.append(stripped_word.lower())

    checked = map(spell_check_word, stripped_sentence)
    checked_with_punctuation_and_uppers = []
    index = 0
    for word in checked:
        formatted_word = word
        if words_with_uppercase.get(index):
            formatted_word = word[0].upper() + word[1:]
        checked_with_punctuation_and_uppers.append(formatted_word + words_with_punctuation.get(index, ''))
        index += 1
    return ' '.join(checked_with_punctuation_and_uppers)


def spell_check_word(word: str) -> str:
    """
    This function returns the word with max probability of occurrence from the corrections
    of the word given as a parameter.

            Parameters:
                    word (str): The word to get word with max probability of occurrence.

            Returns:
                    (str): The word with max probability of occurrence
    """
    possible_word_corrections = possible_corrections(word)
    words_equivalent_with_accent = [possible_correction for possible_correction in possible_word_corrections
                                    if equivalent_with_accents(word, possible_correction)]
    if words_equivalent_with_accent:
        return words_equivalent_with_accent[0]
    return max(possible_word_corrections, key=language_model)


def equivalent_with_accents(word: str, word_with_accents: str) -> bool:
    """
    This function returns true if the word given as a parameter is equal to the word with accents given as
    a parameter. Comparing each letter, if the letter is a vowel, it compares if the vowel with accents of
    the word with accents is the same to the vowel without the accent.

            Parameters:
                    word (str): The word without accents.
                    word_with_accents (str): The word with accents.
            Returns:
                    (str): TTrue if the words are equal without accents.
    """
    if len(word) == len(word_with_accents):
        for i in range(len(word)):
            if word[i] not in VOWELS and word[i] != word_with_accents[i]:
                return False
            elif word[i] in VOWELS and word[i] != word_with_accents[i]:
                if ACCENTS_MAP.get(word[i]) == word_with_accents[i]:
                    continue
                else:
                    return False
        return True
    return False


def language_model(word: str) -> float:
    """
    This function returns the probability of occurrence of a word.

            Parameters:
                    word (str): The word to calculate the occurrence.

            Returns:
                    (float): The probability of occurrence of the word
    """
    N = sum(WORDS_INDEX.values())
    return WORDS_INDEX.get(word, 0) / N


def filter_real_words(words: List[str]) -> Set[str]:
    """
    This function returns a list of words that are contained in the WORDS_INDEX.
    Comparing each word of the set given as a parameter to the words in the WORDS_INDEX.

            Parameters:
                    words (Set[str]): The words set.

            Returns:
                    (Set[str]): The set of words contained in the WORDS_INDEX
    """
    return set(word for word in words if word in WORDS_INDEX)


def one_length_edit(word: str) -> List[str]:
    """
    An edit can be one of the following: remove a character, add a character, change a character, swap 2 characters or
    replace a character.
    This function finds all the possible edits of length 1 of the word given as a parameter.
    First, it splits the word in 2 parts, adding 1 character of the right part to the left part incrementally.
    E.g, for the word hopinion it creates an array of sets of the form: [('', 'hopinion'), ('h', 'opinion'),
     ('ho', 'pinion'), ...]
    Secondly, using the array of sets created before, it calculates the possible words resulting by removing one letter
    of each set.
    Then, calculates the possible words resulting by swapping two contiguous letters.
    After this, calculates the possible words resulting by replacing each character of a word with each character in the
    spanish alphabet.
    Finally, it calculates th possible words resulting by adding a new character to that word.
            Parameters:
                    word (str): The words set.

            Returns:
                    (List[str]): The set of possible edits of the word.
    """
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    removals_of_one_letter = []

    for left, right in splits:
        if right:
            removals_of_one_letter.append(left + right[1:])
    two_letters_transposes = []

    for left, right in splits:
        if len(right) > 1:
            two_letters_transposes.append(left + right[1] + right[0] + right[2:])
    one_letter_replaces = []

    for left, right in splits:
        if right:
            for c in LETTERS:
                one_letter_replaces.append(left + c + right[1:])
    one_letter_insertions = []

    for left, right in splits:
        for c in LETTERS:
            one_letter_insertions.append(left + c + right)
    one_length_editions = removals_of_one_letter + two_letters_transposes + one_letter_replaces + one_letter_insertions

    return list(set(one_length_editions))


def two_length_edit(word: str) -> List[str]:
    """
    This function returns all the possible edits of length 2 of a word.

            Parameters:
                    word (str): The word to find the possible edits of length 2..

            Returns:
                    (List[str]): The set of possible edits of the word.
    """
    return [e2 for e1 in one_length_edit(word) for e2 in one_length_edit(e1)]


def test_spell_check_sentence():
    sentence = 'hopinion'
    print(spell_check_sentence(sentence))
    assert 'opinión' == spell_check_sentence(sentence)

    sentence = 'fabor guardar cilencio para no molestar'
    print(spell_check_sentence(sentence))
    assert 'favor guardar silencio para no molestar' == spell_check_sentence(sentence)

    sentence = 'un lgar para la hopinion'
    print(spell_check_sentence(sentence))
    assert 'un lugar para la opinión' == spell_check_sentence(sentence)

    sentence = 'el Arebol del día'
    print(spell_check_sentence(sentence))
    assert 'el arrebol del día' == spell_check_sentence(sentence)

    sentence = 'Rezpeto por la educasión'
    print(spell_check_sentence(sentence))
    assert 'Respeto por la educación' == spell_check_sentence(sentence)

    sentence = 'RTe encanta conduzir'
    print(spell_check_sentence(sentence))
    assert 'Te encanta conducir' == spell_check_sentence(sentence)

    sentence = 'HOy ay karne azada frezca siga pa dentro'
    print(spell_check_sentence(sentence))
    assert 'Hoy ay carne azada fresca siga la dentro' == spell_check_sentence(sentence)

    sentence = 'En mi ezcuela no enseñan a escrivir ni a ler'
    print(spell_check_sentence(sentence))
    assert 'En mi escuela no enseñan a escribir ni a le' == spell_check_sentence(sentence)

    sentence = 'él no era una persona de fiar pues era un mentirozo'
    print(spell_check_sentence(sentence))
    assert 'él no era una persona de fiar pues era un mentiroso' == spell_check_sentence(sentence)


def test_spell_check_sentence_2():
    sentence = 'Él, no era una persona de fiar. Pues era un mentirozo.'
    print(spell_check_sentence(sentence))
    assert 'Él, no era una persona de fiar. Pues era un mentiroso.' == spell_check_sentence(sentence)

    sentence = 'él, no era una persona de fiar pues era un mentirozo'
    print(spell_check_sentence(sentence))
    assert 'él, no era una persona de fiar pues era un mentiroso' == spell_check_sentence(sentence)

    sentence = 'No era una persona de fiar pues era un mentirozo'
    print(spell_check_sentence(sentence))
    assert 'No era una persona de fiar pues era un mentiroso' == spell_check_sentence(sentence)

    sentence = 'trabaja de dia'
    print(spell_check_sentence(sentence))
    assert 'trabaja de día' == spell_check_sentence(sentence)
