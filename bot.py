import requests , re
from urllib.parse import unquote
import telebot
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
import random
import time

def rand():
	ran = [ Scream ,  Submarine ,  Cheetah ,  Sadness ,  Graffiti ,  Landscape ,  Polygons ,  Illusion ,  Flames ,  Mola ,  Tattoo ,  Mushroom ,  Nebula ,  Daisies ,  Fur ,  Space ,  Brains ,  Acid ,  Night ,  Quirky ,  Waves ,  Coldrain ,  Sparks ,  Splash ,  Floating ,  Frost ,  Berry ,  Leather ,  Frida ,  Grey ,  Nouveau ,  Ceremony ,  Psychedelic ,  Blueswirls ,  Creepy ,  Gauguin ,  Redblush ,  Crayon ,  Escher ,  Fantasy ,  Reptile ,  Pen ,  Homer ,  Tiedye ,  Monster ,  Starry2 ,  Paper Folding ,  Scribble ,  Wallpaper ,  sketch4 ,  Tuscany ,  Barcelona ,  Beauty ,  Rembrandt ,  Delaunay ,  Geometric ,  Metallic ,  Garden ,  Connections ,  Edtaonisl ,  Vangogh ,  Picasso ,  Swirls ,  Shattered ,  Candy ,  Futuristic ,  Yarn ,  Coffee ,  Rave ,  Lily ,  Devilish ,  Smoke ,  Composition ,  Dark ,  Fairy ,  Watercolor ,  Mosaic2 ,  Abstract ,  Blood ,  Brave ,  Jungle ,  Matrix ,  Dreaming ,  Mosaic ,  Flow ,  Reds ,  Flowers ,  Oldrug ,  Chalkboard ,  Storytime ,  Watercolor2 ,  Kandinsky ,  Adventure ,  Pasley ,  Sketch2 ,  Sketch3 ]
	aa = random.choice(ran)
	return aa
	
headers = {
     Accept :  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ,
     Accept-Language :  ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7 ,
     Cache-Control :  max-age=0 ,
     Connection :  keep-alive ,
     Content-Type :  application/x-www-form-urlencoded ,
     Cookie :  srv=www8.lunapic.com; acolor=%23f44336; winw=393; fname=IMG_20230829_142539_492; hide_backups=1; ucount=2; icon_id=169338393193867692; backupid=5; FCNEC=%5B%5B%22AKsRol9HAbM7oSFDoMJ3aaes1nfu3M3fOYX5AdRE8nMVTB5PzkraYbDqm5iRsIPnd3bzjnBxhUxQ_lMLdve1VmST_1YBKpucSF8hSVxNkLrD6YH-cG04ogQXPdnCRyasYHSqwakL6-UQYijzInIchpuLbeWIqQzacA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D ,
     DNT :  1 ,
     Origin :  https://www8.lunapic.com ,
     Referer :  https://www8.lunapic.com/editor/?action=fairy ,
     Sec-Fetch-Dest :  document ,
     Sec-Fetch-Mode :  navigate ,
     Sec-Fetch-Site :  same-origin ,
     Sec-Fetch-User :  ?1 ,
     Upgrade-Insecure-Requests :  1 ,
     User-Agent :  Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 ,
     sec-ch-ua :  "Chromium";v="105", "Not)A;Brand";v="8" ,
     sec-ch-ua-mobile :  ?1 ,
     sec-ch-ua-platform :  "Android" ,
}

params = {
     action : rand(),
}

token = "6677136479:AAHxcr9R0cdL-SRwoXEqKz0k7BTg98o7R2E"
bot = telebot.TeleBot(token)
# @Crrazy_8 & @BRoK8

@bot.message_handler(commands=["start"])
def Welcome(message):
	name = f"[{message.from_user.first_name}](tg://settings)"
	bot.reply_to(message,f   مرحبا بك {name} في
> بوت الفلاتر المجانية
فوق 90 فلتر ارسل فقط صورتك .   ,parse_mode= markdown ,reply_markup=Mak().add(Btn( مبرمجي ,url="tg://user?id=6377763320")))

@bot.message_handler(content_types=[ photo ])
def iimh(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"
    
    start = time.time()
    
    data = {
     action : rand(),
     url : file_url
    }
    # @Crrazy_8 & @BRoK8
    response = requests.post( https://www8.lunapic.com/editor/ , params=params, headers=headers, data=data).text
    img = re.findall( (.*?) rel=nofollow>Get Prints at Zazzle</a> ,response)[0]
    parts = img.split("&t_coverimage_iid=")[1]
    decurl = unquote(parts)
    
    end = time.time()
    tt = end - start
    #print(tt)
    
    bot.send_photo(message.chat.id,decurl,reply_to_message_id=message.message_id,reply_markup=Mak().add(Btn(f ⌛️ {tt} ,url="Crrazy_8.t.me")))
   # @Crrazy_8 & @BRoK8
bot.infinity_polling()