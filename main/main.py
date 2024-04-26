class VowelReplacement:
    @staticmethod
    def main():
        input_string = "National Center for Supercomputing Applications"
        replaced_string, count = VowelReplacement.replace_vowels_and_count_consonants(input_string)
        print("Input string:", input_string)
        print("Resulting string:", replaced_string)
        print("Total number of consonants:", count)

    @staticmethod
    def replace_vowels_and_count_consonants(input_string):
        count = 0
        result = []

        for c in input_string:
            if VowelReplacement.is_vowel(c):
                lowercase_c = c.lower()
                result.append(str(ord(lowercase_c) - ord('a') + 1))
            else:
                if VowelReplacement.is_consonant(c):
                    count += 1
                result.append(c)

        return ''.join(result), count

    @staticmethod
    def is_vowel(c):
        vowels = "aeiouAEIOU"
        return c in vowels

    @staticmethod
    def is_consonant(c):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return c in consonants

if __name__ == '__main__':
    VowelReplacement.main()