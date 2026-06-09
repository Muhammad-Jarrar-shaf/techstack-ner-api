from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_prediction():
    payload = {
        "text": (
            "Built APIs using FastAPI "
            "and Docker."
        )
    }

    response = client.post(
        "/predict",
        json=payload,
    )

    assert response.status_code == 200

    entities = response.json()["entities"]

    labels = {
        entity["label"]
        for entity in entities
    }

    assert "FRAMEWORK" in labels
    assert "DEVOPS_TOOL" in labels