"""Напишіть код після 7 рядка для задачі:
Реалізуйте функцію, яка приймає послідовність слів, 
розділених за допомогою дефісу і друкує слова в послідовності, 
розділеній за допомогою дефісу, після сортування за алфавітом.
"""
# Вхідні дані: "one-two-three-four-five-six-seven"
# Вихідні дані: "five-four-one-seven-six-three-two"

# Vlad
input_string = "one-two-three-four-five-six-seven"

def sort_string(input_str):
    words = input_str.split('-')
    sorted_words = sorted(words)
    result = '-'.join(sorted_words)
    print(result)


sort_string(input_string)


# Andriy
s="one-two-three-four-five-six-seven"
def sort_str(string):
    lst=string.split("-")
    lst.sort()
    res="-".join(lst)
    return res
print(sort_str(s))


# Yura
string = "one-two-three-four-five-six-seven"


def sort_string(text):
    new_text = text.split('-')
    new_text.sort()
    sorted_text = "-".join(new_text)
    print(sorted_text)


sort_string(string)

