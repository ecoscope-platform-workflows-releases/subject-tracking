# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "c8d17ad4f61776c0ce922a6d115c0afca2531810a955140fff1f05d1d295e343"


from pathlib import Path

from fastapi.testclient import TestClient

from ecoscope_workflows_core.testing import TestCase


def test_app(
    client: TestClient,
    execution_mode: str,
    mock_io: bool,
    case: TestCase,
    tmp_path: Path,
):
    request = {"params": case.params}
    query_params = {
        "execution_mode": execution_mode,
        "mock_io": mock_io,
        "results_url": tmp_path.as_uri(),
    }
    headers = {"Content-Type": "application/json"}
    response = client.post(
        "/",
        json=request,
        params=query_params,
        headers=headers,
    )
    assert response.status_code == 200
