def tfhour(time24):
    if "01:" in time24:
        time24 = time24.replace("01:", "13:")
    elif "02:" in time24:
        time24 = time24.replace("02:", "14:")
    elif "03:" in time24:
        time24 = time24.replace("03:", "15:")
    elif "04:" in time24:
        time24 = time24.replace("04:", "16:")
    elif "05:" in time24:
        time24 = time24.replace("05:", "17:")
    elif "06:" in time24:
        time24 = time24.replace("06:", "18:")
    elif "07:" in time24:
        time24 = time24.replace("07:", "19:")
    elif "08:" in time24:
        time24 = time24.replace("08:", "20:")
    elif "09:" in time24:
        time24 = time24.replace("09:", "21:")
    elif "10:" in time24:
        time24 = time24.replace("10:", "22:")
    elif "11:" in time24:
        time24 = time24.replace("11:", "23:")
    elif "12:" in time24:
        return time24
    return time24
# This function is to be only used with the "prayer time output.py" program.