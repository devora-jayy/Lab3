import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(20, 30)
    assert (len(result) == 2)  # Jane (25) and Mary (23)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert (result == 60166.666666666664)  # Math based on the 6 default employees

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Sales")
    assert (len(result) == 2)  # John and Peter