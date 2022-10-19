import unittest
from collections import defaultdict


class Anagrams:
    """A class whose instance is a dictionary containing strings and their anagrams
    """
    def __init__(self):
        self.dictionary = defaultdict(list)

    @classmethod
    def from_file(cls, words_file_path: str) -> object:
        """Create Anagrams object from a file containing words"""
        c = cls()
        with open(words_file_path, 'r') as f:
            words = f.read().split('\n')
        c.dictionary = cls.get_dictionary(words)
        return c

    @classmethod
    def from_list(cls, words: list) -> object:
        """Create Anagrams object from a list of strings"""
        c = cls()
        c.dictionary = cls.get_dictionary(words)
        return c

    @staticmethod
    def get_dictionary(words: list) -> dict:
        """Create anagram dictionary given list of strings.

         Dictionary keys are created from the unique character combinations in given list, and the values are those
         strings in the list which are anagrams of each combination.

         For example, given the list: ['abc', 'bac', 'cab', 'def'], the following dictionary is returned:
         {'abc': ['abc', 'bac', 'cab'], 'def': ['def']}

         :param list words: list of strings used to create anagram dictionary
         :return: dictionary of unique strings and their anagrams
         :rtype: dict

        """
        dictionary = defaultdict(list)
        for word in words:
            if type(word) != str:
                raise ValueError(
                    f'Incorrect type {type(word)} for element {word} in word list. Only strings are permitted.'
                )
            word = word.lower()
            key = "".join(sorted(word))
            dictionary[key].append(word)
            # if key in dictionary:
            #     dictionary[key].append(word)
            # else:
            #     dictionary[key] = [word]

        return dictionary

    def get_anagrams(self, word: str) -> list:
        """ Get list of anagrams for given word from anagrams dictionary. An empty list is returned if the word does
         not exist in the dictionary.

         :param str word: word to get anagrams of
         :return: list of anagrams of given word
         :rtype: list

        """
        word = "".join(sorted(word.lower()))
        if word in self.dictionary:
            return self.dictionary[word]
        else:
            return []


class TestAnagrams(unittest.TestCase):
    """ Test get_anagrams method of Anagrams class"""

    @classmethod
    def setUpClass(cls):
        super(TestAnagrams, cls).setUpClass()
        cls.anagrams = Anagrams.from_file('words.txt')

    def test_anagrams(self):
        """ Test get_anagrams correctly returns list of anagrams for given string"""
        self.assertEqual(
            self.anagrams.get_anagrams('dictionary'),
            ['dictionary', 'indicatory']
        )

    def test_no_anagrams(self):
        """ Test get_anagrams correctly returns empty list if given string does not exist in anagram dictionary"""
        self.assertEqual(
            self.anagrams.get_anagrams('123'),
            []
        )


class TestAnagramsStaticMethods(unittest.TestCase):
    """ Test static methods of Anagrams class"""
    def test_get_dictionary(self):
        """ Test get_dictionary correctly creates anagram dictionary"""
        words = ['abc', 'bac', 'cab', 'dfe']
        expected = {
            'abc': ['abc', 'bac', 'cab'],
            'def': ['dfe']
        }
        self.assertEqual(
            Anagrams.get_dictionary(words),
            expected
        )

    def test_get_dictionary_bad_input(self):
        words = ['345', 123]
        with self.assertRaisesRegex(ValueError, f"Incorrect type {type(words[1])} for element {words[1]}"):
            Anagrams.get_dictionary(words)


class TestAnagramClassMethods(unittest.TestCase):
    """ Test class methods for Anagrams class"""
    def test_from_list(self):
        """ Test from_list class method correctly creates Anagrams object"""
        words = ['abc', 'bac', 'cab']
        anagrams = Anagrams.from_list(words)

        self.assertIsInstance(anagrams, Anagrams)
        self.assertEqual(
            anagrams.dictionary,
            {'abc': words}
        )
