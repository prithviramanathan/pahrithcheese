import json
import random

available = {}
available['stores'] = []

num = 1407

with open('cheese.json') as c:
	cheese = json.load(c)
	cheeses = cheese['cheeses']

	for i in range(1, 500):
		x = random.randint(1, 20)
		cheese_list = []
		for j in range(0, x):
			k = random.randint(1, num)
			cheese_list.append(cheeses[k]['name'])

		available['stores'].append({'store_id': i, 'cheese_name': cheese_list})

with open('available.json', 'w') as outfile:
    json.dump(available, outfile)
