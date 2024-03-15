from vk_messages_downloader import messages_download
from data_lemmatization import data_lemmatization



#PARAMS
token="vk1.a.uaOZO7kDFVPP0fB18k9RewUhmuyQGuGD3P_MwPFtGTLwkdaMSDGMp1yFycWoceW5xUxni6oo6RLgdhpTb7pM0ew48BvNumMcB9k9BcghSt_VGUzMmS_1CPdnN75mqmSg4ftz88qvPKrSOOtkFZ1MHsoebVKMRSDLdRO9cLeKhhpO7RcFlqeX18mxouC5K7LKuhdVA3F-5J3ELQz7zbGQKw"
chat_id=1
user_id=853922680


def main():

	messages_download(token=token, chat_id=chat_id, user_id=user_id)
	data_lemmatization()








if __name__ == "__main__":
	main()