import re
import math
from math import e
from collections import Counter

l_prep = ('a', 'ante', 'até', 'após', 'de', 'desde', 'em', 'entre', 'com', 'contra', 'para', 'por', 'perante', 'sem', 'sobre', 'sob', 'como', 'no', 'nos', 'na', 'nas', 'num', 'numas', 'nuns', 'numa', 'ao', 'à', 'do', 'da', 'dos', 'das', 'pra', 'pro', 'pelo', 'pelos', 'pela', 'pelas')
l_art = ('a', 'o', 'as', 'os', 'um', 'uma', 'uns', 'umas')
l_num = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa', 'cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos', 'mil', 'milhão', 'bilhão', 'bilião', 'trilhão', 'trilião', 'quadrilhão', 'quatrilhão', 'quintilhão')

def all_textos(w):
	#Esta função recebe todos os textos.
	x = 1
	while x<=w:
		print()
		h = input("Cole ou digite o {}º texto, sem aspas de citação: " .format(x))
		x += 1
		li_t.append(h)
	return li_t

def conv_exp(nabsc, fata, expnumerador, expdenominador): 
	#Esta função converte um número a seu correspondente em uma função exponencial | padrão (nabsc, 5, 1, 3)
	if type(nabsc) != str:
		y = fata/(nabsc**(expnumerador/expdenominador))
		return (y)
	pass

def conv_logis_escal(x, valea, cristak, taxadcresb, q, proxmaxgrowv): #converte para função logística e estabalece a escala de 0 a 10
	if type(x) != str:
		y = (valea + (cristak - valea))/((1 + (q*math.e)**(-taxadcresb*x))**(1/proxmaxgrowv))
		val = 10*(y - valea)/(cristak - valea)
		return val
	pass
def lispala(texto):
	#Esta função cria uma lista de palavras dado o texto.
	lista = []
	for i in separa_sentencas(texto):
		for u in separa_frases(i):
			for k in separa_palavras(u):
				lista.append(k)
	return lista
	
def separa_sentencas(texto):
    #Esta função recebe um texto e devolve uma lista das sentenças dentro do texto.
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    #Esta função recebe uma sentença e devolve uma lista das frases dentro da sentença.
    return re.split(r'[,:;—]+', sentenca)

def separa_palavras(frase):
    #Esta função recebe uma frase e devolve uma lista das palavras dentro da frase.
    return frase.split()

def adv_repet(listapalavradiferente):
	#Esta função cria uma lista dos advérbios cujos adjetivos correspondentes já estão no texto
	adv_repet = []
	for i in listapalavradiferente:
		for u in listapalavradiferente:
			if u == i:
				break
			elif (u[:-1] in i) and ('mente' in i):
				adv_repet.append(i)
	return adv_repet

def n_substv(lispala):
	#Esta função determina o número de substantivos formados a partir de verbo em uma lista de palavras por intermédio do usuário
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
	#Esta função determina o número de substantivos formados a partir de verbo em uma lista de palavras por intermédio da interação do usuário
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
	#Esta função recebe uma lista de palavras e devolve a lista de palavras que aparecem uma única vez.
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
	#Esta função define a lista de palavras usadas em um texto dada uma lista de palavras dele.
	paladif = []
	for palavra in lista_palavras:
		p = palavra.lower()
		if p not in paladif:
			paladif.append(p)
	return paladif
	
def ts_palavras_distintas(t_or, tc): #to = texto original | tc = texto a ser comparado
	#Esta função cria um conjunto com as palavras dos dois textos e determina quantas palavras do texto comparada não estão no texto original.
	lipa_to = lispala(t_or)
	lipa_tc = lispala(tc)
	conpad_to = set(l_palavras_diferentes(lipa_to))
	conpad_tc = set(l_palavras_diferentes(lipa_tc))
	palaig = conpad_to.intersection(conpad_tc)
	tspd = (len(conpad_tc) - len(palaig))/(len(conpad_tc))	#dividido por len(conpad_tc) para manter valor razoável
	return tspd

def conv_r(val, limli, limls): #conversor de valor absoluto para razão utilizando valor absoluto e limites logísticos
	pass
	
def compara_assinaturas(ato, as_c):
	somatorio = 0
	for i in (range(0, 7)):
		somatorio += abs(ato[i] - as_c[i])
	return abs(somatorio)

def compara_textos(t_o, tc): #assinatura comparada + funções que comparam texto
	pass
	
def calcula_assinatura(texto):
	if texto[:-1] != ('.', '?', '!'): 
		texto = texto + '.'
	lispala0 = [] #primeira lista de palavras
	ndc = 0 #número de caracteres
	ntp = 0 #número total de palavras
	lispala0 = lispala(texto)[:]
	lispaladif = l_palavras_diferentes(lispala0)
	ntp = len(lispala0)
	for i in lispala0:
		ndc += len(i)
	ndc_cp = ndc + (ntp - 1) + len(separa_frases(texto)) + len(separa_sentencas(texto)) #número total de caracteres com pontuação | respectivamente numero total de caracteres em palavras, espaços, vírgulas e ponto-e-vírgulas, e pontos
	
	# [0] - Tamanho médio de palavra (tmp) é a soma dos tamanhos das palavras dividida pelo número total de palavras.
	tmp = ndc/ntp

	# [1] - Relação Type-Token (rtt) é o número de palavras diferentes dividido pelo número total de palavras.
	rtt = (len(lispaladif))/(len(lispala0))

	# [2] - Razão Hapax Legomana (rhl) é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
	rhl = (len(l_palavras_unicas(lispala0)))/(len(lispala0))

	# [3] - Tamanho médio de sentença (tms) é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).
	tms = (ndc + len(separa_frases(texto)) + (ntp - 1) - 1)/(len(separa_sentencas(texto)))

	# [4] - Complexidade de sentença (cs) é o número total de frases divido pelo número de sentenças.
	nf = 0 #número de frases
	for i in separa_sentencas(texto):
		for u in separa_frases(i):
			nf += 1
	cs = nf/(len(separa_sentencas(texto)))
	w1 = math.fsum((len(separa_frases(i)))**2 for i in separa_sentencas(texto))
	
	# [5] - Tamanho médio de frase (tmf) é a soma do número de caracteres em cada frase dividida pelo número de frases no texto (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
	tmf = (ndc + (ntp - 1))/nf
	
	# [6] - Variedade Vocabular (vv) é o número de palavras diferentes utilizadas exclusive preposições, artigos, e numerais dividido pelo número de palavras.
	vva = set(lispaladif) - set(l_art + l_num + l_prep) - set(adv_repet(lispaladif))
	vv = len(vva)/len(lispala0) #peso menor, um texto plagiado teria variedades lexicais similares, embora diferentes pois o disfarce entre os dois textos produziria redudância ou eliminação dela

	return [tmp, rtt, rhl, tms, cs, tmf, vv]

#NÃO MEXER APÓS AQUI, TERMINAR TODAS AS FUNÇÕES, INTERPRETAR O QUE ESCREVI E FAZER AS ALTERAÇÕES ADEQUADAS
##NÃO CRIAR NENHUMA VARIÁVEL DENOMINADA 'e'.

print("Bem-vindo ao detector automático de COH-PIAH.")
print()
print("Este programa recebe um texto original e o compara com outros para identificar qual destes é mais provável de ser produto de cópia daquele.")
print()
t_or = input("Insira o texto original sem aspas de citação: ")
print()
q = int(input("Quantos textos com suspeita de cópia deseja analisar? "))
li_t = [] #lista de textos
l_asst = [] #lista de assinaturas dos textos | lista de listas
l_assc = [] #lista de assinaturas comparadas

all_textos(q)

t_or2as = calcula_assinatura(t_or) #assinatura do texto original

for i in li_t:
	x = calcula_assinatura(i)
	l_asst.append(x)
	
for i in l_asst:
	j = compara_assinaturas(t_or2as, i)
	l_assc.append(j)	#[0] comparação do texto 1, [1] do texto 2 e assim sucessivamente

print()	
a = 1
	
for i in l_assc:
	if i>0.1:	
		print("O {}º texto tem diferença de: {}" .format(a, i))
		a += 1
	else:
		print("O {}º texto tem diferença de: 0" .format(a, i))
		a += 1
	
print()

input("Pressione a tecla ENTER para sair do programa.")