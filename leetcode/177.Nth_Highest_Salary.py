import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
        return pd.DataFrame([None], columns=[f'getNthHighestSalary({N})'])
    unique_salary = sorted(employee['salary'].unique())[::-1]
    if len(unique_salary) < N:
        return pd.DataFrame([None], columns=[f'getNthHighestSalary({N})'])
    return pd.DataFrame([unique_salary[N - 1]], columns=[f'getNthHighestSalary({N})'])
