import os
from . import Database

linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

print('''
   ========================================
   [ Selamat Datang Di Perpustakaan Anime ]
               by : wannazid
       ~ mempermudah kaum wibu elite ~
   ========================================
''')

DB_NAME = 'data-anime.txt'
TEMPLATE = {
'db':'XXXXXX',
'add_date':'yyyy-mm-dd',
'judul_anime':255*' ',
'genre':255*' ',
'adaptasi':255*' ',
'tahun_rilis':'yyyy',
}

def cek_database():
	try:
		with open(DB_NAME,'r') as data:
			print('Database telah ada, lanjut proses')
	except:
		print('\n~#> Database tidak ada, membuat database')
		Database.membuat_database()