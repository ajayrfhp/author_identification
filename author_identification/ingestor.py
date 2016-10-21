

def ingest():
	#LOADS DATA FROM SOURCE FILES INTO MEMORY AND RETURNS A DICT 
	import os
	cwd = os.getcwd()
	print cwd
	data_path = cwd + '/author_identification/data/'
	screen_names = ['henrywinter','SamWallaceTel', 'Marcotti', 'GaryLineker','honigstein']

	data = {}

	for screen_name in screen_names:
		with open(data_path + screen_name + '.txt') as f:
			this_data = f.read().split('\n')
			data[screen_name] = this_data
	return data


