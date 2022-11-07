from . import Read
from . import CheckDB
from . import Database
import os

def hapus_data(no_anime):
	try:
		with(open(CheckDB.DB_NAME,'r')) as file:
			count = 0
			while True:
				content = file.readline()
				if (len(content)) == 0:
					break
				elif count == no_anime - 1:
					pass
				else:
					with open('temp_anime.txt','a',encoding='utf-8') as temp_anime:
						temp_anime.write(content)
				count += 1
	except:
		print('[!] Menghapus gagal, database error')
	os.rename('temp_anime.txt',CheckDB.DB_NAME)
		

def delete_data():
	Read.read_data()
	while True:
		no_anime = int(input('> Pilih no yang mau di hapus : '))
		database_anime = Database.data_read_anime(index=no_anime)
		
		if database_anime:
			data_anime = database_anime.split(',')
			db = data_anime[0]
			date_add = data_anime[1]
			jdl_anime = data_anime[2]
			genre = data_anime[3]
			adaptasi = data_anime[4]
			tahun_rilis = data_anime[5][:-1]
			
			print('='*60)
			print('Data yang ingin anda hapus\n')		
			print(f'1. Judul Anime: {jdl_anime:.100}')
			print(f'2. Genre Anime: {genre:.60}')
			print(f'3. Adaptasi Anime: {adaptasi:.40}')
			print(f'4. Tahun Rilis: {tahun_rilis:5}')
			print('='*60)
			apakah_selesai = input('> Apa anda yakin mau hapus data ini (y/n) : ')
			print('='*60)
			if apakah_selesai == 'y' or apakah_selesai == 'Y':
				hapus_data(no_anime)
				break
		else:
			print('[!] Nomor tidak ada, silahkan masukan lagi')
	print('[!] Delete data anime berhasil')