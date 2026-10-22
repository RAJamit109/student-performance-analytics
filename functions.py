"""
Reusable functions for the Student Performance Analytics System.
"""

import numpy as np


def calculate_total(row, subjects):
    """Return total marks for one student."""
    return int(np.sum(row[subjects].to_numpy(dtype=float)))


def calculate_average(row, subjects):
    """Return average marks for one student."""
    return round(float(np.mean(row[subjects].to_numpy(dtype=float))), 2)


def calculate_grade(average):
    """Assign a grade using the project's documented grading rule."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def calculate_status(average, attendance):
    """Pass if average >= 40 and attendance >= 75%."""
    return "Pass" if average >= 40 and attendance >= 75 else "Fail"


def add_calculated_columns(df, subjects):
    """Add Total, Average, Grade and Status columns."""
    df = df.copy()
    df["Total"] = df.apply(lambda row: calculate_total(row, subjects), axis=1)
    df["Average"] = df.apply(lambda row: calculate_average(row, subjects), axis=1)
    df["Grade"] = df["Average"].apply(calculate_grade)
    df["Status"] = df.apply(
        lambda row: calculate_status(row["Average"], row["Attendance"]), axis=1
    )
    return df


def get_subject_summary(df, subjects):
    """Return average, highest and lowest marks for every subject."""
    return df[subjects].agg(["mean", "max", "min"]).T.round(2)


def get_top_students(df, n=3):
    """Return the top n students by average marks."""
    return df.nlargest(n, "Average")[["Student_ID", "Name", "Average", "Grade"]]


def get_bottom_students(df, n=3):
    """Return the bottom n students by average marks."""
    return df.nsmallest(n, "Average")[["Student_ID", "Name", "Average", "Grade"]]
