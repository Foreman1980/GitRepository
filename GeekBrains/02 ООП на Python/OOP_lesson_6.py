# ООП на Python (урок № 6):
# Это задание продолжает практическое задание прошлого урока. За основу возьмите свой код с классами Word и Sentence.
# Выполним с ним следующие преобразования:
# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»). Для класса Noun укажите значение по
# умолчанию «сущ» (сокращение от существительное), а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию
# и сделайте свойство grammar защищённым.
# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
# Подсказка: теперь в нём не нужно хранить части речи.
# words = []
# words.append(Noun("собака"))
# words.append(Verb("ела"))
# words.append(Noun("колбасу"))
# words.append(Noun("кот"))
# По желанию добавьте ещё несколько глаголов и существительных.
# 5. Протестируйте работу старого метода show класса Sentence. Если предложения не формируются, исправьте ошибки.
# 6. Допишите в классы Noun и Verb метод part. Данный метод должен возвращать строку с полным названием части речи.
# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
# Подсказка: ранее part был свойством класса Word, а теперь это метод классов Noun и Verb.

# Удаляем свойство класса "part" созданное в д/з предыдущего урока
class Word:
    
    text = '' # не обязательно здесь писать это свойство
    
    def __init__(self, text=text):
        self.text = text


class Sentence:
    
    content = [] # не обязательно здесь писать это свойство
    
    def __init__(self, content=content):
        self.content = content
        
    def show(self, words_list):
        result = ''
        for number in self.content:
            result += words_list[number].text + ' '
        result = result.rstrip()
        return result
    
#   def show_parts(self, words_list):
#       result = ''
#       for number in self.content:
#           result += words_list[number]._grammar + ' '
#       result = result.rstrip()
#       return result
# Исправлено после разбоа д/з:
    def show_parts(self, words_list):
        result = ''
        for number in self.content:
            if words_list[number].part() not in result:
                result += words_list[number].part() + ' '
        result = result.rstrip()
        return result

# Создаём два новых класса, для пробы в оба класса добавим метод '__str__'
class Noun(Word):
    _grammar = 'сущ'
    __full_grammar = 'существительное'
    
    def __init__(self, text):
        self.text = text
        
    def part(self):
        return self.__full_grammar
    
    def __str__(self):
        return self._grammar


class Verb(Word):
    _grammar = 'гл'
    __full_grammar = 'глагол'
    
    def __init__(self, text):
        self.text = text
            
    def part(self):
        return self.__full_grammar
    
    def __str__(self):
        return self._grammar


words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))
words.append(Verb("ел"))
words.append(Noun("сосиску"))

my_sentence = Sentence([0, 1, 5])

# Проверка метода "show()"
print(my_sentence.show(words))
# Вывод вида - "собака ела сосиску"

dog = Noun("собака")
print(type(dog), dog)
# Вывод вида - "<class '__main__.Noun'> сущ"

# Проверка метода "part()"
print(dog.part())
# Вывод вида - "существительное"

ate = Verb('ела')
print(type(ate), ate)
# Вывод вида - "<class '__main__.Verb'> гл"

# Проверка метода "part()"
print(ate.part())
# Вывод вида - "глагол"

# Проверка метода "show_parts()"
print(my_sentence.show_parts(words))
# Вывод вида - "сущ гл сущ"
# Исправлено после разбоа д/з:
# Вывод вида - "существительное глагол"