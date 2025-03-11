#62transfac.py by Karen Nguyen

import re
import json
import sys
import gzip

def is_number(string):
	nums = '1234567890'
	if string in nums: return True 
	return False

catalog = []

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp: 
		if not line.startswith('ID') and not is_number(line[0]) and not line.startswith('//'): continue
		if re.search('ID', line): 
			record = {}
			f = line.split()
			record['id'] = f[1]
			record['pwm'] = []
		if re.search('[0123456789].{2}', line): 
			pwm = {}
			nts = line.split()
			pwm['A'] = nts[1]
			pwm['C'] = nts[2]
			pwm['G'] = nts[3]
			pwm['T'] = nts[4]
			record['pwm'].append(pwm)
		if re.search('//', line):
			catalog.append(record)
			
print(json.dumps(catalog, indent=4))