import json
import sys

# Opening JSON file
f = open('magic_numbers.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# Closing file
f.close()

ext_i = sys.argv[1]
desc_i = sys.argv[2]
hex_i = sys.argv[3]
ref_i = sys.argv[4]

print('Input:')
print('\tExtension ->', ext_i)
print('\tDescription ->', desc_i)
print('\tHex Signature ->', hex_i)
print('\tReference ->', ref_i)

ext = 0

for d in data['docs']:
    if d['ext'] == ext_i:
        ext = d
        break

if ext == 0:
    print('404: Extension NOT found')
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
    data['docs'].append(new_doc)
else:
    print('200: Extension found')
    ext['signatures'].append({ "hex":hex_i, "reference":ref_i })

data_formated = json.dumps(data, indent=4)

with open("magic_numbers.json", "w") as outfile:
    outfile.write(data_formated)
