import telebot

bot = telebot.TeleBot('1245954623:AAE_cqLoDBXhNChwXQqPp4AshXJiUQaD5mw')

from telebot import types
@bot.message_handler(commands=["start"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="/Гитары")
    btn3 = types.KeyboardButton(text="/Ударные")
    btn4 = types.KeyboardButton(text="/Смычковые")
    btn5 = types.KeyboardButton(text="/Клавишные")
    btn6 = types.KeyboardButton(text="/Аксессуары")
    btn7 = types.KeyboardButton(text="/Гитарное_оборудование")
    keyboard.add(btn1,  btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Назад"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="/Гитары")
    btn3 = types.KeyboardButton(text="/Ударные")
    btn4 = types.KeyboardButton(text="/Смычковые")
    btn5 = types.KeyboardButton(text="/Клавишные")
    btn6 = types.KeyboardButton(text="/Аксессуары")
    btn7 = types.KeyboardButton(text="/Гитарное_оборудование")
    keyboard.add(btn1,  btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["/Назад"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="/Струны_для_гитар")
    btn2 = types.KeyboardButton(text="/Медиаторы")
    #btn3 = types.KeyboardButton(text="Звукосниматели")
    btn4 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2,  btn4)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Струны_для_гитар"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Струны для баса")
    btn2 = types.KeyboardButton(text="Струны для электрогит.")
    btn3 = types.KeyboardButton(text="Струны для акустической гитары")
    btn4 = types.KeyboardButton(text="Струны для классической гитары")
    btn5 = types.KeyboardButton(text="Струны для укулеле")
    btn6 = types.KeyboardButton(text="//Назад")
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Гитарное_оборудование"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="/Струны_для_гитар")
    btn2 = types.KeyboardButton(text="/Медиаторы")
    #btn3 = types.KeyboardButton(text="Звукосниматели")
    btn4 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn4)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Медиаторы"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="0.50мм")
    btn2 = types.KeyboardButton(text="0.60мм")
    btn3 = types.KeyboardButton(text="0.73мм")
    btn4 = types.KeyboardButton(text="0.88мм")
    btn5 = types.KeyboardButton(text="1.00мм")
    btn6 = types.KeyboardButton(text="1.14мм")
    btn7 = types.KeyboardButton(text="1.50мм")
    btn8 = types.KeyboardButton(text="2.00мм")
    btn9 = types.KeyboardButton(text="3.00мм")
    btn10 = types.KeyboardButton(text="//Назад")
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Ударные"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Электронные барабаны")
    btn2 = types.KeyboardButton(text="Акустические барабаны")
    btn3 = types.KeyboardButton(text="Перкуссия")
    btn4 = types.KeyboardButton(text="Тарелки для ударных")
    btn5 = types.KeyboardButton(text="Барабанные палочки")
    btn6 = types.KeyboardButton(text="Пластики")
    btn7 = types.KeyboardButton(text="Стойки и механика")
    btn8 = types.KeyboardButton(text="Педали для бас-барабана")
    btn9 = types.KeyboardButton(text="Аксессуары для ударных")
    btn10 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Смычковые"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Скрипки")
    btn2 = types.KeyboardButton(text="Виолончели")
    btn3 = types.KeyboardButton(text="Струны для смычковых")
    btn4 = types.KeyboardButton(text="Аксессуары для смычковых")
    btn5 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Клавишные"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Синтезаторы")
    btn2 = types.KeyboardButton(text="Цифровые пианино")
    btn3 = types.KeyboardButton(text="Аксессуары для клав. инструментов")
    btn4 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Аксессуары"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Тюнеры")
    btn2 = types.KeyboardButton(text="Метрономы")
    btn3 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Гитары"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Акустические гитары")
    btn2 = types.KeyboardButton(text="Классические гитары")
    btn3 = types.KeyboardButton(text="Электрогитары")
    btn4 = types.KeyboardButton(text="Укулеле")
    btn5 = types.KeyboardButton(text="Электро-акустические гитары")
    btn6 = types.KeyboardButton(text="Бас-гитары")
    btn7 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Акустические гитары":
        #photo/PARKSONS_JB4111C
        photo = open('Guitars/PARKSONS_JB4111C_Black_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/PARKSONS_JB4111C
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111С(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111s-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        #photo/parksons_jb411
        photo = open('Guitars/parksons_jb411_black_front.jpg','rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/parksons_jb411
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111 BLACK(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        #photo/AD810_LH_OP
        photo = open('Guitars/AD810_LH_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/AD810_LH_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810LH OP(3 591,00 грн)", url="https://muzon.com.ua/product/cort-ad810lh-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.",reply_markup=keyboard)
        #photo/fg800-nt-main-yamaha
        photo = open('Guitars/fg800-nt-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/fg800-nt-main-yamaha
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA FG800 (NT)(8 832,00 грн)",url="https://muzon.com.ua/product/yamaha-fg800-nt/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Легендарная гитара от известного бренда Yamaha, имеет отличное звучание, качественную сборку, за не высокую стоимость. Каждая деталь гитары FG создана для того, чтобы сделать ее еще лучше.", reply_markup=keyboard)
        #photo/fg800-bs-main-yamaha
        photo = open('Guitars/fg800-bs-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/fg800-bs-main-yamaha
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA FG800 (BS)(8 832,00 грн)", url="https://muzon.com.ua/product/yamaha-fg800-bs/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Легендарная гитара от известного бренда Yamaha, имеет отличное звучание, качественную сборку, за не высокую стоимость. Каждая деталь гитары FG создана для того, чтобы сделать ее еще лучше.", reply_markup=keyboard)
        #photo/PARKSONS JB4111С SUNBURST
        photo = open('Guitars/PARKSONS_JB4111C_Sunburst_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/PARKSONS JB4111С SUNBURST
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111С SUNBURST(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111s-sunburst/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/PARKSONS JB4111С NATURAL
        photo = open('Guitars/PARKSONS_JB4111C_Natural_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PARKSONS JB4111С NATURAL
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111С NATURAL(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111s-natural/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/parksons_jb4111_natural
        photo = open('Guitars/parksons_jb4111_natural.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_jb4111_natural
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111 NATURAL(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111-natural/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/parksons_jb4111_sunburst
        photo = open('Guitars/parksons_jb4111_sunburst.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_jb4111_sunburst
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111 SUNBURST(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111-sunburst/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/AD810_12_OP
        photo = open('Guitars/AD810_12_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with button/AD810_12_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810-12 OP(4 057,00 грн)", url="https://muzon.com.ua/product/cort-ad810-12-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Корпус AD810-12 OP выполнен из ели и красного дерева, данный инструмент является наилучшим выбором для начинающих гитаристов, этому соответствует не высокая стоимость и отличное качество инструмента...", reply_markup=keyboard)
        # photo/AD810_SSB
        photo = open('Guitars/AD810_SSB.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AD810_SSB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810 SSB(2 699,00 грн)", url="https://muzon.com.ua/product/cort-ad810-ssb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/AD810m_op
        photo = open('Guitars/AD810m_op.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AD810m_op
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810M OP(2 799,00 грн)", url="https://muzon.com.ua/product/cort-ad810m-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
    if message.text == "Классические гитары":
        # photo/AC100_OP
        photo = open('Guitars/AC100_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC100_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AC100 OP(2 499,00 грн)", url="https://muzon.com.ua/product/cort-ac100-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/AC50op-main-cort
        photo = open('Guitars/AC50op-main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC50op-main-cort
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CORT AC50 OP W/BAG(3 458,00 грн)", url="https://muzon.com.ua/product/cort-ac50-op-w-bag/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/yamaha_c_70
        photo = open('Guitars/yamaha_c_70.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/yamaha_c_70
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C70(4 206,00 грн)", url="https://muzon.com.ua/product/yamaha-c7/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, великолепное звучание, яркий резонанс.", reply_markup=keyboard)
        # photo/yamaha_c_40_b
        photo = open('Guitars/yamaha_c_40_b.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/yamaha_c_40_b
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C40B(4 146,00 грн)", url="https://muzon.com.ua/product/yamaha-c40b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/yamaha_c_40_m
        photo = open('Guitars/yamaha_c_40_m.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/yamaha_c_40_m
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C40M(3 207,00 грн)", url="https://muzon.com.ua/product/yamaha-c40-kopirovat/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/Yamaha_C_40
        photo = open('Guitars/Yamaha_C_40.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha_C_40
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C40(3 207,00 грн)", url="https://muzon.com.ua/product/yamaha-c40/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/AC100DX_OP
        photo = open('Guitars/AC100DX_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC100DX_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AC100DX OP(3 292,00 грн)", url="https://muzon.com.ua/product/cort-ac100dx-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/AC100_SG
        photo = open('Guitars/AC100_SG.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC100_SG
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AC100 SG(2 699,00 грн)", url="https://muzon.com.ua/product/cort-ac100-sg/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
    if message.text == "Укулеле":
        # photo/parksons_uk_24_c
        photo = open('Guitars/parksons_uk_24_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_24_c
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK24C(1 572,00 грн)", url="https://muzon.com.ua/product/parksons-uk24c/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
        # photo/fzone_fzu_110_m
        photo = open('Guitars/fzone_fzu_110_m.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/fzone_fzu_110_m
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Fzone FZU 110M(1 415,00 грн)", url="https://muzon.com.ua/product/fzone-fzu-110m/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Fzone изготовлена из качественных материалов, обладает глубоким и ярким звучанием.", reply_markup=keyboard)
        # photo/parksons_uk_24_z_front
        photo = open('Guitars/parksons_uk_24_z_front.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_24_z_front
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK24Z(1 750,00 грн)", url="https://muzon.com.ua/product/parksons-uk24z/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
        # photo/parksons_uk_21_z
        photo = open('Guitars/parksons_uk_21_z.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_21_z
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK21Z(1 668,00 грн)", url="https://muzon.com.ua/product/parksons-uk21z/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
        # photo/parksons_uk_21_c-1
        photo = open('Guitars/parksons_uk_21_c-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_21_c-1
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK21C(1 445,00 грн)", url="https://muzon.com.ua/product/parksons-uk21c/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
    if message.text == "Электрогитары":
        # photo/rgx121z-fs-yamaha-main
        photo = open('Guitars/rgx121z-fs-yamaha-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/rgx121z-fs-yamaha-main
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha RGX121Z (Flat Silver)(8 892,00 грн)", url="https://muzon.com.ua/product/yamaha-rgx121z-flat-silver/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Корпус гитары выполнен из ольхи в сочетании с мощным хамбакером и двумя синглами, инструмент имеет выразительную палитру красок классического и рок звучания.", reply_markup=keyboard)
        # photo/YAMAHA-PACIFICA-012-DBM
        photo = open('Guitars/YAMAHA-PACIFICA-012-DBM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA-PACIFICA-012-DBM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PACIFICA 012 (DBM)(7 200,00 грн)", url="https://muzon.com.ua/product/yamaha-pacifica-012-dbm/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA Pacifica 012 характеризуется аналогичными контурами корпуса как у более дорогих моделей PAC112, мощным хамбакером и 2-мя синглами, обеспечивающими чистое звучание. Гитара оснащена удобным грифом,", reply_markup=keyboard)
        # photo/Yamaha PACIFICA 112J (LPB)
        photo = open('Guitars/PAC112J-LPB-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha PACIFICA 112J (LPB)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha PACIFICA 112J (LPB)(9 132,00 грн)", url="https://muzon.com.ua/product/yamaha-pacifica-112j-lpb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Корпус гитары выполнен из ольхи в сочетании с мощным хамбакером и двумя синглами, инструмент имеет выразительную палитру красок классического и рок звучания.", reply_markup=keyboard)
        # photo/KX100MA-main-cort
        photo = open('Guitars/KX100MA-main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/KX100MA-main-cort
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort KX100 METALLIC ASH(6 020,00 грн)", url="https://muzon.com.ua/product/cort-kx100-metallic-ash/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия KX имеет дизайн совместивший в себе как агрессивную внешность, так и утонченную классику, звук подходящий для разных стилей и направлений.", reply_markup=keyboard)
        # photo/Cort KX100 IRON OXIDE
        photo = open('Guitars/KX100IO_main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort KX100 IRON OXIDE
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort KX100 IRON OXIDE(6 020,00 грн)", url="https://muzon.com.ua/product/cort-kx100-iron-oxide/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "ерия KX имеет дизайн совместивший в себе как агрессивную внешность, так и утонченную классику, звук подходящий для разных стилей и направлений.", reply_markup=keyboard)
        # photo/cort_cr_200_bk
        photo = open('Guitars/cort_cr_200_bk.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/cort_cr_200_bk
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort CR200 BK(9 800,00 грн)", url="https://muzon.com.ua/product/cort-cr200-bk/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия CR — инструменты этой линейки имеют винтажный классический дизайн, отлично выполнены и обладают хорошим звучанием!", reply_markup=keyboard)
        # photo/Cort CR150 ODS
        photo = open('Guitars/CR150ODS_main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort CR150 ODS
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort CR150 ODS(8 050,00 грн)", url="https://muzon.com.ua/product/cort-cr150-ods/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Высокое качество материалов и отделки, универсальный инструмент для разных стилей исполнения.", reply_markup=keyboard)
        # photo/Cort G110 2T
        photo = open('Guitars/cort_g_110_2t.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G110 2T
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G110 2T(4 830,00 грн)", url="https://muzon.com.ua/product/cort-g110-2t/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности, надежность и качество за доступную цену.", reply_markup=keyboard)
        # photo/Cort X100 OPB
        photo = open('Guitars/cort_x_100_opb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort X100 OPB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort X100 OPB(4 550,00 грн)", url="https://muzon.com.ua/product/cort-x100-opb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия X представляет линейку инструментов Cort предназначенных для рок/металл жанров музыки, это подчеркивает дизайн инструмента и электронная начинка", reply_markup=keyboard)
        # photo/Cort X100 OPBB
        photo = open('Guitars/cort_x_100_opbb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort X100 OPBB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort X100 OPBB(4 550,00 грн)", url="https://muzon.com.ua/product/cort-x100-opbcb-kopirovat/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия X представляет линейку инструментов Cort предназначенных для рок/металл жанров музыки, это подчеркивает дизайн инструмента и электронная начинка", reply_markup=keyboard)
        # photo/Cort X100 OPBCB
        photo = open('Guitars/cort_x_100_opbcb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort X100 OPBCB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort X100 OPBCB(4 550,00 грн)", url="https://muzon.com.ua/product/cort-x100-opbcb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия X представляет линейку инструментов Cort предназначенных для рок/металл жанров музыки, это подчеркивает дизайн инструмента и электронная начинка", reply_markup=keyboard)
        # photo/Cort G110 SRD
        photo = open('Guitars/cort_g_110_srd.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G110 SRD
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G110 SRD(4 690,00 грн)", url="https://muzon.com.ua/product/cort-g110-srd/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G110 BK
        photo = open('Guitars/cort_g_110_bk.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G110 BK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G110 BK(4 690,00 грн)", url="https://muzon.com.ua/product/cort-g110-bk/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G100 OPBC
        photo = open('Guitars/cort_g100_opbc.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G100 OPBC
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G100 OPBC(3 920,00 грн)", url="https://muzon.com.ua/product/cort-g100-opbc-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G100 OPW
        photo = open('Guitars/cort_g100_opw.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G100 OPW
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G100 OPW(3 920,00 грн)", url="https://muzon.com.ua/product/cort-g100-opbc/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G100 OPB
        photo = open('Guitars/cort_g100_opb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G100 OPB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G100 OPB(3 920,00 грн)", url="https://muzon.com.ua/product/cort-g100-opb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
    if message.text == "Электро-акустические гитары":
        # photo/Cort AD810E OP
        photo = open('Guitars/cort_ad_810e_op.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort AD810E OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810E OP(4 323,00 грн)", url="https://muzon.com.ua/product/cort-ad810e-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/CORT SFX-ME OP
        photo = open('Guitars/SFX-MEOP-main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CORT SFX-ME OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CORT SFX-ME OP(4 795,00 грн)", url="https://muzon.com.ua/product/cort-sfx-me-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/Cort AD810E BKS
        photo = open('Guitars/cort_ad_810e_bks.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort AD810E BKS
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810E BKS(4 522,00 грн)", url="https://muzon.com.ua/product/cort-ad810e-bks/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
    if message.text == "Бас-гитары":
        # photo/Yamaha TRBX-174 OVS
        photo = open('Guitars/trbx174_ovs_f-600x176.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha TRBX-174 OVS
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha TRBX-174 OVS(7 320,00 грн)", url="https://muzon.com.ua/product/yamaha-trbx-174-ovs/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Стильные бас-гитары, в современном дизайне и хорошим звуком. Качество от Yamaha по доступной цене", reply_markup=keyboard)
        # photo/Yamaha TRBX-174 RM
        photo = open('Guitars/yamaha_trbx_174_rm-600x176.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha TRBX-174 RM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha TRBX-174 RM(7 320,00 грн)", url="https://muzon.com.ua/product/yamaha-trbx-174-rm/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Стильные бас-гитары, в современном дизайне и хорошим звуком. Качество от Yamaha по доступной цене", reply_markup=keyboard)
        # photo/Yamaha TRBX-174 BL
        photo = open('Guitars/yamaha_trbx_174_bl-600x176.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha TRBX-174 BL
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha TRBX-174 BL(7 320,00 грн)", url="https://muzon.com.ua/product/yamaha-trbx-174-bl/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Стильные бас-гитары, в современном дизайне и хорошим звуком. Качество от Yamaha по доступной цене", reply_markup=keyboard)
        # photo/Cort Action PJ OPB
        photo = open('Guitars/cort_action_pj_opb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort Action PJ OPB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort Action PJ OPB(4 725,00 грн)", url="https://muzon.com.ua/product/cort-action-pj-opb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия Action отличается высоким качеством и неплохим звуком, за умеренную стоимость. Отличный выбор для обучения", reply_markup=keyboard)
        # photo/Cort Action PJ OPBC
        photo = open('Guitars/cort_action_pj_opbc.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort Action PJ OPBC
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort Action PJ OPBC(4 725,00 грн)", url="https://muzon.com.ua/product/cort-action-pj-opbc/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия Action отличается высоким качеством и неплохим звуком, за умеренную стоимость. Отличный выбор для обучения", reply_markup=keyboard)
    if message.text == "Электронные барабаны":
        # photo/YAMAHA DTX402K
        photo = open('Drums/dtx402k_main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA DTX402K
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA DTX402K(13 437,00 грн)", url="https://muzon.com.ua/product/yamaha-dtx402k/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA DTX402K — электронная ударная установка", reply_markup=keyboard)
        # photo/ALESIS NITRO MESH KIT
        photo = open('Drums/LDLKNitroMeshKit_Ortho_Web_RGB.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/ALESIS NITRO MESH KIT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="ALESIS NITRO MESH KIT(14 700,00 грн)", url="https://muzon.com.ua/product/alesis-nitro-mesh-kit/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "ALESIS NITRO MESH KIT — это полноценная барабанная установка!", reply_markup=keyboard)
        # photo/ALESIS TURBO MESH KIT
        photo = open('Drums/turbo-mesh-kit-ortho-web.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/ALESIS TURBO MESH KIT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="ALESIS TURBO MESH KIT(11 318,00 грн)", url="https://muzon.com.ua/product/alesis-turbo-mesh-kit/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "ALESIS TURBO MESH KIT — это полноценная барабанная установка!", reply_markup=keyboard)
    if message.text == "Акустические барабаны":
        # photo/PDP PDZ522KT Z5 SERIES GREY METAL
        photo = open('Drums/PDP-PDZ522KT-GM-Z5-Series-Grey-Metal-барабаны.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PDP PDZ522KT Z5 SERIES GREY METAL
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PDP PDZ522KT Z5 SERIES GREY METAL(15 288,00 грн)", url="https://muzon.com.ua/product/pdp-pdz522kt-z5-series-grey-metal/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Высокое качество изготовления корпуса и механических деталей, позволяет Z5 Series конкурировать с более дорогими ударными установками.", reply_markup=keyboard)
        # photo/YAMAHA RYDEEN (BLACK GLITTER)
        photo = open('Drums/RDP2F5-BLG-rydeen-front-yam.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA RYDEEN (BLACK GLITTER)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA RYDEEN (BLACK GLITTER)(13 554,00 грн)", url="https://muzon.com.ua/product/yamaha-rydeen-black-glitter/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/YAMAHA RYDEEN (BURGUNDY GLITTER)
        photo = open('Drums/RDP2F5-BGG-main-yamaa.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA RYDEEN (BURGUNDY GLITTER)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA RYDEEN (BURGUNDY GLITTER)(13 554,00 грн)", url="https://muzon.com.ua/product/yamaha-rydeen-burgundy-glitter/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC110 (Red)
        photo = open('Drums/MXC-110-red-2019-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC110 (Red)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC110 (Red)(12 885,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc110-red/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC110 (Black)
        photo = open('Drums/maxtone_mxc_110_black.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC110 (Black)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC110 (Black)(12 885,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc110-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (White)
        photo = open('Drums/MXC3005-1-white.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (White)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (White)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-white/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (Metallic Blue)
        photo = open('Drums/MXC3005-blue-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (Metallic Blue)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (Metallic Blue)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-metallic-blue/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (Wine Red)
        photo = open('Drums/maxtone_mxc3005_red.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (Wine Red)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (Wine Red)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-wine-red/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (Black)
        photo = open('Drums/mxc3005bk-12.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (Black)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (Black)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
    if message.text == "Перкуссия":
        # photo/GON BOPS FS785SB FIESTA
        photo = open('Drums/Bongo-Fiesta-Burnt-Angle-FS785SB.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/GON BOPS FS785SB FIESTA
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="GON BOPS FS785SB FIESTA(2 514,00 грн)", url="https://muzon.com.ua/product/gon-bops-fs785sb-fiesta-bongos-sunburst/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "GON BOPS FS785SB FIESTA BONGOS SUNBURST — деревянные латинские бонги", reply_markup=keyboard)
        # photo/MAXTONE BC13
        photo = open('Drums/MAXTONE-BC13.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE BC13
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE BC13(1 095,00 грн)", url="https://muzon.com.ua/product/maxtone-bc13/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE BC13 — деревянные латинские бонги", reply_markup=keyboard)
        # photo/MAXTONE DJC-1021
        photo = open('Drums/MAXTONEDJC-1021.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DJC-1021
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DJC-1021(4 554,00 грн)", url="https://muzon.com.ua/product/maxtone-djc-1021/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DJC-1021 — джембе барабан", reply_markup=keyboard)
        # photo/MAXTONE ADJ10B
        photo = open('Drums/ADJ_B.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE ADJ10B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE ADJ10B(3 441,00 грн)", url="https://muzon.com.ua/product/maxtone-adj10b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE ADJ10B -деревянный джембе барабан", reply_markup=keyboard)
        # photo/GON BOPS FSCJW FIESTA CAJON WALNUT
        photo = open('Drums/GonBops-FSCJW-Fiesta-cajon-walnut.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/GON BOPS FSCJW FIESTA CAJON WALNUT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="GON BOPS FSCJW FIESTA CAJON WALNUT(3 761,00 грн)", url="https://muzon.com.ua/product/gon-bops-fscjw-fiesta-cajon-walnut/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Gon Bops расширяет модельный ряд кахонов новыми Fiesta моделями — даелая их доступными инструментами для начинающих перкуссионистов", reply_markup=keyboard)
        # photo/GON BOPS FSCJM FIESTA CAJON MAHOGANY
        photo = open('Drums/GON-BOPS-FSCJM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/GON BOPS FSCJM FIESTA CAJON MAHOGANY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="GON BOPS FSCJM FIESTA CAJON MAHOGANY(3 478,00 грн)", url="https://muzon.com.ua/product/gon-bops-fscjm-fiesta-cajon-mahogany/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Gon Bops расширяет модельный ряд кахонов новыми Fiesta моделями — даелая их доступными инструментами для начинающих перкуссионистов", reply_markup=keyboard)
    if message.text == "Тарелки для ударных":
        # photo/SABIAN 45003XEU B8X Performance Set
        photo = open('Drums/45003x-b8x-performance-set_full.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN 45003XEU B8X Performance Set
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN 45003XEU B8X Performance Set(8 694,00 грн)", url="https://muzon.com.ua/product/sabian-45003xeu-b8x-performance-set/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN 45003XEU B8X Performance Set — доступные тарелки с превосходным звучанием", reply_markup=keyboard)
        # photo/SABIAN SBR5001 SBr First Pack
        photo = open('Drums/sbr5001-sbr-first-pack-full.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN SBR5001 SBr First Pack
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN SBR5001 SBr First Pack(3 969,00 грн)", url="https://muzon.com.ua/product/sabian-sbr5001-sbr-first-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN SBR5001 SBr First Pack — доступные тарелки с превосходным звучанием", reply_markup=keyboard)
        # photo/SABIAN SBR5003 SBr Performance Set
        photo = open('Drums/sbr-performance-set_full.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN SBR5003 SBr Performance Set
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN SBR5003 SBr Performance Set(6 678,00 грн)", url="https://muzon.com.ua/product/sabian-sbr5003-sbr-performance-set/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN SBR5003 SBr Performance Set — доступные тарелки с превосходным звучанием", reply_markup=keyboard)
    if message.text == "Барабанные палочки":
        # photo/MAXTONE ADWCW2 — щетки барабанные деревянные
        photo = open('Drums/adwc-w2-main-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE ADWCW2 — щетки барабанные деревянные
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="c(233,00 грн)", url="https://muzon.com.ua/product/maxtone-adwcw2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE ADWCW2 — щетки барабанные деревянные", reply_markup=keyboard)
        # photo/PROMARK LA7AN L.A. SPECIAL 7AN
        photo = open('Drums/LA-7AN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA7AN L.A. SPECIAL 7AN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA7AN L.A. SPECIAL 7AN(186,00 грн)", url="https://muzon.com.ua/product/promark-la7an-l-a-special-7an/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5BN L.A. SPECIAL 5BN
        photo = open('Drums/LA-5BN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5BN L.A. SPECIAL 5BN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5BN L.A. SPECIAL 5BN(186,00 грн)", url="https://muzon.com.ua/product/promark-la5bn-l-a-special-5bn/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5AN L.A. SPECIAL 5AN
        photo = open('Drums/LA-5AN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5AN L.A. SPECIAL 5AN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5AN L.A. SPECIAL 5AN(186,00 грн)", url="https://muzon.com.ua/product/promark-la5an-l-a-special-5an/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/VATER GW7AW GOODWOOD by VATER 7A
        photo = open('Drums/VATER-GW7AW-GOODWOOD-by-VATER-7A.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW7AW GOODWOOD by VATER 7A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW7AW GOODWOOD by VATER 7A(171,00 грн)", url="https://muzon.com.ua/product/vater-gw7aw-goodwood-by-vater-7a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/VATER GW2BW GOODWOOD by VATER 2B
        photo = open('Drums/VATER-GW2BW-600x250.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW2BW GOODWOOD by VATER 2B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW2BW GOODWOOD by VATER 2B(171,00 грн)", url="https://muzon.com.ua/product/vater-gw2bw-goodwood-by-vater-2b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/VATER GW5BW GOODWOOD by VATER 5B
        photo = open('Drums/gw5aw.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW5BW GOODWOOD by VATER 5B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW5BW GOODWOOD by VATER 5B(171,00 грн)", url="https://muzon.com.ua/product/vater-gw5aw-goodwood-by-vater-5b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/VATER GW5AW GOODWOOD by VATER 5A
        photo = open('Drums/VATER-GW5AW.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW5AW GOODWOOD by VATER 5A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW5AW GOODWOOD by VATER 5A(171,00 грн)", url="https://muzon.com.ua/product/vater-gw5aw-goodwood-by-vater-5a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/PROMARK LA7AW L.A. SPECIAL 7A
        photo = open('Drums/LA-7AW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA7AW L.A. SPECIAL 7A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA7AW L.A. SPECIAL 7A(168,00 грн)", url="https://muzon.com.ua/product/promark-la7aw-l-a-special-7a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA2BW L.A. SPECIAL 2B
        photo = open('Drums/LA-2BW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA2BW L.A. SPECIAL 2B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA2BW L.A. SPECIAL 2B(168,00 грн)", url="https://muzon.com.ua/product/promark-la2bw-l-a-special-2b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA2BN L.A. SPECIAL 2BN
        photo = open('Drums/LA-2BN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA2BN L.A. SPECIAL 2BN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA2BN L.A. SPECIAL 2BN(186,00 грн)", url="https://muzon.com.ua/product/promark-la2bn-l-a-special-2bn/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5AW L.A. SPECIAL 5A
        photo = open('Drums/LA-5AW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5AW L.A. SPECIAL 5A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5AW L.A. SPECIAL 5A(168,00 грн)", url="https://muzon.com.ua/product/promark-la5aw-l-a-special-5a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5BW L.A. SPECIAL 5B
        photo = open('Drums/LA-5BW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5BW L.A. SPECIAL 5B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5BW L.A. SPECIAL 5B(168,00 грн)", url="https://muzon.com.ua/product/promark-la5bw-l-a-special-5b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B
        photo = open('Drums/LAU5BW-promark-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B(78,00 грн)", url="https://muzon.com.ua/product/promark-lau5aw-l-a-special-non-printed-5b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B — барабанные палочки", reply_markup=keyboard)
        # photo/PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A
        photo = open('Drums/LAU5AW-promark.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A(78,00 грн)", url="https://muzon.com.ua/product/promark-lau5aw-l-a-special-non-printed-5a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A — барабанные палочки", reply_markup=keyboard)
        # photo/MAXTONE ADWC5AK
        photo = open('Drums/maxtone-5a-china.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE ADWC5AK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE ADWC5AK(49,00 грн)", url="https://muzon.com.ua/product/maxtone-adwc5ak/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE ADWC5AK — барабанные палочки", reply_markup=keyboard)
    if message.text == "Пластики":
        # photo/MAXTONE DHB22
        photo = open('Drums/dhb20-black-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHB22
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHB22(346,00 грн)", url="https://muzon.com.ua/product/maxtone-dhb22/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHB22 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DHB20
        photo = open('Drums/dhb20-black-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHB20
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHB20(343,00 грн)", url="https://muzon.com.ua/product/maxtone-dhb20/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHB20 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DHD22
        photo = open('Drums/dhd22_white.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD22
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD22(451,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd22/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD22 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DHD20
        photo = open('Drums/dhd20_White.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD20
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD20(405,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd20/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD20 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DH22T2
        photo = open('Drums/MAXTONE-DH20T2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH22T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH22T2(260,00 грн)", url="https://muzon.com.ua/product/maxtone-dh22t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH22T2 — пластик для бас-барабана", reply_markup=keyboard)
        # photo/MAXTONE DH20T2
        photo = open('Drums/MAXTONE-DH20T2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH20T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH20T2(254,00 грн)", url="https://muzon.com.ua/product/maxtone-dh20t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH20T2 — пластик для бас-барабана", reply_markup=keyboard)
        # photo/MAXTONE DHD16
        photo = open('Drums/MAxtone_DHD16.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD16
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD16(251,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd16/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD16 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DHD14
        photo = open('Drums/MAxtone_dhd14.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD14
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD14(200,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd14/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD14 — пластик для тома / рабочего барабана", reply_markup=keyboard)
        # photo/MAXTONE DHD13
        photo = open('Drums/MAxtone_dhd14.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD13
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD13(180,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd13/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD13 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DHD12
        photo = open('Drums/MAxtone_dhd14.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD12
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD12(157,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd12/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD12 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DH16T2
        photo = open('Drums/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH16T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH16T2(126,00 грн)", url="https://muzon.com.ua/product/maxtone-dh16t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH16T2 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DH14T2
        photo = open('Drums/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH14T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH14T2(97,00 грн)", url="https://muzon.com.ua/product/maxtone-dh14t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH14T2 — пластик для тома / рабочего барабана", reply_markup=keyboard)
        # photo/MAXTONE DH13T2
        photo = open('Drums/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH13T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH13T2(86,00 грн)", url="https://muzon.com.ua/product/maxtone-dh13t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH13T2 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DH12T2
        photo = open('Drums/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH12T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH12T2(80,00 грн)", url="https://muzon.com.ua/product/maxtone-dh12t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH12T2 — пластик для тома", reply_markup=keyboard)
    if message.text == "Стойки и механика":
        # photo/MAXTONE CBS583
        photo = open('Drums/CBS583-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CBS583
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CBS583(885,00 грн)", url="https://muzon.com.ua/product/maxtone-cbs583/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE CBS583 стойка для тарелки, типа «журавль»,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/MAXTONE CS583
        photo = open('Drums/CS583-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CS583
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CS583(771,00 грн)", url="https://muzon.com.ua/product/maxtone-cs583/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE CS583 прямая стойка под тарелки,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/MAXTONE CS121
        photo = open('Drums/CS121_maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CS121
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CS121(634,00 грн)", url="https://muzon.com.ua/product/maxtone-cs121/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE CS121 прямая стойка под тарелки,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/YAMAHA LC810A
        photo = open('Drums/YamahaLC810A.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA LC810A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA LC810A(342,00 грн)", url="https://muzon.com.ua/product/yamaha-lc810a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA LC810A  хай-хет замок,вся продукция от Yamaha обладает неизменным высоким качеством.", reply_markup=keyboard)
        # photo/MAXTONE 42
        photo = open('Drums/42-main-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE 42
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE 42(185,00 грн)", url="https://muzon.com.ua/product/maxtone-42/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE 42 хай-хет замок,доступная недорогая механика для ударных", reply_markup=keyboard)
    if message.text == "Педали для бас-барабана":
        # photo/MAXTONE DP921
        photo = open('Drums/MAxtone_dp921.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DP921
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DP921(1 870,00 грн)", url="https://muzon.com.ua/product/maxtone-dp921/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DP921 педаль для бас-бочки,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/MAXTONE DPC110
        photo = open('Drums/MAxtone_dp921.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DPC110
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DPC110(954,00 грн)", url="https://muzon.com.ua/product/maxtone-dpc110/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DPC110 педаль для бас-бочки,доступная недорогая механика для ударных", reply_markup=keyboard)
    if message.text == "Аксессуары для ударных":
        # photo/SABIAN SSSC1 CYMBAL CLEANER
        photo = open('Drums/Sabian-SSSC1-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN SSSC1 CYMBAL CLEANER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN SSSC1 CYMBAL CLEANER(199,00 грн)", url="https://muzon.com.ua/product/sabian-sssc1-cymbal-cleaner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN SSSC1 CYMBAL CLEANER — Полироль для тарело", reply_markup=keyboard)
        # photo/DUNLOP 6444 DRUM SHELL POLISH AND CLEANER
        photo = open('Drums/Drum_Shell6444.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 6444 DRUM SHELL POLISH AND CLEANER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 6444POLISH AND CLEANER(197,00 грн)", url="https://muzon.com.ua/product/dunlop-6444-drum-shell-polish-and-cleaner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Полироль-очиститель для деревянных барабанов, также применим для металлических частей барабанов.", reply_markup=keyboard)
        # photo/DUNLOP 6434 CYMBAL CLEANER
        photo = open('Drums/Dunlop-6434.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 6434 CYMBAL CLEANER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 6434 CYMBAL CLEANER(197,00 грн)", url="https://muzon.com.ua/product/dunlop-6434-cymbal-cleaner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Полироль-очиститель для тарелок, состав идеально сбалансированный для металлов тарелок.", reply_markup=keyboard)
        # photo/DUNLOP 6422 CYMBAL INTENSIVE CARE
        photo = open('Drums/6422.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 6422 CYMBAL INTENSIVE CARE
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 6422 CYMBAL INTENSIVE CARE(193,00 грн)", url="https://muzon.com.ua/product/dunlop-6422-cymbal-intensive-care/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Средсво для очистки тарелок Cymbal Intensive Care.", reply_markup=keyboard)
    if message.text == "Скрипки":
        # photo/STENTOR 1500/C VIOLIN OUTFIT 3/4
        photo = open('Violinists/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/C VIOLIN OUTFIT 3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/C VIOLIN OUTFIT 3/4(5 275,00 грн)", url="https://muzon.com.ua/product/stentor-1500-c-student-ii-violin-outfit-3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/A VIOLIN OUTFIT 4/4
        photo = open('Violinists/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/A VIOLIN OUTFIT 4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/A VIOLIN OUTFIT 4/4(5 275,00 грн)", url="https://muzon.com.ua/product/stentor-1500-a-student-ii-violin-outfit-4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II ", reply_markup=keyboard)
        # photo/STENTOR 1500/F VIOLIN OUTFIT 1/4
        photo = open('Violinists/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/F VIOLIN OUTFIT 1/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/F VIOLIN OUTFIT 1/4(5 193,00 грн)", url="https://muzon.com.ua/product/stentor-1500-f-student-ii-violin-outfit-1-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/E VIOLIN OUTFIT 1/2
        photo = open('Violinists/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/E VIOLIN OUTFIT 1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/E VIOLIN OUTFIT 1/2(5 193,00 грн)", url="https://muzon.com.ua/product/stentor-1500-e-student-ii-violin-outfit-1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультантов музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/I VIOLIN OUTFIT 1/16
        photo = open('Violinists/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/I VIOLIN OUTFIT 1/16
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/I VIOLIN OUTFIT 1/16(4 774,00 грн)", url="https://muzon.com.ua/product/stentor-1500-i-student-ii-violin-outfit-1-16/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультантов музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/G VIOLIN OUTFIT 1/8
        photo = open('Violinists/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/G VIOLIN OUTFIT 1/8
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/G VIOLIN OUTFIT 1/8(4 774,00 грн)", url="https://muzon.com.ua/product/stentor-1500-g-student-ii-violin-outfit-1-8/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1018/C STANDARD 3/4
        photo = open('Violinists/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/C STANDARD 3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/C STANDARD 3/4(3 506,00 грн)", url="https://muzon.com.ua/product/stentor-1018-c-student-standard-3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/F STANDARD 1/4
        photo = open('Violinists/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/F STANDARD 1/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/F STANDARD 1/4(3 303,00 грн)", url="https://muzon.com.ua/product/stentor-1018-f-student-standard-1-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/G STANDARD 1/8
        photo = open('Violinists/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/G STANDARD 1/8
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/G STANDARD 1/8(3 303,00 грн)", url="https://muzon.com.ua/product/stentor-1018-g-student-standard-1-8/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/E STANDARD 1/2
        photo = open('Violinists/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/E STANDARD 1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/E STANDARD 1/2(3 303,00 грн)", url="https://muzon.com.ua/product/stentor-1018-e-student-standard-1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/A STANDARD 4/4
        photo = open('Violinists/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/A STANDARD 4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/A STANDARD 4/4(3 506,00 грн)", url="https://muzon.com.ua/product/stentor-1018-a-student-standard-4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
    if message.text == "Виолончели":
        # photo/STENTOR 1102/C CELLO OUTFIT 3/4
        photo = open('Violinists/stentor-1102e-cello12-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1102/C CELLO OUTFIT 3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1102/C CELLO OUTFIT 3/4(13 016,00 грн)", url="https://muzon.com.ua/product/stentor-1102-c-student-i-cello-outfit-3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончели серии Student I изготавливаются на фабрике Stentor из цельных пород древесины, украшаются декоративным орнаментом", reply_markup=keyboard)
        # photo/STENTOR 1102/A CELLO OUTFIT 4/4
        photo = open('Violinists/stentor-1102e-cello12-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1102/A CELLO OUTFIT 4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1102/A CELLO OUTFIT 4/4(13 016,00 грн)", url="https://muzon.com.ua/product/stentor-1102-a-student-i-cello-outfit-4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончели серии Student I изготавливаются на фабрике Stentor из цельных пород древесины, украшаются декоративным орнаментом", reply_markup=keyboard)
        # photo/STENTOR 1102/F CELLO OUTFIT 1/4
        photo = open('Violinists/stentor-1102e-cello12-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1102/F CELLO OUTFIT 1/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1102/F CELLO OUTFIT 1/4(11 114,00 грн)", url="https://muzon.com.ua/product/stentor-1102-f-student-i-cello-outfit-1-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончели серии Student I изготавливаются на фабрике Stentor из цельных пород древесины, украшаются декоративным орнаментом", reply_markup=keyboard)
        # photo/STENTOR 1102/E CELLO OUTFIT 1/2
        photo = open('Violinists/stentor-1102e-cello12-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1102/E CELLO OUTFIT 1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1102/E CELLO OUTFIT 1/2(11 114,00 грн)", url="https://muzon.com.ua/product/stentor-1102-e-student-i-cello-outfit-1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончели серии Student I изготавливаются на фабрике Stentor из цельных пород древесины, украшаются декоративным орнаментом", reply_markup=keyboard)
        # photo/MAXTONE CVC100 4/4
        photo = open('Violinists/CVC100-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CVC100 4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CVC100 4/4(10 354,00 грн)", url="https://muzon.com.ua/product/maxtone-cvc100-4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончель Maxtone отличный вариант для начала обучения игре на этом виде смычкового инструмента, его особенности это не высокая стоимость плюс комплектация кофром и смычком", reply_markup=keyboard)
        # photo/MAXTONE CVC100 1/2
        photo = open('Violinists/CVC100-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CVC100 1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CVC100 1/2(10 354,00 грн)", url="https://muzon.com.ua/product/maxtone-cvc100-1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончель Maxtone отличный вариант для начала обучения игре на этом виде смычкового инструмента, его особенности это не высокая стоимость плюс комплектация кофром и смычком", reply_markup=keyboard)
        # photo/MAXTONE CVC100 3/4
        photo = open('Violinists/CVC100-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CVC100 3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CVC100 3/4(10 354,00 грн)", url="https://muzon.com.ua/product/maxtone-cvc100-3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Виолончель Maxtone отличный вариант для начала обучения игре на этом виде смычкового инструмента, его особенности это не высокая стоимость плюс комплектация кофром и смычком", reply_markup=keyboard)
    if message.text == "Струны для смычковых":
        # photo/D`ADDARIO J810 4/4M Prelude 4/4M
        photo = open('Violinists/J810_4-4M_main_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO J810 4/4M Prelude 4/4M
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO J810 4/4M Prelude 4/4M(580,00 грн)", url="https://muzon.com.ua/product/daddario-j810-4-4m-prelude-4-4m/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO J810 4/4M Prelude 4/4M струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/D`ADDARIO J810 4/4H Prelude 4/4H
        photo = open('Violinists/J810_4-4M_main_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO J810 4/4H Prelude 4/4H
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO J810 4/4H Prelude 4/4H(580,00 грн)", url="https://muzon.com.ua/product/daddario-j810-4-4h-prelude-4-4h/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO J810 4/4H Prelude 4/4H струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/D`ADDARIO J810 4/4L Prelude 4/4L
        photo = open('Violinists/J810_4-4M_main_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO J810 4/4L Prelude 4/4L
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO J810 4/4L Prelude 4/4L(580,00 грн)", url="https://muzon.com.ua/product/daddario-j810-4-4l-prelude-4-4l/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO J810 4/4L Prelude 4/4L струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/D`ADDARIO J810 3/4M Prelude 3/4M
        photo = open('Violinists/J810_4-4M_main_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO J810 3/4M Prelude 3/4M
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO J810 3/4M Prelude 3/4M(580,00 грн)", url="https://muzon.com.ua/product/daddario-j810-3-4m-prelude-3-4m/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO J810 3/4M Prelude 3/4M струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/D`ADDARIO J810 1/2M Prelude 1/2M
        photo = open('Violinists/J810_4-4M_main_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO J810 1/2M Prelude 1/2M
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO J810 1/2M Prelude 1/2M(580,00 грн)", url="https://muzon.com.ua/product/daddario-j810-1-2m-prelude-1-2m/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO J810 1/2M Prelude 1/2M струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/PARKSONS Violin
        photo = open('Violinists/parksons_violin.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PARKSONS Violin
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS Violin(136,00 грн)", url="https://muzon.com.ua/product/parksons-violin/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "PARKSONS Violin 4/4 струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/MAXTONE VN STRING4/4
        photo = open('Violinists/maxtone_vn_4_4.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE VN STRING4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE VN STRING4/4(97,00 грн)", url="https://muzon.com.ua/product/maxtone-vn-string4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE VN STRING4/4 струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/MAXTONE VN STRING3/4
        photo = open('Violinists/maxtone_vn_4_4.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE VN STRING3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE VN STRING3/4(97,00 грн)", url="https://muzon.com.ua/product/maxtone-vn-string3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE VN STRING3/4 струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/MAXTONE VN STRING1/4
        photo = open('Violinists/maxtone_vn_4_4.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE VN STRING1/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE VN STRING1/4(97,00 грн)", url="https://muzon.com.ua/product/maxtone-vn-string1-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE VN STRING1/4 струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
        # photo/MAXTONE VN STRING1/2
        photo = open('Violinists/maxtone_vn_4_4.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE VN STRING1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE VN STRING1/2(97,00 грн)", url="https://muzon.com.ua/product/maxtone-vn-string1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE VN STRING1/2 струны для скрипки, Набор из 4 струн для скрипки", reply_markup=keyboard)
    if message.text == "Аксессуары для смычковых":
        # photo/STENTOR 1390 Violin Rosin (Light Amber)
        photo = open('Violinists/1390_2-stentor.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1390 Violin Rosin (Light Amber)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1390 Violin Rosin (Light Amber)(149,00 грн)", url="https://muzon.com.ua/product/d-stentor-1390-violin-rosin-light-amber/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "STENTOR 1390 Violin Rosin (Light Amber) — канифоль", reply_markup=keyboard)
        # photo/D`ADDARIO KACR7 Kaplan Artcraft Rosin Dark
        photo = open('Violinists/KACR7_daddario.jpg.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO KACR7 Kaplan Artcraft Rosin Dark
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO KACR7 Kaplan Artcraft Rosin Dark(199,00 грн)", url="https://muzon.com.ua/product/daddario-kacr7-kaplan-artcraft-rosin-dark/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO KACR7 Kaplan Artcraft Rosin Dark — канифоль", reply_markup=keyboard)
        # photo/D`ADDARIO KACR6 Kaplan Artcraft Rosin Light
        photo = open('Violinists/KACRlight.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO KACR6 Kaplan Artcraft Rosin Light
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO KACR6 Kaplan Artcraft Rosin Light(199,00 грн)", url="https://muzon.com.ua/product/daddario-kacr6-kaplan-artcraft-rosin-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO KACR6 Kaplan Artcraft Rosin Light — канифоль", reply_markup=keyboard)
        # photo/D`ADDARIO VR300 Natural Rosin Dark
        photo = open('Violinists/bo_prod_VR300_main_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO VR300 Natural Rosin Dark
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO VR300 Natural Rosin Dark(108,00 грн)", url="https://muzon.com.ua/product/daddario-vr300-natural-rosin-dark/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO VR300 Natural Rosin Dark — канифоль", reply_markup=keyboard)
        # photo/D`ADDARIO VR200 Natural Rosin Light
        photo = open('Violinists/naturalrosinlight.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/D`ADDARIO VR200 Natural Rosin Light
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="D`ADDARIO VR200 Natural Rosin Light(108,00 грн)", url="https://muzon.com.ua/product/daddario-vr200-natural-rosin-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "D`ADDARIO VR200 Natural Rosin Light — канифоль", reply_markup=keyboard)
    if message.text == "Синтезаторы":
        # photo/YAMAHA YPT-360 (+блок питания)
        photo = open('Keyboards/ypt360-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA YPT-360 (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA YPT-360 (+блок питания)(7 380,00 грн)", url="https://muzon.com.ua/product/yamaha-ypt-360-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Портативный синтезатор с отличным звучанием, богатым функционалом и динамической клавиатурой", reply_markup=keyboard)
        # photo/YAMAHA DGX-660 WH (+блок питания)
        photo = open('Keyboards/dgx660-w-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA DGX-660 WH (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA DGX-660 WH (+блок питания)(26 565,00 грн)", url="https://muzon.com.ua/product/yamaha-dgx-660-wh-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DGX-660 — это современное цифровое фортепиано, позволяющее вдохновленным пианистам легко улучшить навыки игры", reply_markup=keyboard)
        # photo/YAMAHA DGX-660 B (+блок питания)
        photo = open('Keyboards/dgx660-b-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA DGX-660 B (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA DGX-660 B (+блок питания)(26 565,00 грн)", url="https://muzon.com.ua/product/yamaha-dgx-660-b-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DGX-660 — это современное цифровое фортепиано, позволяющее вдохновленным пианистам легко улучшить навыки игры", reply_markup=keyboard)
        # photo/YAMAHA PSR-E463 (+блок питания)
        photo = open('Keyboards/psr-e463-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA PSR-E463 (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PSR-E463 (+блок питания)(12 048,00 грн)", url="https://muzon.com.ua/product/yamaha-psr-e463-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "С новым PSR-E463, все что вам нужно для превращения ваших идей в музыку — это вдохновение.", reply_markup=keyboard)
        # photo/YAMAHA YPT-260 (+блок питания)
        photo = open('Keyboards/YPT260-main-rus-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA YPT-260 (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA YPT-260 (+блок питания)(5 868,00 грн)", url="https://muzon.com.ua/product/yamaha-ypt-260-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для вдохновения начинающих музыкантов с контрольной панелью на русском языке!", reply_markup=keyboard)
        # photo/YAMAHA PSR-F51 (+блок питания)
        photo = open('Keyboards/psr-f51-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA PSR-F51 (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PSR-F51 (+блок питания)(3 999,00 грн)", url="https://muzon.com.ua/product/yamaha-psr-f51-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "PSR-F51 оснащена встроенной акустической системой и стерео усилителем мощностью 2 х 2.5Вт. В сочетании с высококачественными тембрами Yamaha", reply_markup=keyboard)
    if message.text == "Цифровые пианино":
        # photo/YAMAHA NP-12B (+блок питания)
        photo = open('Keyboards/np12b-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA NP-12B (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA NP-12B (+блок питания)(8 052,00 грн)", url="https://muzon.com.ua/product/yamaha-np-12b-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "NP-12 — прекрасное решение для тех, кому необходимо легкое и в то же время элегантное портативное фортепиано", reply_markup=keyboard)
        # photo/YAMAHA NP-12WH (+блок питания)
        photo = open('Keyboards/np12wh-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA NP-12WH (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA NP-12WH (+блок питания)(8 052,00 грн)", url="https://muzon.com.ua/product/yamaha-np-12wh-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "NP-12 — прекрасное решение для тех, кому необходимо легкое и в то же время элегантное портативное фортепиано", reply_markup=keyboard)
        # photo/YAMAHA P-125 (WH) (+блок питания)
        photo = open('Keyboards/P-125WH-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA P-125 (WH) (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA P-125 (WH) (+блок питания)(20 820,00 грн)", url="https://muzon.com.ua/product/yamaha-p-125-wh-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Yamaha P-125 — это компактное цифровое пианино, сочетающее невероятно реалистичное звучание и естественные ощущения при игре", reply_markup=keyboard)
        # photo/YAMAHA P-125 (B) (+блок питания)
        photo = open('Keyboards/P125-BK-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA P-125 (B) (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA P-125 (B) (+блок питания)(20 820,00 грн)", url="https://muzon.com.ua/product/yamaha-p-125-b-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Yamaha P-125 — это компактное цифровое пианино, сочетающее невероятно реалистичное звучание и естественные ощущения при игре", reply_markup=keyboard)
        # photo/YAMAHA P-45 (+блок питания)
        photo = open('Keyboards/P45_yamaha_main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA P-45 (+блок питания)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA P-45 (+блок питания)(14 409,00 грн)", url="https://muzon.com.ua/product/yamaha-p-45-blok-pitaniya/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Модель отличается технологией AWM семплирования для того чтобы обеспечить музыкантам невероятно реалистичное звучание рояля.", reply_markup=keyboard)
    if message.text == "Аксессуары для клав. инструментов":
        # photo/YAMAHA PA300
        photo = open('Keyboards/pa300-top.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA PA300
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PA300(2 040,00 грн)", url="https://muzon.com.ua/product/yamaha-pa300/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA PA300 адаптер питания для клавишных инструментов Yamaha", reply_markup=keyboard)
        # photo/YAMAHA PA3C
        photo = open('Keyboards/p12785_1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA PA3C
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PA3C(312,00 грн)", url="https://muzon.com.ua/product/yamaha-pa3c/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA PA3C адаптер питания для клавишных инструментов Yamaha", reply_markup=keyboard)
        # photo/YAMAHA PA150B
        photo = open('Keyboards/YAMAHA-PA150B.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA PA150B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PA150B(618,00 грн)", url="https://muzon.com.ua/product/yamaha-pa150b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA PA150B адаптер питания для клавишных инструментов Yamaha", reply_markup=keyboard)
    if message.text == "Тюнеры":
        # photo/DANELECTRO GP2
        photo = open('Accessories/DANELECTRO_GP2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DANELECTRO GP2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DANELECTRO GP2(460,00 грн)", url="https://muzon.com.ua/product/qwik-tune-qtgp1-guitar-professor/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DANELECTRO GP2 — словарь аккордов, хроматический.", reply_markup=keyboard)
        # photo/Cherub WST 520 GB
        photo = open('Accessories/1600.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cherub WST 520 GB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cherub WST 520 GB(290,00 грн)", url="https://muzon.com.ua/product/cherub-wst-520-gb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Cherub WST 520 GB — гитарный тюнер", reply_markup=keyboard)
        # photo/Cherub ST-701
        photo = open('Accessories/cherub.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cherub ST-701
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cherub ST-701(150,00 грн)", url="https://muzon.com.ua/product/cherub-st-701/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Cherub ST701 — гитарный тюнер генератор тона.", reply_markup=keyboard)
        # photo/Aroma ATC-10
        photo = open('Accessories/Aroma-ATC.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Aroma ATC-10
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Aroma ATC-10(310,00 грн)", url="https://muzon.com.ua/product/aroma-atc-10/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Aroma ATC-10 — тюнер прищепка — словарь аккордов, хроматический.", reply_markup=keyboard)
        # photo/PLANET WAVES PW-CT-12
        photo = open('Accessories/PW-CT-12_main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PLANET WAVES PW-CT-12
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PLANET WAVES PW-CT-12(564,00 грн)", url="https://muzon.com.ua/product/planet-waves-pw-ct-12-ns-micro-headstock-tuner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Planet Waves NS Micro Headstock Tuner поможет быстро и точно настроить различные струнные инструменты.", reply_markup=keyboard)
        # photo/FZONE FMT601 Black
        photo = open('Accessories/FMT-601.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FMT601 Black
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FMT601 Black(350,00 грн)", url="https://muzon.com.ua/product/fzone-fmt601-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FMT601 Black — хроматический тюнер-метроном.", reply_markup=keyboard)
        # photo/FZONE FMT700 Black
        photo = open('Accessories/FZONE-FMT700-BLACK.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FMT700 Black
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FMT700 Black(349,00 грн)", url="https://muzon.com.ua/product/fzone-fmt700-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FMT700 Black — хроматический тюнер-метроном прищепка.", reply_markup=keyboard)
        # photo/FZONE FT77 White
        photo = open('Accessories/ft77-white-fzone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FT77 White
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FT77 White(186,00 грн)", url="https://muzon.com.ua/product/fzone-ft77-white/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FT77 White — тюнер прищепка, хроматический.", reply_markup=keyboard)
        # photo/FZONE FT77 Black
        photo = open('Accessories/ft77-black-fzone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FT77 Black
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FT77 Black(186,00 грн)", url="https://muzon.com.ua/product/fzone-ft77-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FT77 Black — тюнер прищепка, хроматический.", reply_markup=keyboard)
        # photo/FZONE FT15 Black
        photo = open('Accessories/fzone-FT-15-BK.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FT15 Black
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FT15 Black(164,00 грн)", url="https://muzon.com.ua/product/fzone-ft15-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FT15 Black — тюнер прищепка, хроматический.", reply_markup=keyboard)
    if message.text == "Метрономы":
        # photo/YAMAHA MP-90
        photo = open('Accessories/mp90bk-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA MP-90
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA MP-90(1 332,00 грн)", url="https://muzon.com.ua/product/yamaha-mp-90/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA MP-90 — Метроном механический", reply_markup=keyboard)
        # photo/FZONE FM310 (White)
        photo = open('Accessories/FM310-White-JAM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FM310 (White)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FM310 (White)(857,00 грн)", url="https://muzon.com.ua/product/fzone-fm310-white/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FM310 (White) — Метроном механический", reply_markup=keyboard)
        # photo/FZONE FM310 (Black)
        photo = open('Accessories/Fzone-FM310-black-JAM.UA_.jpeg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FM310 (Black)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FM310 (Black)(857,00 грн)", url="https://muzon.com.ua/product/fzone-fm310-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FM310 (Black) — Метроном механический. ", reply_markup=keyboard)
        # photo/FZONE FM310 (Wood)
        photo = open('Accessories/FM-310-wooden.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/FZONE FM310 (Wood)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="FZONE FM310 (Wood)(894,00 грн)", url="https://muzon.com.ua/product/fzone-fm310-wood/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "FZONE FM310 (Wood) — Метроном механический.", reply_markup=keyboard)
        # photo/Qwik Time — QT5
        photo = open('Accessories/Qwik.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Qwik Time — QT5
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Qwik Time — QT5(508,00 грн)", url="https://muzon.com.ua/product/qwik-time-qt5/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Qwik Time QT5 —  Цифровой кварцевый метроном.", reply_markup=keyboard)
        # photo/Cherub WSM-012 Intelligent
        photo = open('Accessories/Cherub_WSM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cherub WSM-012 Intelligent
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cherub WSM-012 Intelligent(250,00 грн)", url="https://muzon.com.ua/product/cherub-wsm-012-intelligent/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "метроном-клипса Cherub WSM-012", reply_markup=keyboard)
    if message.text == "Струны для баса":
        # photo/DUNLOP DBS50110 HEAVY 50-110
        photo = open('Strings/DBS50110.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DBS50110 HEAVY 50-110
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DBS50110 HEAVY 50-110(794,00 грн)", url="https://muzon.com.ua/product/dunlop-dbs50110-stainless-steel-heavy-50-110/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DBS50110 STAINLESS STEEL HEAVY 50-110", reply_markup=keyboard)
        # photo/DUNLOP DBS40100 LIGHT 40-100
        photo = open('Strings/DBS40100.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DBS40100 LIGHT 40-100
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DBS40100 LIGHT 40-100(794,00 грн)", url="https://muzon.com.ua/product/dunlop-dbs40100-stainless-steel-light-40-100/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DBS40100 STAINLESS STEEL LIGHT 40-100", reply_markup=keyboard)
        # photo/DUNLOP DBN50110 STEEL HEAVY
        photo = open('Strings/DBS50110.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DBN50110 STEEL HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DBN50110 STEEL HEAVY(794,00 грн)", url="https://muzon.com.ua/product/dunlop-dbn50110-nickel-plated-steel-heavy/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DBN50110 NICKEL PLATED STEEL HEAVY", reply_markup=keyboard)
        # photo/DUNLOP DBN40100 STEEL LIGHT 40-100
        photo = open('Strings/DBS40100.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DBN40100 STEEL LIGHT 40-100
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DBN40100 STEEL LIGHT 40-100(794,00 грн)", url="https://muzon.com.ua/product/dunlop-dbn40100-nickel-plated-steel-light-40-100/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DBN40100 NICKEL PLATED STEEL LIGHT 40-100", reply_markup=keyboard)
        # photo/DUNLOP DBN45105D STEEL MEDIUM 45-105
        photo = open('Strings/DBN45105.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DBN45105D STEEL MEDIUM 45-105
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DBN45105D STEEL MEDIUM 45-105(794,00 грн)", url="https://muzon.com.ua/product/dunlop-dbn45105-nickel-plated-steel-medium-45-105/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DBN45105 NICKEL PLATED STEEL MEDIUM 45-105", reply_markup=keyboard)
        # photo/DUNLOP DBS45105 STEEL MEDIUM 45-105
        photo = open('Strings/DBN45105.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DBS45105 STEEL MEDIUM 45-105
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DBS45105 STEEL MEDIUM 45-105(794,00 грн)", url="https://muzon.com.ua/product/dunlop-dbs45105-stainless-steel-medium-45-105/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DBS45105 STAINLESS STEEL MEDIUM 45-105", reply_markup=keyboard)
    if message.text == "Струны для электрогит.":
        # photo/DUNLOP DHCN1150 CORE HEAVIER
        photo = open('Strings/stringsheavier.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DHCN1150 CORE HEAVIER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DHCN1150 CORE HEAVIER(202,00 грн)", url="https://muzon.com.ua/product/dunlop-dhcn1048-heavy-core-heavy/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DHCN1150 HEAVY CORE HEAVIER", reply_markup=keyboard)
        # photo/CLEARTONE 9420 HEAVY BOTTOM 10-52
        photo = open('Strings/cleartone_9420.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE 9420 HEAVY BOTTOM 10-52
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE 9420 HEAVY BOTTOM 10-52(361,00 грн)", url="https://muzon.com.ua/product/cleartone-9420-electric-nickel-plated-heavy-bottom-10-52/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 9420 ELECTRIC NICKEL-PLATED HEAVY BOTTOM 10-52", reply_markup=keyboard)
        # photo/DUNLOP RWN1046 MEDIUM OLD №10
        photo = open('Strings/rwn1046.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP RWN1046 MEDIUM OLD №10
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP RWN1046 MEDIUM OLD №10(233,00 грн)", url="https://muzon.com.ua/product/dunlop-rwn1046-rev-willys-medium-old-10/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP RWN1046 REV. WiLLYS MEDIUM OLD №10", reply_markup=keyboard)
        # photo/DUNLOP RWN0942 LIGHT OLD №9
        photo = open('Strings/RWN0942.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP RWN0942 LIGHT OLD №9
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP RWN0942 LIGHT OLD №9(233,00 грн)", url="https://muzon.com.ua/product/dunlop-rwn0942-rev-willys-light-old-9/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP RWN0942 REV. WiLLYS LIGHT OLD №9", reply_markup=keyboard)
        # photo/DUNLOP KKN1052 ELECTRIC MEDIUM
        photo = open('Strings/KKN1052.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP KKN1052 ELECTRIC MEDIUM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP KKN1052 ELECTRIC MEDIUM(233,00 грн)", url="https://muzon.com.ua/product/dunlop-kkn1052-kfk-electric-medium/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP KKN1052 KFK ELECTRIC MEDIUM", reply_markup=keyboard)
        # photo/DUNLOP DHCN1254 HEAVYCORE HEAVIEST
        photo = open('Strings/Heavy_Core_Heaviest.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DHCN1254 HEAVYCORE HEAVIEST
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DHCN1254 HEAVYCORE HEAVIEST(202,00 грн)", url="https://muzon.com.ua/product/dunlop-dhcn1254-heavy-core-heaviest/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DHCN1254 HEAVY CORE HEAVIEST", reply_markup=keyboard)
        # photo/DUNLOP DEN1254 ELECTRIC HEAVY
        photo = open('Strings/DEN1254.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN1254 ELECTRIC HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN1254 ELECTRIC HEAVY(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den1254-electric-heavy/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN1254 ELECTRIC HEAVY", reply_markup=keyboard)
        # photo/DUNLOP DEN1052 MEDIUM HEAVY
        photo = open('Strings/DEN1052.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN1052 MEDIUM HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN1052 MEDIUM HEAVY(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den1052-electric-medium-heavy-bottom/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN1052 ELECTRIC MEDIUM HEAVY BOTTOM", reply_markup=keyboard)
        # photo/DUNLOP DEN1046 ELECTRIC MEDIUM
        photo = open('Strings/DEN1046.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN1046 ELECTRIC MEDIUM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN1046 ELECTRIC MEDIUM(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den1046-electric-medium-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN1046 ELECTRIC MEDIUM", reply_markup=keyboard)
        # photo/DUNLOP DHCN1048 HEAVYCORE HEAVY
        photo = open('Strings/stringsheavy.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DHCN1048 HEAVYCORE HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DHCN1048 HEAVYCORE HEAVY(202,00 грн)", url="https://muzon.com.ua/product/dunlop-dhcn1048-heavy-core-heavy-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DHCN1048 HEAVY CORE HEAVY", reply_markup=keyboard)
        # photo/DUNLOP DEN1356 EXTRA HEAVY
        photo = open('Strings/DEN1356.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN1356 EXTRA HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN1356 EXTRA HEAVY(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den1356-electric-extra-heavy/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN1356 ELECTRIC EXTRA HEAVY", reply_markup=keyboard)
        # photo/DUNLOP DEN1150 MEDIUM HEAVY
        photo = open('Strings/DEN1150.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN1150 MEDIUM HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN1150 MEDIUM HEAVY(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den1046-electric-medium/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN1150 ELECTRIC MEDIUM HEAVY", reply_markup=keyboard)
        # photo/DUNLOP DEN0942 ELECTRIC LIGHT
        photo = open('Strings/DEN0942.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN0942 ELECTRIC LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN0942 ELECTRIC LIGHT(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den0942-electric-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN0942 ELECTRIC LIGHT", reply_markup=keyboard)
        # photo/DUNLOP DEN0946 LIGHT/HEAVY
        photo = open('Strings/DEN0946.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN0946 LIGHT/HEAVY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN0946 LIGHT/HEAVY(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den0946-electric-light-heavy-bottom/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN0946 ELECTRIC LIGHT/HEAVY BOTTOM", reply_markup=keyboard)
        # photo/DUNLOP DEN0838 EXTRA LIGHT
        photo = open('Strings/DEN0838.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DEN0838 EXTRA LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DEN0838 EXTRA LIGHT(202,00 грн)", url="https://muzon.com.ua/product/dunlop-den0838-electric-extra-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DEN0838 ELECTRIC EXTRA LIGHT", reply_markup=keyboard)
        # photo/DEAN MARKLEY NICKELSTEEL (11-52)
        photo = open('Strings/2505-dm.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY NICKELSTEEL (11-52)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY NICKELSTEEL (11-52)(156,00 грн)", url="https://muzon.com.ua/product/dean-markley-2505-nickelsteel-electric-med-11-52/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 2505 NICKELSTEEL ELECTRIC MED (11-52)", reply_markup=keyboard)
        # photo/EAN MARKLEY NICKELSTEEL CL(09-46)
        photo = open('Strings/2508-dm.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/EAN MARKLEY NICKELSTEEL CL(09-46)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY NICKELSTEEL CL(09-46)(140,00 грн)", url="https://muzon.com.ua/product/dean-markley-2508-nickelsteel-electric-cl-09-46/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 2508 NICKELSTEEL ELECTRIC CL (09-46)", reply_markup=keyboard)
        # photo/DEAN MARKLEY NICKELSTEEL LT(09-42)
        photo = open('Strings/2502-deanmarkley.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY NICKELSTEEL LT(09-42)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY NICKELSTEEL LT(09-42)(156,00 грн)", url="https://muzon.com.ua/product/dean-markley-2502-nickelsteel-electric-lt-09-42/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 2502 NICKELSTEEL ELECTRIC LT (09-42)", reply_markup=keyboard)
        # photo/CLEARTONE NICKELPLATED HYBRID 09-46
        photo = open('Strings/Cleartone-9419.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE NICKELPLATED HYBRID 09-46
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE NICKELPLATED HYBRID 09-46(361,00 грн)", url="https://muzon.com.ua/product/cleartone-9419-electric-nickel-plated-hybrid-09-46/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 9419 ELECTRIC NICKEL-PLATED HYBRID 09-46", reply_markup=keyboard)
        # photo/CLEARTONE NICKELPLATED MEDIUM 11-48
        photo = open('Strings/cleartone_9411.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE NICKELPLATED MEDIUM 11-48
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE NICKELPLATED MEDIUM 11-48(361,00 грн)", url="https://muzon.com.ua/product/cleartone-9411-electric-nickel-plated-medium-11-48/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 9411 ELECTRIC NICKEL-PLATED MEDIUM 11-48", reply_markup=keyboard)
        # photo/CLEARTONE NICKELPLATED LIGHT 10-46
        photo = open('Strings/9410-Cover.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE NICKELPLATED LIGHT 10-46
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE NICKELPLATED LIGHT 10-46(361,00 грн)", url="https://muzon.com.ua/product/cleartone-9410-electric-nickel-plated-light-10-46/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 9410 ELECTRIC NICKEL-PLATED LIGHT 10-46", reply_markup=keyboard)
        # photo/CLEARTONE NICKELPLATED SUPERLIGHT 09-42
        photo = open('Strings/cleartone_9409.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE NICKELPLATED SUPERLIGHT 09-42
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE NICKELPLATED SUPERLIGHT 09-42(361,00 грн)", url="https://muzon.com.ua/product/cleartone-9409-electric-nickel-plated-super-light-09-42/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 9409 ELECTRIC NICKEL-PLATED SUPER LIGHT 09-42", reply_markup=keyboard)
    if message.text == "Струны для акустической гитары":
        # photo/CLEARTONE ACOUSTIC80/20 BRONZE MEDIUM 13-56
        photo = open('Strings/cleartone-8020-bronze-13-7613.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE ACOUSTIC80/20 BRONZE MEDIUM 13-56
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE ACOUSTIC80/20 BRONZE MEDIUM 13-56(446,00 грн)", url="https://muzon.com.ua/product/cleartone-7613-acoustic-80-20-bronze-medium-13-56/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7613 ACOUSTIC 80/20 BRONZE MEDIUM 13-56", reply_markup=keyboard)
        # photo/DUNLOP DAP1254 PHOSPHOR BRONZE LIGHT
        photo = open('Strings/DAP1254.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DAP1254 PHOSPHOR BRONZE LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DAP1254 PHOSPHOR BRONZE LIGHT(281,00 грн)", url="https://muzon.com.ua/product/dunlop-dap1254-phosphor-bronze-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAP1254 PHOSPHOR BRONZE LIGHT", reply_markup=keyboard)
        # photo/CLEARTONE PHOSPHORBRONZE EXTRALIGHT 11-52
        photo = open('Strings/cleartone-phos-bronze-11-7411-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE PHOSPHORBRONZE EXTRALIGHT 11-52
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE PHOSPHORBRONZE EXTRALIGHT 11-52(456,00 грн)", url="https://muzon.com.ua/product/cleartone-7411-acoustic-phosphor-bronze-extra-light-11-52/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7411 ACOUSTIC PHOSPHOR BRONZE EXTRA LIGHT 11-52", reply_markup=keyboard)
        # photo/DUNLOP DAP1356 PHOSPHORBRONZE MEDIUM
        photo = open('Strings/DAP1356.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP DAP1356 PHOSPHORBRONZE MEDIUM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP DAP1356 PHOSPHORBRONZE MEDIUM(281,00 грн)", url="https://muzon.com.ua/product/dunlop-dap1356-phosphor-bronze-medium/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAP1356 PHOSPHOR BRONZE MEDIUM", reply_markup=keyboard)
        # photo/DUNLOP PHOSPHOR BRONZE MEDIUM LIGHT
        photo = open('Strings/DAP1152.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP PHOSPHOR BRONZE MEDIUM LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP PHOSPHOR BRONZE MEDIUM LIGHT(281,00 грн)", url="https://muzon.com.ua/product/dunlop-dap1152-phosphor-bronze-medium-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAP1152 PHOSPHOR BRONZE MEDIUM LIGHT", reply_markup=keyboard)
        # photo/DUNLOP PHOSPHOR BRONZE EXTRA LIGHT
        photo = open('Strings/DAP1048.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP PHOSPHOR BRONZE EXTRA LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP PHOSPHOR BRONZE EXTRA LIGHT(281,00 грн)", url="https://muzon.com.ua/product/dunlop-dap1048-phosphor-bronze-extra-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAP1048 PHOSPHOR BRONZE EXTRA LIGHT", reply_markup=keyboard)
        # photo/DUNLOP 80/20 BRONZE MEDIUM
        photo = open('Strings/DAB1356.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 80/20 BRONZE MEDIUM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 80/20 BRONZE MEDIUM(219,00 грн)", url="https://muzon.com.ua/product/dunlop-dab1356-80-20-bronze-medium/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAB1356 80/20 BRONZE MEDIUM", reply_markup=keyboard)
        # photo/DUNLOP 80/20 BRONZE LIGHT
        photo = open('Strings/DAB1254.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 80/20 BRONZE LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 80/20 BRONZE LIGHT(219,00 грн)", url="https://muzon.com.ua/product/dunlop-dab1254-80-20-bronze-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAB1254 80/20 BRONZE LIGHT", reply_markup=keyboard)
        # photo/DUNLOP BRONZE MEDIUM LIGHT
        photo = open('Strings/DAB1152.sized_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP BRONZE MEDIUM LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP BRONZE MEDIUM LIGHT(219,00 грн)", url="https://muzon.com.ua/product/dunlop-dab1152-80-20-bronze-medium-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAB1152 80/20 BRONZE MEDIUM LIGHT", reply_markup=keyboard)
        # photo/DUNLOP BRONZE EXTRA LIGHT
        photo = open('Strings/DAB1048.sized_-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP BRONZE EXTRA LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP BRONZE EXTRA LIGHT(219,00 грн)", url="https://muzon.com.ua/product/dunlop-dab1048-80-20-bronze-extra-light/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DAB1048 80/20 BRONZE EXTRA LIGHT", reply_markup=keyboard)
        # photo/DEAN MARKLEY VINTAGEBRONZE ML12
        photo = open('Strings/vb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY VINTAGEBRONZE ML12
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY VINTAGEBRONZE ML12(11-50)(252,00 грн)", url="https://muzon.com.ua/product/dean-markley-2204-vintage-bronze-acoustic-ml12-11-50/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 2204 VINTAGE BRONZE ACOUSTIC ML12 (11-50)", reply_markup=keyboard)
        # photo/DEAN MARKLEY VINTAGEBRONZE MED (13-56)
        photo = open('Strings/2006-VintBr-DM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY VINTAGEBRONZE MED (13-56)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY VINTAGEBRONZE MED (13-56)(180,00 грн)", url="https://muzon.com.ua/product/dean-markley-2006-vintagebronze-acoustic-med-13-56/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 2006 VINTAGEBRONZE ACOUSTIC MED (13-56)", reply_markup=keyboard)
        # photo/DEAN MARKLEY VINTAGEBRONZE ML(12-54)
        photo = open('Strings/2004-VintBr-DM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY VINTAGEBRONZE ML(12-54)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY VINTAGEBRONZE ML(12-54)(180,00 грн)", url="https://muzon.com.ua/product/dean-markley-2004-vintage-bronze-acoustic-ml-12-54/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 2004 VINTAGE BRONZE ACOUSTIC ML (12-54)", reply_markup=keyboard)
        # photo/DEAN MARKLEY BLACKHAWK BRONZE ML(12-53)
        photo = open('Strings/Blackhawk-8020.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY BLACKHAWK BRONZE ML(12-53)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY BLACKHAWK BRONZE ML(12-53)(340,00 грн)", url="https://muzon.com.ua/product/dean-markley-8020-blackhawk-acoustic-80-20-bronze-ml-12-53/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 8020 BLACKHAWK ACOUSTIC 80/20 BRONZE ML (12-53)", reply_markup=keyboard)
        # photo/DEAN MARKLEY BLACKHAWK BRONZE LT(11-52)
        photo = open('Strings/Blackhawk-8019.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY BLACKHAWK BRONZE LT(11-52)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY BLACKHAWK BRONZE LT(11-52)(340,00 грн)", url="https://muzon.com.ua/product/dean-markley-8019-blackhawk-acoustic-80-20-bronze-lt-11-52/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 8019 BLACKHAWK ACOUSTIC 80/20 BRONZE LT (11-52)", reply_markup=keyboard)
        # photo/DEAN MARKLEY BLACKHAWK BRONZE XL(10-47)
        photo = open('Strings/Blackhawk-8018.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY BLACKHAWK BRONZE XL(10-47)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY BLACKHAWK BRONZE XL(10-47)(340,00 грн)", url="https://muzon.com.ua/product/dean-markley-8018-blackhawk-acoustic-80-20-bronze-xl-10-47/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 8018 BLACKHAWK ACOUSTIC 80/20 BRONZE XL (10-47)", reply_markup=keyboard)
        # photo/DEAN MARKLEY BLACKHAWK PHOS ML(12-53)
        photo = open('Strings/Blackhawk-8012.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY BLACKHAWK PHOS ML(12-53)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY BLACKHAWK PHOS ML(12-53)(400,00 грн)", url="https://muzon.com.ua/product/dean-markley-8012-blackhawk-acoustic-phos-ml-12-53/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 8012 BLACKHAWK ACOUSTIC PHOS ML (12-53)", reply_markup=keyboard)
        # photo/DEAN MARKLEY BLACKHAWK PHOS LT(11-52)
        photo = open('Strings/Blackhawk-8011.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY BLACKHAWK PHOS LT(11-52)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY BLACKHAWK PHOS LT(11-52)(400,00 грн)", url="https://muzon.com.ua/product/dean-markley-8011-blackhawk-acoustic-phos-lt-11-52/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 8011 BLACKHAWK ACOUSTIC PHOS LT (11-52)", reply_markup=keyboard)
        # photo/DEAN MARKLEY BLACKHAWK PHOS XL(10-47)
        photo = open('Strings/Blackhawk-8010.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DEAN MARKLEY BLACKHAWK PHOS XL(10-47)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DEAN MARKLEY BLACKHAWK PHOS XL(10-47)(400,00 грн)", url="https://muzon.com.ua/product/dean-markley-8010-blackhawk-acoustic-phos-xl-10-47/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DEAN MARKLEY 8010 BLACKHAWK ACOUSTIC PHOS XL (10-47)", reply_markup=keyboard)
        # photo/CLEARTONE 12-STRING ULTRA LIGHT
        photo = open('Strings/cleartone-phos-bronze-10-12strings-7410-12.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE 12-STRING ULTRA LIGHT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE 12-STRING ULTRA LIGHT(714,00 грн)", url="https://muzon.com.ua/product/cleartone-7410-12-acoustic-phosphor-bronze-12-string-ultra-light-10-47/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7410-12 ACOUSTIC PHOSPHOR BRONZE 12-STRING ULTRA LIGHT 10-47", reply_markup=keyboard)
        # photo/CLEARTONE PHOSPHORBRONZE BLUEGRASS 12-56
        photo = open('Strings/cleart_7423_phosbronz-bluegrass-1256.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE PHOSPHORBRONZE BLUEGRASS 12-56
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE PHOSPHORBRONZE BLUEGRASS 12-56(456,00 грн)", url="https://muzon.com.ua/product/cleartone-7423-acoustic-phosphor-bronze-bluegrass-12-56/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7423 ACOUSTIC PHOSPHOR BRONZE BLUEGRASS 12-56", reply_markup=keyboard)
        # photo/CLEARTONE PHOSPHORBRONZE LIGHT 12-53
        photo = open('Strings/cleartone-phos-bronze-12-7412.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE PHOSPHORBRONZE LIGHT 12-53
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE PHOSPHORBRONZE LIGHT 12-53(456,00 грн)", url="https://muzon.com.ua/product/cleartone-7412-acoustic-phosphor-bronze-light-12-53/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7412 ACOUSTIC PHOSPHOR BRONZE LIGHT 12-53", reply_markup=keyboard)
        # photo/CLEARTONE PHOSPHORBRONZE ULTRALIGHT 10-47
        photo = open('Strings/cleartone-phos-bronze-10-7410.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE PHOSPHORBRONZE ULTRALIGHT 10-47
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE PHOSPHORBRONZE ULTRALIGHT 10-47(456,00 грн)", url="https://muzon.com.ua/product/cleartone-7410-acoustic-phosphor-bronze-ultra-light-10-47/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7410 ACOUSTIC PHOSPHOR BRONZE ULTRA LIGHT 10-47", reply_markup=keyboard)
        # photo/CLEARTONE BRONZELIGHT 12-53
        photo = open('Strings/cleartone-8020-bronze-12-7612.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE BRONZELIGHT 12-53
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE BRONZELIGHT 12-53(446,00 грн)", url="https://muzon.com.ua/product/cleartone-7612-acoustic-80-20-bronze-light-12-53/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7612 ACOUSTIC 80/20 BRONZE LIGHT 12-53", reply_markup=keyboard)
        # photo/CLEARTONE BRONZE ULTRALIGHT 11-52
        photo = open('Strings/cleartone-8020-bronze-11-7611.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CLEARTONE BRONZE ULTRALIGHT 11-52
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CLEARTONE BRONZE ULTRALIGHT 11-52(446,00 грн)", url="https://muzon.com.ua/product/cleartone-7611-acoustic-80-20-bronze-ultra-light-11-52/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "CLEARTONE 7611 ACOUSTIC 80/20 BRONZE ULTRA LIGHT 11-52", reply_markup=keyboard)
    if message.text == "Струны для классической гитары":
        # photo/DUNLOP CLASSIC CONCERT SE
        photo = open('Strings/dcv121h-dunlop-classic.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP CLASSIC CONCERT SE
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP CLASSIC CONCERT SE(323,00 грн)", url="https://muzon.com.ua/product/dunlop-dcv121h-classic-concert-se/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DCV121H CLASSIC CONCERT SE", reply_markup=keyboard)
        # photo/DUNLOP CLASSIC CONCERT SE
        photo = open('Strings/dcv120-dunlop-classic.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP CLASSIC CONCERT SE
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP CLASSIC CONCERT SE(323,00 грн)", url="https://muzon.com.ua/product/dunlop-dcv120-classic-concert-se/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DCV120 CLASSIC CONCERT SE", reply_markup=keyboard)
    if message.text == "Струны для укулеле":
        # photo/DUNLOP UKULELE CONCERT
        photo = open('Strings/duq302-UkuleleStrings-dunlo.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP UKULELE CONCERT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP UKULELE CONCERT(169,00 грн)", url="https://muzon.com.ua/product/dunlop-duq302-ukulele-concert/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DUQ302 UKULELE CONCERT", reply_markup=keyboard)
        # photo/DUNLOP UKULELE SOPRANO STU.
        photo = open('Strings/duq201-UkuleleStrings-dunlo.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP UKULELE SOPRANO STU.
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP UKULELE SOPRANO STU.(148,00 грн)", url="https://muzon.com.ua/product/dunlop-duq201-ukulele-soprano-student/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP DUQ201 UKULELE SOPRANO STUDENT", reply_markup=keyboard)
    if message.text == "0.50мм":
        # photo/DUNLOP TRIANGLE PLAYER’S PACK
        photo = open('Picks/RED_picks.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP TRIANGLE PLAYER’S PACK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP PLAYER’S PACK(112,00 грн)", url="https://muzon.com.ua/product/dunlop-431p-50-tortex-triangle-players-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 431P.50 TORTEX TRIANGLE PLAYER’S PACK", reply_markup=keyboard)
    if message.text == "0.60мм":
        # photo/DUNLOP PLAYER’S PACK 0.60
        photo = open('Picks/img_95544.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP PLAYER’S PACK 0.60
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP PLAYER’S PACK 0.60(115,00 грн)", url="https://muzon.com.ua/product/dunlop-421p-60-ultex-standard-players-pack-0-60/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 421P.60 ULTEX STANDARD PLAYER’S PACK 0.60", reply_markup=keyboard)
        # photo/DUNLOP PLAYER’S PACK
        photo = open('Picks/61u70SSg0L._SY355_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP PLAYER’S PACK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP PLAYER’S PACK(112,00 грн)", url="https://muzon.com.ua/product/dunlop-431p-60-tortex-triangle-players-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 431P.60 TORTEX TRIANGLE PLAYER’S PACK", reply_markup=keyboard)
        # photo/DUNLOP PLAYER’S PACK 0.60
        photo = open('Picks/ap_hn144264.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP PLAYER’S PACK 0.60
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP PLAYER’S PACK 0.60(126,00 грн)", url="https://muzon.com.ua/product/dunlop-bl100p-60-blackline-original-players-pack-0-60/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP BL100P.60 BLACKLINE ORIGINAL PLAYER’S PACK 0.60", reply_markup=keyboard)
    if message.text == "0.73мм":
        # photo/DUNLOP ORIGINAL PLAYER’S PACK0.73
        photo = open('Picks/BLACKLINE-ORIGINAL-PLAYERS.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP ORIGINAL PLAYER’S PACK0.73
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP ORIGINAL PLAYER’S PACK0.73(126,00 грн)", url="https://muzon.com.ua/product/dunlop-bl100p-73-blackline-original-players-pack-0-73/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP BL100P.73 BLACKLINE ORIGINAL PLAYER’S PACK 0.73", reply_markup=keyboard)
        # photo/DUNLOP STANDARD PLAYER’S PACK 0.73
        photo = open('Picks/DUN_421P73__96189.1421108303.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STANDARD PLAYER’S PACK 0.73
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STANDARD PLAYER’S PACK 0.73(115,00 грн)", url="https://muzon.com.ua/product/dunlop-421p-73-ultex-standard-players-pack-0-73/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 421P.73 ULTEX STANDARD PLAYER’S PACK 0.73", reply_markup=keyboard)
        # photo/DUNLOP TRIANGLE PLAYER’S PACK
        photo = open('Picks/61F-FnJuwGL._SY355_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP TRIANGLE PLAYER’S PACK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP TRIANGLE PLAYER’S PACK(112,00 грн)", url="https://muzon.com.ua/product/dunlop-431p-73-tortex-triangle-players-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 431P.73 TORTEX TRIANGLE PLAYER’S PACK", reply_markup=keyboard)
    if message.text == "0.88мм":
        # photo/DUNLOP STANDARD PLAYER’SPACK 0.88
        photo = open('Picks/421P.88-set-dunlop.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STANDARD PLAYER’SPACK 0.88
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STANDARD PLAYER’SPACK 0.88(115,00 грн)", url="https://muzon.com.ua/product/dunlop-421p-73-ultex-standard-players-pack-0-88/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 421P.88 ULTEX STANDARD PLAYER’S PACK 0.88", reply_markup=keyboard)
        # photo/DUNLOP TRIANGLE PLAYER’S PACK
        photo = open('Picks/611oMcpb1XL._SY355_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP TRIANGLE PLAYER’S PACK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP TRIANGLE PLAYER’S PACK(112,00 грн)", url="https://muzon.com.ua/product/dunlop-431p-88-tortex-triangle-players-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 431P.88 TORTEX TRIANGLE PLAYER’S PACK", reply_markup=keyboard)
    if message.text == "1.00мм":
        # photo/DUNLOP ORIGINAL PLAYER’S PACK 1.0
        photo = open('Picks/BLACKLINE-ORIGINAL-PLAYERS.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP ORIGINAL PLAYER’S PACK 1.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP ORIGINAL PLAYER’S PACK 1.0(126,00 грн)", url="https://muzon.com.ua/product/dunlop-bl100p1-0-blackline-original-players-pack-1-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP BL100P1.0 BLACKLINE ORIGINAL PLAYER’S PACK 1.0", reply_markup=keyboard)
        # photo/DUNLOP STUBBY PLAYER’S PACK 1.0
        photo = open('Picks/475p1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STUBBY PLAYER’S PACK 1.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STUBBY PLAYER’S PACK 1.0(133,00 грн)", url="https://muzon.com.ua/product/dunlop-475p1-0-big-stubby-players-pack-1-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 475P1.0 BIG STUBBY PLAYER’S PACK 1.0", reply_markup=keyboard)
        # photo/DUNLOP ART SERIES PLAYER’SPACK 1.0
        photo = open('Picks/1_1_310183-600x438.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP ART SERIES PLAYER’SPACK 1.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP ART SERIES PLAYER’SPACK 1.0(117,00 грн)", url="https://muzon.com.ua/product/dunlop-l13bp1-0-lucky13-art-series-players-pack-1-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP L13BP1.0 LUCKY13 ART SERIES PLAYER’S PACK 1.0", reply_markup=keyboard)
        # photo/DUNLOP STANDARD PLAYER’S PACK 1.0
        photo = open('Picks/DUN_421P100__87225.1421108341.1280.1280.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STANDARD PLAYER’S PACK 1.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STANDARD PLAYER’S PACK 1.0(115,00 грн)", url="https://muzon.com.ua/product/dunlop-421p1-0-ultex-standard-players-pack-1-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 421P1.0 ULTEX STANDARD PLAYER’S PACK 1.0", reply_markup=keyboard)
        # photo/DUNLOP TRIANGLE PLAYER’S PACK
        photo = open('Picks/615wu9v5aRL._SY355_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP TRIANGLE PLAYER’S PACK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP TRIANGLE PLAYER’S PACK(112,00 грн)", url="https://muzon.com.ua/product/dunlop-431p1-0-tortex-triangle-players-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 431P1.0 TORTEX TRIANGLE PLAYER’S PACK", reply_markup=keyboard)
    if message.text == "1.14мм":
        # photo/DUNLOP STANDARD PLAYER’SPACK 1.14
        photo = open('Picks/img_114.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STANDARD PLAYER’SPACK 1.14
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STANDARD PLAYER’SPACK 1.14(115,00 грн)", url="https://muzon.com.ua/product/dunlop-421p1-14-ultex-standard-players-pack-1-14/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 421P1.14 ULTEX STANDARD PLAYER’S PACK 1.14", reply_markup=keyboard)
        # photo/DUNLOP TRIANGLE PLAYER’S PACK
        photo = open('Picks/61uTme3vn4L._SY355_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP TRIANGLE PLAYER’S PACK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP TRIANGLE PLAYER’S PACK(112,00 грн)", url="https://muzon.com.ua/product/dunlop-431p1-14-tortex-triangle-players-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 431P1.14 TORTEX TRIANGLE PLAYER’S PACK", reply_markup=keyboard)
    if message.text == "1.50мм":
        # photo/DUNLOP STUBBY PLAYER’SPACK 1.5
        photo = open('Picks/473P1.5.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STUBBY PLAYER’SPACK 1.5
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STUBBY PLAYER’SPACK 1.5(133,00 грн)", url="https://muzon.com.ua/product/dunlop-473p1-5-tri-stubby-players-pack-1-5/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 473P1.5 TRI STUBBY PLAYER’S PACK 1.5", reply_markup=keyboard)
    if message.text == "2.00мм":
        # photo/DUNLOP STUBBY PLAYER’SPACK 2.0
        photo = open('Picks/61Q3TtZdY7L._SL1400_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STUBBY PLAYER’SPACK 2.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STUBBY PLAYER’SPACK 2.0(133,00 грн)", url="https://muzon.com.ua/product/dunlop-473p2-0-tri-stubby-players-pack-2-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 473P2.0 TRI STUBBY PLAYER’S PACK 2.0", reply_markup=keyboard)
        # photo/DUNLOP STUBBY PLAYER’SPACK 2.
        photo = open('Picks/s-l1000.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STUBBY PLAYER’SPACK 2.
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STUBBY PLAYER’SPACK 2.0(133,00 грн)", url="https://muzon.com.ua/product/dunlop-475p2-0-big-stubby-players-pack-2-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 475P2.0 BIG STUBBY PLAYER’S PACK 2.0", reply_markup=keyboard)
    if message.text == "3.00мм":
        # photo/DUNLOP STUBBY PLAYER’S PACK 3.0
        photo = open('Picks/24473300006.FRNT_.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STUBBY PLAYER’S PACK 3.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STUBBY PLAYER’S PACK 3.0(133,00 грн)", url="https://muzon.com.ua/product/dunlop-473p3-0-tri-stubby-players-pack-3-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 473P3.0 TRI STUBBY PLAYER’S PACK 3.0", reply_markup=keyboard)
        # photo/DUNLOP STUBBY PLAYER’S PACK 3.0
        photo = open('Picks/big-stubby-players-pack-3mm-6-set-hd-139729.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP STUBBY PLAYER’S PACK 3.0
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP STUBBY PLAYER’S PACK 3.0(133,00 грн)", url="https://muzon.com.ua/product/dunlop-475p3-0-big-stubby-players-pack-3-0/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "DUNLOP 475P3.0 BIG STUBBY PLAYER’S PACK 3.0", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)

# iiii];)'
