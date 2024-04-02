from telebot import types


def menu_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    k1 = types.KeyboardButton(text="Профиль")
    k2 = types.KeyboardButton(text="Доход")
    k3 = types.KeyboardButton(text="Расход")
    k4 = types.KeyboardButton(text="График")
    k5 = types.KeyboardButton(text="Поддержка")

    markup.row(k1)
    markup.row(k2, k3)
    markup.row(k4)
    markup.row(k5)

    return markup

def income_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    k1 = types.KeyboardButton(text="Зарплата")
    k2 = types.KeyboardButton(text="Родственники")
    k3 = types.KeyboardButton(text="Пассивный доход")
    k4 = types.KeyboardButton(text="Аренда недвижимости")
    k5 = types.KeyboardButton(text="Инвестиции")
    k6 = types.KeyboardButton(text="Фриланс")
    k7 = types.KeyboardButton(text="Бизнес")
    k8 = types.KeyboardButton(text="Пенсия")
    k9 = types.KeyboardButton(text="Стипендия")
    k10 = types.KeyboardButton(text="Другое")
    k11 = types.KeyboardButton(text="Отмена")

    markup.row(k1, k2)
    markup.row(k3, k4)
    markup.row(k5, k6)
    markup.row(k7, k8)
    markup.row(k9, k10)
    markup.row(k11)

    return markup

def expense_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    k1 = types.KeyboardButton(text="Проезд")
    k2 = types.KeyboardButton(text="Одежда и обувь")
    k3 = types.KeyboardButton(text="Питание и продукты")
    k4 = types.KeyboardButton(text="Рестораны и кафе")
    k5 = types.KeyboardButton(text="Развлечения и хобби")
    k6 = types.KeyboardButton(text="Путешествия и отпуск")
    k7 = types.KeyboardButton(text="Коммунальные услуги")
    k8 = types.KeyboardButton(text="Здоровье и медицина")
    k9 = types.KeyboardButton(text="Красота и уход")
    k10 = types.KeyboardButton(text="Спорт и фитнес")
    k11 = types.KeyboardButton(text="Образование")
    k12 = types.KeyboardButton(text="Техника и электроника")
    k13 = types.KeyboardButton(text="Домашние животные")
    k14 = types.KeyboardButton(text="Страхование и финансовые услуги")
    k15 = types.KeyboardButton(text="Хозяйственные товары")
    k16 = types.KeyboardButton(text="Подарки и праздники")
    k17 = types.KeyboardButton(text="Транспортные услуги")
    k18 = types.KeyboardButton(text="Коммуникации и интернет")
    k19 = types.KeyboardButton(text="Ремонт и обслуживание")
    k20 = types.KeyboardButton(text="Прочее")
    k21 = types.KeyboardButton(text="Отмена")

    markup.row(k1, k2, k3, k4)
    markup.row(k5, k6, k7, k8)
    markup.row(k9, k10, k11, k12)
    markup.row(k13, k14, k15, k16)
    markup.row(k17, k18, k19, k20)
    markup.row(k21)

    return markup



def chart_button():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    k1 = types.KeyboardButton(text="График доходов")
    k2 = types.KeyboardButton(text="График расходов")
    k3 = types.KeyboardButton(text="Отмена")

    markup.row(k1, k2)
    markup.row(k3)

    return markup