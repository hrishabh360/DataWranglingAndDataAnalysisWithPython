 #!/usr/bin/python
# -*- coding: utf-8 -*-


class EnglishMessage:

    def __init__(self, message):
        self.message = message
        self.letter_to_morse = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            ' ': '/',
            }

    def encode(self):
        try:
            text = []
            for i in self.message:
                morse_letter = self.letter_to_morse[i]
                text.append(morse_letter)
            morse_combined = ' '.join(text)
            return morse_combined
        except RuntimeError as e:
            raise RuntimeError(f"invalid. Can not encode {self.message}")


class MorseMessage:
    
    def __init__(self, message):
        self.message = message
        letter_to_morse = {
            'a': '.-',
            'b': '-...',
            'c': '-.-.',
            'd': '-..',
            'e': '.',
            'f': '..-.',
            'g': '--.',
            'h': '....',
            'i': '..',
            'j': '.---',
            'k': '-.-',
            'l': '.-..',
            'm': '--',
            'n': '-.',
            'o': '---',
            'p': '.--.',
            'q': '--.-',
            'r': '.-.',
            's': '...',
            't': '-',
            'u': '..-',
            'v': '...-',
            'w': '.--',
            'x': '-..-',
            'y': '-.--',
            'z': '--..',
            '0': '-----',
            '1': '.----',
            '2': '..---',
            '3': '...--',
            '4': '....-',
            '5': '.....',
            '6': '-....',
            '7': '--...',
            '8': '---..',
            '9': '----.',
            ' ': '/',
            }

        self.morse_to_letter = {}
        for letter in letter_to_morse:
            morse = letter_to_morse[letter]
            self.morse_to_letter[morse] = letter

    def decode(self):
        try:
            text = []
            morse_list = self.message.split(' ')
    
            for letter in morse_list:
                text.append(self.morse_to_letter[letter])
            text_combined = ''.join(text)
            return text_combined
        except RuntimeError as e:
            raise RuntimeError(f"invalid. Can not dencode {self.message}")