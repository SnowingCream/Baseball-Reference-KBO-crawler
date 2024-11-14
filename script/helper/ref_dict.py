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
    
    

    
}

first_name_dict_kor = {
    "u": "woo", # no 어? guess it's fine
    "been": "bin",
    "see": "si",
    "sin": "shin",
    "wahn": "wan",
    "yu": "yoo",
    "young": "yeong",
    "gi": "ki",
    "suh": "seo",
    "seop": "seob",
    "sup": "seob",
    "gyu": "kyu",
    "geun": "keun",
    "ttaum": "tteum",
    # "gap": "gab", # there is 갑 (홍성갑)
    "june": "joon", 
    "pill": "pil",
    "bu": "boo", # no 버, so it's fine
    "sub": "seob", # no 숩, so it's fine
    "guk": "kook", # no 걱, so it's fine
    "hyuk": "hyeok", # no 휵, so it's fine
    "ju": "joo", # no 저, so it's fine
    "hsiang": "sang",
    "oug": "wook",
    "yol": "yeol",
    
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
    "park seunghoon": "seung hoon park", # fillped format, no -
    "pilljoon jang": "pill joon jang", # no -
    "shin  ho lim": "shin ho lim", # extra space
    "dan woo  kim": "dan woo kim", # extra space
    "shin wojae": "woo jae shin", # flipped format, no -
    "chae wonhu": "won hoo chae", # flipped format, no -
    "das sung koo": "dae seong koo", # typo
    "jose para": "jose parra", # typo
    "julio depaula": "julio de paula", # missing space
    "rick vandenhurk": "rick van den hurk", # missing space
    "kevin dattolla": "kevin dattola", # typo
    "ki hyo ahn": "ki hyo nam", # typo
    "kiyoung moon": "ki young moon", # missing space
    "leang keu beul": "matt blank", # ??????? 
    "lang gyun gil": "rang gyun kil", # unique name, manual match
    "r": "reu", # hard to handle
    "michael bowdent": "michael bowden", # typo
    "sangr yul jeon": "sang rul jeon", # space typo
    "scoot baker": "scott baker", # typo
    "satohshi iriki": "satoshi iriki", # unique name, manual match
    "tylor wilson": "tyler wilson", # typo
    "wes obermuller": "wes obermueller", # typo
    "tyrone hornes": "tyrone horne", # typo
    "yu naml": "yool nam", # space typo
    "yeop sagong": "gong yeop sa", # space typo
    "young jae gp": "young jae ko", # typo
    "soo hyung kjim": "soo hyung kim", # typo
    "park sion": "si on park", # flipped format, no -
    "lee ju heon": "joo heon lee", # flipped format
    "lee hyeonmin": "hyeon min lee", # flipped format, no -
    "kim gyudae": "gyoo dae kim", # flipped format, no -
    "kim donghyeok": "dong hyeok kim", # flipped format, no -
    "jun rugun": "roo geon jeon", # flipped format, no -
    "jun pyo jhun": "jun pyo jeon", # typo
    "jo sung hyeon": "seong hyeon jo", # flipped format
    "jo hyo won": "hyo won jo", # flipped format
    "hwang sung woong": "seong woong hwang", # flipped format
    "je hwan yoo": "hwan yoo je", # flipped format
    "hong ji hun": "ji hoon hong", # flipped format
    "hong jae young": "jae young hong", # flipped format
    "han minwoo": "min woo han", # flipped format
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
    "byungho park": "byung ho park", # no -
    "byunggeol woo": "byung geol woo", # no -
    "bubba smith": "charles smith", # unique name, manual match
    "um pyungjae": "pyeong jae eom", # flipped format, no -
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