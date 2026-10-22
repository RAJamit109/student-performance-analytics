"""
Student Performance Analytics System
Course: Python with AI
Technologies: Python, NumPy, Pandas

This program:
1. Loads student data from CSV.
2. Uses Pandas for data processing.
3. Uses NumPy for numerical calculations.
4. Uses functions and loops.
5. Calculates total, average, grade and pass/fail status.
6. Performs subject-wise and student-wise analysis.
"""

from pathlib import Path
import numpy as np
import pandas as pd

from functions import (
    add_calculated_columns,
    get_subject_summary,
    get_top_students,
    get_bottom_students,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "students.csv"

SUBJECTS = ["Python", "Java", "DBMS", "Computer_Networks"]


def display_section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def main():
    # Step 1 & 2: Load and organize data using Pandas
    df = pd.read_csv(DATA_FILE)

    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("Dataset loaded successfully.")
    print(f"Number of records: {len(df)}")
    print(f"Columns: {', '.join(df.columns)}")

    # Step 3: Process the data using reusable functions
    df = add_calculated_columns(df, SUBJECTS)

    # Required numerical analysis using NumPy
    all_marks = df[SUBJECTS].to_numpy(dtype=float)
    overall_class_average = round(float(np.mean(all_marks)), 2)
    highest_mark = float(np.max(all_marks))
    lowest_mark = float(np.min(all_marks))

    display_section("1. STUDENT PERFORMANCE TABLE")
    display_columns = [
        "Student_ID", "Name", "Department", "Total",
        "Average", "Grade", "Attendance", "Status"
    ]
    print(df[display_columns].to_string(index=False))

    display_section("2. CLASS SUMMARY")
    passed = int((df["Status"] == "Pass").sum())
    failed = int((df["Status"] == "Fail").sum())

    print(f"Total students       : {len(df)}")
    print(f"Passed students      : {passed}")
    print(f"Failed students      : {failed}")
    print(f"Overall class average: {overall_class_average}")
    print(f"Highest individual mark: {highest_mark:.0f}")
    print(f"Lowest individual mark : {lowest_mark:.0f}")

    display_section("3. HIGHEST AND LOWEST PERFORMANCE")
    highest_student = df.loc[df["Average"].idxmax()]
    lowest_student = df.loc[df["Average"].idxmin()]
    print(f"Highest performer: {highest_student['Name']} "
          f"({highest_student['Average']:.2f}, Grade {highest_student['Grade']})")
    print(f"Lowest performer : {lowest_student['Name']} "
          f"({lowest_student['Average']:.2f}, Grade {lowest_student['Grade']})")

    display_section("4. SUBJECT-WISE PERFORMANCE ANALYSIS")
    subject_summary = get_subject_summary(df, SUBJECTS)
    print(subject_summary.to_string())
    best_subject = subject_summary["mean"].idxmax()
    weakest_subject = subject_summary["mean"].idxmin()
    print(f"\nBest subject   : {best_subject} "
          f"({subject_summary.loc[best_subject, 'mean']:.2f})")
    print(f"Weakest subject: {weakest_subject} "
          f"({subject_summary.loc[weakest_subject, 'mean']:.2f})")

    display_section("5. TOP 3 PERFORMERS")
    print(get_top_students(df, 3).to_string(index=False))

    display_section("6. BOTTOM 3 PERFORMERS")
    print(get_bottom_students(df, 3).to_string(index=False))

    display_section("7. GRADE DISTRIBUTION")
    # Loop is deliberately used for clear iteration in the project.
    grade_order = ["A+", "A", "B", "C", "D", "F"]
    grade_counts = df["Grade"].value_counts()
    for grade in grade_order:
        print(f"Grade {grade}: {int(grade_counts.get(grade, 0))} student(s)")

    display_section("8. ATTENDANCE ANALYSIS")
    attendance_average = round(float(np.mean(df["Attendance"].to_numpy(dtype=float))), 2)
    low_attendance = df[df["Attendance"] < 75]
    print(f"Average attendance: {attendance_average}%")
    print(f"Students below 75% attendance: {len(low_attendance)}")
    if not low_attendance.empty:
        print(low_attendance[["Student_ID", "Name", "Attendance", "Status"]].to_string(index=False))
    else:
        print("No student is below 75% attendance.")

    display_section("9. PRACTICAL QUESTIONS ANSWERED")
    print(f"Which student has the highest average? {highest_student['Name']}")
    print(f"Which subject has the best average? {best_subject}")
    print(f"How many students passed? {passed}")
    print(f"What is the overall class average? {overall_class_average}")
    print(f"Which subject has the lowest average? {weakest_subject}")

    display_section("10. PROJECT COMPLETED")
    print("Analysis completed successfully.")
    print("Technologies used: Python, NumPy, Pandas")


if __name__ == "__main__":
    main()
