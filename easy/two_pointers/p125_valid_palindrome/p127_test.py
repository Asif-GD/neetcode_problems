import re

text = "Python 3.7: Easy & Effective!"
clean_text_1 = ''.join(char for char in text if char.isalnum())
print(clean_text_1)

clean_text_2 = re.sub(r"[^a-zA-Z0-9]", "", string=text)
print(clean_text_2)
