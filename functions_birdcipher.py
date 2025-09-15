import psycopg2
import string
import random
import os
import base64
import time
import pyhibp
from pyhibp import pwnedpasswords as pw
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from psycopg2 import sql
from hash import *
from Practice_fernet_with_password import *

user_db = ''
user_old = ''
results = []
words_password = []
password_creator = ''
random_separator = ''
login_check = False


def hibp_breach(password_hibp):

	# Required: A descriptive user agent must be set describing the application consuming
	#   the HIBP API

	pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")

	# Check a password to see if it has been disclosed in a public breach corpus
	resp = pw.is_password_breached(password = password_hibp)

	return resp




def check_master_password(password_checking):

	specials = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~¡"
	mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
	minusculas = 'abcdefghijklmnñopqrstuvwxyz'
	numeros = '1234567890'
	password_checking_ok = False


	password_to_evaluate = password_checking
	evaluation = [False, False, False, False, False]
	evaluation_audios_es = ['Audios/caracter_especial.mp3', 'Audios/letra_mayuscula.mp3', 'Audios/letra_minuscula.mp3', 
	'Audios/numero_contrasena.mp3']

	for i in password_to_evaluate:

		if i in specials:

			evaluation[0] = True
		
		if i in mayusculas:

			evaluation[1] = True

		if i in minusculas:

			evaluation[2] = True

		if i in numeros:

			evaluation[3] = True


	if len(password_checking) >= 15:

		evaluation[4] = True


	count_lack = 4
	x = 0

	while x < 4:

		if evaluation[x] == False:

			
			print(evaluation_audios_es[x])

		else:

			count_lack = count_lack - 1

		x = x + 1

	if count_lack == 0 and evaluation[4]:

		password_checking_ok = True
		

	evaluation.append(password_checking_ok)

	return evaluation


def login_user(username, password, role):

	global results
	global user_db
	global login_check
	global user_old
	global salt
	
	results = []
	wdatos = bytes(password, 'utf-8')
	h = hashlib.new(algoritmo, wdatos)
	hash2 = HASH.generaHash(h)

	salt = os.urandom(16)
	salt_dec = base64.b64encode(salt).decode('ascii')

	miConexion1 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

	miCursor1 = miConexion1.cursor()

	sql1 = 'select * from users where username = (%s)'
	sql1_data = (username, )

	sql2 = 'insert into users(username, password, position, salt, books, keys, swords, caduceus) values(%s,%s,%s,%s,%s,%s,%s,%s)'
	sql2_data = (username, hash2, role, salt_dec, 1, 0, 0, 0)

	sql202 = 'insert into user_words(username, password, words) values(%s,%s,%s)'
	sql202_data = (username, hash2, '')

	miCursor1.execute(sql1, sql1_data)
	dlt1 = miCursor1.fetchall()

	if len(dlt1) == 0 and username != '' and password != '':

		user_old = ''
		login_check = False
		pass_check = check_master_password(password)

		if pass_check[5]:

			miCursor1.execute(sql2, sql2_data)
			miCursor1.execute(sql202, sql202_data)
			miCursor1.execute(sql1, sql1_data)
			dlt2 = miCursor1.fetchall()
			user_db = dlt2[0][1]
			login_check = True
			user_old = 'New'

		else:

			user_old = 'Weak'

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
		sql3 = 'update user_words set words = concat(words, %s, %s) where username = (%s)'
		sql3_data = (' ', word, user)
		miCursor22.execute(sql3, sql3_data)
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


# def encrypt_fernet(salt, password, pass_app):

# 	kdf = PBKDF2HMAC(
# 		algorithm = hashes.SHA256(),
# 		length = 32,
# 		salt = salt,
# 		iterations = 1_200_000,
# 		)

# 	password = password.encode()

# 	key = base64.urlsafe_b64encode(kdf.derive(password))
# 	print(key)
# 	f = Fernet(key)

# 	token = f.encrypt(pass_app.encode())
# 	print(token)

# 	return token





def send_random_password(username, password, app, user_app, pass_app):

	qdatos = bytes(password, 'utf-8')
	h = hashlib.new(algoritmo, qdatos)
	hash31 = HASH.generaHash(h)
	print('the password is: ', pass_app)
	send_rand_success = False

	try:

		miConexion31 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
		user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

		miCursor31 = miConexion31.cursor()
		sql31 = 'select * from users where username = (%s)'
		sql31_data = (username, )
		miCursor31.execute(sql31, sql31_data)
		dlt31 = miCursor31.fetchall()
		salt_user = dlt31[0][4]
		salt_user2 = base64.b64decode(salt_user)
		print(salt_user2)
		token_user_final = encrypt_with_fernet(salt_user2, password, pass_app)
		sql311 = 'insert into password_vault(username, password, app, user_app, pass_app) values(%s, %s, %s, %s, %s)'
		sql311_data = (username, hash31, app, user_app, token_user_final.decode())

		#if login_check and username != '' and password == hash31:

		miCursor31.execute(sql311, sql311_data)


		miConexion31.commit()
		miConexion31.close()
		send_rand_success = True

	except IndexError:

		print('Debes iniciar sesion o crear tu usuario')

	return send_rand_success



def bring_password(username, password, app):

	xdatos = bytes(password, 'utf-8')
	h = hashlib.new(algoritmo, xdatos)
	hash41 = HASH.generaHash(h)

	recovery_pass = False

	try:

		miConexion41 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
		user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

		miCursor41 = miConexion41.cursor()
		sql41 = 'select * from users where username = (%s)'
		sql41_data = (username, )
		miCursor41.execute(sql41, sql41_data)
		dlt41 = miCursor41.fetchall()
		salt_user41 = dlt41[0][4]
		print(salt_user41)
		salt_user412 = base64.b64decode(salt_user41)
		print(salt_user412)

		kdf = PBKDF2HMAC(
			algorithm = hashes.SHA256(),
			length = 32,
			salt = salt_user412,
			iterations = 1_200_000,
			)

		key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))
		print(key)
		f = Fernet(key)

		sql444 = 'select * from password_vault where username = (%s) and app = (%s)'
		sql444_data = (username, app)
		miCursor41.execute(sql444, sql444_data)
		dlt444 = miCursor41.fetchall()
		username_app = dlt444[0][4]
		token_user = dlt444[0][5].encode()
		print(token_user)
		password_final = f.decrypt(token_user)
		print(password_final)
		password_final = password_final.decode()
		recovery_pass = True
		result_vault_query = [username_app, password_final, recovery_pass]

		miConexion41.commit()
		miConexion41.close()

	except IndexError:

		result_vault_query = ['', '', False]

	return result_vault_query



def split_secretwords(username, num_words, sep):

	miConexion51 = psycopg2.connect(host = 'bps57o4k0svfjp9fi4vv-postgresql.services.clever-cloud.com', port = 50013, 
	user = 'u8kpoxoaaxlswsvwrn12', dbname = 'bps57o4k0svfjp9fi4vv', password = '5Q00YR5C0e4pnZZEnd5e')

	miCursor51 = miConexion51.cursor()
	sql51 = 'select * from user_words where username = (%s)'
	sql51_data = (username, )
	miCursor51.execute(sql51, sql51_data)
	dlt51 = miCursor51.fetchall()
	sec_words = dlt51[0][3]

	miConexion51.commit()
	miConexion51.close()

	sec_words_list = sec_words.split()
	passphrase = ''

	if num_words <= len(sec_words_list) - 1:

		subset = random.sample(sec_words_list, num_words)

	passphrase = sep.join(subset)
	print(passphrase)

	return passphrase












