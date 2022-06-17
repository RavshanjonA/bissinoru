import telegram

from django.conf import settings
from django.template.loader import render_to_string

def order_product_on_telegram(orders):
    message_html = render_to_string('index.html', {
        'orders': orders
    })
    telegram_settings = settings.TELEGRAM
    bot = telegram.Bot(token=telegram_settings['bot_token'])
    bot.send_message(chat_id="@%s" % telegram_settings['channel_name'],
                     text=message_html, parse_mode=telegram.ParseMode.HTML)