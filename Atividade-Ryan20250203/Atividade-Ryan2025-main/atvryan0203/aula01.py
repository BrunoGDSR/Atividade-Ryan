def inverter_string(s):
    if len(s) == 0:
        return ""
    return inverter_string(s[1:]) + s[0]

print(inverter_string("recursao"))