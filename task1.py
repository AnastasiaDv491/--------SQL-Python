import sqlite3


try:

    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect("client.sqlite")
    cursor = sqliteConnection.cursor()
    print("DB Init")

    # Write a query and execute it with cursor
    query = """INSERT INTO endpoints
    (id, name, active)
    VALUES
    (7,"Сварочный аппарат №1","true" )
    (8,"Пильный аппарат №2","true" )
    (9,"Фрезер №3","true" )

"""
    # “Сварочный аппарат №1”, “Пильный аппарат №2”, “Фрезер №3”,
    cursor.execute(query)

    # Fetch and output result
    # result = cursor.fetchall()
    # print(result)
    sqliteConnection.commit()

    print("Record inserted successfully into endpoints table ", cursor.rowcount)

    # Close the cursor
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print("Error occurred - ", error)

# Close DB Connection irrespective of success
# or failure
finally:

    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite Connection closed")
