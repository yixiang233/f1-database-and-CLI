import argparse
import psycopg2

# 显示菜单
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

# 处理用户选择
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

# 连接到数据库
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

# 关闭数据库连接
def close_connection(conn, cur=None):
    try:
        if cur:
            cur.close()
        conn.close()
    except psycopg2.Error as e:
        print("Error closing database connection:", e)


# 插入数据
def insert_data():
    try:
        # 连接到数据库
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 接收用户输入
        driverId = input("Enter driver id: ")
        driverRef = input("Enter reference name: ")
        forename = input("Enter first name: ")
        surname = input("Enter last name: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        nationality = input("Enter nationality: ")
        url = input("Enter Wikipedia URL: ")
        
        # 执行插入操作
        cur.execute("INSERT INTO drivers (driverId, driverRef, forename, surname, dob, nationality, url) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (driverId, driverRef, forename, surname, dob, nationality, url))
        
        # 提交事务
        conn.commit()
        
        print("Data inserted successfully!")
        
    except psycopg2.Error as e:
        print("Error inserting data:", e)
        
    finally:
        # 关闭游标和连接
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# 删除数据
def delete_data():
    try:
        # 连接到数据库
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 接收用户输入
        driverId = input("Enter driver ID to delete: ")
        
        # 执行删除操作
        cur.execute("DELETE FROM drivers WHERE driverId = %s", (driverId,))
        
        # 提交事务
        conn.commit()
        
        print("Data deleted successfully!")
        
    except psycopg2.Error as e:
        print("Error deleting data:", e)
        
    finally:
        # 关闭游标和连接
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# 更新数据
def update_data():
    try:
        # 连接到数据库
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 接收用户输入
        driverId = input("Enter driver ID to update: ")
        attribute = input("Enter attribute to update (driverRef (reference name), forename (first name), surname (last name), dob (date of birth), nationality, url): ")
        new_value = input(f"Enter new value for {attribute}: ")
        
        # 执行更新操作
        cur.execute(f"UPDATE drivers SET {attribute} = %s WHERE driverId = %s", (new_value, driverId))
        
        # 提交事务
        conn.commit()
        
        print("Data updated successfully!")
        
    except psycopg2.Error as e:
        print("Error updating data:", e)
        
    finally:
        # 关闭游标和连接
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# 搜索数据
def search_data():
    try:
        # 连接到数据库
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 接收用户输入
        driverId = input("Enter driver ID to search: ")
        
        # 执行搜索操作
        cur.execute("SELECT * FROM drivers WHERE driverId = %s", (driverId,))
        
        # 获取搜索结果
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
        # 关闭游标和连接
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# 聚合函数
def aggregate_functions():
    try:
        # 连接到数据库
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 执行聚合函数操作
        cur.execute("SELECT COUNT(*) FROM drivers")
        
        # 获取查询结果
        result = cur.fetchone()
        
        if result:
            total_drivers = result[0]
            print("Total number of drivers:", total_drivers)
        else:
            print("No drivers found.")
        
    except psycopg2.Error as e:
        print("Error executing aggregate function:", e)
        
    finally:
        # 关闭游标和连接
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# 排序
def sorting():
    try:
        # 连接到数据库
        conn = psycopg2.connect(
            dbname='f1',
            user='postgres',
            password='0123',
            host='localhost',
            port='5432'
        )
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 执行排序操作
        cur.execute("SELECT forename, surname FROM drivers ORDER BY surname")
        
        # 获取查询结果
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
        # 关闭游标和连接
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

# 连接
def joins():
    try:
        # 连接到数据库
        conn = connect_to_database()
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 执行联接操作
        cur.execute("""
            SELECT drivers.driverId, drivers.forename, drivers.surname, driver_standings.points
            FROM drivers
            INNER JOIN driver_standings ON drivers.driverId = driver_standings.driverId
        """)
        
        # 获取查询结果
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
        # 关闭数据库连接
        close_connection(conn, cur)

# 分组
def grouping():
    try:
        # 连接到数据库
        conn = connect_to_database()
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 执行分组操作
        cur.execute("""
            SELECT nationality, COUNT(*) 
            FROM drivers 
            GROUP BY nationality
        """)
        
        # 获取查询结果
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
        # 关闭数据库连接
        close_connection(conn, cur)

# 子查询
def subqueries():
    try:
        # 连接到数据库
        conn = connect_to_database()
        
        # 获取数据库游标
        cur = conn.cursor()
        
        # 执行子查询操作
        cur.execute("""
            SELECT drivers.driverId, drivers.forename, drivers.surname, driver_standings.points
            FROM drivers
            INNER JOIN driver_standings ON drivers.driverId = driver_standings.driverId
            WHERE driver_standings.points >= 90
        """)
        
        # 获取查询结果
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
        # 关闭数据库连接
        close_connection(conn, cur)

# 根据 driverId 删除 drivers 表中的数据
def delete_from_drivers(driverId, cur):
    try:
        cur.execute("DELETE FROM drivers WHERE driverId = %s", (driverId,))
    except psycopg2.Error as e:
        print("Error deleting from drivers table:", e)
        raise e

# 根据 driverId 删除 driver_standings 表中的数据
def delete_from_driver_standings(driverId, cur):
    try:
        cur.execute("DELETE FROM driver_standings WHERE driverId = %s", (driverId,))
    except psycopg2.Error as e:
        print("Error deleting from driver_standings table:", e)
        raise e
    
# 事务
def transactions():
    try:
        # 连接到数据库
        conn = connect_to_database()
        
        # 获取数据库游标
        cur = conn.cursor()
        
        driverId = input("Enter driver ID to delete all related data: ") 

        # 开始事务
        cur.execute("BEGIN TRANSACTION;")
        
        # 删除 drivers 表中的数据
        delete_from_drivers(driverId, cur)
        
        # 删除 driver_standings 表中的数据
        delete_from_driver_standings(driverId, cur)
        
        # 提交事务
        conn.commit()
        print("Related data deleted successfully.")
        
    except psycopg2.Error as e:
        print("Error executing transaction:", e)
        
        # 回滚事务
        conn.rollback()
        
    finally:
        # 关闭数据库连接
        close_connection(conn, cur)

# 主函数
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (one of the numbers listed above): ")
        handle_choice(choice)

if __name__ == '__main__':
    main()
