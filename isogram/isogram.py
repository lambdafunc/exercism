def is_isogram(value):
    """
    Verify if given string is isogram.
    return: False if letter occurence is repeated.
    return: True if string has unique letters and no repeated occurcences.
    """
    if value is "":
        return True
    value = format(value)
    for i in value:
        i = value.count(i)
        if i > 1:
            status = False
            return status
        else:
            status = True
    return status

def format(value):
    """
    Format input string as following:
        remove " " occurcences
        remove "-" occurcences
        convert into lower form
    args: str(value)
    return: formatted string
    """
    if " " in value:
        value = value.replace(" ", "").lower()
        return value
    elif "-" in value:
        value = value.replace("-", "").lower()
        return value
    else:
        value = value.lower()
        return value

