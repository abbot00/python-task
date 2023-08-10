num_3 = "3.147"
def isfloat(str_val_):
    try:
        float(str_val_)
        return True
    except ValueError:
        return False
print("Is pi a Float :", isfloat(num_3))