import random, re, getpass, codecs, os
def lisel(texto):
	return re.split(r'(\S+)', texto)
def criptodic():
	global crcod, licod, beta
	crcod, ja = {}, [None]
	for i in beta:
		w = None
		while w in ja: w = random.randrange(0, len(beta))
		crcod[i] = beta[w]
		ja.append(w)
	liscod.append(crcod)
	return crcod
liscod, beta, lispa, listex, texcrip = [], ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'à', 'â', 'ã', 'é', 'ê', 'è', 'î', 'í', 'ì', 'ó', 'ô', 'õ', 'ò', 'ú', 'ù', 'û', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Ç', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Á', 'À', 'Ã', 'Â', 'É', 'È', 'Ê', 'Î', 'Í', 'Ì', 'Ó', 'Ò', 'Ô', 'Õ', 'Ú', 'Ù', 'Û', '!', '?', '-', '_', '<', '>', '£', '¢', '—', '*', '¬', '@', '#', '$', '%', '&', '+', '=', '§', ',', '.', ';', ':', '/', '[', ']', '{', '}', 'ç', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'), lisel(input("Insert the text you want to encrypt: ").strip()), [], ''
for i in lispa:
	listex.append(list(i))
for i in listex:
	criptodic()
	for u in i:
		if u in beta:
			texcrip += crcod[u] 
		else:
			texcrip += u
user = getpass.getuser()
key_file = open(r'C:\Users\\' + user + "\provicrypt100.py", "w") 
key_file.write('# coding=utf8')
key_file = open(r'C:\Users\\' + user + "\provicrypt100.py", "a") 
key_file.write('''
d_liscod =''' + str(liscod))
key_file.write('''
import getpass, re
d_texcrip, d_texdecrip, d_decrip_crcod = input('Insert the encrypted string: ').strip(), '', [{v: k for k, v in i.items()} for i in d_liscod] #d_texdecrip -> texto decriptografado | d_decrip_crcod -> lista de dicionários inversos
print()
d_lisel = re.split(r'(\S+)', d_texcrip)
for i in d_lisel:
	for u in i:
		try:
			if u in d_decrip_crcod[d_lisel.index(i)]:
				d_texdecrip += d_decrip_crcod[d_lisel.index(i)][u] 
		except:
			pass
		try:
			if u not in d_decrip_crcod[d_lisel.index(i)]:
				d_texdecrip += u 
		except:
			pass
print('The decrypted text is:', d_texdecrip)
input()''')
key_file = open(r'C:\Users\\' + user + "\provicrypt100.py", "r")
key_file.read()
with codecs.open(r'C:\Users\\' + user + "\provicrypt100.py", 'r', 'cp1252') as sourcefile:
	with codecs.open(r'C:\Users\\' + user + "\Desktop\keycrypt100.py", 'w', 'utf-8') as targetfile:
		contents = sourcefile.read()
		if not contents:
			pass
		targetfile.write(contents)
key_file.close()
os.remove(r'C:\Users\\' + user + "\provicrypt100.py")
print()
print('The encrypted text is:', texcrip, end='\n\n\n')
print(r'Your key is available on your Desktop C:\Users\\' + user + "\Desktop\keycrypt100.py by the name keycrypt100", end='\n\n')
print('''Attention: next time you run the program and generate another key, if you don't rename the older, it will be deleted.''', end='\n\n')
input('Press ENTER to exit the program.')
