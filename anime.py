import CRUD as CRUD
import os

if __name__ == '__main__':
	
	CRUD.cek_database()
	
	while True:
		linux = 'clear'
		windows = 'cls'
		os.system([linux,windows][os.name == 'nt'])
		
		tampilan_awal = '''
   ========================================
   [ Selamat Datang Di Perpustakaan Anime ]
             github.com/wannazid
       ~ mempermudah kaum wibu elite ~
   ========================================
		'''
		print(tampilan_awal)
		print(f'''
   1. Read Data Anime
   2. Create Data Anime
   3. Update Data Anime
   4. Delete Data Anime
		''')
		
		memilih_no = input('~#> Pilih No (1,2,3,4) : ')
		match memilih_no:
			case '1': CRUD.read_data()
			case '2': CRUD.create_data()
			case '3': CRUD.edit_data()
			case '4': CRUD.delete_data()
		apakah_selesai = input('~#> Apakah sudah selesai menjalankan program nya (y/n) : ')
		if apakah_selesai == 'y' or apakah_selesai == 'Y':
			break
	print('\n~> Program Telah Berhenti, Arigatou >_<')