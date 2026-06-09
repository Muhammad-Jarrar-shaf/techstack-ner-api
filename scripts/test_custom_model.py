from app.services.custom_inference import predict

examples = [
    "I built REST APIs using FastAPI and PostgreSQL.",
    "The system was deployed on AWS using Docker.",
    "The team developed the backend in Python using Flask.",
    "We migrated MongoDB databases to Azure.",
]

for sentence in examples:
    print("\nText:")
    print(sentence)

    print("\nEntities:")

    predictions = predict(sentence)

    for entity in predictions:
        print(entity)

    print("-" * 50)