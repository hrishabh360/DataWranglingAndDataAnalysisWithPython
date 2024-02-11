letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}


def encode(mes_text):
    text = []
    for i in mes_text:
        morse_letter = letter_to_morse[i]
        text.append(morse_letter)
    morse_combined = " ".join(text)
    return morse_combined
    

# We need to invert the dictionary. This will create a dictionary
# that can go from the morse back to the letter
morse_to_letter = {}
for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter

def decode(morse_message):
    text = []
    morse_list = morse_message.split(" ")
    
    for letter in morse_list:
        text.append(morse_to_letter[letter])
    text_combined = "".join(text)
    return text_combined
