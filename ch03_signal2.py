import asyncio
import signal


async def await_all_tasks():
    tasks = asyncio.all_tasks()
    [await task for task in tasks]


async def main():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(
        signal.SIGINT, lambda: asyncio.create_task(await_all_tasks())
    )


asyncio.run(main())
