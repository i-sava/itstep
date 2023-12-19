"""Напишіть код після 7 рядка для задачі:
Реалізуйте функцію, яка приймає послідовність слів, 
розділених за допомогою дефісу і друкує слова в послідовності, 
розділеній за допомогою дефісу, після сортування за алфавітом.
"""
# Вхідні дані: "one-two-three-four-five-six-seven"
# Вихідні дані: "five-four-one-seven-six-three-two"


string = "one-two-three-four-five-six-seven"


def sort_string(text):
    new_text = text.split('-')
    new_text.sort()
    sorted_text = "-".join(new_text)
    print(sorted_text)


sort_string(string)