import pytest
pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize("endpoint", ["/docs", "/openapi.json"])
async def test_ancillary(client, endpoint):
    response = await client.get(endpoint)
    assert response.status_code == 200


# need to mock the grpc server
@pytest.mark.parametrize("payload, response_json", [({""})])
async def test_meter(client, payload, response_json):
    response = await client.post("/meter", json=payload)
    assert response.status_code == 200
    assert response.json() == response_json
