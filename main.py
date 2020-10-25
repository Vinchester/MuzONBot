import telebot

bot = telebot.TeleBot('1245954623:AAE_cqLoDBXhNChwXQqPp4AshXJiUQaD5mw')

from telebot import types
@bot.message_handler(commands=["start"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="/Гитары")
    btn2 = types.KeyboardButton(text="/Струны")
    btn3 = types.KeyboardButton(text="/Ударные")
    btn4 = types.KeyboardButton(text="/Смычковые")
    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, "Товары", reply_markup=keyboard)

@bot.message_handler(commands=["Назад"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="/Гитары")
    btn2 = types.KeyboardButton(text="/Струны")
    btn3 = types.KeyboardButton(text="/Ударные")
    btn4 = types.KeyboardButton(text="/Смычковые")
    keyboard.add(btn1, btn2, btn3, btn4)
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

@bot.message_handler(commands=["Струны"])
def get_text_messages(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Струны на акустику")
    btn2 = types.KeyboardButton(text="Струны на классику")
    btn3 = types.KeyboardButton(text="Струны на электрогитару")
    btn4 = types.KeyboardButton(text="Струны на скрипку")
    btn5 = types.KeyboardButton(text="/Назад")
    keyboard.add(btn1, btn2, btn3, btn4, btn5)
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
        photo = open('Photoex/PARKSONS_JB4111C_Black_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/PARKSONS_JB4111C
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111С(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111s-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        #photo/parksons_jb411
        photo = open('Photoex/parksons_jb411_black_front.jpg','rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/parksons_jb411
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111 BLACK(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        #photo/AD810_LH_OP
        photo = open('Photoex/AD810_LH_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/AD810_LH_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810LH OP(3 591,00 грн)", url="https://muzon.com.ua/product/cort-ad810lh-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.",reply_markup=keyboard)
        #photo/fg800-nt-main-yamaha
        photo = open('Photoex/fg800-nt-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/fg800-nt-main-yamaha
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA FG800 (NT)(8 832,00 грн)",url="https://muzon.com.ua/product/yamaha-fg800-nt/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Легендарная гитара от известного бренда Yamaha, имеет отличное звучание, качественную сборку, за не высокую стоимость. Каждая деталь гитары FG создана для того, чтобы сделать ее еще лучше.", reply_markup=keyboard)
        #photo/fg800-bs-main-yamaha
        photo = open('Photoex/fg800-bs-main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/fg800-bs-main-yamaha
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA FG800 (BS)(8 832,00 грн)", url="https://muzon.com.ua/product/yamaha-fg800-bs/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Легендарная гитара от известного бренда Yamaha, имеет отличное звучание, качественную сборку, за не высокую стоимость. Каждая деталь гитары FG создана для того, чтобы сделать ее еще лучше.", reply_markup=keyboard)
        #photo/PARKSONS JB4111С SUNBURST
        photo = open('Photoex/PARKSONS_JB4111C_Sunburst_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        #info with btn/PARKSONS JB4111С SUNBURST
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111С SUNBURST(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111s-sunburst/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/PARKSONS JB4111С NATURAL
        photo = open('Photoex/PARKSONS_JB4111C_Natural_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PARKSONS JB4111С NATURAL
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111С NATURAL(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111s-natural/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/parksons_jb4111_natural
        photo = open('Photoex/parksons_jb4111_natural.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_jb4111_natural
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111 NATURAL(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111-natural/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/parksons_jb4111_sunburst
        photo = open('Photoex/parksons_jb4111_sunburst.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_jb4111_sunburst
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PARKSONS JB4111 SUNBURST(2 099,00 грн)", url="https://muzon.com.ua/product/parksons-jb4111-sunburst/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Отлично зарекомендовавший себя инструмент в доступном классе акустических гитар.", reply_markup=keyboard)
        # photo/AD810_12_OP
        photo = open('Photoex/AD810_12_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with button/AD810_12_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810-12 OP(4 057,00 грн)", url="https://muzon.com.ua/product/cort-ad810-12-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Корпус AD810-12 OP выполнен из ели и красного дерева, данный инструмент является наилучшим выбором для начинающих гитаристов, этому соответствует не высокая стоимость и отличное качество инструмента...", reply_markup=keyboard)
        # photo/AD810_SSB
        photo = open('Photoex/AD810_SSB.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AD810_SSB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810 SSB(2 699,00 грн)", url="https://muzon.com.ua/product/cort-ad810-ssb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/AD810m_op
        photo = open('Photoex/AD810m_op.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AD810m_op
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810M OP(2 799,00 грн)", url="https://muzon.com.ua/product/cort-ad810m-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
    if message.text == "Классические гитары":
        # photo/AC100_OP
        photo = open('Photoex/AC100_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC100_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AC100 OP(2 499,00 грн)", url="https://muzon.com.ua/product/cort-ac100-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/AC50op-main-cort
        photo = open('Photoex/AC50op-main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC50op-main-cort
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CORT AC50 OP W/BAG(3 458,00 грн)", url="https://muzon.com.ua/product/cort-ac50-op-w-bag/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/yamaha_c_70
        photo = open('Photoex/yamaha_c_70.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/yamaha_c_70
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C70(4 206,00 грн)", url="https://muzon.com.ua/product/yamaha-c7/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, великолепное звучание, яркий резонанс.", reply_markup=keyboard)
        # photo/yamaha_c_40_b
        photo = open('Photoex/yamaha_c_40_b.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/yamaha_c_40_b
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C40B(4 146,00 грн)", url="https://muzon.com.ua/product/yamaha-c40b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/yamaha_c_40_m
        photo = open('Photoex/yamaha_c_40_m.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/yamaha_c_40_m
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C40M(3 207,00 грн)", url="https://muzon.com.ua/product/yamaha-c40-kopirovat/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/Yamaha_C_40
        photo = open('Photoex/amaha_C_40.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha_C_40
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha C40(3 207,00 грн)", url="https://muzon.com.ua/product/yamaha-c40/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/AC100DX_OP
        photo = open('Photoex/AC100DX_OP.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC100DX_OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AC100DX OP(3 292,00 грн)", url="https://muzon.com.ua/product/cort-ac100dx-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
        # photo/AC100_SG
        photo = open('Photoex/AC100_SG.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/AC100_SG
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AC100 SG(2 699,00 грн)", url="https://muzon.com.ua/product/cort-ac100-sg/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Доступный инструмент для учеников музыкальных школ, и любителей исполнять классическую музыку, качество за за не высокую стоимость.", reply_markup=keyboard)
    if message.text == "Укулеле":
        # photo/parksons_uk_24_c
        photo = open('Photoex/parksons_uk_24_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_24_c
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK24C(1 572,00 грн)", url="https://muzon.com.ua/product/parksons-uk24c/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
        # photo/fzone_fzu_110_m
        photo = open('Photoex/fzone_fzu_110_m.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/fzone_fzu_110_m
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Fzone FZU 110M(1 415,00 грн)", url="https://muzon.com.ua/product/fzone-fzu-110m/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Fzone изготовлена из качественных материалов, обладает глубоким и ярким звучанием.", reply_markup=keyboard)
        # photo/parksons_uk_24_z_front
        photo = open('Photoex/parksons_uk_24_z_front.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_24_z_front
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK24Z(1 750,00 грн)", url="https://muzon.com.ua/product/parksons-uk24z/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
        # photo/parksons_uk_21_z
        photo = open('Photoex/parksons_uk_21_z.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_21_z
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK21Z(1 668,00 грн)", url="https://muzon.com.ua/product/parksons-uk21z/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
        # photo/parksons_uk_21_c-1
        photo = open('Photoex/parksons_uk_21_c-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/parksons_uk_21_c-1
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Parksons UK21C(1 445,00 грн)", url="https://muzon.com.ua/product/parksons-uk21c/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Укулеле от Parksons имеет яркий звук, выполнена из качественных материалов, отличный инструмент за свои деньги.", reply_markup=keyboard)
    if message.text == "Электрогитары":
        # photo/rgx121z-fs-yamaha-main
        photo = open('Photoex/rgx121z-fs-yamaha-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/rgx121z-fs-yamaha-main
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha RGX121Z (Flat Silver)(8 892,00 грн)", url="https://muzon.com.ua/product/yamaha-rgx121z-flat-silver/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Корпус гитары выполнен из ольхи в сочетании с мощным хамбакером и двумя синглами, инструмент имеет выразительную палитру красок классического и рок звучания.", reply_markup=keyboard)
        # photo/YAMAHA-PACIFICA-012-DBM
        photo = open('Photoex/YAMAHA-PACIFICA-012-DBM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA-PACIFICA-012-DBM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA PACIFICA 012 (DBM)(7 200,00 грн)", url="https://muzon.com.ua/product/yamaha-pacifica-012-dbm/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA Pacifica 012 характеризуется аналогичными контурами корпуса как у более дорогих моделей PAC112, мощным хамбакером и 2-мя синглами, обеспечивающими чистое звучание. Гитара оснащена удобным грифом,", reply_markup=keyboard)
        # photo/Yamaha PACIFICA 112J (LPB)
        photo = open('Photoex/PAC112J-LPB-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha PACIFICA 112J (LPB)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha PACIFICA 112J (LPB)(9 132,00 грн)", url="https://muzon.com.ua/product/yamaha-pacifica-112j-lpb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Корпус гитары выполнен из ольхи в сочетании с мощным хамбакером и двумя синглами, инструмент имеет выразительную палитру красок классического и рок звучания.", reply_markup=keyboard)
        # photo/KX100MA-main-cort
        photo = open('Photoex/KX100MA-main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/KX100MA-main-cort
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort KX100 METALLIC ASH(6 020,00 грн)", url="https://muzon.com.ua/product/cort-kx100-metallic-ash/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия KX имеет дизайн совместивший в себе как агрессивную внешность, так и утонченную классику, звук подходящий для разных стилей и направлений.", reply_markup=keyboard)
        # photo/Cort KX100 IRON OXIDE
        photo = open('Photoex/KX100IO_main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort KX100 IRON OXIDE
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort KX100 IRON OXIDE(6 020,00 грн)", url="https://muzon.com.ua/product/cort-kx100-iron-oxide/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "ерия KX имеет дизайн совместивший в себе как агрессивную внешность, так и утонченную классику, звук подходящий для разных стилей и направлений.", reply_markup=keyboard)
        # photo/cort_cr_200_bk
        photo = open('Photoex/cort_cr_200_bk.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/cort_cr_200_bk
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort CR200 BK(9 800,00 грн)", url="https://muzon.com.ua/product/cort-cr200-bk/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия CR — инструменты этой линейки имеют винтажный классический дизайн, отлично выполнены и обладают хорошим звучанием!", reply_markup=keyboard)
        # photo/Cort CR150 ODS
        photo = open('Photoex/CR150ODS_main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort CR150 ODS
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort CR150 ODS(8 050,00 грн)", url="https://muzon.com.ua/product/cort-cr150-ods/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Высокое качество материалов и отделки, универсальный инструмент для разных стилей исполнения.", reply_markup=keyboard)
        # photo/Cort G110 2T
        photo = open('Photoex/cort_g_110_2t.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G110 2T
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G110 2T(4 830,00 грн)", url="https://muzon.com.ua/product/cort-g110-2t/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности, надежность и качество за доступную цену.", reply_markup=keyboard)
        # photo/Cort X100 OPB
        photo = open('Photoex/cort_x_100_opb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort X100 OPB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort X100 OPB(4 550,00 грн)", url="https://muzon.com.ua/product/cort-x100-opb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия X представляет линейку инструментов Cort предназначенных для рок/металл жанров музыки, это подчеркивает дизайн инструмента и электронная начинка", reply_markup=keyboard)
        # photo/Cort X100 OPBB
        photo = open('Photoex/cort_x_100_opbb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort X100 OPBB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort X100 OPBB(4 550,00 грн)", url="https://muzon.com.ua/product/cort-x100-opbcb-kopirovat/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия X представляет линейку инструментов Cort предназначенных для рок/металл жанров музыки, это подчеркивает дизайн инструмента и электронная начинка", reply_markup=keyboard)
        # photo/Cort X100 OPBCB
        photo = open('Photoex/cort_x_100_opbcb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort X100 OPBCB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort X100 OPBCB(4 550,00 грн)", url="https://muzon.com.ua/product/cort-x100-opbcb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия X представляет линейку инструментов Cort предназначенных для рок/металл жанров музыки, это подчеркивает дизайн инструмента и электронная начинка", reply_markup=keyboard)
        # photo/Cort G110 SRD
        photo = open('Photoex/cort_g_110_srd.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G110 SRD
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G110 SRD(4 690,00 грн)", url="https://muzon.com.ua/product/cort-g110-srd/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G110 BK
        photo = open('Photoex/cort_g_110_bk.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G110 BK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G110 BK(4 690,00 грн)", url="https://muzon.com.ua/product/cort-g110-bk/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G100 OPBC
        photo = open('Photoex/cort_g100_opbc.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G100 OPBC
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G100 OPBC(3 920,00 грн)", url="https://muzon.com.ua/product/cort-g100-opbc-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G100 OPW
        photo = open('Photoex/cort_g100_opw.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G100 OPW
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G100 OPW(3 920,00 грн)", url="https://muzon.com.ua/product/cort-g100-opbc/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
        # photo/Cort G100 OPB
        photo = open('Photoex/cort_g100_opb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort G100 OPB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort G100 OPB(3 920,00 грн)", url="https://muzon.com.ua/product/cort-g100-opb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия G это начальная линейка электрогитар от компании Cort , отличный вариант для старта творческой деятельности", reply_markup=keyboard)
    if message.text == "Электро-акустические гитары":
        # photo/Cort AD810E OP
        photo = open('Photoex/cort_ad_810e_op.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort AD810E OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810E OP(4 323,00 грн)", url="https://muzon.com.ua/product/cort-ad810e-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/CORT SFX-ME OP
        photo = open('Photoex/SFX-MEOP-main-cort.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/CORT SFX-ME OP
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="CORT SFX-ME OP(4 795,00 грн)", url="https://muzon.com.ua/product/cort-sfx-me-op/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
        # photo/Cort AD810E BKS
        photo = open('Photoex/cort_ad_810e_bks.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort AD810E BKS
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort AD810E BKS(4 522,00 грн)", url="https://muzon.com.ua/product/cort-ad810e-bks/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Идеальный инструмент для новичка, который удивит и профессионалов. Отличное исполнение, яркое звучание.", reply_markup=keyboard)
    if message.text == "Бас-гитары":
        # photo/Yamaha TRBX-174 OVS
        photo = open('Photoex/trbx174_ovs_f-600x176.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha TRBX-174 OVS
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha TRBX-174 OVS(7 320,00 грн)", url="https://muzon.com.ua/product/yamaha-trbx-174-ovs/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Стильные бас-гитары, в современном дизайне и хорошим звуком. Качество от Yamaha по доступной цене", reply_markup=keyboard)
        # photo/Yamaha TRBX-174 RM
        photo = open('Photoex/yamaha_trbx_174_rm-600x176.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha TRBX-174 RM
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha TRBX-174 RM(7 320,00 грн)", url="https://muzon.com.ua/product/yamaha-trbx-174-rm/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Стильные бас-гитары, в современном дизайне и хорошим звуком. Качество от Yamaha по доступной цене", reply_markup=keyboard)
        # photo/Yamaha TRBX-174 BL
        photo = open('Photoex/yamaha_trbx_174_bl-600x176.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Yamaha TRBX-174 BL
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Yamaha TRBX-174 BL(7 320,00 грн)", url="https://muzon.com.ua/product/yamaha-trbx-174-bl/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Стильные бас-гитары, в современном дизайне и хорошим звуком. Качество от Yamaha по доступной цене", reply_markup=keyboard)
        # photo/Cort Action PJ OPB
        photo = open('Photoex/cort_action_pj_opb.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort Action PJ OPB
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort Action PJ OPB(4 725,00 грн)", url="https://muzon.com.ua/product/cort-action-pj-opb/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия Action отличается высоким качеством и неплохим звуком, за умеренную стоимость. Отличный выбор для обучения", reply_markup=keyboard)
        # photo/Cort Action PJ OPBC
        photo = open('Photoex/cort_action_pj_opbc.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/Cort Action PJ OPBC
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Cort Action PJ OPBC(4 725,00 грн)", url="https://muzon.com.ua/product/cort-action-pj-opbc/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Серия Action отличается высоким качеством и неплохим звуком, за умеренную стоимость. Отличный выбор для обучения", reply_markup=keyboard)
    if message.text == "Электронные барабаны":
        # photo/YAMAHA DTX402K
        photo = open('Photoex/dtx402k_main-yamaha.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA DTX402K
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA DTX402K(13 437,00 грн)", url="https://muzon.com.ua/product/yamaha-dtx402k/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA DTX402K — электронная ударная установка", reply_markup=keyboard)
        # photo/ALESIS NITRO MESH KIT
        photo = open('Photoex/LDLKNitroMeshKit_Ortho_Web_RGB.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/ALESIS NITRO MESH KIT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="ALESIS NITRO MESH KIT(14 700,00 грн)", url="https://muzon.com.ua/product/alesis-nitro-mesh-kit/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "ALESIS NITRO MESH KIT — это полноценная барабанная установка!", reply_markup=keyboard)
        # photo/ALESIS TURBO MESH KIT
        photo = open('Photoex/turbo-mesh-kit-ortho-web.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/ALESIS TURBO MESH KIT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="ALESIS TURBO MESH KIT(11 318,00 грн)", url="https://muzon.com.ua/product/alesis-turbo-mesh-kit/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "ALESIS TURBO MESH KIT — это полноценная барабанная установка!", reply_markup=keyboard)
    if message.text == "Акустические барабаны":
        # photo/PDP PDZ522KT Z5 SERIES GREY METAL
        photo = open('Photoex/PDP-PDZ522KT-GM-Z5-Series-Grey-Metal-барабаны.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PDP PDZ522KT Z5 SERIES GREY METAL
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PDP PDZ522KT Z5 SERIES GREY METAL(15 288,00 грн)", url="https://muzon.com.ua/product/pdp-pdz522kt-z5-series-grey-metal/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Высокое качество изготовления корпуса и механических деталей, позволяет Z5 Series конкурировать с более дорогими ударными установками.", reply_markup=keyboard)
        # photo/YAMAHA RYDEEN (BLACK GLITTER)
        photo = open('Photoex/RDP2F5-BLG-rydeen-front-yam.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA RYDEEN (BLACK GLITTER)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA RYDEEN (BLACK GLITTER)(13 554,00 грн)", url="https://muzon.com.ua/product/yamaha-rydeen-black-glitter/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/YAMAHA RYDEEN (BURGUNDY GLITTER)
        photo = open('Photoex/RDP2F5-BGG-main-yamaa.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA RYDEEN (BURGUNDY GLITTER)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA RYDEEN (BURGUNDY GLITTER)(13 554,00 грн)", url="https://muzon.com.ua/product/yamaha-rydeen-burgundy-glitter/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC110 (Red)
        photo = open('Photoex/MXC-110-red-2019-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC110 (Red)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC110 (Red)(12 885,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc110-red/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC110 (Black)
        photo = open('Photoex/maxtone_mxc_110_black.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC110 (Black)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC110 (Black)(12 885,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc110-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (White)
        photo = open('Photoex/MXC3005-1-white.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (White)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (White)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-white/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (Metallic Blue)
        photo = open('Photoex/MXC3005-blue-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (Metallic Blue)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (Metallic Blue)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-metallic-blue/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (Wine Red)
        photo = open('Photoex/maxtone_mxc3005_red.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (Wine Red)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (Wine Red)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-wine-red/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
        # photo/MAXTONE MXC3005 (Black)
        photo = open('Photoex/mxc3005bk-12.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE MXC3005 (Black)
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE MXC3005 (Black)(14 673,00 грн)", url="https://muzon.com.ua/product/maxtone-mxc3005-black/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Ударная установка начального класса, отличный вариант для первой ударной установки, для обучения", reply_markup=keyboard)
    if message.text == "Перкуссия":
        # photo/GON BOPS FS785SB FIESTA
        photo = open('Photoex/Bongo-Fiesta-Burnt-Angle-FS785SB.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/GON BOPS FS785SB FIESTA
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="GON BOPS FS785SB FIESTA(2 514,00 грн)", url="https://muzon.com.ua/product/gon-bops-fs785sb-fiesta-bongos-sunburst/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "GON BOPS FS785SB FIESTA BONGOS SUNBURST — деревянные латинские бонги", reply_markup=keyboard)
        # photo/MAXTONE BC13
        photo = open('Photoex/MAXTONE-BC13.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE BC13
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE BC13(1 095,00 грн)", url="https://muzon.com.ua/product/maxtone-bc13/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE BC13 — деревянные латинские бонги", reply_markup=keyboard)
        # photo/MAXTONE DJC-1021
        photo = open('Photoex/MAXTONEDJC-1021.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DJC-1021
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DJC-1021(4 554,00 грн)", url="https://muzon.com.ua/product/maxtone-djc-1021/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DJC-1021 — джембе барабан", reply_markup=keyboard)
        # photo/MAXTONE ADJ10B
        photo = open('Photoex/ADJ_B.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE ADJ10B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE ADJ10B(3 441,00 грн)", url="https://muzon.com.ua/product/maxtone-adj10b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE ADJ10B -деревянный джембе барабан", reply_markup=keyboard)
        # photo/GON BOPS FSCJW FIESTA CAJON WALNUT
        photo = open('Photoex/GonBops-FSCJW-Fiesta-cajon-walnut.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/GON BOPS FSCJW FIESTA CAJON WALNUT
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="GON BOPS FSCJW FIESTA CAJON WALNUT(3 761,00 грн)", url="https://muzon.com.ua/product/gon-bops-fscjw-fiesta-cajon-walnut/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Gon Bops расширяет модельный ряд кахонов новыми Fiesta моделями — даелая их доступными инструментами для начинающих перкуссионистов", reply_markup=keyboard)
        # photo/GON BOPS FSCJM FIESTA CAJON MAHOGANY
        photo = open('Photoex/GON-BOPS-FSCJM.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/GON BOPS FSCJM FIESTA CAJON MAHOGANY
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="GON BOPS FSCJM FIESTA CAJON MAHOGANY(3 478,00 грн)", url="https://muzon.com.ua/product/gon-bops-fscjm-fiesta-cajon-mahogany/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Gon Bops расширяет модельный ряд кахонов новыми Fiesta моделями — даелая их доступными инструментами для начинающих перкуссионистов", reply_markup=keyboard)
    if message.text == "Тарелки для ударных":
        # photo/SABIAN 45003XEU B8X Performance Set
        photo = open('Photoex/45003x-b8x-performance-set_full.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN 45003XEU B8X Performance Set
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN 45003XEU B8X Performance Set(8 694,00 грн)", url="https://muzon.com.ua/product/sabian-45003xeu-b8x-performance-set/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN 45003XEU B8X Performance Set — доступные тарелки с превосходным звучанием", reply_markup=keyboard)
        # photo/SABIAN SBR5001 SBr First Pack
        photo = open('Photoex/sbr5001-sbr-first-pack-full.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN SBR5001 SBr First Pack
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN SBR5001 SBr First Pack(3 969,00 грн)", url="https://muzon.com.ua/product/sabian-sbr5001-sbr-first-pack/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN SBR5001 SBr First Pack — доступные тарелки с превосходным звучанием", reply_markup=keyboard)
        # photo/SABIAN SBR5003 SBr Performance Set
        photo = open('Photoex/sbr-performance-set_full.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN SBR5003 SBr Performance Set
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN SBR5003 SBr Performance Set(6 678,00 грн)", url="https://muzon.com.ua/product/sabian-sbr5003-sbr-performance-set/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN SBR5003 SBr Performance Set — доступные тарелки с превосходным звучанием", reply_markup=keyboard)
    if message.text == "Барабанные палочки":
        # photo/MAXTONE ADWCW2 — щетки барабанные деревянные
        photo = open('Photoex/adwc-w2-main-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE ADWCW2 — щетки барабанные деревянные
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="c(233,00 грн)", url="https://muzon.com.ua/product/maxtone-adwcw2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE ADWCW2 — щетки барабанные деревянные", reply_markup=keyboard)
        # photo/PROMARK LA7AN L.A. SPECIAL 7AN
        photo = open('Photoex/LA-7AN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA7AN L.A. SPECIAL 7AN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA7AN L.A. SPECIAL 7AN(186,00 грн)", url="https://muzon.com.ua/product/promark-la7an-l-a-special-7an/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5BN L.A. SPECIAL 5BN
        photo = open('Photoex/LA-5BN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5BN L.A. SPECIAL 5BN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5BN L.A. SPECIAL 5BN(186,00 грн)", url="https://muzon.com.ua/product/promark-la5bn-l-a-special-5bn/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5AN L.A. SPECIAL 5AN
        photo = open('Photoex/LA-5AN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5AN L.A. SPECIAL 5AN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5AN L.A. SPECIAL 5AN(186,00 грн)", url="https://muzon.com.ua/product/promark-la5an-l-a-special-5an/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/VATER GW7AW GOODWOOD by VATER 7A
        photo = open('Photoex/VATER-GW7AW-GOODWOOD-by-VATER-7A.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW7AW GOODWOOD by VATER 7A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW7AW GOODWOOD by VATER 7A(171,00 грн)", url="https://muzon.com.ua/product/vater-gw7aw-goodwood-by-vater-7a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/VATER GW2BW GOODWOOD by VATER 2B
        photo = open('Photoex/VATER-GW2BW-600x250.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW2BW GOODWOOD by VATER 2B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW2BW GOODWOOD by VATER 2B(171,00 грн)", url="https://muzon.com.ua/product/vater-gw2bw-goodwood-by-vater-2b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/VATER GW5BW GOODWOOD by VATER 5B
        photo = open('Photoex/gw5aw.png', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW5BW GOODWOOD by VATER 5B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW5BW GOODWOOD by VATER 5B(171,00 грн)", url="https://muzon.com.ua/product/vater-gw5aw-goodwood-by-vater-5b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/VATER GW5AW GOODWOOD by VATER 5A
        photo = open('Photoex/VATER-GW5AW.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/VATER GW5AW GOODWOOD by VATER 5A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="VATER GW5AW GOODWOOD by VATER 5A(171,00 грн)", url="https://muzon.com.ua/product/vater-gw5aw-goodwood-by-vater-5a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Goodwood by Vater — это доступные, но при этом качественные и очень надежные барабанные палочки.", reply_markup=keyboard)
        # photo/PROMARK LA7AW L.A. SPECIAL 7A
        photo = open('Photoex/LA-7AW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA7AW L.A. SPECIAL 7A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA7AW L.A. SPECIAL 7A(168,00 грн)", url="https://muzon.com.ua/product/promark-la7aw-l-a-special-7a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA2BW L.A. SPECIAL 2B
        photo = open('Photoex/LA-2BW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA2BW L.A. SPECIAL 2B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA2BW L.A. SPECIAL 2B(168,00 грн)", url="https://muzon.com.ua/product/promark-la2bw-l-a-special-2b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA2BN L.A. SPECIAL 2BN
        photo = open('Photoex/LA-2BN-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA2BN L.A. SPECIAL 2BN
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA2BN L.A. SPECIAL 2BN(186,00 грн)", url="https://muzon.com.ua/product/promark-la2bn-l-a-special-2bn/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5AW L.A. SPECIAL 5A
        photo = open('Photoex/LA-5AW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5AW L.A. SPECIAL 5A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5AW L.A. SPECIAL 5A(168,00 грн)", url="https://muzon.com.ua/product/promark-la5aw-l-a-special-5a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LA5BW L.A. SPECIAL 5B
        photo = open('Photoex/LA-5BW-2017.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LA5BW L.A. SPECIAL 5B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LA5BW L.A. SPECIAL 5B(168,00 грн)", url="https://muzon.com.ua/product/promark-la5bw-l-a-special-5b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "L.A. Special — это доступная серия барабанных палочек от Pro-Mark", reply_markup=keyboard)
        # photo/PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B
        photo = open('Photoex/LAU5BW-promark-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B(78,00 грн)", url="https://muzon.com.ua/product/promark-lau5aw-l-a-special-non-printed-5b/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "PROMARK LAU5BW L.A. SPECIAL Non-Printed 5B — барабанные палочки", reply_markup=keyboard)
        # photo/PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A
        photo = open('Photoex/LAU5AW-promark.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A(78,00 грн)", url="https://muzon.com.ua/product/promark-lau5aw-l-a-special-non-printed-5a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "PROMARK LAU5AW L.A. SPECIAL Non-Printed 5A — барабанные палочки", reply_markup=keyboard)
        # photo/MAXTONE ADWC5AK
        photo = open('Photoex/maxtone-5a-china.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE ADWC5AK
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE ADWC5AK(49,00 грн)", url="https://muzon.com.ua/product/maxtone-adwc5ak/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE ADWC5AK — барабанные палочки", reply_markup=keyboard)
    if message.text == "Пластики":
        # photo/MAXTONE DHB22
        photo = open('Photoex/dhb20-black-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHB22
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHB22(346,00 грн)", url="https://muzon.com.ua/product/maxtone-dhb22/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHB22 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DHB20
        photo = open('Photoex/dhb20-black-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHB20
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHB20(343,00 грн)", url="https://muzon.com.ua/product/maxtone-dhb20/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHB20 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DHD22
        photo = open('Photoex/dhd22_white.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD22
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD22(451,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd22/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD22 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DHD20
        photo = open('Photoex/dhd20_White.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD20
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD20(405,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd20/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD20 — пластик для бас-бочки", reply_markup=keyboard)
        # photo/MAXTONE DH22T2
        photo = open('Photoex/MAXTONE-DH20T2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH22T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH22T2(260,00 грн)", url="https://muzon.com.ua/product/maxtone-dh22t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH22T2 — пластик для бас-барабана", reply_markup=keyboard)
        # photo/MAXTONE DH20T2
        photo = open('Photoex/MAXTONE-DH20T2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH20T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH20T2(254,00 грн)", url="https://muzon.com.ua/product/maxtone-dh20t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH20T2 — пластик для бас-барабана", reply_markup=keyboard)
        # photo/MAXTONE DHD16
        photo = open('Photoex/MAxtone_DHD16.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD16
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD16(251,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd16/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD16 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DHD14
        photo = open('Photoex/MAxtone_dhd14.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD14
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD14(200,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd14/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD14 — пластик для тома / рабочего барабана", reply_markup=keyboard)
        # photo/MAXTONE DHD13
        photo = open('Photoex/MAxtone_dhd14.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD13
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD13(180,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd13/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD13 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DHD12
        photo = open('Photoex/MAxtone_dhd14.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DHD12
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DHD12(157,00 грн)", url="https://muzon.com.ua/product/maxtone-dhd12/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DHD12 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DH16T2
        photo = open('Photoex/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH16T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH16T2(126,00 грн)", url="https://muzon.com.ua/product/maxtone-dh16t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH16T2 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DH14T2
        photo = open('Photoex/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH14T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH14T2(97,00 грн)", url="https://muzon.com.ua/product/maxtone-dh14t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH14T2 — пластик для тома / рабочего барабана", reply_markup=keyboard)
        # photo/MAXTONE DH13T2
        photo = open('Photoex/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH13T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH13T2(86,00 грн)", url="https://muzon.com.ua/product/maxtone-dh13t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH13T2 — пластик для тома", reply_markup=keyboard)
        # photo/MAXTONE DH12T2
        photo = open('Photoex/DH-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DH12T2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DH12T2(80,00 грн)", url="https://muzon.com.ua/product/maxtone-dh12t2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DH12T2 — пластик для тома", reply_markup=keyboard)
    if message.text == "Стойки и механика":
        # photo/MAXTONE CBS583
        photo = open('Photoex/CBS583-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CBS583
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CBS583(885,00 грн)", url="https://muzon.com.ua/product/maxtone-cbs583/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE CBS583 стойка для тарелки, типа «журавль»,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/MAXTONE CS583
        photo = open('Photoex/CS583-1.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CS583
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CS583(771,00 грн)", url="https://muzon.com.ua/product/maxtone-cs583/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE CS583 прямая стойка под тарелки,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/MAXTONE CS121
        photo = open('Photoex/CS121_maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE CS121
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE CS121(634,00 грн)", url="https://muzon.com.ua/product/maxtone-cs121/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE CS121 прямая стойка под тарелки,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/YAMAHA LC810A
        photo = open('Photoex/YamahaLC810A.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/YAMAHA LC810A
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="YAMAHA LC810A(342,00 грн)", url="https://muzon.com.ua/product/yamaha-lc810a/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "YAMAHA LC810A  хай-хет замок,вся продукция от Yamaha обладает неизменным высоким качеством.", reply_markup=keyboard)
        # photo/MAXTONE 42
        photo = open('Photoex/42-main-maxtone.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE 42
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE 42(185,00 грн)", url="https://muzon.com.ua/product/maxtone-42/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE 42 хай-хет замок,доступная недорогая механика для ударных", reply_markup=keyboard)
    if message.text == "Педали для бас-барабана":
        # photo/MAXTONE DP921
        photo = open('Photoex/MAxtone_dp921.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DP921
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DP921(1 870,00 грн)", url="https://muzon.com.ua/product/maxtone-dp921/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DP921 педаль для бас-бочки,доступная недорогая механика для ударных", reply_markup=keyboard)
        # photo/MAXTONE DPC110
        photo = open('Photoex/MAxtone_dp921.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/MAXTONE DPC110
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="MAXTONE DPC110(954,00 грн)", url="https://muzon.com.ua/product/maxtone-dpc110/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "MAXTONE DPC110 педаль для бас-бочки,доступная недорогая механика для ударных", reply_markup=keyboard)
    if message.text == "Аксессуары для ударных":
        # photo/SABIAN SSSC1 CYMBAL CLEANER
        photo = open('Photoex/Sabian-SSSC1-main.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/SABIAN SSSC1 CYMBAL CLEANER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="SABIAN SSSC1 CYMBAL CLEANER(199,00 грн)", url="https://muzon.com.ua/product/sabian-sssc1-cymbal-cleaner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "SABIAN SSSC1 CYMBAL CLEANER — Полироль для тарело", reply_markup=keyboard)
        # photo/DUNLOP 6444 DRUM SHELL POLISH AND CLEANER
        photo = open('Photoex/Drum_Shell6444.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 6444 DRUM SHELL POLISH AND CLEANER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 6444POLISH AND CLEANER(197,00 грн)", url="https://muzon.com.ua/product/dunlop-6444-drum-shell-polish-and-cleaner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Полироль-очиститель для деревянных барабанов, также применим для металлических частей барабанов.", reply_markup=keyboard)
        # photo/DUNLOP 6434 CYMBAL CLEANER
        photo = open('Photoex/Dunlop-6434.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 6434 CYMBAL CLEANER
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 6434 CYMBAL CLEANER(197,00 грн)", url="https://muzon.com.ua/product/dunlop-6434-cymbal-cleaner/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Полироль-очиститель для тарелок, состав идеально сбалансированный для металлов тарелок.", reply_markup=keyboard)
        # photo/DUNLOP 6422 CYMBAL INTENSIVE CARE
        photo = open('Photoex/6422.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/DUNLOP 6422 CYMBAL INTENSIVE CARE
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="DUNLOP 6422 CYMBAL INTENSIVE CARE(193,00 грн)", url="https://muzon.com.ua/product/dunlop-6422-cymbal-intensive-care/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Средсво для очистки тарелок Cymbal Intensive Care.", reply_markup=keyboard)
    if message.text == "Скрипки":
        # photo/STENTOR 1500/C VIOLIN OUTFIT 3/4
        photo = open('Photoex/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/C VIOLIN OUTFIT 3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/C VIOLIN OUTFIT 3/4(5 275,00 грн)", url="https://muzon.com.ua/product/stentor-1500-c-student-ii-violin-outfit-3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/A VIOLIN OUTFIT 4/4
        photo = open('Photoex/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/A VIOLIN OUTFIT 4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/A VIOLIN OUTFIT 4/4(5 275,00 грн)", url="https://muzon.com.ua/product/stentor-1500-a-student-ii-violin-outfit-4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II ", reply_markup=keyboard)
        # photo/STENTOR 1500/F VIOLIN OUTFIT 1/4
        photo = open('Photoex/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/F VIOLIN OUTFIT 1/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/F VIOLIN OUTFIT 1/4(5 193,00 грн)", url="https://muzon.com.ua/product/stentor-1500-f-student-ii-violin-outfit-1-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/E VIOLIN OUTFIT 1/2
        photo = open('Photoex/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/E VIOLIN OUTFIT 1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/E VIOLIN OUTFIT 1/2(5 193,00 грн)", url="https://muzon.com.ua/product/stentor-1500-e-student-ii-violin-outfit-1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультантов музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/I VIOLIN OUTFIT 1/16
        photo = open('Photoex/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/I VIOLIN OUTFIT 1/16
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/I VIOLIN OUTFIT 1/16(4 774,00 грн)", url="https://muzon.com.ua/product/stentor-1500-i-student-ii-violin-outfit-1-16/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультантов музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1500/G VIOLIN OUTFIT 1/8
        photo = open('Photoex/1500A_2.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1500/G VIOLIN OUTFIT 1/8
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1500/G VIOLIN OUTFIT 1/8(4 774,00 грн)", url="https://muzon.com.ua/product/stentor-1500-g-student-ii-violin-outfit-1-8/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Большинство преподавателей и консультанты музыкальных магазинов рекомендуют Stentor Student II", reply_markup=keyboard)
        # photo/STENTOR 1018/C STANDARD 3/4
        photo = open('Photoex/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/C STANDARD 3/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/C STANDARD 3/4(3 506,00 грн)", url="https://muzon.com.ua/product/stentor-1018-c-student-standard-3-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/F STANDARD 1/4
        photo = open('Photoex/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/F STANDARD 1/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/F STANDARD 1/4(3 303,00 грн)", url="https://muzon.com.ua/product/stentor-1018-f-student-standard-1-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/G STANDARD 1/8
        photo = open('Photoex/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/G STANDARD 1/8
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/G STANDARD 1/8(3 303,00 грн)", url="https://muzon.com.ua/product/stentor-1018-g-student-standard-1-8/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/E STANDARD 1/2
        photo = open('Photoex/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/E STANDARD 1/2
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/E STANDARD 1/2(3 303,00 грн)", url="https://muzon.com.ua/product/stentor-1018-e-student-standard-1-2/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)
        # photo/STENTOR 1018/A STANDARD 4/4
        photo = open('Photoex/stantor_1018_c.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo)
        # info with btn/STENTOR 1018/A STANDARD 4/4
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="STENTOR 1018/A STANDARD 4/4(3 506,00 грн)", url="https://muzon.com.ua/product/stentor-1018-a-student-standard-4-4/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Даже когда бюджет не позволяет приобрести дорогой инструмент для начинающих, у Stentor есть решение — модель Stentor Student Standard!", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)