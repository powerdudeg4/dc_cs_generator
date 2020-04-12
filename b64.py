import base64

message = input ("what do you want to encode into b64 to look edgy as fuck on your discord profile\n")

message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')


print(base64_message)


import pyperclip
pyperclip.copy(base64_message)
pyperclip.paste()
print('Your message has been copied to your clipboard.')


