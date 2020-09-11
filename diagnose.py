def diagnoseBP(bp):
    result = ""
    bld_pre = float(bp)
    if bld_pre < 60:
        result = "Low Blood Pressure"
    elif bld_pre < 80:
        result = "Normal Blood Pressure"
    elif bld_pre < 90:
        result = "High Blood Pressure (Hypertension) Stage 1"
    elif bld_pre < 120:
        result = "High Blood Pressure (Hypertension) Stage 2"
    else:
        result = "High Blood Pressure (Hypertension) Stage 3"
    return result

def diagnoseBMI(bmi):
    BMI = float(bmi)
    result = ""
    if BMI < 15:
        result = "Very severely underweight"
    elif BMI < 16:
        result = "Severely underweight"
    elif BMI < 18.5:
        result = "Underweight"
    elif BMI < 25:
        result = "Normal Body Weight"
    elif BMI < 30:
        result = "Overweight"
    elif BMI < 35:
        result = "Obese Class 1 - Moderately Obese"
    elif BMI < 40:
        result = "Obese Class 2 - Severely Obese"
    else:
        result = "Obese Class 3 - Very Severely Obese"
    return result
