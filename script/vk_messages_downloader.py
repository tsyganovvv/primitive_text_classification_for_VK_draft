def messages_download(token, chat_id, user_id):
    import vk_api
    from vk_api.longpoll import VkLongPoll, VkEventType


    vk_session = vk_api.VkApi(token=token)
    session_api = vk_session.get_api()


    f = open('data/new_vk_messages.txt', 'x', encoding="utf-8")


    print("\nloading messages in progress...")

    lastMessage = session_api.messages.getHistory(count=1, peer_id=2000000000+chat_id, user_id=user_id)
    pages=int(lastMessage['items'][0]['id']/200+1)


    for i in range(1, pages+1):
        history = session_api.messages.getHistory(count=200, peer_id=2000000000+chat_id, user_id=user_id, start_message_id=200*i)
        history = history['items']
        for j in reversed(history):
            f.write(str(j['text'])+"\n")


    f.close()
    print("messages_download --> success")