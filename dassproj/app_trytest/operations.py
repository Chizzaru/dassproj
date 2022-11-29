def getResultDepression(score):
    if score >= 0 and score <= 4:
        return 'Normal'
    elif score >= 5 and score <= 6:
        return 'Mild'
    elif score >= 7 and score <= 10:
        return 'Moderate'
    elif score >= 11 and score <= 13:
        return 'Severe'
    else:
        return 'Extremely Severe'


def getResultAnxiety(score):
    if score >= 0 and score <= 3:
        return 'Normal'
    elif score >= 4 and score <= 5:
        return 'Mild'
    elif score >= 6 and score <= 7:
        return 'Moderate'
    elif score >= 8 and score <= 9:
        return 'Severe'
    else:
        return 'Extremely Severe'


def getResultStress(score):
    if score >= 0 and score <= 7:
        return 'Normal'
    elif score >= 8 and score <= 9:
        return 'Mild'
    elif score >= 10 and score <= 12:
        return 'Moderate'
    elif score >= 13 and score <= 16:
        return 'Severe'
    else:
        return 'Extremely Severe'
    

#DASS 21 ALGORITHM
def DASS21_compute(arr_answers):
    result = 0
    summation  = 0
    for x in arr_answers:
        summation += int(x)
    
    result = summation * 2

    return result


    
