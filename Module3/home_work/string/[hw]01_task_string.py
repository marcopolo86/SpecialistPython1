# Дан произвольный текст. Каких символов больше, точек "." или запятых ","?
# Если точек и запятых одинаково - выведите "одинаково"

new_string = input()

# new_string = ',,,!!!///....'

comma = new_string.count(',')
point = new_string.count('.')
print(comma)
print(point)
if comma > point:
    print("больше запятых")
elif comma < point:
    print("больше точек")
elif comma == point:
    print("одинаково")
