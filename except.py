def cut_cake(parts):
    try:
        return 1/parts
    except ZeroDivisionError:
        return "С ума сошли?"
a = cut_cake(2)
print(a)