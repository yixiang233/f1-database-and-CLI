import argparse
import psycopg2

# show menu
def show_menu():
    print("\nWelcome to the Formula 1 World Championship Driver Database!\n")
    print("Please select an option:")
    print("1. Add driver information")
    print("2. Delete driver information")
    print("3. Update driver information")
    print("4. Search driver information")
    print("5. Total number of drivers")
    print("6. List of drivers")
    print("7. Driver's points")
    print("8. Driver's nationality")
    print("9. Drivers with points of 90 or above")
    print("10. Delete all related data for a driver")
    print("11. Exit")

# handle user's choice
def handle_choice(choice):
    if choice == '1':
        insert_data()
    elif choice == '2':
        delete_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        search_data()
    elif choice == '5':
        aggregate_functions()
    elif choice == '6':
        sorting()
    elif choice == '7':
        joins()
    elif choice == '8':
        grouping()
    elif choice == '9':
        subqueries()
    elif choice == '10':
        transactions()
    elif choice == '11':
        print("Exit successfully.")
        exit()
    else:
        print("Invalid choice!")

# connect to database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to database:", e)

# close database connection
def close_connection(conn, cur=None):
    try:
        if cur:
            cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error closing database connection:", e)


# insert data
def insert_data():
    try:
        # connect to database
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # get database cursor
        cur = conn.cursor()
        
        # receive the user's input
        driverId = input("Enter driver id: ")
        driverRef = input("Enter reference name: ")
        forename = input("Enter first name: ")
        surname = input("Enter last name: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        nationality = input("Enter nationality: ")
        url = input("Enter Wikipedia URL: ")
        
        # execute insert operation
        cur.execute("INSERT INTO drivers (driverId, driverRef, forename, surname, dob, nationality, url) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (driverId, driverRef, forename, surname, dob, nationality, url))
        
        # commit transaction
        conn.commit()
        
        print("Data inserted successfully!")
        
    except psycopg2.Error as e:
        print("Error inserting data:", e)
        
    finally:
        # close curcor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# delete data
def delete_data():
    try:
        # connect to database
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # get database cursor
        cur = conn.cursor()
        
        # receive the user's input
        driverId = input("Enter driver ID to delete: ")
        
        # execute delete operation
        cur.execute("DELETE FROM drivers WHERE driverId = %s", (driverId,))
        
        # commit transaction
        conn.commit()
        
        print("Data deleted successfully!")
        
    except psycopg2.Error as e:
        print("Error deleting data:", e)
        
    finally:
        # close curcor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# update data
def update_data():
    try:
        # connect to database
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # get database cursor
        cur = conn.cursor()
        
        # receive user input
        driverId = input("Enter driver ID to update: ")
        attribute = input("Enter attribute to update (driverRef (reference name), forename (first name), surname (last name), dob (date of birth), nationality, url): ")
        new_value = input(f"Enter new value for {attribute}: ")
        
        # execute update operation
        cur.execute(f"UPDATE drivers SET {attribute} = %s WHERE driverId = %s", (new_value, driverId))
        
        # commit transaction
        conn.commit()
        
        print("Data updated successfully!")
        
    except psycopg2.Error as e:
        print("Error updating data:", e)
        
    finally:
        # Close the cursor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# search data
def search_data():
    try:
        # connect to database
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # get database cursor
        cur = conn.cursor()
        
        # receive the user's input
        driverId = input("Enter driver ID to search: ")
        
        # execute search operation
        cur.execute("SELECT * FROM drivers WHERE driverId = %s", (driverId,))
        
        # get the searching result
        result = cur.fetchone()
        
        if result:
            print("Search result:")
            print("Driver ID:", result[0])
            print("Reference name:", result[1])
            print("First name:", result[2])
            print("Last name:", result[3])
            print("Date of bith:", result[4])
            print("Nationality:", result[5])
            print("url:", result[6])
        else:
            print("Driver not found.")
        
    except psycopg2.Error as e:
        print("Error searching data:", e)
        
    finally:
        # close curcor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# aggregate functions
def aggregate_functions():
    try:
        # connect to database
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # get database cursor
        cur = conn.cursor()
        
        # execute aggregate functions operation
        cur.execute("SELECT COUNT(*) FROM drivers")
        
        # get the searching result
        result = cur.fetchone()
        
        if result:
            total_drivers = result[0]
            print("Total number of drivers:", total_drivers)
        else:
            print("No drivers found.")
        
    except psycopg2.Error as e:
        print("Error executing aggregate function:", e)
        
    finally:
        # close curcor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# sorting
def sorting():
    try:
        # connect to database
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # get database cursor
        cur = conn.cursor()
        
        # execute sorting operation
        cur.execute("SELECT forename, surname FROM drivers ORDER BY surname")
        
        # get the searching result
        results = cur.fetchall()
        
        if results:
            print("Full name list of drivers (sorted by last name):")
            for result in results:
                full_name = " ".join(result)
                print(full_name)
        else:
            print("No drivers found.")
        
    except psycopg2.Error as e:
        print("Error executing sorting function:", e)
        
    finally:
        # close curcor and connection
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# joins
def joins():
    try:
        # connect to database
        conn = connect_to_database()
        
        # get database cursor
        cur = conn.cursor()
        
        # execute 联接operation
        cur.execute("""
            SELECT drivers.driverId, drivers.forename, drivers.surname, driver_standings.points
            FROM drivers
            INNER JOIN driver_standings ON drivers.driverId = driver_standings.driverId
        """)
        
        # get the searching result
        results = cur.fetchall()
        
        if results:
            print("DriverID  |  First Name  |  Last Name  |  Points")
            print("-" * 50)
            for result in results:
                driverId, forename, surname, points = result
                print(f"{driverId:<9} | {forename:<12} | {surname:<11} | {points}")
        else:
            print("No results found.")
        
    except psycopg2.Error as e:
        print("Error executing join operation:", e)
        
    finally:
        # close database connection
        close_connection(conn, cur)

# grouping
def grouping():
    try:
        # connect to database
        conn = connect_to_database()
        
        # get database cursor
        cur = conn.cursor()
        
        # execute grouping operation
        cur.execute("""
            SELECT nationality, COUNT(*) 
            FROM drivers 
            GROUP BY nationality
        """)
        
        # get the searching result
        results = cur.fetchall()
        
        if results:
            print("Nationality  |  Count")
            print("-" * 25)
            for result in results:
                nationality, count = result
                print(f"{nationality:<12} | {count}")
        else:
            print("No results found.")
        
    except psycopg2.Error as e:
        print("Error executing grouping operation:", e)
        
    finally:
        # close database connection
        close_connection(conn, cur)

# subqueries
def subqueries():
    try:
        # connect to database
        conn = connect_to_database()
        
        # get database cursor
        cur = conn.cursor()
        
        # execute subqueries operation
        cur.execute("""
            SELECT drivers.driverId, drivers.forename, drivers.surname, driver_standings.points
            FROM drivers
            INNER JOIN driver_standings ON drivers.driverId = driver_standings.driverId
            WHERE driver_standings.points >= 90
        """)
        
        # get the searching result
        results = cur.fetchall()
        
        if results:
            print("DriverID  |  First Name  |  Last Name  |  Points")
            print("-" * 50)
            for result in results:
                driverId, forename, surname, points = result
                print(f"{driverId:<9} | {forename:<12} | {surname:<11} | {points}")
        else:
            print("No results found.")
        
    except psycopg2.Error as e:
        print("Error executing subquery operation:", e)
        
    finally:
        # close database connection
        close_connection(conn, cur)

# delete the data in 'drivers' base on driverId
def delete_from_drivers(driverId, cur):
    try:
        cur.execute("DELETE FROM drivers WHERE driverId = %s", (driverId,))
    except psycopg2.Error as e:
        print("Error deleting from drivers table:", e)
        raise e

# delete the data in 'driver_standings' base on 'driverId'
def delete_from_driver_standings(driverId, cur):
    try:
        cur.execute("DELETE FROM driver_standings WHERE driverId = %s", (driverId,))
    except psycopg2.Error as e:
        print("Error deleting from driver_standings table:", e)
        raise e
    
# transactions
def transactions():
    try:
        # connect to database
        conn = connect_to_database()
        
        # Gets the database cursor
        cur = conn.cursor()
        
        driverId = input("Enter driver ID to delete all related data: ") 

        # execute transaction
        cur.execute("BEGIN TRANSACTION;")
        
        # delete the data in 'drivers'
        delete_from_drivers(driverId, cur)
        
        # delete the data in the 'driver_standings' table
        delete_from_driver_standings(driverId, cur)
        
        # commit transaction
        conn.commit()
        print("Related data deleted successfully.")
        
    except psycopg2.Error as e:
        print("Error executing transaction:", e)
        
        # rollback transaction
        conn.rollback()
        
    finally:
        # close database connection
        close_connection(conn, cur)

# main function
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (one of the numbers listed above): ")
        handle_choice(choice)

if __name__ == '__main__':
    main()
