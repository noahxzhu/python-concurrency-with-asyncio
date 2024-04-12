import asyncio

import asyncpg
from asyncpg.transaction import Transaction


async def main():
    connection = await asyncpg.connect(
        host="10.1.2.51", port=5432, user="noah", database="products", password="vz1234"
    )

    transaction: Transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1)")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2)")
    except asyncpg.PostgresError:
        print("Errors, rolling back transaction!")
        await transaction.rollback()
    else:
        print("No errors, committing transaction!")
        await transaction.commit()

    query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


asyncio.run(main())
