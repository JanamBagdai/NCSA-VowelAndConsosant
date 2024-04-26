import unittest
from main import VowelReplacement

class TestVowelReplacement(unittest.TestCase):

    def test_replace_vowels_and_count_consonants(self):
        input_string1 = "National Center for Supercomputing Applications"
        result1, count1 = VowelReplacement.replace_vowels_and_count_consonants(input_string1)
        self.assertEqual(result1, "N1t915n1l C5nt5r f15r S21p5rc15mp21t9ng 1ppl9c1t915ns")
        self.assertEqual(count1, 26)

        input_string2 = "aeiou"
        result2, count2 = VowelReplacement.replace_vowels_and_count_consonants(input_string2)
        self.assertEqual(result2, "1591521")
        self.assertEqual(count2, 0)

        input_string3 = "a e i o u"
        result3, count3 = VowelReplacement.replace_vowels_and_count_consonants(input_string3)
        self.assertEqual(result3, "1 5 9 15 21")
        self.assertEqual(count3, 0)

        input_string4 = ""
        result4, count4 = VowelReplacement.replace_vowels_and_count_consonants(input_string4)
        self.assertEqual(result4, "")
        self.assertEqual(count4, 0)
        
        input_string4 = "I am a human"
        result4, count4 = VowelReplacement.replace_vowels_and_count_consonants(input_string4)
        self.assertEqual(result4, "9 1m 1 h21m1n")
        self.assertEqual(count4, 4)
        

    def test_is_vowel(self):
        self.assertTrue(VowelReplacement.is_vowel('a'))
        self.assertTrue(VowelReplacement.is_vowel('e'))
        self.assertTrue(VowelReplacement.is_vowel('i'))
        self.assertTrue(VowelReplacement.is_vowel('o'))
        self.assertTrue(VowelReplacement.is_vowel('u'))
        self.assertTrue(VowelReplacement.is_vowel('A'))
        self.assertTrue(VowelReplacement.is_vowel('E'))
        self.assertTrue(VowelReplacement.is_vowel('I'))
        self.assertTrue(VowelReplacement.is_vowel('O'))
        self.assertTrue(VowelReplacement.is_vowel('U'))

        self.assertFalse(VowelReplacement.is_vowel('b'))
        self.assertFalse(VowelReplacement.is_vowel('z'))
        self.assertFalse(VowelReplacement.is_vowel('B'))
        self.assertFalse(VowelReplacement.is_vowel('Z'))

    def test_is_consonant(self):
        self.assertTrue(VowelReplacement.is_consonant('b'))
        self.assertTrue(VowelReplacement.is_consonant('z'))
        self.assertTrue(VowelReplacement.is_consonant('B'))
        self.assertTrue(VowelReplacement.is_consonant('Z'))

        self.assertFalse(VowelReplacement.is_consonant('a'))
        self.assertFalse(VowelReplacement.is_consonant('e'))
        self.assertFalse(VowelReplacement.is_consonant('i'))
        self.assertFalse(VowelReplacement.is_consonant('o'))
        self.assertFalse(VowelReplacement.is_consonant('u'))
        self.assertFalse(VowelReplacement.is_consonant('A'))
        self.assertFalse(VowelReplacement.is_consonant('E'))
        self.assertFalse(VowelReplacement.is_consonant('I'))
        self.assertFalse(VowelReplacement.is_consonant('O'))
        self.assertFalse(VowelReplacement.is_consonant('U'))