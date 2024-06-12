import aiohttp

from fastapi.encoders import jsonable_encoder


from fastapi.responses import JSONResponse


async def make_request(url, headers, method, body):
    json_compatible_body = jsonable_encoder(body)
    async with aiohttp.ClientSession() as session:
        try:
            async with session.request(
                method,
                url,
                json=json_compatible_body,
            ) as response:
                json_body = await response.json()
                json_response = JSONResponse(
                    content=json_body, status_code=response.status
                )
                return json_response
        except Exception:
            # Add a custom error message
            pass
