import nltk
import re

def on_each_line(text, callbacks):
    lines = text.splitlines()
    output = []
    for line in lines:
        for fn in callbacks:
            line = fn(line)
        if line:
            output.append(line + '\n')
    out_text = "".join(output)
    return out_text
    
def remove_specials(line):
    special_pattern = r'[^\w ;:.,\—\–\-!?\'\"&\(\)/\$\+]+'
    return re.sub(special_pattern, ' ', line.strip())

def strip_whitespace(line):
    whitespace_only = r'^\s*$'
    if re.match(whitespace_only, line):
        return None
    else:
        return line

def clean(text):
    cleaning_functions = [remove_specials, strip_whitespace]
    output = on_each_line(text, cleaning_functions)
    return output