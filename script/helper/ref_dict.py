'''
Used to merge uncommon notations for a given last name into the most common notation.
criteria for chooing the standard notation:
    1. Avoided 'u' as much as I could because it is one of the main reasons for the naming conflict, which can be pronounced in various ways.
        1.1. if 'u' was used to represent 'ㅜ', replace it to "oo".
        1.2. if 'u' was used to represent 'ㅓ', replace it to 'eo'.
    2. Avoided negative words or common word ex) 'no', 'an', 'go', 'im'.
        2-1. 'park' and 'moon' are exceptions, because they have already been too popular and common.
    3. Avoided 'g', as much as I could because it may confuse english speakers (great and giant sound different).
        3-1. if 'g' was used to represent 'ㄱ' (the case of great), replace it to 'k'.
        3-2. if 'g' was used to represent 'ㅈ' (the case of giant), replace it to 'j'.
'''
last_name_dict_kor = {
    "yun": "yoon", # check 연 -> no conflict (good)
    "chung": "jeong",
    "jung": "jeong", # check 중 -> no such last name (good)
    "jun": "jeon", # check 준 -> no such last name (good)
    "an": "ahn",
    "chang": "jang", #check 창 -> no such last name (good)
    "gwak": "kwak",
    "pae": "bae",
    "paek": "baek",
    "back": "baek",
    "pak": "park", # pak is never 백? not sure -> manually check, no conflict (good)
    "im": "lim",
    "sim": "shim",
    "sin": "shin",
    "gwon": "kwon",
    "jo": "cho",
    "gu": "koo",
    "ku": "koo",
    "chou": "choi",
    "go": "ko",
    "mun": "moon",
    "yu": "yoo",
    "wu": "woo",
    "bang": "pang",
    "no": "noh",
    "roh": "noh",
    "byun": "byeon",
    "gong": "kong",
    "senyu": "seonwoo",
    "seonu": "seonwoo",
    "jeun": "jeon",
    "hur": "heo",
    "her": "heo",
    "hor": "heo",
    "huh": "heo",
    "ho": "heo", # check 호 -> no such last name (good)
    "gi": "ki",
    "tong": "dong",
    "chen": "cheon",
    "chun": "cheon",
    "chi": "ji",
    "wee": "wi",
    "geum": "keum",
    "ju": "joo",
    "youm": "yeom",
    "kum": "keum",
    "son": "sohn",
    "shon": "sohn", # only 1 case
    "kweon": "kwon", # only 1 case
    "mon": "moon", # only 1 case
    "baik": "baek", # only 1 case
    "koh": "ko", # only 1 case
    "dang": "tang", # only 1 case
    "tian": "cheon", # only 1 case
    "ro": "noh", # only 1 case
    "sok": "seok", # only 1 case
    "o": "oh", # only 1 case
    "weon": "won", # only 1 case
    "ga": "ka", # only 1 case
    "uhm": "eom", # only 1 case
    "um": "eom", # only 1 case
    "joung": "jeong", # only 1 case
    "pyon": "byeon", # only 1 case
    "yi": "lee", # only 1 case
    "jong": "jeong", # only 1 case
    "liu": "yoo", # only 1 case
    "kuk": "kook", # only 1 case
    "beak": "baek", # only 1 case
    "yuk": "yook", # only 1 case
    "chei": "chae", # only 1 case
    "gam": "kam", # only 1 case
    "yo": "yeo", # only 2 cases
    "to": "doh", # only 2 cases
    "do": "doh", # only 1 case
    "in": "yin", # only 2 cases
    "ryou": "ryu", # only 2 cases
    "gil": "kil",
    "sun": "seon",
    "you": "yoo",
    "aum": "eom",
    "gye": "kye",
    "chin": "jin",
    "sung": "seong",
    
    

    
}

first_name_dict_kor = {
    "u": "woo", # no 어? guess it's fine
    "i": "yi",
    "o": "oh",
    "been": "bin",
    "see": "si",
    "sin": "shin",
    "wahn": "wan",
    "yu": "yoo",
    "gi": "ki",
    "suh": "seo",
    "seop": "seob",
    "sup": "seob",
    "yeop": "yeob",
    "yup": "yeob",
    "hyeop": "hyeob",
    "hyub": "hyeob",
    # "kun": "koon",
    "ttaum": "tteum",
    # "gap": "gab", # there is 갑 (홍성갑)
    "june": "joon", 
    "pill": "pil",
    "bu": "boo", # no 버, so it's fine
    "sub": "seob", # no 숩, so it's fine
    "guk": "kook", # no 걱, so it's fine
    "hyuk": "hyeok", # no 휵, so it's fine
    "hyun": "hyeon", # no 휸, so it's fine
    "ju": "joo", # no 저, so it's fine
    "ung": "woong", # no 엉, so it's fine
    "hsiang": "sang",
    "oug": "wook",
    "yol": "yeol",
    "uk": "wook", # cases of 억 have been handled (checked both br and st)
    "un": "woon", # cases of 언 have been handled (checked both br and st)
    "chul": "cheol", # no 출, so it's fine
    "gook": "kook",
    "dai": "dae",
    "hai": "hae",
    "ick": "ik",
    "deog": "deok",
    "duck": "deok", # no 둑, so it's fine
    "duk": "deok", 
    "hack": "hak",
    "gu": "goo", # cases of 거 have been handled (checked both br and st)
    "gang": "kang",
    "gil": "kil",
    "go": "ko",
    "gu": "koo",
    "gwan": "kwan", # no 좐, so it's fine
    "geun": "keun", # no 즌, so it's fine
    "geon": "keon", # conventional 
    "gyu": "kyu", # conventional
    "gyeom": "kyeom",
    "gyeong": "kyeong", # conventional
    "gwang": "kwang", # no 좡, so it's fine
    "jip": "jib",
    "ku": "koo",
    "sung": "seong",
    "hyoun": "hyeon",
    "no": "noh",
    "back": "baek",
    "youl": "yeol",
    "jung": "jeong", # handled all 중
    
    
    
    
    
    
    
    
    
    
}

recover_dash_dict = {
    "Um Pyungjae": "Pyeong-Jae Eom", # 엄평재, flipped format, no -
    "Seungchul Yang": "Seung-Cheol Yang", # 양승철, no -
    "Byunggeol Woo": "Byeong-Geol Woo", # 우병걸, no -
    "Park Seunghoon": "Seung-Hoon Park", # 박승훈, fillped format, no -
    "Son Ho Won": "Ho-Won Sohn", # 손호원, flipped format, no -
    "Park Sion": "Si-On Park", # 박시온, flipped format, no -
    "Kiyoung Moon": "Ki-Yeong Moon", # 문기영, no -
    "Chilsung Park": "Chil-Seong Park", # 박칠성, no -
    "Yeop Sagong": "Gong-Yeop Sa", # 사공엽, flipped format, no -
    "Chae Wonhu": "Won-Hoo Chae", # 채원후, flipped format, no -
    "Jun Rugun": "Roo-Geon Jeon", # 전루건, flipped format, no -
    "Giho Park": "Ki-Ho Park", # 박기호, no -
    "Kim Donghyeok": "Dong-Hyeok Kim", # 김동혁, flipped format, no -
    "Hawon Jeon": "Ha-Won Jeon", # 전하원, no -
    "Kim Gyudae": "Gyoo-Dae Kim", # 김규대, flipped format, no -
    "Han Minwoo": "Min-Woo Han", # 한민우, flipped format, no -
    "Lee Hyeonmin": "Hyeon-Min Lee", # 이현민, flipped format, no -
    "Rian Kim": "Ri-An Kim", # 김리안, no -
    "Shin Wojae": "Woo-Jae Shin", # 신우재, flipped format, no -
    "Pilljoon Jang": "Pill-Joon Jang", # 장필준, no - (br)
    "ByungHo Park": "Byeong-Ho Park", # 박병호, no - (br)
    "Hyeseong Kim": "Hye-Seong Kim", # 김혜성, no - (br)
    
}


'''
1-to-1 correction for unique cases that must be manually handled: usually typo, with some rare names
'''
manual_handle_dict = {
    "aarona ltherr": "aaron altherr", # space typo
    "seok sang ho": "sang ho seok", # flipped format
    "seol jae min": "jae min seol", # flipped format
    "no gun woo": "gun woo no", # flipped format
    "noh jae won": "jae won noh", # flipped format
    "nam yun sung": "yun sung nam", # flipped format
    "park tae won": "tae won park", # flipped format
    "das sung koo": "dae seong koo", # typo
    "jose para": "jose parra", # typo
    "julio cesar depaula": "julio de paula", # missing space
    "rick vandenhurk": "rick van den hurk", # missing space
    "kevin dattolla": "kevin dattola", # typo
    "ki hyo ahn": "ki hyo nam", # typo
    "leang keu beul": "matt blank", # ??????? 
    "lang gyun gil": "rang gyun kil", # unique name, manual match
    "r": "reu", # hard to handle
    "michael bowdent": "michael bowden", # typo
    "sangr yul jeon": "sang ryeol jeon", # space typo
    "scoot baker": "scott baker", # typo
    "satohshi iriki": "satoshi iriki", # unique name, manual match
    "tylor wilson": "tyler wilson", # typo
    "wes obermuller": "wes obermueller", # typo
    "tyrone hornes": "tyrone horne", # typo
    "yu naml": "yool nam", # space typo
    "young jae gp": "young jae ko", # typo
    "soo hyung kjim": "soo hyung kim", # typo
    "lee ju heon": "joo heon lee", # flipped format
    "jun pyo jhun": "jun pyo jeon", # typo
    "jo sung hyeon": "seong hyeon jo", # flipped format
    "jo hyo won": "hyo won jo", # flipped format
    "hwang sung woong": "seong woong hwang", # flipped format
    "je hwan yoo": "hwan yoo je", # flipped format
    "hong ji hun": "ji hoon hong", # flipped format
    "hong jae young": "jae young hong", # flipped format
    "eom tae kyoung": "tae kyeong eom", # flipped format
    "eom tae ho": "tae ho eom", # flipped format
    "yeong jin do": "yeong jin doo", # unique name, manual match
    "jung bong": "joong keun bong", # typo
    "jin jong kil": "jong kil jin", # flipped format
    "deuk han yong": "deok han yong", # unique name, manual match
    "yeo seung cheol": "seung cheol yeo", # flipped format
    "choi yun cheol": "yoon cheol choi", # flipped format
    "gil ho song": "gil ho son", # typo
    "jeung woo seok": "jeong woo seok", # unique name, manual match
    "lee jung seok": "joong seok lee", # flipped format
    "sang guk pang": "sang kook park", # typo
    "j.r. philllips": "j.r. phillips", # typo
    "ohkamoto sinya": "okamoto sinya", # typo
    "bubba smith": "charles smith", # unique name, manual match
    "luis manuel de los santos martinez": "luis de los santos", # unique name, manual match
    "michael serveneck": "mike cervenak", # typo
    "gustavo karim garcia aguayo": "karim garcia", # unique name, manual match
    "joshua lee josh bell": "josh bell", # unique name, manual match
    "kevin heon ju lee": "kevin lee", # unique name, manual match
    "eum jang yoon": "jang yoon eom", # flipped format
    "gu sun jung" : "goo seon jung", # double u
    "bum jun park": "beom joon park", # double u
    "byung hwee lee": "yoo chan lee", # changed name
    "chang hun choo": "chang hoon joo", # typo
    "dong sik chu": "dong sik joo", # typo
    "chung yeol chou": "chung yeol cho", # typo
    "sang un park": "sang eon park", # typo (언)
    "un hak ahn": "eon hak ahn", # typo (언)
    "il yung kim": "il yoong kim", # typo (융)
    "don hun kwak": "dong hoon kwak", # typo
    "donk keun lee": "dong keun lee", # typo
    "geong gyu park": "jeong kyoo park", # typo
    "gyeon eon kim": "kyeong eon kim", # typo
    "hei chun lee": "hye cheon lee", # typo
    "heo yong joo": "yong joo heo", # typo
    "myung woom park": "myeong woon park", # typo
    "nak soo song": "nak soo seong", # typo
    "myuong ki lee": "myeong ki lee", # typo
    "sang wahn chu": "sang wan choo", # typo
    "sang ryul chun": "sang ryul jeon", # typo
    "seong bhin park": "seong bin park", # typo
    "sung heon hong": "seong heun hong", # typo
    "seong jae yang": "seong je yang", # typo
    "sung geon chu": "seong geon choo", # typo
    "seong mou ahn": "seong moo ahn", # typo
    "seung rak son": "seung lak sohn", # typo
    "tae lyong kim": "tae ryong kim", # typo
    "seong woo choo": "seung woo choo", # typo
    "tae yean kim": "tae yeon kim", # typo
    "tae youn lee": "tae yeon lee", # typo
    "tong keon yeo": "dong keon yeo", # typo
    "jea jung chang": "jae joong jang", # typo
    "ui ji yang": "eui ji yang", # typo
    "pil jung jin": "pil joong jin", # removing 중 to handle jung (st)
    "jung il ryu": "joong il ryu",  # removing 중 to handle jung (st)
    "jung geun cho": "joong keun cho",  # removing 중 to handle jung (st)
    "jung keun bong": "joong keun bong",  # removing 중 to handle jung (st)
    "wang jung baek": "wang joong baek",  # removing 중 to handle jung (st)
    "jung yeol an": "joong yeol ahn",  # removing 중 to handle jung (st)
    "young jung kim": "yeong joong kim",  # removing 중 to handle jung (st)
    "won jung kim": "won joong kim", # removing 중 to handle jung (br)
    "ho jung lee": "ho joong lee", # removing 중 to handle jung (br)
    "se jung kim": "se joong kim", # removing 중 to handle jung (br)
    "gap jung kim": "gap joong kim", # removing 중 to handle jung (br)
    "jung hwa lee": "joong hwa lee", # removing 중 to handle jung (br)
    "dae jung kim": "dae joong kim", # removing 중 to handle jung (br)
    "jung seok cho": "joong seok cho", # removing 중 to handle jung (br)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # "shin  ho lim": "shin ho lim", # extra space
    # "chang  yang choi": "chang yang choi", # extra space
    # "dan woo  kim": "dan woo kim", # extra space
}

first_name_dict_eng = {
    "albert": "al",
    "alessandro": "alex",
    "andrew": "andy",
    "andrew": "drew",
    "bennett": "ben",
    "benjamin": "ben",
    "bradley": "brad",
    "chadwick": "chad",
    "charles": "chuck",
    "christopher": "chris",
    # "daniel": "dan",
    "roberto": "robert",
    "raymond": "ray",
    # "daniel": "danny",
    "david": "dave",
    "douglas": "doug",
    "eduardo": "eddie",
    "bienvenido": "ben",
    "clifford": "cliff",
    "jacob": "jake",
    "jeffrey": "jeff",
    "james": "jimmy",
    "jonathan": "jon",
    "joshua": "josh",
    # "kenneth": "kenny",
    # "kenneth": "ken",
    "kirkland": "kirk",
    "leslie": "les",
    "lenin": "len",
    "louis": "lou",
    "matthew": "matt",
    "martin": "marty",
    "melquicedec": "melqui",
    "michael": "mike",
    "philip:": "pil",
    "patrick": "pat",
    "richard": "rick",
    "ronald": "ron",
    "samual": "sam",
    "timothy": "tim",
    # "thomas": "tom",
    # "thomas": "tommy",
    "tyrone": "ty",
    "vincent": "vinny",
    "william": "will",
    "zachary": "zach",
}