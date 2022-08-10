from pyobigram.utils import sizeof_fmt,get_file_size,createID,nice_time
from pyobigram.client import ObigramClient,inlineQueryResultArticle
from pyobigram.client import inlineKeyboardMarkup,inlineKeyboardMarkupArray,inlineKeyboardButton
if '/start' in msgText:
            start_msg = '<b>✅ SECCIÓN INICIADA✅</b>\n'
            start_msg+= '<b>🌎Este es un bot configurado para la descarga de contenido de internet sin gastos de mb 🌎
            start_msg+= '<b>🌟GUIA: </b> <a href="/tutorial">/tutorial</a>\n'
            start_msg+= '<b>☺️FUNCIONAMIENTO☺️: Enviame enlaces de descarga directa para procesar :) PRIMERO CONFIGURAR</b>\n'
            start_msg+= '<b>💚DESAROLLADOR @nautaii 💚</b>\n'
            bot.editMessageText(message,start_msg,parse_mode='html')
        elif '/token' in msgText:
            message2 = bot.editMessageText(message,'Obteniendo Token...')
            try:
                proxy = ProxyCloud.parse(user_info['proxy'])
                client = MoodleClient(user_info['moodle_user'],
                                      user_info['moodle_password'],
                                      user_info['moodle_host'],
                                      user_info['moodle_repo_id'],proxy=proxy)
                loged = client.login()
                if loged:
                    token = client.userdata
                    modif = token['token']
                    bot.editMessageText(message2,'Su Token es: '+modif)
                    client.logout()

bot_token = os.environ.get('5385354366:AAHUlY12aEGiFevVAJmrt6C1NjtwofZx8cI')
    print('init bot.')
    #set in debug
    #bot_token = '5385354366:AAHUlY12aEGiFevVAJmrt6C1NjtwofZx8cI'
    bot = ObigramClient(bot_token)
    bot.onMessage(onmessage)
    bot.onCallbackData('/cancel ',cancel_task)
    bot.onCallbackData('/maketxt ', maketxt)
    bot.onCallbackData('/deleteproxy ',deleteproxy)
    bot.onCallbackData('/convert2calendar ',convert2calendar)
    bot.run()
