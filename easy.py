from telebot import TeleBot
import random
from telebot import types
import asyncio
from googletrans import Translator

bot = TeleBot('7563200872:AAHLhJsQi2w8Q7B0RWdVt4AI8aaOWIqNjMA')
p = []
q = ['Психология', 'Космос', 'Технологии', 'Природа', 'История']
d = {'Психология': 'Один из самых любопытных эффектов в психологии — это эффект плацебо. '
                   'Он заключается в том, что если человек искренне верит, что принимает лекарство, даже если это просто пустышка (например, сахарная таблетка), его состояние может реально улучшиться. '
                   'Мозг, считая, что организму помогают, запускает физиологические процессы самовосстановления. '
                   'В экспериментах было замечено, что даже цвет и форма таблетки могут влиять на эффективность плацебо. Например, синие таблетки ассоциируются с успокоением, а красные — с бодростью. '
                   'Это говорит о том, насколько сильно наше восприятие и ожидания могут влиять на объективные процессы в организме.',
     'Космос': 'Космос — это место невероятных парадоксов и условий, полностью отличающихся от земных. '
               'Например, в открытом космосе невозможно услышать звук, потому что там нет воздуха или другого вещества, через которое звук может передаваться. '
               'А ещё существуют так называемые "горячие льды" — планеты, на которых вода находится в состоянии льда, несмотря на температуру в сотни градусов по Цельсию, из-за экстремального давления. '
               'Один из самых удивительных объектов во Вселенной — это нейтронные звёзды. Они образуются после взрыва сверхновой и обладают настолько высокой плотностью, что чайная ложка вещества из нейтронной звезды весила бы около миллиарда тонн. '
               'Это вес сопоставим с массой всей горы Эверест!',
     'Технологии': 'Технологии развиваются с невероятной скоростью, и один из самых ярких примеров — искусственный интеллект. '
                   'Ещё 20 лет назад казалось фантастикой, что компьютер сможет распознавать речь или обыгрывать человека в шахматы. '
                   'Сегодня же ИИ способен генерировать тексты, распознавать лица, переводить языки в реальном времени и даже сочинять музыку. '
                   'Один из самых интересных проектов последних лет — это нейросети, такие как GPT, которые обучаются на огромных объёмах информации и способны вести диалог, анализировать тексты и даже помогать в программировании. '
                   'В будущем развитие искусственного интеллекта, вероятно, кардинально изменит рынок труда, медицину, образование и другие ключевые сферы.',
     'Природа': 'В мире природы множество удивительных явлений, которые поражают воображение. '
                'Например, существует так называемое "биолюминесцентное" свечение — способность некоторых живых организмов излучать свет. '
                'Это явление можно наблюдать у светлячков, некоторых видов грибов и морских организмов, таких как планктон. '
                'На пляжах Мальдив и в некоторых регионах Азии ночью можно увидеть, как волны светятся голубым светом — это миллиарды микроорганизмов реагируют на движение воды. '
                'Ещё один интересный факт: деревья в лесу способны "общаться" друг с другом через корневую систему, используя грибковую сеть, известную как микориза. '
                'С помощью этой сети деревья могут обмениваться питательными веществами и даже "предупреждать" друг друга об угрозах, например, о вредителях.',
     'История': 'История полна удивительных и часто малоизвестных фактов. '
                'Например, в Древнем Египте врачи были настолько специализировавшимися, что один лечил только глаза, другой — только зубы, и так далее. '
                'А в средневековой Европе существовала практика "живых шахмат" — когда вместо фигур на шахматной доске выступали люди, а проигравшие "фигуры" часто реально сражались или подвергались наказаниям. '
                'Также в Древнем Риме существовали граффити, очень похожие на современные: на стенах домов оставляли надписи с жалобами, шутками или политическими лозунгами. '
                'Некоторые из них дошли до наших дней, например: "Я удивляюсь, о стенка, что ты не развалилась от количества написанного на тебе!" Эти детали позволяют нам почувствовать, насколько люди прошлого были похожи на нас.'}

x = 0
v = 0
qwerty = 0
qwerty1 = 0
qwerty2 = 0
hex = 0
prev = 0


def qxx0(message):
    global qwerty
    qwerty = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да.1')
    btn2 = types.KeyboardButton('Нет.1')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Является ли эффект плацебо примером влияния убеждений на физиологию?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, qxx1)


def qxx1(message):
    qx0(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да.2')
    btn2 = types.KeyboardButton('Нет.2')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Входит ли эффект плацебо в стандартную практику клинических испытаний?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, qxx2)


def qxx2(message):
    qx0(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да.3')
    btn2 = types.KeyboardButton('Нет.3')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Помогает ли плацебо всегда, независимо от ожиданий пациента?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, qxx3)


def qxx3(message):
    qx0(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да.4')
    btn2 = types.KeyboardButton('Нет.4')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Уложатся ли люди в среднем более чем 10 объектов в кратковременную память?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, qxx4)


pl = 0


def qxx4(message):
    global v, pl
    qx0(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Синий')
    btn2 = types.KeyboardButton('Красный')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Какой цвет таблетки чаще ассоциируется с бодростью?',
                     reply_markup=markup)
    pl = 1
    bot.register_next_step_handler(message, qx0)


def new(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/Again')
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Еще больше очень полезной информации?',
                     reply_markup=markup)


def rev0(message):
    global qwerty1
    qwerty1 = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, конечно')
    btn2 = types.KeyboardButton('Нет, конечно')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Есть ли звук в открытом космосе?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, rev1)


def rev1(message):
    qx1(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Вращается ли Венера в ту же сторону, что и Земля?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, rev2)


def rev2(message):
    qx1(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, естественно')
    btn2 = types.KeyboardButton('Нет, естественно')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Может ли лёд существовать при температуре выше 100 °C при высоком давлении?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, rev3)


def rev3(message):
    qx1(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Эверест')
    btn2 = types.KeyboardButton('Нейтроны')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Что весит больше: чайная ложка вещества с нейтронной звезды или Эверест?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, rev4)


pl1 = 0


def rev4(message):
    global pl1
    qx1(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Нейтронная')
    btn2 = types.KeyboardButton('Сверхновая')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Какой тип звезды формируется после взрыва сверхновой??',
                     reply_markup=markup)
    pl1 = 1
    bot.register_next_step_handler(message, qx1)


def uwu0(message):
    global qwerty2
    qwerty2 = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, больше')
    btn2 = types.KeyboardButton('Нет, меньше')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Больше ли весил первый жёсткий диск, чем современный холодильник?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, uwu1)


def uwu1(message):
    qx2(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, можно')
    btn2 = types.KeyboardButton('Нет, нельзя')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Можно ли было хранить фильмы на диске IBM 1956 года?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, uwu2)


def uwu2(message):
    qx2(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Используется ли ИИ для перевода текста?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, uwu3)


def uwu3(message):
    qx2(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Gpt')
    btn2 = types.KeyboardButton('Gtp')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Назови один пример технологии ИИ',
                     reply_markup=markup)
    bot.register_next_step_handler(message, uwu4)


pl2 = 0


def uwu4(message):
    global pl2
    qx2(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, конечно')
    btn2 = types.KeyboardButton('Нет, человек совершенен')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Существует ли ИИ, способный обыгрывать человека в шахматы?',
                     reply_markup=markup)
    pl2 = 1
    bot.register_next_step_handler(message, qx2)


def gop0(message):
    global qwerty2
    qwerty2 = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, естественно')
    btn2 = types.KeyboardButton('Нет, естественно')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Может ли бамбук вырасти почти на метр за сутки?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, gop1)


def gop1(message):
    qx3(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, конечно')
    btn2 = types.KeyboardButton('Нет, конечно')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Светятся ли некоторые микроорганизмы в океане?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, gop2)


def gop2(message):
    qx3(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Думаю да')
    btn2 = types.KeyboardButton('Определенно нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Является ли микориза грибом?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, gop3)


def gop3(message):
    qx3(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Конечно')
    btn2 = types.KeyboardButton('Ну не')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Могут ли деревья передавать друг другу сигналы о вредителях?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, gop4)


def gop4(message):
    global pl2
    qx3(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Биолюминесценция наблюдается только на суше?',
                     reply_markup=markup)
    pl2 = 1
    bot.register_next_step_handler(message, qx3)


def lpl0(message):
    global qwerty2
    qwerty2 = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Естественно')
    btn2 = types.KeyboardButton('Естественно нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Были ли в Древнем Риме специализированные врачи?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, lpl1)


def lpl1(message):
    qx4(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да')
    btn2 = types.KeyboardButton('Нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Являются ли "живые шахматы" из Средневековья компьютерной игрой?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, lpl2)


def lpl2(message):
    qx4(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Да, конечно!')
    btn2 = types.KeyboardButton('Нет, конечно?')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Существовали ли древние аналоги современных граффити?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, lpl3)


def lpl3(message):
    qx4(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Yes')
    btn2 = types.KeyboardButton('Noo')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Писали ли римляне надписи прямо на стенах домов?',
                     reply_markup=markup)
    bot.register_next_step_handler(message, lpl4)


def lpl4(message):
    global pl2
    qx4(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Думаю да')
    btn2 = types.KeyboardButton('Думаю нет')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Использовали ли египтяне письменность?',
                     reply_markup=markup)
    pl2 = 1
    bot.register_next_step_handler(message, qx4)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}!')
    bot.send_message(message.chat.id,
                     f'Этот бот является источником полезной информации, которую ты будешь получать каждый день, закрепляя полученные знания на тестах')
    dexter(message)


def dexter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/Russian')
    btn2 = types.KeyboardButton('/English')
    btn3 = types.KeyboardButton('/French')
    btn4 = types.KeyboardButton('/Japanese')
    btn5 = types.KeyboardButton('/German')
    btn6 = types.KeyboardButton('/Chinese')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id,
                     f'Можете выбрать язык, на котором будет представлен текст, но вопросы будут на отечественном',
                     reply_markup=markup)


@bot.message_handler(commands=["Russian"])
def z1(message):
    global hex
    hex = 'ru'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Lets_go")
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Начнем?', reply_markup=markup)


@bot.message_handler(commands=["English"])
def z2(message):
    global hex
    hex = 'en'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Lets_go")
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Начнем?', reply_markup=markup)


@bot.message_handler(commands=["French"])
def z3(message):
    global hex
    hex = 'fr'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Lets_go")
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Начнем?', reply_markup=markup)


@bot.message_handler(commands=["Japanese"])
def z4(message):
    global hex
    hex = 'ja'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Lets_go")
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Начнем?', reply_markup=markup)


@bot.message_handler(commands=["German"])
def z5(message):
    global hex
    hex = 'de'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Lets_go")
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Начнем?', reply_markup=markup)


@bot.message_handler(commands=["Chinese"])
def z6(message):
    global hex
    hex = 'zh-cn'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/Lets_go")
    btn2 = types.KeyboardButton('/No_thanks')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Начнем?', reply_markup=markup)


@bot.message_handler(commands=["Lets_go"])
def go(message):
    global x
    global hex
    global prev
    x = random.randint(0, 4)
    prev = d[q[x]]

    async def tranz():
        global hex, prev
        async with Translator() as translator:
            result = await translator.translate(prev, src="ru", dest=f'{hex}')
            bot.send_message(message.chat.id, result.text)

    asyncio.run(tranz())
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/Of_course')
    btn2 = types.KeyboardButton('/Not_good')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Готовы пройти тест?', reply_markup=markup)


@bot.message_handler(commands=['Again'])
def new1(message):
    dexter(message)


@bot.message_handler(commands=["Of_course"])
def go1(message):
    global x
    if x == 0:
        qx0(message)
    elif x == 1:
        qx1(message)
    elif x == 2:
        qx2(message)
    elif x == 3:
        qx3(message)
    elif x == 4:
        qx4(message)


@bot.message_handler(commands=["Not_good"])
def fu(message):
    bot.send_message(message.chat.id, f'Ну ладно, хорошего дня!')
    new(message)


@bot.message_handler(commands=["No_thanks"])
def noo(message):
    bot.send_message(message.chat.id, f'Значит в другой раз, пока!')


@bot.message_handler(commands=["stop"])
def kill(message):
    bot.send_message(message.chat.id, f'Пока!')
    bot.stop_polling()


@bot.message_handler(content_types=['text'])
def qx4(message):
    global x
    global v
    global qwerty2, pl2
    if qwerty2 != 1:
        lpl0(message)
    if message.text == 'Естественно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Естественно нет':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Да, конечно!':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет, конечно?':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Yes':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Noo':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Думаю да':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Думаю нет':
        bot.send_message(message.chat.id, f'Неверно')
    if pl2 == 1:
        bot.send_message(message.chat.id, f'Итог: {v} верных ответов!')
        v = 0
        qwerty2 = 0
        pl2 = 0
        new(message)


def qx3(message):
    global x
    global v
    global qwerty2, pl2
    if qwerty2 != 1:
        gop0(message)
    if message.text == 'Да, естественно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет, естественно':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Да, конечно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет, конечно':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Определенно нет':
        bot.send_message(message.chat.id, f'Верно')
        bot.send_message(message.chat.id, f'(Это грибковая сеть)')
        v += 1
    elif message.text == 'Думаю да':
        bot.send_message(message.chat.id, f'Неверно')
        bot.send_message(message.chat.id, f'(Это грибковая сеть)')
    elif message.text == 'Конечно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Ну не':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да':
        bot.send_message(message.chat.id, f'Неверно')
    if pl2 == 1:
        bot.send_message(message.chat.id, f'Итог: {v} верных ответов!')
        v = 0
        qwerty2 = 0
        pl2 = 0
        new(message)


def qx2(message):
    global x
    global v
    global qwerty2, pl2
    if qwerty2 != 1:
        uwu0(message)
    if message.text == 'Да, больше':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет, меньше':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нет, нельзя':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да, можно':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Gpt':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Gtp':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Да, конечно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет, человек совершенен':
        bot.send_message(message.chat.id, f'Неверно')
    if pl2 == 1:
        bot.send_message(message.chat.id, f'Итог: {v} верных ответов!')
        v = 0
        qwerty2 = 0
        pl2 = 0
        new(message)


def qx1(message):
    global x
    global v
    global qwerty1, pl1
    if qwerty1 != 1:
        rev0(message)
    if message.text == 'Нет, конечно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да, конечно':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Да, естественно':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет, естественно':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нейтроны':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Эверест':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нейтронная':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Сверхновая':
        bot.send_message(message.chat.id, f'Неверно')
    if pl1 == 1:
        bot.send_message(message.chat.id, f'Итог: {v} верных ответов!')
        v = 0
        qwerty1 = 0
        pl1 = 0
        new(message)


def qx0(message):
    global x
    global v, pl
    global qwerty
    if qwerty != 1:
        qxx0(message)
    if message.text == 'Да.1':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет.1':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Да.2':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Нет.2':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нет.3':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да.3':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Нет.4':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Да.4':
        bot.send_message(message.chat.id, f'Неверно')
    elif message.text == 'Красный':
        bot.send_message(message.chat.id, f'Верно')
        v += 1
    elif message.text == 'Синий':
        bot.send_message(message.chat.id, f'Неверно')
    if pl == 1:
        bot.send_message(message.chat.id, f'Итог: {v} верных ответов!')
        v = 0
        qwerty = 0
        pl = 0
        new(message)


bot.polling(none_stop=True)

# @eassssy_learn_bot
# (чтобы бот работал, код нужно запустить, я не выкладывала на хостинг)
