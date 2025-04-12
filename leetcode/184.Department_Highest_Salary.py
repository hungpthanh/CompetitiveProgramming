import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
    highest_salary = merged.groupby('departmentId').apply(lambda x: x[x['salary'] == x['salary'].max()])
    highest_salary = highest_salary.reset_index(drop=True)
    result = highest_salary[['name_department', 'name_employee', 'salary']]
    result.columns = ['Department','Employee', 'Salary']
    return result

# Second approach using transform
# import pandas as pd

# def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
#     merged = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_employee', '_department'))
#     merged['max_salary'] = merged.groupby('departmentId')['salary'].transform('max')
#     results = merged[merged['salary'] == merged['max_salary']][['name_department', 'name_employee', 'salary']]
#     results = results.rename(columns={
#         'name_department': 'Department',
#         'name_employee': 'Employee',
#         'salary_employee': 'Salary'
#     })
#     return results
    
