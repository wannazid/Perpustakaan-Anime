import random
import string
from datetime import datetime
from . import CheckDB

def membuat_database():
	judul_anime = input('> Judul Anime : ')
	genre = input('> Genre Anime (romance, school) : ')
	adaptasi = input('> Adaptasi (manga/light n/dll) : ')
	while True:
		try:
			tahun_rilis = int(input('> Tahun Rilis : '))
			if len(str(tahun_rilis)) == 4:
				break
			else:
				print('[!] Masukan 4 angka tidak boleh lebih, silahkan ulang lagi')
		except:
			print('[!] Tahun harus angka bukan huruf, silahkan ulang lagi')
	
	dt = datetime.now()
	data_anime = CheckDB.TEMPLATE.copy()
	data_anime['db'] = ''.join(random.choice(string.ascii_letters) for i in range(6))
	data_anime['add_date'] = dt.strftime('%Y-%m-%d/%H:%M:%S')
	data_anime['judul_anime'] = judul_anime + CheckDB.TEMPLATE['judul_anime'][len(judul_anime):]
	data_anime['genre'] = genre + CheckDB.TEMPLATE['genre'][len(genre):]
	data_anime['adaptasi'] = adaptasi + CheckDB.TEMPLATE['adaptasi'][len(adaptasi):]
	data_anime['tahun_rilis'] = str(tahun_rilis)
	
	data_anime_lengkap = f"{data_anime['db']},{data_anime['add_date']},{data_anime['judul_anime']},{data_anime['genre']},{data_anime['adaptasi']},{data_anime['tahun_rilis']}\n"
	
	try:
		with open(CheckDB.DB_NAME,'w',encoding='utf-8') as data:
			data.write(data_anime_lengkap)
	except:
		print('~#> Gagal membuat database, error program')
	
def data_read_anime(**kwargs):
	try:
		with open(CheckDB.DB_NAME,'r') as files:
			view_content = files.readlines()
			jumlah_anime = len(view_content)
			if 'index' in kwargs:
				hal_anime = kwargs['index']-1
				if hal_anime < 0 or hal_anime > jumlah_anime:
					return False
				else:
					return view_content[hal_anime]
			else:
				return view_content
	except:
		print('~#> Gagal membaca database, error')
		return False