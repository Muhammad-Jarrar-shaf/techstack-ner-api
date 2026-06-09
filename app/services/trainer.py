import json
import random
import spacy

from spacy.training.example import Example


def train_ner(
    data_path="data/processed/annotations.json",
    output_dir="models/tech_ner",
    iterations=30,
):
    with open(data_path, "r") as f:
        training_data = json.load(f)

    nlp = spacy.blank("en")

    ner = nlp.add_pipe("ner")

    labels = set()

    for example in training_data:
        for start, end, label in example["entities"]:
            labels.add(label)

    for label in labels:
        ner.add_label(label)

    nlp.initialize()

    for iteration in range(iterations):

        random.shuffle(training_data)

        losses = {}

        examples = []

        for item in training_data:

            doc = nlp.make_doc(item["text"])

            annotations = {
                "entities": item["entities"]
            }

            example = Example.from_dict(
                doc,
                annotations,
            )

            examples.append(example)

        nlp.update(
            examples,
            losses=losses,
        )

        print(
            f"Iteration {iteration + 1}/{iterations}",
            losses,
        )

    nlp.to_disk(output_dir)

    print(f"\nModel saved to {output_dir}")