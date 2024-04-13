import asyncio
from asyncio import AbstractEventLoop

from chapter_08.listing_8_1 import HTTPGetClientProtocol


async def make_request(host: str, port: int, loop: AbstractEventLoop) -> str:
    def protocal_factory():
        return HTTPGetClientProtocol(host, loop)

    _, protocal = await loop.create_connection(protocal_factory, host=host, port=port)

    return await protocal.get_response()


async def main():
    loop = asyncio.get_running_loop()
    result = await make_request("www.example.com", 80, loop)
    print(result)


asyncio.run(main())
