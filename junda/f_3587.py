import pandas as pd
import matplotlib.pyplot as plt
from random import choice, seed
import random
import numpy as np

def f_3587(n, students=None, courses=None, random_seed=42):
    """
    Generate a DataFrame of random grades for n students across multiple courses, 
    and plot a histogram for each course. A random seed can be set for reproducibility.

    Parameters:
    - n (int): The number of students.
    - students (list): A list of student names. If None, a default list will be used.
    - courses (list): A list of course names. If None, a default list will be used.
    - random_seed (int): An optional random seed for reproducibility.

    Returns:
    - DataFrame: A pandas DataFrame with random grades for the students.

    Raises:
    - ValueError: If n is not a positive integer.

    Required Libraries:
    - pandas
    - matplotlib.pyplot
    - random
    - numpy
    
    Default values:
    
    students = ['John', 'Mary', 'Peter', 'Susan', 'Thomas', 'Julia', 'Robert', 'Linda']
    courses = ['Math', 'English', 'History', 'Biology', 'Chemistry', 'Physics', 'Art', 'Computer Science']
    random_seed=42
    
    Example:
    >>> grades = f_3587(10, random_seed=42)
    >>> print(grades)
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer.")

    random.seed(random_seed)
    np.random.seed(random_seed)
    if not students:
        students = ['John', 'Mary', 'Peter', 'Susan', 'Thomas', 'Julia', 'Robert', 'Linda']
    if not courses:
        courses = ['Math', 'English', 'History', 'Biology', 'Chemistry', 'Physics', 'Art', 'Computer Science']

    student_names = [choice(students) for _ in range(n)]
    data = {course: np.random.randint(0, 100, size=n) for course in courses}
    data['Student'] = student_names

    df = pd.DataFrame(data)
    df.set_index('Student', inplace=True)

    axes = df.hist(bins=10, figsize=(20, 15))
    for ax in axes.flatten():
        ax.set_title("Histogram of " + ax.get_title())
        ax.set_xlabel("Grades")
        ax.set_ylabel("Frequency")
    return df, ax

import unittest
import pandas as pd

class TestF3587(unittest.TestCase):
    def test_normal_functionality(self):
        df, _ = f_3587(10)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (10, 8))

    def test_invalid_number_of_students(self):
        with self.assertRaises(ValueError):
            f_3587(-1)

    def test_single_student(self):
        df, _ = f_3587(1)
        self.assertEqual(df.shape, (1, 8))  # 7 courses + 1 student name column

    def test_no_students(self):
        with self.assertRaises(ValueError):
            f_3587(0)
            
    def test_normal_functionality(self):
        df, _ = f_3587(10, random_seed=42)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (10, 8))

    def test_reproducibility_with_seed(self):
        df1, _ = f_3587(5, random_seed=123)
        df2, _ = f_3587(5, random_seed=123)
        pd.testing.assert_frame_equal(df1, df2)

    def test_without_seed(self):
        df1, _ = f_3587(5)
        df2, _ = f_3587(5)
        self.assertEqual(df1.to_string(), df2.to_string())

    # Remaining test cases can stay the same as before

if __name__ == '__main__':
    unittest.main()