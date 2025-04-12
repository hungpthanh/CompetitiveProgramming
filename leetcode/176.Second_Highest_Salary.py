import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    N = 2
    unique_salary = sorted(employee['salary'].unique())[::-1]
    if len(unique_salary) < N:
        return pd.DataFrame([None], columns=[f'SecondHighestSalary'])
    return pd.DataFrame([unique_salary[N - 1]], columns=[f'SecondHighestSalary'])
