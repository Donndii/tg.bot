import re

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,

)

from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    PicklePersistence,
    Filters,
    MessageHandler,
    updater,
    CallbackQueryHandler
)
from menu import main_menu_keyboard, coffeshop_keyboard
from button import start_b, coffeshop_b
from message import panf_info, beskan_info, alya_info, mokki_info, adriano_info, arte_info, aldo_info, biscuit_info, lesnoy_info, michelle_info
from message2 import cake_info, herb_info, zebra_info, flask_info, lovely_info, yun_info, bulcoff_info, vangogh_info, tucano_info, moqa_info
from token_bot import TOKEN

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Здравствуй, {username}! Что вас интересует?'.format(
        username = update.effective_user.first_name\
            if update.effective_user.first_name is not None \
                else update.effective_user.username
    ),
    reply_markup=main_menu_keyboard()
    )

CAFE_REGEX=r"(?=("+(start_b[0]) + r"))"
SALE_REGEX=r"(?=("+(start_b[1]) + r"))"
COFFEE_REGEX=r"(?=("+(start_b[2]) + r"))"

LENIN_REGEX=r"(?=("+(coffeshop_b[0]) + r"))"
OCTOBER_REGEX=r"(?=("+(coffeshop_b[1]) + r"))"
SVERDLOV_REGEX=r"(?=("+(coffeshop_b[2]) + r"))"
PERVOMAY_REGEX=r"(?=("+(coffeshop_b[3]) + r"))"
DISTRICT_REGEX=r"(?=("+(coffeshop_b[4]) + r"))"
BACK_REGEX=r"(?=("+(coffeshop_b[5]) + r"))"


def receive_location(update: Update, context: CallbackContext):
    info = re.match(CAFE_REGEX, update.message.text)
    update.message.reply_text(
        'Выберите район, который вам подходит:)',
        reply_markup=coffeshop_keyboard()
    )

def back(update:Update, context: CallbackContext):
     info = re.match(BACK_REGEX,update.message.text)
     update.message.reply_text(
        'Вы вернулись на главное меню;)',
        reply_markup=main_menu_keyboard()    
    )

def lenin(update: Update, context:CallbackContext):
    info = re.match(LENIN_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Adriano Coffee', callback_data = 'adriano')],
        [InlineKeyboardButton('Coffee Arte Gallery', callback_data = 'coffeearte')],
        [InlineKeyboardButton('Michelle', callback_data = 'michelle')],
    ]    
    
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите кофейню:',
        reply_markup=reply_markup1
    )

def october(update: Update, context:CallbackContext):
    info = re.match(OCTOBER_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Aldo Coffee', callback_data = 'aldo')],
        [InlineKeyboardButton('Van Gogh coffee', callback_data = 'vangogh')],
    
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите кофейню:',
        reply_markup=reply_markup1
    )
def sverdlov(update: Update, context:CallbackContext):
    info = re.match(SVERDLOV_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Lesnoy', callback_data = 'lesnoy')],
        [InlineKeyboardButton('Tucano Coffee', callback_data = 'tucano')],

    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите кофейню:',
        reply_markup=reply_markup1
    )
def pervomay(update: Update, context:CallbackContext):
    info = re.match(PERVOMAY_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Panfiloff coffee', callback_data = 'panfilof')],
        [InlineKeyboardButton('Beskan', callback_data = 'beskan')],
        [InlineKeyboardButton('А ля де Поля', callback_data = 'alya')],
        [InlineKeyboardButton('Mokki coffee', callback_data = 'mokki')],
        
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите кофейню:',
        reply_markup=reply_markup1
    )

def district(update: Update, context:CallbackContext):
    info = re.match(DISTRICT_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Biscuit', callback_data = 'biscuit')],
        [InlineKeyboardButton('MOQA', callback_data = 'moqa')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите кофейню:',
        reply_markup=reply_markup1
    )

def sales(update: Update, context:CallbackContext):
    info = re.match(SALE_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Herb Cafe', callback_data = 'herb')],
        [InlineKeyboardButton('Cakes & bubbles', callback_data = 'cake')],
        [InlineKeyboardButton('Yuns Kitchen', callback_data = 'yun')],
        [InlineKeyboardButton('Bulcoffs Coffee', callback_data = 'bulcoff')],
        
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите место:',
        reply_markup=reply_markup1
    )


def coffeeshop(update: Update, context:CallbackContext):
    info = re.match(COFFEE_REGEX,update.message.text)
    keyboard = [
        [InlineKeyboardButton('Zebra COFFEE', callback_data = 'zebra')],
        [InlineKeyboardButton('FLASK coffee', callback_data = 'flask')],
        [InlineKeyboardButton('Lovely Cake', callback_data = 'lovely')],
           
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите место:',
        reply_markup=reply_markup1
    )

def inline_buttons(update: Update, context: CallbackContext):
    keyboard = [ 
        [InlineKeyboardButton('Panfiloff coffee', callback_data = 'panfilof')],
        [InlineKeyboardButton('Beskan', callback_data = 'beskan')],
        [InlineKeyboardButton('А ля де Поля', callback_data = 'alya')],
        [InlineKeyboardButton('Mokki coffee', callback_data = 'mokki')],
        
    ]

    reply_markup1 = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()

    if query.data == 'panfilof':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/panfiloff.jpg', 'rb')   
        )
        query.message.reply_text(
            panf_info 
        )
        

        

    if query.data == 'beskan':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/beskan.jpg', 'rb')  
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open( 'img/beskann.jpg', 'rb') 
        )
        query.message.reply_text(
            beskan_info
        )
    
    if query.data == 'alya':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/alya.jpg', 'rb')   
        )
        query.message.reply_text(
            alya_info
        )

    if query.data == 'mokki':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/mokki.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/mokk.jpg', 'rb') 
        )    
        query.message.reply_text(
            mokki_info
        )

    if query.data == 'adriano':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/adriano.jpg', 'rb')   
        )
        query.message.reply_text(
            adriano_info
        )

    if query.data == 'coffeearte':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/arte.jpg', 'rb')   
        )
        query.message.reply_text(
            arte_info
        )
        
    if query.data == 'michelle':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/michell.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/michelle.jpg', 'rb')   
        )
        query.message.reply_text(
            michelle_info
        )
        
    if query.data == 'aldo':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/aldo.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/ald.jpg', 'rb')   
        )
        query.message.reply_text(
            aldo_info
        )

    if query.data == 'vangogh':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/vangogh.jpg', 'rb')   
        )
        query.message.reply_text(
            vangogh_info
        )
        
    if query.data == 'lesnoy':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/lesnoy.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/lesnoi.jpg', 'rb')   
        )
        query.message.reply_text(
            lesnoy_info
        )
        
    if query.data == 'tucano':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/tucano.jpg', 'rb')   
        )
        query.message.reply_text(
            tucano_info
        )

    if query.data == 'moqa':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/moqa.jpg', 'rb')   
        )
        query.message.reply_text(
            moqa_info
        )
    
    if query.data == 'biscuit':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/biscuit.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/bis.jpg', 'rb')   
        )
        query.message.reply_text(
            biscuit_info
        )

    if query.data == 'cake':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/cake.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/cakes.jpg', 'rb')   
        )
        query.message.reply_text(
            cake_info
        )

    if query.data == 'bulcoff':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/bulcof.jpg', 'rb')   
        )
        query.message.reply_text(
            bulcoff_info
        )
    if query.data == 'yun':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/yuns.jpg', 'rb')   
        )
        query.message.reply_text(
            yun_info
        )
    if query.data == 'herb':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/herb.jpg', 'rb')   
        )
        query.message.reply_text(
            herb_info
        )
    if query.data == 'zebra':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/zebra.jpg', 'rb')   
        )
        query.message.reply_text(
            zebra_info
        )
    if query.data == 'lovely':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/lovely.jpg', 'rb')   
        )
        query.message.reply_text(
            lovely_info
        )
    if query.data == 'flask':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/flas.jpg', 'rb')   
        )
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo = open('img/flask.jpg', 'rb')   
        )
        query.message.reply_text(
            flask_info
        )




updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))   

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CAFE_REGEX),
    receive_location 
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_REGEX),
    back
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LENIN_REGEX),
    lenin
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(OCTOBER_REGEX),
    october
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SVERDLOV_REGEX),
    sverdlov
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PERVOMAY_REGEX),
    pervomay
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DISTRICT_REGEX),
    district
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(SALE_REGEX),
    sales
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COFFEE_REGEX),
    coffeeshop
))

updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))
updater.start_polling()
updater.idle()