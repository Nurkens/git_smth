



def my_func2(value):
    try:
        value = float(value)
        vat = value/100 * 40
        return round (vat,3)
    except TypeError:
        return "can't read. "
result = my_func2(0.5356)
print(result)            