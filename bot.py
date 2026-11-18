import telebot

TOKEN = "9113387835:AAEgHgaow1duLEKr9FWbuSxMnHLDkGE0eNU"
ADMIN_ID = "7562367120"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if str(message.from_user.id) == ADMIN_ID:
        bot.reply_to(message, "أهلاً بيك يا  عمرو يا مطور! 🚀 بوت كيريو شغال وجاهز لاستقبال الأوامر.")
    else:
        bot.reply_to(message, "عذراً، هذا البوت مخصص للمطور فقط.")

if __name__ == "__main__":
    print("البوت يعمل الآن ومتصل بتليجرام بنجاح...")
    bot.infinity_polling()          
