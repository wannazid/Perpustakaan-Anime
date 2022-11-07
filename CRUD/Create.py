import string, random
from datetime import datetime
from . import CheckDB
from . import Read

def create_data():
	print('='*35)
	print('''
   [ Membuat Data Anime Baru ]
 ~ silahkan isi inputan berikut ~
	''')
	print('='*35)
	jdl_anime = input('\n> Judul Anime : ')
	genre = input('> Genre (romance/school/happy): ')
	adaptasi = input('> Adaptasi (manga/light n) : ')
	while True:
		try:
			thn_rilis = int(input('> Tahun Rilis : '))
			if len(str(thn_rilis)) == 4:
				break
			else:
				print('[!] Masukan 4 angka tidak boleh lebih, silahkan ulang lagi')
		except:
			print('[!] Tahun harus angka bukan huruf, silahkan ulang lagi')
	
	dt = datetime.now()
	data_anime = CheckDB.TEMPLATE.copy()
	data_anime['db'] = ''.join(random.choice(string.ascii_letters) for i in range(6))
	data_anime['add_date'] = dt.strftime('%Y-%m-%d/%H:%M:%S')
	data_anime['judul_anime'] = jdl_anime + CheckDB.TEMPLATE['judul_anime'][len(jdl_anime):]
	data_anime['genre'] = genre + CheckDB.TEMPLATE['genre'][len(genre):]
	data_anime['adaptasi'] = adaptasi + CheckDB.TEMPLATE['adaptasi'][len(adaptasi):]
	data_anime['tahun_rilis'] = str(thn_rilis)
	
	semua_data = f"{data_anime['db']},{data_anime['add_date']},{data_anime['judul_anime']},{data_anime['genre']},{data_anime['adaptasi']},{data_anime['tahun_rilis']}\n"
	
	try:
		with open(CheckDB.DB_NAME,'a',encoding='utf-8') as data_file:
			data_file.write(semua_data)
			print('\n> Data anime berhasil di tambahkan\n')
	except:
		print('\n> Gagal membuat database baru, error')
	
	view_data = Read.read_data()