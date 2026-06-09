from app.services.custom_inference import predict

examples = [
    "Our backend uses Django with PostgreSQL deployed on AWS.",
    "The DevOps team manages Kubernetes clusters.",
    "The data pipeline was written in Go.",
    "React applications communicate with FastAPI services.",
    "Jenkins automates Docker deployments."
]

for sentence in examples:
    print("\nText:")
    print(sentence)

    print("\nEntities:")

    predictions = predict(sentence)

    for entity in predictions:
        print(entity)

    print("-" * 50)