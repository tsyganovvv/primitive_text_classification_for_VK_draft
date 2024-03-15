
def data_lemmatization():
	from string import punctuation
	from pymystem3 import Mystem


	path='data/new_vk_messages.txt'


	with open(path, "r", encoding="utf-8") as df:
		lemmatized_df=str()
		df = list(map(lambda x: x[:-1],df.readlines()))
		print("\nlemmatization of message text in progress...")
		for message in df:
			message=message.lower()
			try:
				message = "".join(Mystem().lemmatize(message)).strip()
			except Exception:
				word=None
				continue
			if message == '':
				continue
			for word in message.split():
				if len(word) < 4:
					word=None
					continue
				if word[-1] in punctuation:	word = word[:-1]
				lemmatized_df+=(" "+word)


		print("lemmatization --> success")
		

		file = open("data/lemmatized_df.txt", "w", encoding="utf-8")
		file.write(lemmatized_df)
		file.close()