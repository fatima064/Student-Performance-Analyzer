from flask import Flask, render_template
import pandas as pd
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():

    # Connect to database
    connection = sqlite3.connect("students.db")

    # Read student data using SQL
    students = pd.read_sql_query(
        "SELECT * FROM students",
        connection
    )

    connection.close()

    # Calculate average
    students["Average"] = (
        students["Python"] +
        students["SQL"] +
        students["DBMS"]
    ) / 3

    students["Average"] = students["Average"].round(2)

    # Classify performance
    def performance_category(average):

        if average >= 80:
            return "Excellent"

        elif average >= 60:
            return "Good"

        elif average >= 40:
            return "Average"

        else:
            return "Needs Improvement"

    students["Performance"] = students["Average"].apply(
        performance_category
    )

    # Dashboard statistics
    total_students = len(students)

    class_average = round(
        students["Average"].mean(),
        2
    )

    top_student = students.loc[
        students["Average"].idxmax(),
        "Name"
    ]

    # Convert data into a format HTML can use
    student_records = students.to_dict(
        orient="records"
    )

    # Data for chart
    student_names = students["Name"].tolist()

    student_averages = students["Average"].tolist()

    # Send data to HTML
    return render_template(
        "index.html",
        students=student_records,
        total_students=total_students,
        class_average=class_average,
        top_student=top_student,
        student_names=student_names,
        student_averages=student_averages
    )


if __name__ == "__main__":
    app.run(debug=True)