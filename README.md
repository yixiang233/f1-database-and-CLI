codebase setup:
<br>The cli.py file implements a command-line interface program for interacting with a Formula 1 World Championship driver database. The main functionalities include adding, deleting, updating, and searching for driver information, as well as executing various data queries and operations. Here's an overview of the code's main structure and functionalities:
<br><br>
1. Import the `argparse` and `psycopg2` libraries.
<br><br>
2. Define a `show_menu()` function to display the user menu, listing available operation options.
<br><br>
3. Define a `handle_choice(choice)` function to call the appropriate function based on the user's input choice.
<br><br>
4. Define a series of functions including connecting to the database, closing the database connection, inserting data, deleting data, updating data, searching data, executing aggregate functions, sorting, joining, grouping, and subqueries.
<br><br>
5. The main function `main()` loops to display the menu and calls the appropriate function based on the user's choice.
<br><br>
6. Use the `if __name__ == '__main__':` statement to ensure the main function is executed only when the script is run directly.
<br><br>
It provides a way to interact with the Formula 1 driver database via a command-line interface. Users can select different operations by inputting numbers, and the program will perform the corresponding database operations based on the user's choice.
<br><br>
In order to run it, we can open the terminal and go to the file’s location, then we input “python cli.py”, then it will show the menu.
