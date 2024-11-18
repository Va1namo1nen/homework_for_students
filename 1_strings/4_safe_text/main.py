import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    wrong_article = wrong_article.replace('!',  '') #Убираем '!'
    wrong_article = wrong_article.split(SPLIT_SYMBOL) #Сплитим
    reversed_sentences = [sentence[::-1] for sentence in wrong_article] #Разворачиваем
    wrong_article = SPLIT_SYMBOL.join(reversed_sentences) #Соединяем
    wrong_article = wrong_article.lower() #Понижаем
    wrong_article = wrong_article.replace('woof-woof', 'cat') #Я бы про собак и оставил
    lines = wrong_article.split(SPLIT_SYMBOL) #Выделяем отдельные лайны
    wrong_article = [line.capitalize() for line in lines] #Капитализируем первые буквы
    wrong_article = SPLIT_SYMBOL.join(wrong_article) #Вуаля
    return wrong_article