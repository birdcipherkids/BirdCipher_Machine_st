import psycopg2
import string
import random
from hash import *

user_db = ''
user_old = ''
results = []
words_password = []
password_creator = ''
random_separator = ''
login_check = False


def login_user(username, password, role):

	global results
	global user_db
	global login_check
	global user_old

	results = []
	wdatos = bytes(password, 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	miConexion1 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

	miCursor1 = miConexion1.cursor()

	sql1 = 'select * from users where username = (%s)'
	sql1_data = (username, )

	sql2 = 'insert into users(username, password, position, books, keys, swords, caduceus) values(%s,%s,%s,%s,%s,%s,%s)'
	sql2_data = (username, hash2, role, 1, 0, 0, 0)

	sql202 = 'insert into user_words(username, password, words) values(%s,%s,%s)'
	sql202_data = (username, hash2, '')

	miCursor1.execute(sql1, sql1_data)
	dlt1 = miCursor1.fetchall()

	if len(dlt1) == 0 and username != '' and password != '':

		user_old = ''
		login_check = False
		miCursor1.execute(sql2, sql2_data)
		miCursor1.execute(sql202, sql202_data)
		miCursor1.execute(sql1, sql1_data)
		dlt2 = miCursor1.fetchall()
		user_db = dlt2[0][1]
		login_check = True
		user_old = 'New'

	elif len(dlt1) > 0 and hash2 == dlt1[0][2]:

		user_old = ''
		login_check = False
		login_check = True
		user_old = 'Old'
		user_db = dlt1[0][1]
		print(dlt1[0][2])
		print(dlt1[0][4])
		print(user_old)

	elif len(dlt1) > 0 and hash2 != dlt1[0][2]:

		user_old = ''
		login_check = False
		user_old = 'Incorrect'
		print(user_old)

	elif username == '' or password == '':

		user_old = ''
		login_check = False
		user_old = 'blank'

	if login_check and user_old == 'New':

		results.append(dlt2[0][2])
		results.append(user_old)

	elif login_check and user_old == 'Old':

		results.append(dlt1[0][2])
		results.append(user_old)

	elif login_check == False:

		print(user_old)
		results.append(hash2)
		results.append(user_old)


	miConexion1.commit()
	miConexion1.close()

	return results


def words_inclusion(word, user):

	global words_password
	global user_db
	global login_check

	if login_check:

		user = user_db
		miConexion22 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
			user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

		miCursor22 = miConexion22.cursor()
		sql3 = 'update user_words set words = concat(words, word) where username = (%s)'
		sql3_data = (user, )
		miCursor22.execute(sql3, sql3_data)
		#dlt3 = miCursor22.fetchall()
		miConexion22.commit()
		miConexion22.close()

		words_password.append(word)
		print(words_password)

	



	return words_password


def query_rockyou(word):

	hacked_word = False

	with open('C:/rockyou.txt', 'r', encoding = 'utf-8', errors='replace') as file:

		while True:

			line = file.readline()

			if line.strip() == word:

				hacked_word = True
				break

			elif not line:

				break

		
	return hacked_word

def password_generator(length, upper, lower, num, special):

	global words_password
	global password_creator
	global random_separator

	length_pass = length
	characters = ''
	
	if upper:

		characters = characters + string.ascii_uppercase

	if lower:

		characters = characters + string.ascii_lowercase

	if num:

		characters = characters + string.digits

	if special:

		characters = characters + string.punctuation

	password_creator = ''
	password_creator = ''.join(random.choice(characters) for i in range(length_pass))

	
	# if not words:

	#  	password_creator = ''
	#  	password_creator = ''.join(random.choice(characters) for i in range(length_pass))

	# if words:

	# 	password_creator = ''

	# 	for i in range(3):

	# 		random_separator = random_separator + random.choice(characters)

	# 	random_words = random.sample(words_password, length)
	# 	print(random_words)
	# 	password_creator = random_separator.join(random_words)
		
	#except IndexError:

		#print('You must choose at least one character category')

	wdatos = bytes(password_creator, 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	results_passcreator = [password_creator, hash2]

	return results_passcreator


#def send_passphrase():





