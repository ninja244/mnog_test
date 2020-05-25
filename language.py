import random

slovar = {}


print("КУ, ща будут слова ты их пиши, а чтобы закончить пиши'enough'")

while True:
    key = input("Введите слово на английском:\n:")
    if key == 'enough':
        break
    value = input("Введите слово на русском:\n:")
    slovar[key] = value

print("Пора потренироваться, ошибок у вас не более 5")

errors = 0
bonus = 0

for key in random.sample(slovar.keys(), len(slovar)):
    print('Введите значение слова: ' + key)
    answer = input("Вы считаете, что это слово переводится как ").lower().strip()
    if slovar[key] == answer:
        bonus += 1
        print("Отлично, ваш счет составляет :", bonus)
    elif errors > 4:
        print("game over")
        break
    else:
        errors += 1
print("Правильное слово было: ", slovar[key])
print("Количество ошибок", errors)
