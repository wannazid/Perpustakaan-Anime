from . import Read
from . import Database
from . import CheckDB

def update_data(no_edit,db,date_add,judul_anime,genre,adaptasi,tahun_rilis):
	
	data_anime = CheckDB.TEMPLATE.copy()
	data_anime['db'] = db
	data_anime['add_date'] = date_add
	data_anime['judul_anime'] = judul_anime + CheckDB.TEMPLATE['judul_anime'][len(judul_anime):]
	data_anime['genre'] = genre + CheckDB.TEMPLATE['genre'][len(genre):]
	data_anime['adaptasi'] = adaptasi + CheckDB.TEMPLATE['adaptasi'][len(adaptasi):]
	data_anime['tahun_rilis'] = str(tahun_rilis)
	
	semua_data = f"{data_anime['db']},{data_anime['add_date']},{data_anime['judul_anime']},{data_anime['genre']},{data_anime['adaptasi']},{data_anime['tahun_rilis']}\n"
	data_panjang = len(semua_data)
	
	try:
		with(open(CheckDB.DB_NAME,'r+',encoding='utf-8')) as data_file:
			data_file.seek(data_panjang*(no_edit-1))
			data_file.write(semua_data)
	except:
		print('[!] Update database gagal, error')

def edit_data():
	Read.read_data()
	while True:
		no_edit = int(input('> Pilih no yang mau di edit : '))
		edit_anime = Database.data_read_anime(index=no_edit)
		if edit_anime:
			break
		else:
			print('> Tidak ada nomor yang anda pilih! ')
			
	data_anime = edit_anime.split(',')
	db = data_anime[0]
	date_add = data_anime[1]
	jdl_anime = data_anime[2]
	genre = data_anime[3]
	adaptasi = data_anime[4]
	tahun_rilis = data_anime[5][:-1]
	
	while True:
		print('='*60)
		print(' [ Silahkan pilih data mana yang mau di ubah ] \n')
		print(f'             No Anime List : {no_edit}')
		print('='*60)
		print(f'1. Judul Anime: {jdl_anime:.100}')
		print(f'2. Genre Anime: {genre:.60}')
		print(f'3. Adaptasi Anime: {adaptasi:.40}')
		print(f'4. Tahun Rilis: {tahun_rilis:.5}')
		
		print('='*60)
		pilihan_user = input('> Pilih nomor yang mau di edit [1,2,3,4] : ')
		match pilihan_user:
			case "1": jdl_anime = input('#> Judul Anime: ')
			case "2": genre = input('#> Genre Anime: ')
			case "3": adaptasi = input('#> Adaptasi : ')
			case "4":
				while True:
					try:
						tahun_rilis = int(input('> Tahun Rilis : '))
						if len(str(tahun_rilis)) == 4:
							break
						else:
							print('[!] Masukan 4 angka tidak boleh lebih, silahkan ulang lagi')
					except:
						print('[!] Tahun harus angka bukan huruf, silahkan ulang lagi')
			case _:
				print('> Data yang anda pilih tidak valid!')
		print('='*60)		
		print(f'1. Judul Anime: {jdl_anime:.100}')
		print(f'2. Genre Anime: {genre:.60}')
		print(f'3. Adaptasi Anime: {adaptasi:.40}')
		print(f'4. Tahun Rilis: {tahun_rilis:5}')
		print('='*60)
		apakah_selesai = input('> Apakah data sudah sesuai? (y/n) : ')
		print('='*60)
		if apakah_selesai == 'y' or apakah_selesai == 'Y':
			break
			
	update_data(no_edit,db,date_add,jdl_anime,genre,adaptasi,tahun_rilis)
		