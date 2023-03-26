import telebot
from openpyxl import load_workbook
wb = load_workbook("لواء ٣٠٨.xlsx",read_only=True)
bot = telebot.TeleBot(input("Token : "))
@bot.message_handler(content_types=["text"])
def start(message):
    if message.text == "/start":
        bot.reply_to(message, f"• ارسل اسم للبحث عليه داخا بيانات ميليشا سرايا السلام .")
    msg = message.text
    if "" in msg:
        ws = wb.active
        for row in ws.rows:
            if str(msg) in row[0].value:
            	Message = f'''• الاسم الرباعي : {row[0].value}\n• المواليد : {row[1].value}\n• محل التولد : {row[2].value}\n• الجنس : {row[3].value}\n• اسم الام الثلاثي : {row[4].value}\n• رقم هوية الاحوال المدنية : {row[5].value}\n• الحالة الزوجية : {row[6].value}\n• اسم الزوجة : {row[7].value}\n• عدد الاطفال : {row[8].value}\n• التحصيل الدراسي : {row[9].value}\n• القومية : {row[10].value}\n• الديانة : {row[11].value}\n• المذهب : {row[12].value}\n• العمل او الوظيفة : {row[13].value}\n• عنوان المهنة : {row[14].value}\n• الحرفة : {row[15].value}\n• المحافظة : {row[16].value}\n• القضاء : {row[17].value}\n• الناحية : {row[18].value}\n• المنطقة : {row[19].value}\n• المحلة : {row[20].value}\n• الزقاق : {row[21].value}\n• الدار : {row[22].value}\n• اقرب نقطة دالة : {row[23].value}\n• الهاتف : {row[24].value}\n• اللواء : {row[25].value}\n• فوج : {row[26].value}\n• سرية : {row[27].value}\n• الصنف : {row[28].value}\n• الخدمة العسكرية : {row[29].value}\n• عدد سنوات الخدمة : {row[30].value}\n• المعرف الأول : {row[31].value}\n• الهاتف : {row[32].value}\n> @FFF8FFFF'''
            	bot.reply_to(message, f"{Message}")
bot.infinity_polling()
