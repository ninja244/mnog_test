#сегодня мы с вами попробуем выступить в роли детектива
# у нас есть множество людей, которые пользуется машиной той же марки, которую пользуется убийца
# есть множество людей, которые живут недалеко от мест преступления
# и множество людей, у которых и работа недалеко от мест преступления

#имена обычно значения неуникальные, но предплоложим, это были бы номер соц страховок
shevrole_owner = {'sam', 'edit', 'semen', 'petr'}

work_near = {'konstantin', 'vladislav', 'sam', 'petr', 'edit'}

live_near = {'john', 'vladislav', 'olga', 'mike', 'grant', 'covid', 'bilbo' }

#  д/з объединить множество людей, которые живут и работают рядом
# вывести множество людей, которые и владеют авто нужной марки, и живут и работают рядом

print("Люди живущие и работающие рядом с местом преступления: ")
live_work = work_near & live_near
if len(live_work) == 0:
    print("Отсутствуют\n")
for people in live_work:
    print(people)
    print("")

print("Люди, которые владеют авто шевроле, при этом работают рядомс местом преступления: ")
work_shevrole = work_near & shevrole_owner
if len(work_shevrole) == 0:
    print("Отсутствуют\n")
for people in work_shevrole:
    print(people)
    print("")

print("Люди c шевроле которые живут и работают рядом с местом преступления: ")
live_work_shevrole = work_near & live_near & shevrole_owner
if len(live_work_shevrole) == 0:
    print("Отсутствуют\n")

for people in live_work_shevrole:
    print(people)
    print("")

print("Люди с шевроле,живущие рядом: ")
live_shevrole = live_near & shevrole_owner
if len(live_shevrole) == 0:
    print("Отсутствуют\n")
for people in live_shevrole:
    print(people)
    print("")
