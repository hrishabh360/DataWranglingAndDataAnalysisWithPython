
# message = "please help"

# # `morse` is a list which will eventually contain the 
# # strings for each morse code letter in the message.
# morse = []

# for letter in message:
#     morse_letter = letter_to_morse[letter]
#     morse.append(morse_letter)

# # We need to join together Morse code letters with spaces
# morse_message = " ".join(morse)

# print(f"Incoming message: {message}")
# print(f"   Morse encoded: {morse_message}")


#############################################
import morse 

mes_text = "hello"    
morse_com = morse.encode(mes_text)
print(f"The morse code for {mes_text} is: {morse_com}.")

#############################################


