# Student Performance Analytics System

A Python-based Student Performance Analytics System developed for the **Python with AI** project assignment.

## Objective

The project reads student records from a CSV dataset and analyzes academic performance using Python, NumPy and Pandas. It calculates marks summaries, averages, grades, pass/fail status, subject-wise performance, attendance statistics and top performers.

## Technologies Used

- Python
- NumPy
- Pandas
- CSV dataset
- GitHub for version control/submission

## Project Structure

```text
student-performance-analytics/
├── main.py
├── functions.py
├── students.csv
├── README.md
├── Project_Documentation.md
└── requirements.txt
```

## Dataset

The dataset contains 25 CSE student records with:

- Student ID
- Name
- Department
- Python marks
- Java marks
- DBMS marks
- Computer Networks marks
- Attendance percentage

## Features

1. Load student data using Pandas.
2. Store and process data in a Pandas DataFrame.
3. Use NumPy for numerical calculations.
4. Calculate total marks.
5. Calculate average marks.
6. Assign grades.
7. Determine pass/fail status.
8. Find highest and lowest performance.
9. Perform subject-wise analysis.
10. Identify top-performing students.
11. Analyze attendance.
12. Display a clear final report.

## Grading Rule

| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

## Pass/Fail Rule

A student is considered **Pass** when:

- Average marks >= 40
- Attendance >= 75%

Otherwise, the student is **Fail**.

## How to Run

### 1. Install Python

Python 3.x is recommended.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python main.py
```

## Expected Output

The program displays:

- Student performance table
- Number of students
- Passed and failed students
- Overall class average
- Highest and lowest performers
- Subject-wise averages
- Best and weakest subject
- Top 3 performers
- Bottom 3 performers
- Grade distribution
- Attendance analysis
- Answers to practical analysis questions

## Learning Outcomes

This project demonstrates practical use of:

- Variables and data types
- Conditions
- Loops
- Functions
- NumPy
- Pandas
- CSV data handling
- Data analysis

## Important Note

Advanced machine learning is not required for this assignment. The project focuses on Python data analysis using the concepts covered in the course.

## Author

**Amit Mondal**  
B.Tech CSE
