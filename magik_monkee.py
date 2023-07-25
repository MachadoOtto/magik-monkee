#!/usr/bin/env python3

### MAGIK_MONKEE.py				###
### Magic Numbers made easy!!!  ###
### github.com/MachadoOtto 		###

# Imports
import argparse
import json
import os

# Color Constants
BLUE = '\33[34m'
GREEN = '\33[32m'
RED = '\33[31m'
NOCOLOR = '\33[0m'

# Visual Functions
def printScreen():
	t = """┌───────────────────────────────────────────────►
│{1}###{0}   {2}MAGIK_MONKEE.py{0}                       {1}###{0}│
│{1}###{0}        {3}Magic Numbers made easy!!!{0}       {1}###{0}│
│{1}###{0}   github.com/MachadoOtto                {1}###{0}│
◄───────────────────────────────────────────────┘"""
	print(t.format(NOCOLOR, BLUE, GREEN, RED))
	
def printMonkee():
	print('''\t    .-"-.
\t  _/.-.-.\_
\t ( ( o o ) )
\t  |/  "  \|\tspeak no evil...
\t   \\'/^\\'/
\t   /`\ /`\\
\t  /  /|\  \\
\t ( (/ T \) )
\t  \__/^\__/''')
	input()
	print('''\t     .-"-.
\t   _/_-.-_\_
\t  / __> <__ \\
\t / //  "  \\ \\\tsee no evil...
\t/ / \\'---'/ \ \\
\t\ \_/`"""`\_/ /
\t \           /''')
	input()
	print('''\t     .-"-.
\t   _/_-.-_\_
\t  /|( o o )|\\
\t | //  "  \\ |\thear no evil...
\t/ / \\'---'/ \ \\
\t\ \_/`"""`\_/ /
\t \           /''')
	input()
	print('''\t   .-"-.
\t  /.-.-.\_
\t( ( o o ) )
\t |/  "  \|\thave no fun...
\t  \ .-. /
\t  /`"""`\\
\t /       \ ''')

### Main Functions

# Function to charge the data from the JSON extension database file
def chargeData(db_path, arr_ext):
	f = open(db_path)
	data = json.load(f)
	f.close()
	if (arr_ext):
		valid = {}
		for e in arr_ext:
			for d in data['docs']:
				if d['ext'] == e:
					valid[e] = d
					break
		data = valid
	return data

# Function to list all extensions available in the database
def listExtensions(data):
	print('Extension:\tDescription:')
	for d in data['docs']:
		print(d['ext'], '\t\t', d['description'])

# Function to print detailed information about the selected extensions
def printInfo(data):
	for d in data.keys():
		print(d, '=>')
		ext = data[d]
		print('\tDescription:', ext['description'])
		sign = ext['signatures']
		print('\tSignatures (' + str(len(sign)) + '):')
		for s in sign:
			print('\t\t', s['hex'])
			print('\t\t', s['reference'] + '\n')

# Function to apply the magic numbers to the source file
def applyMagik(source, sgn, hex, output, ext):
	basename = os.path.basename(source)
	if (not output):
		output = os.path.splitext(basename)[0]
	ext = (os.path.splitext(basename)[1], '.' + sgn)[ext]
	with open(output + '_' + sgn + ext, 'w+b') as fout:
		fout.write(bytes.fromhex(hex))
		with open(source, 'rb') as fin:
			for line in fin:	
				fout.write(line)
		fout.seek(6,0)
	return output + '_' + sgn + '.' + ext

# Main function
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--database', help = 'path to database to be used', default = 'mgk_num_db.json')
	parser.add_argument('-e', '--ext', help = 'list of extensions to use', type = str)
	parser.add_argument('-i', '--info', action = 'store_true', help = 'get detailed information on the selected extensions')
	parser.add_argument('-l', '--list', action = 'store_true', help = 'list all extensions currently available in the database selected')
	parser.add_argument('-m', '--monkee', action = 'store_true', help = 'print the monkee')
	parser.add_argument('-o', '--output', help = 'name of the file to be generated', default = None)
	parser.add_argument('-x', '--change-extension', action = 'store_true', help = 'change output extension to the new one selected')
	parser.add_argument('file_source', nargs='?', help = 'source file to inject the magic numbers')
	args = parser.parse_args()
	if (args.list):
		printScreen()
		data = chargeData(args.database, None)
		listExtensions(data)
	elif (args.monkee):
		printMonkee()
	elif (args.file_source and args.ext):
		printScreen()
		sel_ext = [e.strip() for e in args.ext.split(',')]
		data = chargeData(args.database, sel_ext)
		if (data):
			if (args.info):
				printInfo(data)
			else:
				for e in data.keys():
					opt = 0
					len_sgn =len(data[e]['signatures'])
					if (len_sgn > 1):
						print('[' + BLUE + 'INFO' + NOCOLOR +']: "' + e + '" extension has more than one Hex signature, select one:')
						i = 1
						for s in data[e]['signatures']:
							print(BLUE + str(i) + ')' + NOCOLOR + '\t', s['reference'])
							i += 1
						while True:
							opt = input('Option [1 - ' + str(len_sgn) + ']: ')
							if int(opt) in range(len_sgn + 1):
								break
							else:
								print('[' + RED + 'ERROR' + NOCOLOR + ']: Option is not valid')
					print('[' + BLUE + 'INFO' + NOCOLOR +']: Generating file with "' + e + '" signature...')
					applyMagik(args.file_source, e, data[e]['signatures'][int(opt)]['hex'], args.output, args.change_extension)
				print('[' + GREEN + 'OK' + NOCOLOR +']: Files successful generated')
		else:
			print('[' + RED + 'ERROR' + NOCOLOR + ']: Signatures selected are not valid')
	else:
		if (not args.file_source):
			print('[' + RED + 'ERROR' + NOCOLOR + ']: Please provide a valid data source')
		elif (not args.ext):
			print('[' + RED + 'ERROR' + NOCOLOR + ']: Please provide a valid extension')
		else:
			print('[' + RED + 'ERROR' + NOCOLOR + ']: Please check the arguments provided')
		parser.print_help()

if __name__ == '__main__':
	main()