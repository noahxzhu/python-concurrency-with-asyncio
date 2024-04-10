import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)
    return "Hello World!"


async def main() -> None:
    message = await hello_world_message()
    print(message)


async def delay(delay_seconds: int) -> int:
    print(f"sleeping for {delay_seconds} second(s)")
    await asyncio.sleep(delay_seconds)
    print(f"finished sleeping for {delay_seconds} second(s)")
    return delay_seconds


asyncio.run(main())
