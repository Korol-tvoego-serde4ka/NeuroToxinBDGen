import sys

def generate(file, output):
	s = open(file, "rt")
	s = s.read()
	
	for i in range(0,4):
		s = s.replace('\\'+str(i), '|')
	
	s = s.replace('\\', '|')
	
	arr = s.split('\n')
	for k,v in enumerate(arr):
		phase = v.split('|')
		links = []
		phaseOtvet = phase[1].split(' ')
	
		for i, word in enumerate(phaseOtvet):
			if len(word) > 14:
				if word[:14] == "https://vk.com" or word[:14] == "http://vk.com/":
					links.append(word)
					phaseOtvet.pop(i)
		
		phase[1] = ' '.join(phaseOtvet)
		
		for i, link in enumerate(links):
			link = link.replace("https://vk.com/", "")
			link = link.replace("http://vk.com/", "")
			
			links[i] = link
			
		phase[2] = ",".join(links)
		stroka = '|'.join(phase)
		arr[k] = stroka
	
	s = "\n".join(arr)
	
	f = open(output, "w")
	f.write(s)
	print("Готово!")


if len(sys.argv) == 2:
	generate(sys.argv[1], "PhasesDB.txt")
elif len(sys.argv) >= 3:
	generate(sys.argv[1], sys.argv[2])
else:
	print("Ошибка! Вы не указали файл!")
