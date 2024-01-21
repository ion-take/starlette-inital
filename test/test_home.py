from starlette.status import HTTP_200_OK

import pytest

@pytest.mark.asyncio
async def test_home(client):
   resp = await client.get('/')
   assert resp.status_code == HTTP_200_OK
