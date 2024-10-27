# TODO Напишите функцию find_common_participants
def find_common_participants(s1,s2, razdelenie=','):
    s_1=set(s1.split(razdelenie))
    s_2=set(s2.split(razdelenie))
    sss=s_1.intersection(s_2)
    return sorted((sss))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group,participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой
