def uppercaseletters(text):
    """Функция принимает строку и возвращает эту строку заглавными буква."""
    return text.upper()


def upperfirstletter(text):
    """Функция делает заглавными первые буквы каждого слова в строке"""
    text_list = text.split()
    text_new = ''
    for i in text_list:
        text_new = text_new + i.capitalize() + ' '
    return print(text_new)
