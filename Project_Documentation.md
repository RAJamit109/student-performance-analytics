# Project Documentation
## Student Performance Analytics System

### 1. Project Title

**Student Performance Analytics System**

**Student:** Amit Mondal  
**Course:** Python with AI  
**Department:** Computer Science and Engineering

---

## 2. Objective

The objective of this project is to build a Python-based system that reads student academic data and performs meaningful analysis.

The system helps identify student performance by calculating total marks, average marks, grades, pass/fail status, subject-wise performance, attendance statistics and top-performing students.

---

## 3. Technologies Used

- Python
- NumPy
- Pandas
- CSV
- GitHub

### Why these technologies?

**Python:** Main programming language used to implement the project.

**Pandas:** Used to read the CSV file, create the DataFrame and perform data analysis.

**NumPy:** Used for numerical operations such as mean, maximum and minimum.

---

## 4. Dataset Description

The project uses a CSV dataset named `students.csv`.

It contains **25 student records**.

### Columns

| Column | Description |
|---|---|
| Student_ID | Unique ID of each student |
| Name | Student name |
| Department | Academic department |
| Python | Python marks |
| Java | Java marks |
| DBMS | DBMS marks |
| Computer_Networks | Computer Networks marks |
| Attendance | Attendance percentage |

The dataset contains realistic values and more than the required minimum of 15–20 records.

---

## 5. Grading Rule

The following grading rule is used:

| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

---

## 6. Pass/Fail Rule

A student passes when:

1. Average marks are at least 40.
2. Attendance is at least 75%.

If either condition is not satisfied, the student is marked as Fail.

---

## 7. Implementation

### Step 1: Dataset Preparation

A CSV file containing 25 student records was created.

### Step 2: Reading Data

Pandas is used:

```python
df = pd.read_csv("students.csv")
```

This loads the CSV data into a Pandas DataFrame.

### Step 3: Calculating Total

The marks of all four subjects are added for each student.

### Step 4: Calculating Average

The average of the four subject marks is calculated.

### Step 5: Grade Calculation

A reusable function checks the average and assigns a grade according to the documented grading rule.

### Step 6: Pass/Fail Calculation

Another reusable function checks average marks and attendance.

### Step 7: NumPy Analysis

NumPy is used to calculate:

- Overall class average
- Highest individual mark
- Lowest individual mark
- Average attendance

### Step 8: Subject-Wise Analysis

Pandas is used to calculate mean, maximum and minimum marks for every subject.

### Step 9: Top Performers

Students are sorted by average marks and the top three are displayed.

### Step 10: Final Output

The final program displays a complete, readable analysis report.

---

## 8. Key Features

- CSV dataset handling
- Pandas DataFrame
- NumPy numerical analysis
- Reusable functions
- Loops
- Conditions
- Total marks
- Average marks
- Grade assignment
- Pass/fail identification
- Highest performance
- Lowest performance
- Subject-wise performance
- Top performers
- Attendance analysis
- Grade distribution

---

## 9. Output / Screenshots

Run:

```bash
python main.py
```

Take screenshots of these important output sections and add them to the final documentation:

1. Student Performance Table
2. Class Summary
3. Highest and Lowest Performance
4. Subject-Wise Analysis
5. Top 3 Performers
6. Grade Distribution
7. Attendance Analysis
8. Practical Questions Answered

---

## 10. Final Outcome

The completed system successfully reads student data and produces meaningful academic performance analysis.

It provides a quick way to understand:

- Individual student performance
- Class average
- Pass/fail statistics
- Best and weakest subjects
- Top-performing students
- Attendance performance

The project demonstrates practical use of Python, functions, loops, NumPy and Pandas.

---

## 11. Challenges & Learning

### Challenges

1. Organizing student data in CSV format.
2. Applying the same calculations to every student.
3. Creating a clear grading and pass/fail rule.
4. Combining NumPy calculations with Pandas DataFrame operations.
5. Presenting the output in a readable format.

### Learning

Through this project, I learned:

- How to work with CSV data.
- How to create and use Pandas DataFrames.
- How to perform numerical operations with NumPy.
- How to write reusable Python functions.
- How to use loops and conditions in a practical application.
- How to perform basic data analysis.
- How to organize a project for GitHub.

---

## 12. GitHub Repository

After creating the GitHub repository, paste the repository URL here:

**GitHub Repository:** `PASTE-YOUR-GITHUB-REPOSITORY-LINK-HERE`

---

## 13. Conclusion

The Student Performance Analytics System meets the required Python data-analysis objectives. It uses a realistic student dataset and demonstrates Python fundamentals, NumPy, Pandas, reusable functions, loops and meaningful data analysis.

Advanced machine learning is not required for this project, so the implementation focuses on the concepts covered in the course.
