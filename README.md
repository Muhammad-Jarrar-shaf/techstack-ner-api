# TechStack NER API

A custom Named Entity Recognition (NER) system built with **spaCy** and **FastAPI** for extracting technology-related entities from unstructured text.

This project was developed as **Day 5 of my #100ProjectsIn100Days challenge**, with the goal of gaining hands-on experience in Natural Language Processing (NLP), machine learning workflows, and API development.

## Features

* Extract technology-related entities from text
* Train a custom NER model using spaCy
* Generate domain-specific training data
* Serve predictions through a FastAPI application
* Interactive API documentation with Swagger UI
* Automated API testing using pytest
* Professional Python project structure

## Supported Entities

| Entity Type          | Examples                      |
| -------------------- | ----------------------------- |
| PROGRAMMING_LANGUAGE | Python, Java, Go              |
| FRAMEWORK            | FastAPI, Django, Flask, React |
| DATABASE             | PostgreSQL, MongoDB, MySQL    |
| CLOUD_PLATFORM       | AWS, Azure, GCP               |
| DEVOPS_TOOL          | Docker, Kubernetes, Jenkins   |

## Project Architecture

Technology Taxonomy
↓
Synthetic Dataset Generator
↓
Annotated Training Dataset
↓
spaCy Custom NER Training Pipeline
↓
Serialized Tech Stack NER Model
↓
Inference Layer
↓
FastAPI API
↓
Swagger Documentation & Automated Tests

## Project Structure

```text
techstack-ner-api/
├── app/
│   ├── api/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── data/
├── models/
├── scripts/
├── screenshots/
├── tests/
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/techstack-ner-api.git
cd techstack-ner-api
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

## Example Request

```json
{
    "text": "Built APIs using FastAPI and Docker on AWS with PostgreSQL."
}
```

## Example Response

```json
{
    "entities": [
        {
            "text": "FastAPI",
            "label": "FRAMEWORK"
        },
        {
            "text": "Docker",
            "label": "DEVOPS_TOOL"
        },
        {
            "text": "AWS",
            "label": "CLOUD_PLATFORM"
        },
        {
            "text": "PostgreSQL",
            "label": "DATABASE"
        }
    ]
}
```

## Running Tests

```bash
pytest
```

## Key Learnings

* Named Entity Recognition (NER)
* Sequence labeling concepts
* Character-level annotations
* Custom spaCy model training
* FastAPI application development
* Automated API testing
* Professional Git workflows

## Future Improvements

* Replace synthetic data with human-annotated datasets
* Add evaluation metrics such as Precision, Recall, and F1-score
* Containerize the application using Docker
* Deploy the API to a cloud platform
* Expand entity categories and dataset diversity

## Technologies Used

* Python
* spaCy
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* Git

## License

This project is licensed under the MIT License.
