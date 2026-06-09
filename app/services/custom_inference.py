import spacy
from functools import lru_cache


@lru_cache
def get_model():
    return spacy.load("models/tech_ner")


def predict(text: str):
    doc = get_model()(text)

    entities = []

    for ent in doc.ents:
        entities.append(
            {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
            }
        )

    return entities