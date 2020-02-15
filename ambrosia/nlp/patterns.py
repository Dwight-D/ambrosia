import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher
from spacy.cli.download import download as spacy_download



def setup_model(model):
    try:
        nlp = spacy.load(model)
    except OSError:
        print(f"Spacy model '{model}' not found.  Downloading and installing.")
        spacy_download(model)
        nlp = spacy.load(model)
    return nlp