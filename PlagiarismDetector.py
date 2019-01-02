import re, math
from math import e
from collections import Counter

l_prep = ('above', 'across', 'after', 'at', 'around', 'before', 'behind', 'below', 'beside', 'between', 'by', 'down', 'during', 'for', 'from', 'in', 'inside', 'onto', 'of', 'off', 'on, out', 'through', 'to', 'under', 'up', 'with')
l_art = ('the', 'a', 'an', 'some')
l_num = ('one') #...

def all_textos(w):
	#This function receives all texts.
	x = 1
	while x<=w:
		print()
		h = input("Paste or type down the {} text, without quotation marks: " .format(x))
		x += 1
		li_t.append(h)
	return li_t

def conv_exp(nabsc, fata, expnumerador, expdenominador): 
	#This function converts a numbers to its match in an exponential function | pattern (nabsc, 5, 1, 3)
	if type(nabsc) != str:
		y = fata/(nabsc**(expnumerador/expdenominador))
		return (y)
	pass

def conv_logis_escal(x, valea, cristak, taxadcresb, q, proxmaxgrowv): 
 #This function converts a numbers to its match in a logistical function e establishes a range from 0 to 10.
	if type(x) != str:
		y = (valea + (cristak - valea))/((1 + (q*math.e)**(-taxadcresb*x))**(1/proxmaxgrowv))
		val = 10*(y - valea)/(cristak - valea)
		return val
	pass
def lispala(texto):
	#This function creates a list of words from a given text.
	lista = []
	for i in separa_sentencas(texto):
		for u in separa_frases(i):
			for k in separa_palavras(u):
				lista.append(k)
	return lista
	
def separa_sentencas(texto):
    #This function receives a text and outputs a list of periods inside the text.
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #This function receives a period and outputs a list of subphrases inside the period.
    return re.split(r'[,:;—]+', sentenca)

def separa_palavras(frase):
    #This function receives a subphrase and outputs a list of words inside this subphrase.
    return frase.split()

def adv_repet(listapalavradiferente):
	#This function creates a list of adverbs whose corresponding adjectives are already in the text.
	adv_repet = []
	for i in listapalavradiferente:
		for u in listapalavradiferente:
			if u == i:
				break
			elif (u[:-1] in i) and ('mente' in i):
				adv_repet.append(i)
	return adv_repet

def n_substv(lispala):
	#This function determines the number of nouns formed from a verb in a list of words.
	n_substv = 0
	for i in lispala:
		if (("ção" in i) or ("ções" in i)) and len(i)>6:
			x = input("Esta palavra '{}' é substantivo formado a partir de verbo (terminação -ção)? Digite S para 'Sim', digite N para 'Não': " .format(i))
			while 'n' and "'Não'" and 's' and "'Sim'" and 'N' and 'S' != x:
				print("Comando inválido")
				x = input("Esta palavra '{}' é substantivo formado a partir de verbo (terminação -ção)? Digite S para 'Sim', digite N para 'Não': " .format(i))
			if 's' and "'Sim'" and 'S' == x:
					n_substv += 1
	return n_substv

def n_adv(lispala):
	#This function determines the number of adverbs formed from an adjective in a list of words.
	n_adv = 0
	for i in lispala:
		if "mente" in i and len(i)>6:
			x = input("Esta palavra '{}' é advérbio? Digite S para 'Sim', digite N para 'Não': " .format(i))
			while 'n' and "'Não'" and 's' and "'Sim'" and 'N' and 'S' != x:
				print("Comando inválido")
				x = input("Esta palavra '{}' é advérbio? Digite S para 'Sim', digite N para 'Não': " .format(i))
			if 's' and "'Sim'" and 'S' == x:
				n_adv += 1
	return n_adv

def l_palavras_unicas(lista_palavras):
	#This function receives a list of words and outputs a list of words whch show up only once.
	palaunic = lista_palavras[:]
	j = 0
	for p in palaunic:
		palaunic[j] = p.lower()
		j += 1
	a = Counter(palaunic)
	palaunic = []
	for i in a:
		if (a[i]) < 2:
			palaunic.append(i)
	return palaunic

def l_palavras_diferentes(lista_palavras):
	#This function defines a list of distinct words used in a text given its list of words.
	paladif = []
	for palavra in lista_palavras:
		p = palavra.lower()
		if p not in paladif:
			paladif.append(p)
	return paladif
	
def ts_palavras_distintas(t_or, tc): #to = original text | tc = text to be compared
	#This function creates a set with words of two texts and determines how many words in the compared text are not in the original text.
	lipa_to = lispala(t_or)
	lipa_tc = lispala(tc)
	conpad_to = set(l_palavras_diferentes(lipa_to))
	conpad_tc = set(l_palavras_diferentes(lipa_tc))
	palaig = conpad_to.intersection(conpad_tc)
	tspd = (len(conpad_tc) - len(palaig))/(len(conpad_tc))	#divided by len(conpad_tc) to keep a reasonable value.
	return tspd
	
def compara_assinaturas(ato, as_c):
	#Compares the texts' signatures.
	somatorio = 0
	for i in (range(0, 7)):
		somatorio += abs(ato[i] - as_c[i])
	return abs(somatorio)

def compara_textos(t_o, tc): #compared signature + functions that compare both texts
	pass
	
def calcula_assinatura(texto):
	#Calculates the linguistical signature of a text.
	if texto[:-1] != ('.', '?', '!'): 
		texto = texto + '.'
	lispala0 = [] #First list of words
	ndc = 0 #Number of characters
	ntp = 0 #Total number of words
	lispala0 = lispala(texto)[:]
	lispaladif = l_palavras_diferentes(lispala0)
	ntp = len(lispala0)
	for i in lispala0:
		ndc += len(i)
	ndc_cp = ndc + (ntp - 1) + len(separa_frases(texto)) + len(separa_sentencas(texto)) #Number of characters, with punctutation (=) Total number of characters in all words (+) Total number of words [- 1] (+) Total number of commas, colons, semicolons, and en dashes (+) Total number of dots.
	
	# [0] - Average word size is the sum of the lenghts of words divided by the number of words.
	tmp = ndc/ntp

	# [1] - Type-Token Ratio (rtt) is the number of distinct words divided by the total number of words.
	rtt = (len(lispaladif))/(len(lispala0))

	# [2] - Hapax Legomana Ratio (rhl) is the number of words that show up only once divided by the total number of words.
	rhl = (len(l_palavras_unicas(lispala0)))/(len(lispala0))

	# [3] - Average period size (tms) is the sum of the number of characters in all periods divided by the number of period (the characters that set apart one period from the other are not be counted as part of the period).
	tms = (ndc + len(separa_frases(texto)) + (ntp - 1) - 1)/(len(separa_sentencas(texto)))

	# [4] - Period complexity (cs) is the total number of subphrases divided by the number of periods.
	nf = 0 #number of subphrases
	for i in separa_sentencas(texto):
		for u in separa_frases(i):
			nf += 1
	cs = nf/(len(separa_sentencas(texto)))
	w1 = math.fsum((len(separa_frases(i)))**2 for i in separa_sentencas(texto))
	
	# [5] - Tamanho médio de frase (tmf) is the sum of the number of characters in each subphrase divided by the number of subphrases in the text (the characters that set apart one subperiod from the other are not be counted as part of the subphrase).
	tmf = (ndc + (ntp - 1))/nf
	
	# [6] - Lexical Variety (vv) is the number of distinct words (except prepositions, articles, and numerals) divided by the number of words.
	vva = set(lispaladif) - set(l_art + l_num + l_prep) - set(adv_repet(lispaladif))
	vv = len(vva)/len(lispala0) #lower weight, a plagiarized text would have similar lexical varieties, albeit different as the concealment between the two texts would produce redudancy or lack thereof.

	return [tmp, rtt, rhl, tms, cs, tmf, vv]

input("Press ENTER to exit the program.")
