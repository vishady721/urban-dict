from lxml import html
import requests

print(' ')
input0 = input("Enter 1 for today's word or 2 for a specific word to be translated: ")
if input0 == "1":
	page0 = requests.get('https://www.urbandictionary.com')
	tree0 = html.fromstring(page0.content)
	Description = tree0.xpath( '//meta[@name = "Description" ]/@content' )
	Word = tree0.xpath( '//meta[@property = "og:title" ]/@content' )
	print(' ')
	print(Word[0])
	print(' ')
	print(Description[0])
	print(' ')

elif input0 =="2":
	print(' ')
	input1 = input("Enter something to be translated on urban dictionary: ")
	L = input1.split()

	if len(L) > 1:
		for i in L[1:]:
			str1 = str('+' + i)
		str2 = str(L[0] + str1)
	else:
		str2 = str(L[0])
	try:
		page = requests.get('https://www.urbandictionary.com/define.php?term={0}'.format(str2))
	except:
		print("this word is not in the urban dictionary")
		exit()
	tree = html.fromstring(page.content)
	Description = tree.xpath( '//meta[@name = "Description" ]/@content' )
	print(' ')
	print(Description[0])
	print(' ')

else:
	print("Follow instructions")
