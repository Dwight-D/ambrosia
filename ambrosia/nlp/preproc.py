import re

def clean(text):
    print("cleaning")
    text = strip_repeat_newlines(text)
    return text

def strip_repeat_newlines(text):
    return re.sub(r'[\n ]*\n+[\n ]*', '\n', text)