from arsein import Messenger
import os,sys
import time as t
import json
import requests as req
import builtwith
import wikipedia
global ip
from ChatbotAPI import ChatBot as bt
import ping3

proxies =  {'https': 'socks5://127.0.0.1:9050','http': 'socks://127.0.0.1:9050'}
#proxies = {'https': 'socks5://127.0.0.1:9050','https': 'http://127.0.0.1:8080'}
print ("getting ip")

ai1 = bt("173702","FDlqnSgrORqzpyQV")

#ip=req.get("https://api.ipify.org", proxies=proxies).text
ip = "unknown"
from translate import Translator
from googletrans import Translator as G

gtranslator = G(service_urls=['translate.googleapis.com'])

en = "en"
fa = "fa"

ins = "29101561"

#guid = 'g0C4lSt05cd6dab038575af643d80fe3' # spi
#guid = "g0CeiuY02a9ca8c79aa26874c150e1f4" # my gap
#guid = "g0B2iYw067a18094b021469d8cae8560" # shift
#guid = 'g0Bs9Qw065532f19817080f0a9de3f22' # virtual

guid = "g0DAhHP02cbb0d71fec5bd6abd754a63" # ai gap mji

#guid ="g0BUv910c971af87c546ea4c649876a5" # ai 2.4 k

#guid = "g0BkJo306fd01b8b5cb8fbec142057d8" # barbi anon

#guid = "g0Cosr8074963d1d96a1eea044e4dd0e"

author2 = ["u0DkUcl0f686228990565c0482b2e46c","u0BM7Ar06b37f6d9d368b01d6800030f", "u0BM7Ar06b37f6d9d368b01d6800030f","u0EosfZ090a77cb67a160c42aa0fb63d","u0FPpTA0b17ec8643111be96cba415f7","u0Dggg60555ffbdfef5d6071041cf17c","u0Dggg60555ffbdfef5d6071041cf17c"]

author = ["u0DkUcl0f686228990565c0482b2e46c","u0BM7Ar06b37f6d9d368b01d6800030f", "u0BM7Ar06b37f6d9d368b01d6800030f","u0EosfZ090a77cb67a160c42aa0fb63d","u0Dggg60555ffbdfef5d6071041cf17c","u0Dggg60555ffbdfef5d6071041cf17c"]


authxakep = "xbbxvtkfsjyfgcilsqqkwqnqhnumwcdb"


bot = Messenger(authxakep)

bots = []

# bot.sendVoice(guid=guid, file='', time=1, caption=None, message_id=mid)
print ('runed\n\n')
#print(len(bots))

AdminGroups = []

try:
    GroupAdmins = bot.getGroupAdmins(guid_gap=guid)
    len_admins = str(len(group_admins['data']['in_chat_members']))
    int_lenadmins = int(len_admins)
    for admins_ in range(int_lenadmins):
        single_admin = group_admins['data']['in_chat_members'][admins_]
        AdminGroups.append(single_admin['member_guid'])
        print(" geted "+len_admins+"admins")
#    for i in

except Exception as eee3:
    print ("cant Get Admin Group err: "+str(eee3))
try:
    run = False
    list_msg = []
    link_id = []
    while True:

        try:

            while True:
                chats = bot.getChatGroup(guid)[-1]
                print("get chats\n")
                print (chats)
#                all_chats = bot.getChatGroup(guid)[:]
                mid = chats['message_id']
                if chats['author_object_guid'] in author:
                     # capture mode on !
                    if mid in list_msg:
                        pass
                    else:
                        pass
#                        list_msg.append(mid)

                        #print (list_msg)
#                if len(mid) == 10:
                #print(mid)
  #                  bot.sendVoice(guid=guid, file='ClearingLogs.ogg', time=1, message_id=mid, caption='AUTOMATICALLY CLEANER !!!!')
   #                 deleter_logs = bot.deleteMessages(guid=guid, message_ids=list_msg)
    #                list_msg.clear()
     #           else:
      #              pass


                if chats["text"] == "/DarlinOn" and chats["author_object_guid"] in author:
                    run = True
                    bot.sendMessage(guid=guid,text="initializing Darlin Ai Bot...", message_id=mid)
                    t.sleep(1.4)
                    bot.sendMessage(guid=guid,text="Completed ✓ \nIp v4 initialized .", message_id=mid)
                    t.sleep(1)
                    bot.sendMessage(guid=guid,text="Reading configuration file...", message_id=mid)
                    t.sleep(4)
                    bot.sendMessage(guid=guid, text="Darlin Bot initializing Completed ✓ ", message_id=mid)
                    t.sleep(1)
                    bot.sendMessage(guid=guid,text=f"New Anonymous ipv4 address: {ip}", message_id=mid)
                    t.sleep(3)
                    bot.sendMessage(guid=guid,text=f"به پنل مدیریت دارل‍ین خوش اومدی مجی حالت چطوره ؟ امروز اینجام فقط کافیه دستورات رو بفرستی تا انجام بدم !", message_id=mid)
                    statusSendMsg = bot.sendVoice(guid=guid, file='DarlinNowOnlined.ogg', time=1, message_id=mid)
                    #print(statusSendMsg)
                else:
                    pass
                if run == True:
                    pass
                else:
                    continue
                if chats["text"] == "/DarlinOff" and chats["author_object_guid"] in author:
                    statusSendMsg = bot.sendVoice(guid=guid, file='ByeDarlin.ogg', time=1, message_id=mid)
                    run = False
                    continue
                if chats["text"] == "/DarlinRestart" and chats["author_object_guid"] in author:
                    statusSendMsg = bot.sendVoice(guid=guid, file='Restart.ogg', time=1, message_id=mid)
                    run = True
                    bot.sendMessage(guid=guid,text="initializing Darlin Ai Bot...", message_id=mid)
                    t.sleep(1)
                    bot.sendMessage(guid=guid,text="Completed ✓ \nIp v4 initialized .", message_id=mid)
                    t.sleep(2)
                    bot.sendMessage(guid=guid,text="Reading configuration file...", message_id=mid)
                    t.sleep(2)
                    bot.sendMessage(guid=guid, text="Darlin Bot initializing Completed ✓ ", message_id=mid)
                    t.sleep(3)
                    bot.sendMessage(guid=guid,text=f"Killing All HUP signals...", message_id=mid)
                    os.system("killall -HUP tor")
                    t.sleep(1)
                    bot.sendMessage(guid=guid,text=f"New Anonymous ipv4 address: {ip}", message_id=mid)
                    t.sleep(3)
                    bot.sendMessage(guid=guid,text="RESTART COMPLETED✓", message_id=mid)
                    continue
                if "دارلین" in chats["text"] and chats["author_object_guid"] in author2:
                    if chats["author_object_guid"] in author:
                        bot.sendMessage(guid=guid, text="جانم مجی!؟ من (دارل‍ین) اینجام دستیار همه کاره شما ! چه کاری از دستم بر میاد؟ فقط کافیه اونو بگی تا برات انجامش بدم!", message_id=mid)

                if chats["text"] == "/DarlinPin" and chats["author_object_guid"] in author2:
                    msg_rply = (chats)['reply_to_message_id']
                    pn = bot.pin(guid=guid, message_id=msg_rply)
                    bot.sendMessage(guid=guid,text=f"Message Pinned Sucessfully",message_id=msg_rply)
                    continue

                if chats["text"] == "/DarlinUnlockGroup" and chats["author_object_guid"] in author2:
                    unlock_group = bot.unlockGroup(guid_gap=guid)
                    st_un = (f"Status Command [/unlockGroup] ->> {unlock_group['status']}")
                    bot.sendVoice(guid=guid, file='UnlockGroup.ogg', time=1, message_id=mid, caption=st_un)
                    continue

                if chats["text"] == "/DarlinLockGroup" and chats["author_object_guid"] in author2:
                    lock_group = bot.lockGroup(guid_gap=guid)
                    lock_gp = (f"Status Command [/DarlinLockGroup] -> {lock_group['status']}")
                    bot.sendVoice(guid=guid, file='LockGroup.ogg', time=1, message_id=mid,caption=lock_gp)
                    continue

                if "/DarlinEditBioGroup" in chats["text"] and chats["author_object_guid"] in author:
                    bio = ['text'][20:]
                    status_edit_bio = bot.EditBioGroup(groupgu=guid, biogp=chats['text'][14:])
                    # chats['text'][14:]
                    bot.sendMessage(guid=guid, text=f"Status Command [!editBioGroup] -> {status_edit_bio['status']}",message_id=mid)
                    continue

                if "/DarlinEditNameGroup" in chats["text"] and chats["author_object_guid"] in author2:
                    status_edit_name = bot.EditNameGroup(groupgu=guid, namegp=chats['text'][21:])
                    ch_name = (f"Status Command [/editNameGroup] -> {chats['status'][14:]} | Name Group Updated Successfully !")
                    bot.sendVoice(guid=guid, file='ChangeNameGroup.ogg', time=1, message_id=mid, caption=ch_name)
                    continue

                if chats["text"] == "/DarlinHideChatGroup" and chats["author_object_guid"] in author2:
                    status_hidegpmsg = bot.VisitChatGroup(guid_gap=guid, visiblemsg=True)
                    bot.sendMessage(guid=guid, text=f"Status Command [!hideChatGroup] -> {status_hidegpmsg['status']}",message_id=mid)
                    continue

                if "/DarlinInfoUser" in chats["text"] and chats["author_object_guid"] in author:
                    username = chats['text'][17:]
                    #print('ok')
                    #if '@' in username:
                        #username = username.replace('@','')
                    userinfo = bot.getInfoByUsername(username=username)
                    ex = (userinfo['data']['exist'])
                    #print(ex)
        #            print (userinfo['data'])
                    if userinfo['data']['exist'] == 'False' or userinfo['data']['exist'] == False:
                        notFound = (f"Status Command [!info[user= @{username}\n Can\'t get info ! user is exist ? check !!! ]]")
                        bot.sendVoice(guid=guid, file='CantRunYourCommand.ogg', time=1, message_id=mid, caption=notFound)

                    if userinfo['data']['exist'] == 'True' or userinfo['data']['exist'] == True:
                        #print ('hale')
                        try:
                            #print('tru')

                            user_lastn = None
                            user_guid = None
                            user_firstn = None
                            user_bi = None

                            user_guid = userinfo['data']['user']['user_guid']

                            user_firstn = userinfo['data']['user']['first_name']

                            user_lastn = userinfo['data']['user']['last_name']

                            usern = userinfo['data']['user']['username']

                            user_bi = userinfo['data']['user']['bio']

                            user_bio = str(user_bi)

                            infobot = (f"""
Status Command [!info[user= @{username} ]]

 user-GUID-> {user_guid}

 First-Name-> {user_firstn}

 Last-Name-> {user_lastn}

 Username-> @{usern}

 Biography->

  {user_bio}""")
                            infobot = str(infobot)

                            re2 = bot.sendVoice(guid=guid, file='InfoUser.ogg', time=1, message_id=mid, caption=infobot)
                            bot.sendMessage(guid=guid, text=infobot, message_id=mid)
                            #print (re2)
                            continue
                            #user_objectguid = userinfo['data']['user']['object_guid']
            #                user_avatar = userinfo['data']['user']['avatar_thumbnail']['file_id']
                        except:
                            continue
#                         try:
#
#                             #print(infobot)
#
#                             continue
#                         except Exception as info_error:
#                             print(info_error)
#                             continue
                    else:

                        bot.sendVoice(guid=guid, file='CantRunYourCommand.ogg', time=1, message_id=mid)
                        continue
            #          pass


                if chats["text"] == "/DarlinAddMemberToGroup" and chats["author_object_guid"] in author2:
                    user_guid_add_group = chats[24:]
                    status_addmm = bot.addMemberGroup(guid_gap=guid, user_ids=user_guid_add_group)
                    add_me = (f"Status Command [/DarlinAddMemberGroup] -> {status_addmm['status']}")
                    bot.sendVoice(guid=guid, file='AddMemberToGroup.ogg', time=1, message_id=mid, caption=add_me)
                    continue

                if "/DarlinSetTarget" in chats["text"] and chats["author_object_guid"] in author:
                    target_guid = chats['text'][17:]
                    settarget = (f"Set Target GUID -> {target_guid}\n")
                    bot.sendVoice(guid=guid, file='TargetSetSucess.ogg', time=1, message_id=mid, caption=settarget)

                if "/DarlinSpamText" in chats["text"] and chats["author_object_guid"] in author:
                    spam_text = chats['text'][16:]
                    spmtxt = (f"Target -> {target_guid}\n\t| Set Spam Text -> {spam_text} ")
                    bot.sendVoice(guid=guid, file='SetSpamTextSuccess.ogg', time=1, message_id=mid, caption=spmtxt)

                if "/DarlinRunSpamAll" in chats["text"] and chats["author_object_guid"] in author:
                    rnspm = (f"Target -> {target_guid}\n\t| Spam Text -> {spam_text}\n\t\t | Action -> SpamAll \n\t\t\t | [Zombies Running . . .]")
                    bot.sendVoice(guid=guid, file='ZombiesRunning.ogg', time=1, message_id=mid, caption=rnspm)
                    zeroZombies = 0
                    for singleBot in bots:
                        lenZombies = len(bots)
                        #zeroZombies = 0
                        try:
                            zombie = Messenger(str(singleBot))
                            #editZombie = zombie.editUser(first_name='0x00 | zombie', last_name="", bio="PWNED BY 0X00")
                            send_txt = zombie.sendMessage(guid=target_guid, text=spam_text)
                            zeroZombies = zeroZombies + 1
        #                   if int(zeroZombies) <= int(lenZombies):
        #                        bot.sendMessage(guid=guid, text=f"Target -> {target_guid}\n\t| Spam Text -> {spam_text}\n\t\t | Action -> SpamAll \n\t\t\t | [SPAM ENDED !]")
        #                   else:
        #                      pass
                        except Exception as spam_all_error:
                            pass
        #                    bot.sendMessage(guid=guid, text=f"Status Command [!runSpamAll] -> {spam_all_error}")

                if "/DarlinRunBlockAll" in chats["text"] and chats["author_object_guid"] in author:
                    blvk = (f"TARGET -> {target_guid} \n\t| ACTION -> BLOCK-ALL-ZOMBIES ! \n\t\t | RUNNING IN BG . . . ")
                    bot.sendVoice(guid=guid, file='BlockingAttackRun.ogg', time=1, message_id=mid, caption=blvk)
                    zeroZombies = 0
                    for singleBot in bots:
                        lenZombies = len(bots)
                        try:
                            zombie = Messenger(str(singleBot))
                            block_status = zombie.block(guid_user=target_guid)
                            #zeroZombies = zeroZombies + 1
                            print ('blocking attack runed...')
                            if int(zeroZombies) == int(lenZombies):
                                pass
                                #bot.sendMessage(guid=guid, text=f"TARGET -> {target_guid} \n\t| ACTION -> BLOCK-ALL-ZOMBIES ! \n\t\t | RUNNING IN BG . . . ",message_id=mid)
                            else:
                                zeroZombies = zeroZombies + 1
                        except Exception as block_error:
        #                    bot.sendMessage(guid=guid, text=f"Status Command [!addMemberGroup] -> {block_error}")
                            pass

                if "/DarlinGetAdminList" in chats["text"] and chats["author_object_guid"] in author:
                    group_admins = bot.getGroupAdmins(guid_gap=guid)
                    stat = group_admins['status']
                    if group_admins['status'] == 'OK':

                        len_admins = str(len(group_admins['data']['in_chat_members']))
                        zero = 1

                        admins = (f"| VERBOSE: |\n\t| Status Command [!DarlinGetAdminList] -> TOTAL ADMINS : {len_admins} \n\t | slepping 10 seconds for send more info af admins to your PV . . .")
                        bot.sendVoice(guid=guid, file='GetAdminList.ogg', time=1, message_id=mid, caption=admins)

                        list_admins = []


                        #single_admin = group_admins['data']['in_chat_members'][admins_]
                        #bot.sendMessage(guid=guid, text=single_admin)
                        int_lenadmins = int(len_admins)
                        for admins_ in range(int_lenadmins):
                            #print(admins_)
                            try:
                                single_admin = group_admins['data']['in_chat_members'][admins_]

                                bot.sendMessage(guid=guid, text=single_admin)
                                user_guid = single_admin['member_guid']
                                type_user = single_admin['member_type']
                                first_name_admin = single_admin['first_name']
                                last_name_admin = single_admin['last_name']
                                join_type_admin = single_admin['join_type']
                                single_admin__ = ('type user -> '+type_user+'\nuser guid ->  '+user_guid+'\nfirst name -> '+first_name_admin+'\nlast name -> '+last_name_admin+'\njoin type admin -> '+join_type_admin)

                                #print(single_admin__)

                                #list_admins.append(single_admin__)
                                #print (list_admins)
                                sss = bot.sendMessage(guid=guid_me, text=single_admin__,message_id=mid)
                                #print (sss)
                                if zero == int_lenadmins:
                                    print (zero)
                                    st = bot.sendMessage(guid=guid_me, text=single_admin__,message_id=mid)
                                    #print (st)
                                    break
                                else:
                                    list_admins.append(single_admin__)
                                    zero = zero + 1
                            except Exception as get_admin_group_error:
                                st = (f"Status Command [!addMemberGroup] -> {get_admin_group_error}")
                                bot.sendVoice(guid=guid, file='CantRunYourCommand.ogg', time=1, message_id=mid, caption=st)
                                break
                    else:
                        pass

                if "/DarlinGetGroupInfo" in chats["text"] and chats["author_object_guid"] in author:

                    link_gp = chats['text'][20:]
                    g_group = bot.seeGroupbyLink(link_gp)
                    final_guid_gap = g_group['group']['group_guid']
                    title_group = g_group['group']['group_title']
                    mem_counts = g_group['group']['count_members']
                    try:
                        description = g_group['group']['description']
                    except:
                        description = None
                    chat_for_new = g_group['group']['chat_history_for_new_members']
                    result_guid = (f"""
    reply Command [!DarlinGetGroupInfo] ->
GUID ->{final_guid_gap}

TitleGroup  -> {title_group}

member counts -> {mem_counts}

Biography ->

  {description}

can See History for new members ? {chat_for_new}""")

                    ts = bot.sendVoice(guid=guid, file='GetGroupInfo.ogg', time=1, message_id=mid, caption=str(result_guid))
                    print(ts)
                    bot.sendMessage(guid=guid, text=str(result_guid), message_id=mid)

                if "/DarlinGetChanelInfo" in chats["text"] and chats["author_object_guid"] in author:
                    link_ch = chats['text'][22:]

                    ch_info = bot.joinChannelByID(link_ch)
                    ch_guid = ch_info['data']['chat_update']['object_guid']
                    ch_title = ch_info['data']['chat_update']['chat']['abs_object']['title']
                    ch_type = ch_info['data']['chat_update']['chat']['abs_object']['type']
                    result_guid = (f"reply Command [!DarlinGetChanelInfo] -> \nGUID ->`{ch_guid}`\nTitleChannel -> `{ch_title}`\nType -> {ch_type}")


                if "/DarlinGetPrivateChanelInfo" in chats["text"] and chats["author_object_guid"] in author:
                    p8link = chats['text'][28:]
                    ch_linkp8 = bot.joinChannelByLink(link=p8link)
                    ch_p8guid = ch_linkp8['data']['channel']['channel_guid']
                    ch_mem = ch_linkp8['data']['channel']['count_members']
                    ch_p8title = ch_linkp8['data']['channel']['channel_title']
                    ch_p8bio = ch_linkp8['data']['channel']['description']

                    result_guidp8  = (f"reply Command [!DarlinGetPrivateChanelInfo] -> \nGUID ->`{ch_p8guid}`\nTitleChannel -> `{ch_p8title}`\nMembers -> {ch_mem}\n Biography -> `{ch_p8bio}`")
                    bot.sendVoice(guid=guid, file='getP8ChInfo.ogg', time=1, message_id=mid)



                if "/DarlinClearLogs" in chats["text"] and chats["author_object_guid"] in author:
                    log_count = len(list_msg)
                    log_count = str(log_count)
                    log_caption = (f'you sended {log_count} messages and etc contents ...!\n going to clearing logs . . .')
                    #t.sleep(1)
                    new_lst = list_msg

                    #for delet in new_lst:
                    deleter_logs = bot.deleteMessages(guid=guid, message_ids=list_msg)
                    bot.sendVoice(guid=guid, file='ClearingLogs.ogg', time=1, message_id=mid, caption=log_caption)
                    list_msg.clear()
                    #print (deleter_logs)
                        #new_lst.remove(delet)

                if "/DarlinFuck" in chats["text"] and chats["author_object_guid"] in author:
                    bot.sendVoice(guid=guid, file='fuckGroup.ogg', time=1, message_id=mid)
                    t.sleep(7)
                    bot.sendVoice(guid=guid, file='Restart.ogg', time=9999999999, message_id=mid)
                    bug_midd = bot.getChatGroup(guid)[-1]
                    bug_mid = bug_midd['message_id']
                    bot.sendMessage(text="Fuck Completed 🚬💀", message_id=mid, guid=guid)

                if "/DarlinClearFuck" in chats["text"] and chats["author_object_guid"] in author:
                    bug_list=[]
                    bug_list.append(bug_mid)
                    bot.deleteMessages(guid=guid, message_ids=bug_list)
                    bug_list.clear()
                    bot.sendMessage(guid=guid, text="Successful 🚬💀 group unFucked ✓",  message_id=mid)

                if "/DarlinNsLookup" in chats["text"] and chats["author_object_guid"] in author:
                    host_dns = chats['text'][16:]
                    url = (f'https://api.dnslab.ir/DNSLookUp/Query?Query={host_dns}&queryType=2')
                    result_dns = req.get(url).text

                    result_dns1 = json.loads(result_dns)
                    f_result = f"result Command [!DarlinNsLookup] \n   ---(dns lookup)--- \n ->   {result_dns1}"
                    bot.sendVoice(guid=guid, file='dnsLookup.ogg', time=1, message_id=mid, caption=f_result)

                if "/DarlinDetectCMS" in chats["text"] and chats["author_object_guid"] in author:
                    url = chats['text'][17:]
                    information_url = builtwith.parse(url)
                    boy = str(information_url)
                    tect = boy.replace(',','\n\n')
                    f_res = (f"""
    --(cms detection)---
      ->   {tect}""")
                    d = bot.sendVoice(guid=guid, file='cmsdetect.ogg', time=1, message_id=mid, caption=f_res)
                    bot.sendMessage(guid=guid, text=f_res, message_id=mid)
                    continue

                if "/DarlinTestWork" in chats["text"] and chats["author_object_guid"] in author:
                    bot.sendVoice(guid=guid, file='DarlinTest.ogg', time=1, message_id=mid, caption='Working => True 🚬💀')

                if "/DarlinCheckHTTP" in chats["text"] and chats["author_object_guid"] in author:
                    hed = {"Accept": "application/json"}
                    url = chats['text'][17:]
                    print (url)
                    data_ = req.get(f'https://check-host.net/check-http?host={url}&max_nodes=30', headers=hed).text
                    data_http = json.loads(data_)
                    nodes = data_http['nodes']
                    # #dataf = json.loads(data_http)
                    link_report = data_http['permanent_link']
                    txt = (f'''RESULT TCP CHECK ->
👾NODES👾 -> {nodes}

🚩REPORT LINK🚩 -> None''')
                    txt1 = txt.replace('[','')
                    txt2 = txt1.replace('],','\n💀〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰💀\n')
                    txt3 = txt2.replace('{','')
                    txt4 = txt3.replace(']}','')
                    txt5 = txt4.replace(':','\n\t')
                    txt6 = txt5.replace('\'','')
                    txtt = (txt6)
                    bot.sendMessage(guid=guid, text=txtt,message_id=mid)
                    continue
                    # n1='ae1.node.check-host.net'
                    # n2='at1.node.check-host.net'
                    # n2='bg1.node.check-host.net'
                    # n3='ch1.node.check-host.net'
                    # n4='cz1.node.check-host.net'
                    # n5='de1.node.check-host.net'
                    # n6'de4.node.check-host.net'
                    # n7='fi1.node.check-host.net' #finland
                    # n8='fr1.node.check-host.net' # france
                    # n9='hk1.node.check-host.net' # hong kong
                    # n10='il1.node.check-host.net' # israel
                    # n11='in1.node.check-host.net' #india
                    # n12='ir1.node.check-host.net' # iran teh
                    # n13='ir3.node.check-host.net' #shiraz
                    # n14='ir4.node.check-host.net' # tabriz
                    # n15='it2.node.check-host
#.net' #italey
                    # n16='nl1.node.check-host.net' # netherlands
                    # n17='ru1.node.check-host.net' # russia
                    # n18='ua2.node.check-host.net' #ukraine
                    # n19 = 'us3.node.check-host.net' # usa

                if "/DarlinAskPersian" in chats["text"]: #and chats["author_object_guid"] in author:
                    wikipedia.set_lang("fa")
                    ask = chats['text'][18:]
                    say = wikipedia.summary(ask, sentences=5)
                    rep = f'''
💀 [ DARLIN ] SEARCH RESULT AI TO YOU\'R ASK-> {ask}

Say:

\t{say}
'''
                    bot.sendMessage(guid=guid, text=rep, message_id=mid)

                if "/DarlinAskEnglish" in chats["text"] and chats["author_object_guid"] in author:
                    wikipedia.set_lang("en")
                    ask = chats['text'][18:]
                    say = wikipedia.summary(ask, sentences=10)
                    rep = f'''
💀 [ DARLIN ] SEARCH RESULT AI TO YOU\'R ASK-> {ask}

Say:

\t{say}
'''
                    bot.sendMessage(guid=guid, text=rep, message_id=mid)
                if chats["text"].startswith("||"):
                    ask=chats['text'][2:]
#                    translator = Translator(to_lang=en)
#                    bot.sendmsg("oh im tired")
                    En = gtranslator.translate(ask,lang_tgt='fa')
                    ok_ = ai1.sendmsg(En.text)
                    print(ok_)
                    translator = Translator(to_lang=fa)
                    Fa = gtranslator.translate(ok_,dest=fa)
                    bot.sendMessage(guid=guid, text=Fa.text, message_id=mid)
                if chats["text"].startswith("|||"):
                    ask=chats['text'][3:]
#                    translator = Translator(to_lang=en)
                    En = gtranslator.translate(ask,lang_tgt='fa')
                    data = {'botkey': 'df10ab2577c975f8fdd89751d99f26b405998bb0798727f3523ea6b60b82ba32',
 'input': En.text,
 'client_name': 'meji'}
                    resp_text = req.post("https://devman.kuki.ai/talk", data=data).text
                    resp_ = json.loads(resp_text)
#                    print (resp_)
                    raw_data = resp_['responses'][0]
#                    translator = gtranslator(dest=fa)
                    Fa = gtranslator.translate(raw_data,dest=fa)
#                    print (Fa)
                    bot.sendMessage(guid=guid, text=Fa.text, message_id=mid)




                if chats["text"].startswith("|"):
                    mjiai = None
                    ask=chats['text'][1:]
                    agent = 'Mozilla/5.0 (Linux; U; Android 11; en; M2010J19CG Build/Android-Q-build-20221116220604) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.0.0 Mobile Safari/537.36'
                    agent = 'Mozilla/5.0 (Linux; Android 9; Primo H8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36'
                    header = {'Cookie': '_ga_0MN0L0RJXZ=GS1.1.1680957567.1.1.1680958736.0.0.0; _ga=GA1.1.689617292.1680957567; __gads=ID=afe1df7ea8872427-22ec281f54dc00b8:T=1680957563:RT=1680957563:S=ALNI_MZL2AC3yHk3yg_Mlo84FOwO0dpzDg; __gpi=UID=00000bfe7c56bdfe:T=1680957563:RT=1680957563:S=ALNI_MYuXr2TTsL58O5r6NbeVmvaEhTlwA; __cf_bm=1aw2Fv9eeYPi.BBQeJX2Sz3cf5Wx10JUm2cRQgSaPH0-1680958725-0-AV6f+jjCRIr0+cN7FKzihfkRtqiVbOJw9DM+Is42XKQgUi45H1aXqeb18I+9/Hq/wfHNu2Dlrk++jcS5XKTqmWY=','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','User-Agent': agent,'Referer': 'https://chatbot.theb.ai/#/chat/1002'}
                    ai_bot = 'https://chatbot.theb.ai/api/chat-process'
                    data = {'prompt': '','options':{}}
# 'options': {}}
                    data['prompt'] = ask
#                    data = ("{'prompt': '%s','options':{}}" % ask)
                    print(data)
#                    data = str(dta)
                    resp = req.post(ai_bot, headers=header, json=data).text
                    # proxies
                    print ('ok 1')
                    do = resp.split("\n")
                    print ('ok 2 split done')
#                    print(do)
                    body = json.loads(do[-1])
                    print ('body done')
                    tex = body["text"]
                    print (tex+"\n\n\n")
                    tex = str(tex)
                    ntex = tex
                    if "OpenAI" in tex:
#                        print ("ai found\n")
                        ntex = ntex.replace("OpenAI","MjiAI")
                        mjiai = False
                    #else:
                      #  ntex = tex
#                        print (ntex+"\n\n\n\n")
#                        print (teex)
                    elif "GPT-3.5" in tex:
                        ntex = ntex.replace("GPT-3.5","DarlinAI")
                        mjiai = False
   #                 else:
  #                      ntex = tex
                    elif "BAI" in tex:
                        ntex = ntex.replace("BAI","DARLIN")
                        mjiai = False
 #                   else:
#                        ntex = tex
                    elif "Little B" in tex:
                        ntex = ntex.replace("Little B","Mji-Zero")
                        mjiai = False
     #               else:
    #                    ntex = tex
                    elif "OpenAI GPT-3.5" in tex:
                        ntex = ntex.replace("OpenAI GPT-3.5","DARLIN AI")
                        mjiai = False
                    else:
                        mjiai = True
                        bot.sendMessage(guid=guid, text=tex, message_id=mid)
                    if mjiai == False:
                        bot.sendMessage(guid=guid, text=ntex, message_id=mid)
                    else:
                        pass




                if "/DarlinAddAdmin" in chats["text"] and chats["author_object_guid"] in author:
                    super_admin = chats['text'][17:]
                    userinfo = bot.getInfoByUsername(username=super_admin)
                    user_guid = userinfo['data']['user']['user_guid']
                    author2.append(user_guid)
                    bot.sendMessage(guid=guid,text=f"User {super_admin} added to authors (level1)", message_id=mid)
                    #bot.sendVoice()


                if "/DarlinSetGapTimer" in chats["text"] and chats["author_object_guid"] in author2:
                    timer = chats['text'][17:]
                    bot.setGroupTimer(guid_gap=guid, time=timer)
                    #voice

                if "/DarlinAddGapAdmin" in chats["text"] and chats["author_object_guid"] in author2:
                    Admin = chats['text'][19:]
                    bot.setGroupAdmin(guid_gap=guid, guid_member=Admin, access_admin=None)

                if "/DarlinStartVoiceChat" in chats["text"] and chats["author_object_guid"] in author2:
                    bot.startVoiceChat(guid=guid)

                # if:
                #     finishVoiceChat(self, guid, voice_chat_id)
#                if "!DarlinBanByGuid" in chats["text"] and chats["author_object_guid"] in author2:
 #                   bot.
                if "/DarlinTestPing" in chats["text"] and chats["author_object_guid"] in author:
                    host = chats["text"][16:]
                    ping_count = 3
                    response_time = ping3.ping(host, unit='ms')
                    bot.sendMessage(guid=guid, text=f"\nResponse Time : {response_time} ms | DNS -> GOOGLE DNS", message_id=mid)
                AntiLink=False
                if "/DarlinAntiLink" in chats["text"] and chats["author_object_guid"] in author:
                    AntiLink = True
                    bot.sendMessage(guid=guid, text="Anti Link -> On ", message_id=mid)
                if AntiLink == True:
                    if "https://" in chats["text"] or "http://" in chats["text"] or "@" in chats["text"]:
                            if chats["author_object_guid"] not in AdminGroups:

                                link_id.append(mid)
                                bot.deleteMessages(guid=guid, message_ids=link_id)
                                link_id.clear()




















                else:
                    pass
        except Exception as global_error:
            print (global_error)
            continue

except Exception as er:
    print(er)
