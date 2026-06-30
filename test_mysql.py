import pymysql # pyright: ignore[reportMissingModuleSource]

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="medisense_ai",
        port=3306,
    )

    print("✅ Connected successfully!")

    connection.close()

except Exception as e:
    print(e)