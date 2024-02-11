from morse2 import EnglishMessage, MorseMessage

message_string = "hello world"
message = EnglishMessage(message_string)

code_string = message.encode()
code = MorseMessage(code_string)
decoded = code.decode()

print(decoded == message_string)
    