"""Напишіть код після 7 рядка для задачі:
Реалізуйте функцію, яка приймає послідовність слів, 
розділених за допомогою дефісу і друкує слова в послідовності, 
розділеній за допомогою дефісу, після сортування за алфавітом.
"""
# Вхідні дані: "one-two-three-four-five-six-seven"
# Вихідні дані: "five-four-one-seven-six-three-two"

s="one-two-three-four-five-six-seven"
def sort_str(string):
    lst=string.split("-")
    lst.sort()
    res="-".join(lst)
    return res
print(sort_str(s))


