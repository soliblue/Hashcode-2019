def parse(file: str):
	print("Working on {}".format(file))
	with open(file, 'r') as opened_file:
		i = 0
		photos = {}
		tags = set()
		for line in opened_file:
			if i == 0:
				number_of_photos = line.split(" ")[0]
				print(number_of_photos)
			else:
				photo = {}
				vals = line.split(' ')
				photo['orient'] = vals[0]
				photo['tags'] = int(vals[1])
				photo['id'] = i - 1

				if photo['tags'] not in photos:
					photos[photo['tags']] = {'H':[],'V':[]}

				photos[photo['tags']][photo['orient']].append(photo)

				tags.add(photo['tags'])
			i += 1
		tags = sorted(list(tags))
	print("Done reading {} photos from {}".format(i-1,file))
	return photos,tags

def generate_solution(slides,file):
	print(slides)
	with open("solution/" + file,"w+") as sol:
		sol.write("{}\n".format(len(slides)))
		for slide in slides:
			if isinstance(slide['id'],int):
				sol.write("{}\n".format(slide['id']))
