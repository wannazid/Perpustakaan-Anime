from . import Database

def read_data():
	read_data_anime = Database.data_read_anime()
	
	nomor = 'No'
	judul = 'Judul Anime'
	genre = 'Genre'
	adaptasion = 'Adaptasi'
	thn_rilis = 'Tahun Rilis'
	
	print('\n'+'='*118)
	print(f'{nomor:4} | {judul:45} | {genre:30} | {adaptasion:15} | {thn_rilis:5}')
	print('_'*118)
	
	for nomor,data in enumerate(read_data_anime):
		data_enumerate = data.split(',')
		db = data_enumerate[0]
		add_date = data_enumerate[1]
		judul = data_enumerate[2]
		genre = data_enumerate[3]
		adaptasion = data_enumerate[4]
		thn_rilis = data_enumerate[5]
		print(f'{nomor+1:4} | {judul:.45} | {genre:.30} | {adaptasion:.15} | {thn_rilis:5}',end='')
		
	print('='*118+'\n')
	