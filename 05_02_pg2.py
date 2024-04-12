import asyncio
from typing import List

import asyncpg
from asyncpg import Record


async def main():
    connection = await asyncpg.connect(
        host="10.1.2.51", port=5432, user="noah", database="products", password="vz1234"
    )

    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()


asyncio.run(main())
