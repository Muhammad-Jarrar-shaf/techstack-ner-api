from app.services.inference import extract_entities

text = """
Apple hired John Smith in California for a role paying $120,000.
"""

entities = extract_entities(text)

for entity in entities:
    print(entity)