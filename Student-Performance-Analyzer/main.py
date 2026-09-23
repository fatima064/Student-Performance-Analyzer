import pandas as pd
import sqlite3


# Read student data
students = pd.read_csv("students.csv")


# Connect to SQLite database
connection = sqlite3.connect("students.db")


# Store data in database
students.to_sql("students", connection, if_exists="replace", index=False)


# Calculate average
students["Average"] = (
    students["Python"] +
    students["SQL"] +
    students["DBMS"]
) / 3

students["Average"] = students["Average"].round(2)


# Performance category function
def performance_category(average):

    if average >= 80:
        return "Excellent"

    elif average >= 60:
        return "Good"

    elif average >= 40:
        return "Average"

    else:
        return "Needs Improvement"


students["Performance"] = students["Average"].apply(performance_category)


# ---------------- MENU ----------------

while True:

    print("\n========================================")
    print("       STUDENT PERFORMANCE ANALYZER")
    print("========================================")

    print("1. View All Students")
    print("2. Search Student")
    print("3. Find Top Student")
    print("4. View Passed Students")
    print("5. View Performance Report")
    print("6. Exit")

    choice = input("\nEnter your choice: ")


    # Option 1
    if choice == "1":

        print("\nAll Students:")
        print(students)


    # Option 2
    elif choice == "2":

        name = input("\nEnter student name: ")

        query = "SELECT * FROM students WHERE Name = ?"

        result = pd.read_sql_query(
            query,
            connection,
            params=(name,)
        )

        if result.empty:
            print("\nStudent not found.")

        else:
            print("\nStudent Details:")
            print(result)


    # Option 3
    elif choice == "3":

        query = """
        SELECT Name, Python, SQL, DBMS,
               (Python + SQL + DBMS) / 3.0 AS Average
        FROM students
        ORDER BY Average DESC
        LIMIT 1
        """

        top_student = pd.read_sql_query(
            query,
            connection
        )

        print("\nTop Student:")
        print(top_student)


    # Option 4
    elif choice == "4":

        query = """
        SELECT Name, Python, SQL, DBMS,
               (Python + SQL + DBMS) / 3.0 AS Average
        FROM students
        WHERE (Python + SQL + DBMS) / 3.0 >= 40
        """

        passed_students = pd.read_sql_query(
            query,
            connection
        )

        print("\nPassed Students:")
        print(passed_students)


    # Option 5
    elif choice == "5":

        print("\nPerformance Report:")
        print(students)


    # Option 6
    elif choice == "6":

        print("\nThank you for using Student Performance Analyzer!")

        break


    else:

        print("\nInvalid choice. Please enter a number from 1 to 6.")


# Close database
connection.close()