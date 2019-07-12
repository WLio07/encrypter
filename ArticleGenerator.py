import random, re, requests, sys
from bs4 import BeautifulSoup

print("Insert the informations asked below. If they are not pertinent/important/available, enter the text n/a")

moduler = input('''What
was the subject?
1 - New anime announced
2 - New LN/manga announced
3 - Single title announcement
4 - ?''') # 2-
differentiation between license and new product is made in module_2_1



datto = input("What day is today (aa-mm-dd)? ")
datan = input("When
was the announcement made (aa-mm-dd)? ")

mult_confirm = input("Are there multiple items? 1 for yes | 2 for no: ")

print("What
is the type of midia the objects pertains to (manga, movie, novel, light novel,
anime)? ")

obj3 =
sys.stdin.readlines() #many in case it's needed

print("Did
anything in context happened before the news (the airing of a final episode
before the announcement of a new season etc)? ")
beforewards1 = sys.stdin.readlines()

print("Did
anything in context happened after the news (the schedulement of an event after
the announcement of a new season etc)? ")
afterwards1 = sys.stdin.readlines()



src1 = input("Who
made the announcement? ")



ÃÂ 



adcj_temp = ('Recently','These days', 'Some days ago', 'In ' + months[datan[3:5]] + ' ' + datan[6:8] + 'st' if int(datan[7:8])==1 else 'nd' if int(datan[7:8])==2 else 'rd' if int(datan[7:8])==3 else 'th', 'Today' if datto=dattan)



months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}



verbs, indicative_of_many, pos_adjec, indicative_of_airing = ('announced', 'revealed', 'put out', 'released', 'reported'), ('a series', 'a barrage', 'a streak', 'a chain', 'a plethora', 'multiple', 'various'), ('exhilarating', 'breathtaking', 'exciting', 'thrilling', 'uplifiting'), ('aired', 'broadcasted', 'went live', 'televised')



ÃÂ 



obj3, beforewards1, afterwards1 = ''.join(str(i.capitalize()) for i in obj3), ''.join(str(i.capitalize()) for i in beforewards1), ''.join(str(i.capitalize()) for i in
afterwards1)



ÃÂ 



obj3, beforewards1, afterwards1 = re.split('\n', obj3), re.split('\n', beforewards1), re.split('\n',
afterwards1)



ÃÂ 



def module_1(a, b):



ÃÂ ÃÂ ÃÂ  name_apre = input("What's the name of the anime? ")



ÃÂ ÃÂ ÃÂ  name_scrap = input("Anime/manga no namae wa? ")



ÃÂ ÃÂ ÃÂ  return [a, ] #a is random of adcj_temp



ÃÂ 



def module_2():



ÃÂ ÃÂ ÃÂ  pass



ÃÂ 



def module_2_1():



ÃÂ ÃÂ ÃÂ  a = int(input('Was it: 1 - a license purchase or 2 - a brand new product?'))



ÃÂ ÃÂ ÃÂ  return a



ÃÂ 



def module_3():



ÃÂ ÃÂ ÃÂ  pass



ÃÂ 



def check_airing(line):



ÃÂ ÃÂ ÃÂ  if 'episode' or ''ÃÂ  in line:



ÃÂ ÃÂ ÃÂ ÃÂ ÃÂ ÃÂ ÃÂ  return True



ÃÂ 



def scraper(ob):



ÃÂ ÃÂ ÃÂ  el = re.split(' ', ob)



ÃÂ ÃÂ ÃÂ  #mangadex
scraper



ÃÂ ÃÂ ÃÂ  manga_dex = 



ÃÂ ÃÂ ÃÂ ÃÂ #mangakakalot
scraper



ÃÂ ÃÂ ÃÂ  manga_kakalot = r'https://mangakakalot.com/manga/' + ('_'.join(i for i in el))



ÃÂ ÃÂ ÃÂ  #wikipedia
scraper



ÃÂ ÃÂ ÃÂ  wiki_pedia = r'https://en.wikipedia.org/wiki/' + ('_'.join(i for i in el))



ÃÂ 



def conditional_clause_builder(ver1, ver2, tocheck): #ver1 is tuple 'verbs' and ver2
'indicative_or_airing' and tocheck is always re.split(' ', ' '.join(i for i in
[*lista de dados em que pode haver indicativo de airing*]))



ÃÂ ÃÂ ÃÂ  conjunctions = ('as ' + ('has ' + (ver1+ver2)[random.randint(0,len(ver1+ven2))] if check_airing(tocheck) elseÃÂ  ver1[random.randint(0,len(ver1))], 'with the ', '')



ÃÂ 



#ideas:


#when doing plot, scrap it from many sources and
combine
