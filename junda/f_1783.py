import numpy as np
import pandas as pd
import statistics

def f_1783(rows, columns=['A', 'B', 'C', 'D', 'E', 'F'], seed=42):
    """
    Create a Pandas DataFrame with a specified number of rows and six columns (default A-F), 
    each filled with random numbers between 1 and 100, using a specified seed for reproducibility. 
    Additionally, calculate the mean and median for each column.

    Parameters:
        - rows (int): The number of rows in the DataFrame. Must be a positive integer greater than 0.
        - columns (list, optional): Column names for the DataFrame. Defaults to ['A', 'B', 'C', 'D', 'E', 'F'].
        - seed (int, optional): Seed for the random number generator. Defaults to 42.

    Returns:
        - DataFrame: A pandas DataFrame with the generated data.
        - dict: A dictionary containing the calculated mean and median for each column. 
                The dictionary format is:
                {
                    'ColumnName': {
                        'mean': MeanValue,
                        'median': MedianValue
                    }, ...
                }
                where 'ColumnName' is each of the specified column names, 'MeanValue' is the calculated mean, 
                and 'MedianValue' is the calculated median for that column.

    Raises:
        - ValueError: If 'rows' is not a positive integer greater than 0.

    Requirements:
        - numpy
        - pandas
        - statistics

    Example:
        >>> df, stats = f_1783(10)
        >>> print(df)
        >>> print(stats)
    """
    if not isinstance(rows, int) or rows <= 0:
        raise ValueError("rows must be a positive integer greater than 0.")

    np.random.seed(seed)
    data = np.random.randint(1, 101, size=(rows, len(columns)))
    df = pd.DataFrame(data, columns=columns)
    
    stats_dict = {}
    for col in columns:
        stats_dict[col] = {
            'mean': statistics.mean(df[col]),
            'median': statistics.median(df[col])
        }
    
    return df, stats_dict


import unittest
import pandas as pd

class TestF_1783(unittest.TestCase):
    def test_dataframe_structure(self):
        df, _ = f_1783(10)
        self.assertEqual(df.shape, (10, 6))  # 10 rows, 6 columns

    def test_invalid_rows_input_negative(self):
        with self.assertRaises(ValueError):
            f_1783(-1)

    def test_invalid_rows_input_zero(self):
        with self.assertRaises(ValueError):
            f_1783(0)

    def test_invalid_rows_type(self):
        with self.assertRaises(ValueError):
            f_1783("five")

    def test_stats_calculation(self):
        _, stats = f_1783(10)
        for col_stats in stats.values():
            self.assertIn('mean', col_stats)
            self.assertIn('median', col_stats)
            
    def test_specific_stats_values(self):
        df, stats = f_1783(10)
        for col in df.columns:
            expected_mean = df[col].mean()
            expected_median = df[col].median()
            self.assertAlmostEqual(stats[col]['mean'], expected_mean)
            self.assertAlmostEqual(stats[col]['median'], expected_median)

    def test_reproducibility_with_seed(self):
        df1, _ = f_1783(10, seed=123)
        df2, _ = f_1783(10, seed=123)
        pd.testing.assert_frame_equal(df1, df2)

if __name__ == '__main__':
    unittest.main()
