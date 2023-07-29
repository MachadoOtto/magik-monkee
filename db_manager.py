#!/usr/bin/env python3

### MAGIK_MONKEE.py				###
### Magic Numbers made easy!!!  ###
### github.com/MachadoOtto 		###

### DB Manager Submodule	    ###

# Imports
import argparse
import json
import json
import sys
import os

# Color Constants
BLUE = '\33[34m'
GREEN = '\33[32m'
RED = '\33[31m'
NOCOLOR = '\33[0m'

### Main Functions

# Add a new signature to a extension in the database
def addSignature(database):
	# Opening JSON file
	f = open(database, "r")
	data = json.load(f)
	f.close()

	ext_i = input('Extension: ')
	ext_f = False
	for d in data['docs']:
		if d['ext'] == ext_i:
			ext_f = d['ext']
			break
	
	if (ext_f):
		print('[' + GREEN + 'OK' + NOCOLOR + ']: Extension found! Adding new signature...')
		hex_i = input('Hex Signature: ')
		ref_i = input('Reference: ')
		ext_f['signatures'].append({ "hex":hex_i, "reference":ref_i })
		print('[' + BLUE + 'INFO' + NOCOLOR + ']: The signature to add is:')
		print('\tHex Signature ->', hex_i)
		print('\tReference ->', ref_i)
		input('Press ENTER to continue... (or CTRL+C to cancel)')
		data_formated = json.dumps(data, indent=4)
		with open("magic_numbers.json", "w") as outfile:
			outfile.write(data_formated)
		print('[' + GREEN + 'OK' + NOCOLOR + ']: Signature added!')
	else:
		print('[' + RED + 'ERROR' + NOCOLOR + ']: Extension NOT found.')
		create = input('Do you want to create a new extension? (y/n): ')
		if ((create == 'y') or (create == 'Y')):
			print('[' + BLUE + 'INFO' + NOCOLOR + ']: Creating new extension...')
			desc_i = input('Description: ')
			hex_i = input('Hex Signature: ')
			ref_i = input('Reference: ')
			new_doc = {
				"ext": ext_i,
				"description": desc_i,
				"signatures": [
					{
						"hex": hex_i,
						"reference": ref_i
					}
				]
			}
			print('[' + BLUE + 'INFO' + NOCOLOR + ']: The extension/signature to add is:')
			print('\tExtension ->', ext_i)
			print('\tDescription ->', desc_i)
			print('\tHex Signature ->', hex_i)
			print('\tReference ->', ref_i)
			input('Press ENTER to continue... (or CTRL+C to cancel)')
			data['docs'].append(new_doc)
			data_formated = json.dumps(data, indent=4)
			with open(database, "w") as outfile:
				outfile.write(data_formated)
			print('[' + GREEN + 'OK' + NOCOLOR + ']: Extension created!')
		else:
			print('[' + BLUE + 'INFO' + NOCOLOR + ']: Operation canceled!')
			
# Generate a new empty database file
def newDatabase(database):
	# Opening JSON file
	f = open(database, "w")
	data = {
		"docs": []
	}
	data_formated = json.dumps(data, indent=4)
	f.write(data_formated)
	f.close()
	print('[' + GREEN + 'OK' + NOCOLOR + ']: New database file created!')

# Update the database file from the magik_monkee repository
def updateDatabase(database):
	print('[' + BLUE + 'INFO' + NOCOLOR + ']: Updating database file...')
	os.system('wget https://raw.githubusercontent.com/MachadoOtto/magik-monkee/main/mgk_num_db.json -O ' + database)
	print('[' + GREEN + 'OK' + NOCOLOR + ']: Database file updated!')

# List all extensions currently available in the database selected
def listExtensions(database):
	# Opening JSON file
	f = open(database, "r")
	data = json.load(f)
	f.close()
	print('[' + BLUE + 'INFO' + NOCOLOR + ']: The extensions currently available are:')
	for d in data['docs']:
		print('\t' + d['ext'])

# Get detailed information on the selected extensions
def printInfo(database, ext):
	# Opening JSON file
	f = open(database, "r")
	data = json.load(f)
	f.close()
	ext_f = False
	for d in data['docs']:
		if d['ext'] == ext:
			ext_f = d
			break
	if (ext_f):
		print('[' + BLUE + 'INFO' + NOCOLOR + ']: The extension selected is:')
		print('\tExtension ->', ext_f['ext'])
		print('\tDescription ->', ext_f['description'])
		print('\tSignatures:')
		for s in ext_f['signatures']:
			print('\t\tHex Signature ->', s['hex'])
			print('\t\tReference ->', s['reference'], '\n')
	else:
		print('[' + RED + 'ERROR' + NOCOLOR + ']: Extension NOT found.')

# Main function
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--add', help = 'add a new signature to a extension in the database', action = 'store_true')
	parser.add_argument('-i', '--info', help = 'get detailed information on the selected extensions', type = str)
	parser.add_argument('-l', '--list', action = 'store_true', help = 'list all extensions currently available in the database selected')
	parser.add_argument('-n', '--new', help = 'generate a new empty database file', action = 'store_true')
	parser.add_argument('-u', '--update', help = 'update the database file', action = 'store_true')
	parser.add_argument('database', nargs='?', help = 'database file path', default = 'mgk_num_db.json')
	args = parser.parse_args()
	if (args.add):
		addSignature(args.database)
	elif (args.new):
		newDatabase(args.database)
	elif (args.update):
		updateDatabase(args.database)
	elif (args.list):
		listExtensions(args.database)
	elif (args.info):
		printInfo(args.database, args.info)
	else:
		print('[' + RED + 'ERROR' + NOCOLOR + ']: No arguments given')
		parser.print_help()

if __name__ == '__main__':
	main()