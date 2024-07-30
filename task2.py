import sqlite3


try:

    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect("client.sqlite")
    cursor = sqliteConnection.cursor()
    print("DB Init")

    # Write a query and execute it with cursor
    # Данное квери использовалось, чтобы внести изменения в таблицу endpoint_reasons
    # Параметры в SELECT и WHERE менялись, чтобы внести три новых станка.
    query = """insert into endpoint_reasons (endpoint_id, reason_name, reason_hierarchy)
select 
    8, 
    reason_name ,
    reason_hierarchy
from endpoint_reasons
where endpoint_id =5;

"""
    # “Сварочный аппарат №1”, “Пильный аппарат №2”, “Фрезер №3”,
    cursor.execute(query)

    # Fetch and output result
    # result = cursor.fetchall()
    # print(result)
    sqliteConnection.commit()

    print("Success ", cursor.rowcount)

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
