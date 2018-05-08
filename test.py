# 首先导包
from concurrent.futures import ThreadPoolExecutor
import itchat
from itchat.content import TEXT
import jieba

@itchat.msg_register([TEXT], isGroupChat=True)
def handle_receive_msg(msg):
    groupid = msg['FromUserName']
    chatroom = itchat.search_chatrooms(userName=groupid)
    print(chatroom['NickName'])


if __name__ == '__main__':
    s = '代充游戏币'
    r = jieba.cut(s)
    for ele in r:
        print(ele)

    # itchat.auto_login(hotReload=True)
    # itchat.run()
