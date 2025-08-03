import psycopg2
from hash import *

results = []


def login_user(username, password, role):

	global results

	results = []
	login_check = False
	user_old = ''
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

	miCursor1.execute(sql1, sql1_data)
	dlt1 = miCursor1.fetchall()

	if len(dlt1) == 0 and username != '' and password != '':

		miCursor1.execute(sql2, sql2_data)
		miCursor1.execute(sql1, sql1_data)
		dlt2 = miCursor1.fetchall()
		login_check = True
		user_old = 'New'

	elif len(dlt1) > 0 and hash2 == dlt1[0][2]:

		login_check = True
		user_old = 'Old'
		print(dlt1[0][2])
		print(dlt1[0][4])
		print(user_old)

	elif len(dlt1) > 0 and hash2 != dlt1[0][2]:

		user_old = 'Incorrect'
		print(user_old)

	elif username == '' or password == '':

		user_old = 'blank'

	if login_check and user_old == 'New':

		results.append(dlt2[0][2])
		results.append(user_old)

	elif login_check and user_old == 'Old':

		results.append(dlt1[0][2])
		results.append(user_old)

	elif login_check == False:

		results.append(hash2)
		results.append(user_old)


	miConexion1.commit()
	miConexion1.close()

	return results

