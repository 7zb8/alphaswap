input("The Tool Has Been Stop For a While For The New Update 
exit(00)
c1 = ''
c2 = ''
ee = Tk()
nosp = 0
ee.withdraw()
emaa = []
Si = []
f = []
os.system('mode con: cols=83 lines=20')
SettingsO = []
os.system(f"title #ALPHA SWAP")
os.system('cls' if os.name == 'nt' else 'clear')
Token = string.ascii_lowercase + string.ascii_uppercase + string.digits
TOKEN = (''.join(random.choice(Token) for i in range(30)))
try:
    TEXT = requests.get('https://pastebin.com/raw/1QUpyQNZ').text
    GetIP = requests.get('https://api.ipify.org?format=json').text
    GETIP = re.findall('{"ip":"(.*?)"}', GetIP)
    IP = " ".join(GETIP)
    if IP in TEXT:
        pass
    else:
        input(f'{c2}{c1}  x{c2} , Sorry You Can Not Access To This Tool [{IP}]')
        exit(1)
except:
    exit(1)

def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))


def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))


def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result


###########################################################login#######################################################
def generateUSER_AGENT():
    Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
    DPIs = [
        '480', '320', '640', '515', '120', '160', '240', '800'
    ]
    randResolution = random.randrange(2, 9) * 180
    lowerResolution = randResolution - 180
    DEVICE_SETTINTS = {
        'system': "Android",
        'Host': "Instagram",
        'manufacturer': f'{random.choice(Devices_menu)}',
        'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
        'android_version': random.randint(18, 25),
        'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
        "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
        'resolution': f'{randResolution}x{lowerResolution}',
        'randomL': f"{RandomString(6)}",
        'dpi': f"{random.choice(DPIs)}"
    }
    return '{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
        **DEVICE_SETTINTS)


d, p, e = 0, 0, 0
os.system('cls' if os.name == 'nt' else 'clear')
print(f"""

       ___    __    ___    __ __   ___         ____  _      __   ___    ___ 
      / _ |  / /   / _ \  / // /  / _ |       / __/ | | /| / /  / _ |  / _ |
     / __ | / /__ / ___/ / _  /  / __ |      _\ \   | |/ |/ /  / __ | / ___/
    /_/ |_|/____//_/    /_//_/  /_/ |_|     /___/   |__/|__/  /_/ |_|/_/ 

{c2}""")
SIS = input(f'{c1}  #{c2} , Enter Sessionid : {c1}')
SES = {'sessionid': SIS}
try:

    headerss = {
        'User-Agent': generateUSER_AGENT(),
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "3brTvw==",
        "X-IG-Connection-Type": "WIFI",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'Host': 'i.instagram.com',
        'Connection': 'keep-alive'}
    GetUrl = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
    gett = requests.get(GetUrl, headers=headerss, cookies=SES).json()
    username = gett['user']['username']
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""

       ___    __    ___    __ __   ___         ____  _      __   ___    ___ 
      / _ |  / /   / _ \  / // /  / _ |       / __/ | | /| / /  / _ |  / _ |
     / __ | / /__ / ___/ / _  /  / __ |      _\ \   | |/ |/ /  / __ | / ___/
    /_/ |_|/____//_/    /_//_/  /_/ |_|     /___/   |__/|__/  /_/ |_|/_/ 

    {c2}""")
    print(f'{c2}{c1}  #{c2} , Login Successfully @{c2}{username}')
    time.sleep(0.2)
    try:
        email = gett['user']['email']
        print(f'{c2}{c1}  #{c2} , Done Grab E-mail')
        time.sleep(0.2)
        see = open('settings.txt', 'r').read().splitlines()
        for i in see:
            SettingsO.append(i)
        bio = SettingsO[0]
        firstname = SettingsO[1]
        webhook = SettingsO[2]
        MMSGP = SettingsO[3]
        MSGB = SettingsO[4]
        FGIF = SettingsO[5]
        B = re.findall('bio : {(.*?)}', bio)
        BIO = " ".join(B)
        ###
        NA = re.findall('firstname : {(.*?)}', firstname)
        NAME = " ".join(NA)
        ###
        ###
        WEB = re.findall('webhook : {(.*?)}', webhook)
        HOOK = " ".join(WEB)
        ###
        MSG = re.findall('msg : {(.*?)}', MMSGP)
        MSGA = " ".join(MSG)
        ##
        MSGBOX = re.findall('msgbox : {(.*?)}', MSGB)
        MSGAX = " ".join(MSGBOX)
        ##
        GIDD = re.findall('gif : {(.*?)}', FGIF)
        GIF = " ".join(GIDD)
        print(f'{c2}{c1}  #{c2} , Done Grab Settings')
        time.sleep(0.2)


        def Check():
            print(f'{c2}{c1}  #{c2} , Checking Block {c1}..{c2}')
            changeUrl = 'https://i.instagram.com/api/v1/accounts/edit_profile/'
            data = {}
            data["_uid"] = f"47641699268"
            data["device_id"] = "android-d595db3f5c276071"
            data["_uuid"] = uuid.uuid4(),
            data["external_url"] = ""
            data['_csrftoken'] = 'massing'
            data["phone_number"] = ""
            data["username"] = username + '.checkblock'
            data["first_name"] = ""
            data["biograph"] = ""
            data["email"] = email
            Swap = requests.post(changeUrl, headers=headerss, data=data, cookies=SES).text
            if ('"status":"ok"') in Swap:
                print(f'{c2}{c1}  #{c2} , Account Is Work')
            elif ('"login_required"') in Swap:
                print(f'{c2}{c1}  x{c2} , Please Use A Api Session Not Web !')
                input(f'{c2}{c1}  x{c2} , Account Is Not Working !')
            else:
                input(f'{c2}{c1}  x{c2} , Account Is Not Working !')
        def conferm():
            print(f'{c2}{c1}  #{c2} , Sending Confirm  {c1}..{c2}')
            urlconf = 'https://www.instagram.com/accounts/send_confirm_email/'
            headersww = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                'x-csrftoken': 'Kel09zcVhier8jdZqQe9MUu35FsP9b5Y'}
            red = requests.post(urlconf, headers=headersww, cookies={'sessionid': SES})
            if ('"Check Your Email"') in red.text:
                print(f'{c2}{c1}  #{c2} , Done Sent Confirm')
            else:
                print(f'{c2}{c1}  x{c2} , Can Not Sent Confirm')
                ss = input(f'{c2}{c1}  x{c2} , Do You Want Continue ? [y/n] :')
                if ss == 'y':
                    pass
                else:
                    exit(0)

        Check()
        conferm()
        Target = input(f'{c2}{c1}  #{c2} , Enter Target : {c1}')
        THE = int(input(f'{c1}  #{c2} , Enter Thread : {c1}'))
    except:
        input(f'{c2}{c1}  x{c2} , Sessionid Is Not Working or Insert E-mail In Ur Acc!')

except:
    input(f'{c2}{c1}  x{c2} , Sessionid Is Not Working !')


def swapped():
    global nosp
    if nosp == 0:
        nosp = 1
        print(f'{c2}{c1}  #{c2} , {MSGA} @{Target}')
        mUrl = HOOK
        murl2 = 'https://discord.com/api/webhooks/922443688175628400/rNsWgomzdduBZmFcm_lPwjeIc3_a8Nl3Cl2RMsqTp7J4Nj90HrLfTvdxQxyCAwxe_yWt'
        data = {}
        data["embeds"] = [
            {"description": f"\nSwapped Successfully => [@{Target}](https://instagram.com/{Target})\nBy #Alpha Swap",
             "color": random.choice([0x3498db]), "thumbnail": {"url": GIF}, "author": {"name": "#New Notification"}}]
        try:
            response = requests.post(murl2, json=data)
            response2 = requests.post(mUrl, json=data)
        except:
            pass
        try:
            requests.post('https://i.instagram.com/api/v1/accounts/set_biography/', data={"raw_text": BIO},
                          headers=headerss, cookies=SES)
            requests.post('https://i.instagram.com/api/v1/accounts/set_phone_and_name/', data={"first_name": NAME},
                          headers=headerss, cookies=SES)
        except:
            pass
        ctypes.windll.user32.MessageBoxW(0, f'{MSGAX} @{Target}', '#ALPHA SWAP')
        exit()


def editprofile():
    global d, e
    url1 = 'https://i.instagram.com/api/v1/accounts/edit_profile/'
    data = {}
    data["_uid"] = f"47641699268"
    data["device_id"] = "android-d595db3f5c276071"
    data["_uuid"] = uuid.uuid4(),
    data["external_url"] = ""
    data['_csrftoken'] = 'massing'
    data["phone_number"] = ""
    data["username"] = Target
    data["first_name"] = ""
    data["biograph"] = ""
    data["email"] = email
    SwapA = requests.post(url1, headers=headerss, data=data, cookies=SES)
    if ('"status":"ok"') in SwapA.text:
        swapped()
    elif SwapA.status_code == 400:
        d += 1
        os.system(f"title ATM : {d} / ERROR : {e}")
    else:
        e += 1
        os.system(f"title ATM : {d} / ERROR : {e}")


def set_user():
    global d, e
    url2 = 'https://i.instagram.com/api/v1/accounts/set_username/'
    data2 = {'username': Target}
    SwapS = requests.post(url2, headers=headerss, data=data2, cookies=SES)
    if ('"status":"ok"') in SwapS.text:
        swapped()
    elif SwapS.status_code == 400:
        d += 1
        os.system(f"title ATM : {d} / ERROR : {e}")
    else:
        e += 1
        os.system(f"title ATM : {d} / ERROR : {e}")


tkinter.messagebox.showwarning('#ALPHA SWAP', f'Ready ?\nTarget : {Target}\nThread : {THE}')


def chose():
    modes = [editprofile(), set_user()]
    return random.choice(modes)


threads1 = []
TR = int(THE)
for i in range(TR):
    thread1 = threading.Thread(target=chose)
    thread1.start()
    threads1.append(thread1)
for thread in threads1:
    thread.join()
