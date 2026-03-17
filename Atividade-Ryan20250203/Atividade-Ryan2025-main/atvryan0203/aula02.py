def decimal_para_binario(n):
    if n == 0:
        return ""
    return decimal_para_binario(n // 2) + str(n % 2)

print(decimal_para_binario(13))