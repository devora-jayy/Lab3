import Lab2.bmi as bmi

def test_bmi_normal_weight():
    # Weight 65, Height 1.75 = BMI 21.2 (Normal)
    result = bmi.calculate_bmi(weight=65, height=1.75) 
    assert (result == 0)

def test_bmi_over_weight():
    # Weight 85, Height 1.75 = BMI 27.7 (Overweight)
    result = bmi.calculate_bmi(weight=85, height=1.75)
    assert (result == 1)

def test_bmi_under_weight():
    # Weight 50, Height 1.75 = BMI 16.3 (Underweight)
    result = bmi.calculate_bmi(weight=50, height=1.75)
    assert (result == -1)