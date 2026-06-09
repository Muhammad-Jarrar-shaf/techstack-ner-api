import json
import random

from data.raw.technologies import (
    LANGUAGES,
    FRAMEWORKS,
    DATABASES,
    CLOUDS,
    DEVOPS,
    NAMES,
)

templates = [
    "{name} built APIs using {framework} and {database}.",
    "{name} developed applications in {language} with {framework}.",
    "{name} deployed services on {cloud} using {devops}.",
    "{name} managed {database} databases using {language}.",
    "{name} containerized applications with {devops} and deployed to {cloud}.",
]


def create_annotation(text, entity, label):
    start = text.find(entity)
    end = start + len(entity)

    return (start, end, label)


dataset = []

for _ in range(100):
    template = random.choice(templates)

    values = {
        "name": random.choice(NAMES),
        "language": random.choice(LANGUAGES),
        "framework": random.choice(FRAMEWORKS),
        "database": random.choice(DATABASES),
        "cloud": random.choice(CLOUDS),
        "devops": random.choice(DEVOPS),
    }

    text = template.format(**values)

    entities = []

    for key, label in [
        ("language", "PROGRAMMING_LANGUAGE"),
        ("framework", "FRAMEWORK"),
        ("database", "DATABASE"),
        ("cloud", "CLOUD_PLATFORM"),
        ("devops", "DEVOPS_TOOL"),
    ]:
        value = values[key]

        if value in text:
            entities.append(create_annotation(text, value, label))

    dataset.append(
        {
            "text": text,
            "entities": entities,
        }
    )

with open("data/processed/annotations.json", "w") as f:
    json.dump(dataset, f, indent=4)

print(f"Generated {len(dataset)} examples.")