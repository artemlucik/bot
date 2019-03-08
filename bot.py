from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
#------------------------GREET_USER------------------------------------#
def greet_user(bot, update):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text)
#----------------------------------------------------------------------#

#------------------------TALK_TO_ME------------------------------------#
def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
#----------------------------------------------------------------------#

#-------------------------DATE-----------------------------------------#
def today_date():
	date = datetime.datetime.now().strftime('%Y/%m/%d')
	#print(date)
	return date
#----------------------------------------------------------------------#

#-------------------------ASTRONOMY------------------------------------#
planets = {'Mercury':ephem.Mercury(today_date()),
		   'Venus':ephem.Venus(today_date()),
		   'Mars':ephem.Mars(today_date()),
		   'Jupiter':ephem.Jupiter(today_date()),
		   'Saturn':ephem.Saturn(today_date()),
		   'Uranus':ephem.Uranus(today_date()),
		   'Neptune':ephem.Neptune(today_date()),
		   'Pluto':ephem.Pluto(today_date()),
		   'Sun':ephem.Sun(today_date()),
		   'Moon':ephem.Moon(today_date())
		  }

def astronomy_help(bot, update):
	#print('astronomy_help')
	planets_list = [key for key in planets]
	update.message.reply_text(f'Planets: {",".join(planets_list)}')

def astronomy(bot, update):
	#print('astronomy')
	user_text = update.message.text.split('/planet')[-1].strip()
	#print(user_text)
	if len(user_text) == 0:
		update.message.reply_text('What is planet name, man?')
	else:
		planet = planets.get(user_text)
		galaxy = ephem.constellation(planet)
		#print(galaxy)
		update.message.reply_text(f'Today {user_text} in {galaxy[1]} galaxy.')

def next_full_moon(bot, update):
	#print('next_full_moon')
	moon = ephem.next_full_moon(today_date())
	update.message.reply_text(f'Next full moon will be {moon}')
#----------------------------------------------------------------------#

#-----------------------WORDS_COUNT------------------------------------#
def words_count(bot, update):
	user_text = update.message.text.split('/wordcount')[-1].strip()
	#print(user_text)
	if len(user_text) == 0:
		update.message.reply_text('Enter something')
	else:
		update.message.reply_text(f'Amount of words: {len(user_text.split())}')
#----------------------------------------------------------------------#

#-------------------CALCULATIION---------------------------------------#
def calculation(bot, update):
	print('calculation')
	user_text = str(update.message.text.split('/calc')[-1].strip())

	if len(user_text) == 0:
		answer = 'Soo...And where is digits?'
		permission = False
	else:
		permission = True

	operation_sign = ['+', '-', '*', '/']
	if permission == True:
		for sign in operation_sign:
			#print(sign)
			if sign in user_text:
				math_sign = sign
				permission = True
				break
			else:
				answer = 'Dude, where is operation_sign such as +,-,* or / ?'
				permission = False

	if permission == True:
		digits = user_text.strip().split(math_sign)
		for digit in digits:
			#print(digit)
			if len(digit) == 0 or not digit.isdigit():
				#print('Enter only 2 digits, please')
				answer = 'Enter only 2 digits, please'
				permission = False
			else:
				permission =True

	if permission == True:
		a = float(digits[0])
		b = float(digits[1])
		if math_sign == '+':
			answer = a + b
		elif math_sign == '-':
			answer = a - b
		elif math_sign == '*':
			answer = a * b
		else:
			if b == 0:
				answer = 'Sorry, but it is impossible to divide by 0'
			else:
				answer = a / b

	update.message.reply_text(answer)
#----------------------------------------------------------------------#

#-------------------------CITIES---------------------------------------#
cities_dic = [
	{'а' : ['Амстердам', 'Архангельск', 'Афины', 'Атланта', 'Астрахань']},
	{'б' : ['Берлин', 'Буэнос-Айрес', 'Биробиджан', 'Барселона', 'Базель']},
	{'в' : ['Вена', 'Воронеж', 'Венеция', 'Вашингтон', 'Варшава']},
	{'г' : ['Гамбург', 'Ганновер', 'Гданьск']},
	{'д' : ['Донецк', 'Детройт', 'Дублин', 'Дрезден', 'Дорчестер']},
	{'е' : ['Екатеринбург', 'Елабуга', 'Евпатория']},
	{'ж' : ['Женева', 'Житомир']},
	{'з' : ['Загреб', 'Зеленоград']},
	{'и' : ['Иваново', 'Иерусалим', 'Иркутск', 'Ингельхайм-ам-Райн']},
	{'к' : ['Калгари','Кале','Калининград', 'Кёльн', 'Копенгаген']},
	{'л' : ['Лондон', 'Луганск', 'Лос-Анджелес', 'Лион', 'Лозанна']},
	{'м' : ['Мадрид', 'Мурманск', 'Монреаль', 'Мюнхен', 'Марсель']},
	{'н' : ['Нью-Йорк', 'Неаполь', 'Ницца', 'Нижний Новгород', 'Новый Орлеан']},
	{'о' : ['Омск','Оренбург','Оттава']},
	{'п' : ['Париж', 'Пермь', 'Прага', 'Псков', 'Пиза']},
	{'р' : ['Рим', 'Рио-де-Жанейро', 'Рязань', 'Ростов-на-Дону' 'Рига']},
	{'с' : ['Сан-Франциско', 'Сочи', 'Стамбул', 'Страсбург', 'Сиэтл']},
	{'т' : ['Торонто', 'Тель-Авив', 'Таганрог', 'Тверь', 'Тобольск']},
	{'у' : ['Уссурийск']},
	{'ф' : ['Фонтенбло']},
	{'х' : ['Хельсинки', 'Хьюстон', 'Химки', 'Ханты-Мансийск', 'Хабаровск']},
	{'ц' : ['Цюрих']},
	{'ч' : ['Чикаго']},
	{'ш' : ['Шаффхаузен']},
	{'э' : ['Эрфурт']},
	{'ю' : ['Южно-Курильск']},
	{'я' : ['Ялуторовск', 'Ялта']}
	]
unused_letters = ['ь', 'ъ', 'ы', 'щ']
unused_cities = []
last_answer_letter = 'temp'#<----------------------------------PROBLEM-

def cities(bot, update):
	print('Cities')
	user_text = update.message.text.split('/city')[-1].strip()
	print(user_text)
	last_letter = user_text[-1]
	firs_letter = user_text[0]
	
	print('\nStage_1\n')
	print(last_answer_letter)
	if len(unused_cities) == 0:
		print('first_time')
		permission = True
		pass
	else:
		print(f'firs_letter - {firs_letter}')
		print(f'last_letter - {last_answer_letter}')
		if firs_letter == last_answer_letter:
			print('all_checked_letters_OK')
			permission = True
		else:
			print('check_letters')
			answer  = f'Dude, the first letter of your city isn\'t {last_answer_letter}!'
			permission = False
	
	print('\nStage_2\n')
	if permission == True:
		if user_text in unused_cities:
			answer = 'Come on...This city was used. Enter another one'
			permission = False
		else:
			permission = True
		unused_cities.append(user_text)
	
	print('\nStage_3\n')
	if last_letter in unused_letters:
		last_letter = user_text[-2]
	print(last_letter)
	
	print('\nStage_4\n')
	if permission == True:
		for city in cities_dic:
			if city.get(last_letter) == None:
				pass
			else:
				cities_list = city.get(last_letter)
				if len(cities_list) == 0:
					answer = 'Emm... I don\'t know any city on this latter'
				else:
					answer_accept = False
					while answer_accept == False:
						answer = cities_list[0]
						last_answer_letter = answer[-1]
						print(answer)
						if answer in unused_cities:
							cities_list.pop(0)
							city[last_letter] = cities_list
							answer_accept = False
						else:
							cities_list.pop(0)
							city[last_letter] = cities_list
							unused_cities.append(answer)
							answer_accept = True
	
	print('\nStage_5\n')
	print(f'last_answer_letter: {last_answer_letter}\n\n\n')
	print(f'unused_cities: {unused_cities}')
	print(answer)
	update.message.reply_text(answer)

#----------------------------------------------------------------------#

#-------------------------BOT------------------------------------------#
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
	mybot = Updater('746668598:AAFXlhfmDLzT7oSpV1HDamNj-AXy4db0iIE', request_kwargs = PROXY)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	dp.add_handler(CommandHandler('planet', astronomy))
	dp.add_handler(CommandHandler('planet_help', astronomy_help))
	dp.add_handler(CommandHandler('next_full_moon', next_full_moon))
	dp.add_handler(CommandHandler('wordcount', words_count))
	dp.add_handler(CommandHandler('calc', calculation))
	dp.add_handler(CommandHandler('city', cities))
	mybot.start_polling()
	mybot.idle()

main()