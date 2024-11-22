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
    "gi": "ki", # might cause problem... hasn't been checked
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
    "yeup": "yeob",
    "yub": "yeob",
    "yuop": "yeob", 
    "hyeop": "hyeob",
    "hyub": "hyeob",
    # "kun": "koon",
    "ttaum": "tteum",
    "gap": "kab", 
    "gab": "kab",
    "kap": "kab",
    "pill": "pil",
    "bu": "boo", # no 버, so it's fine
    "sub": "seob", # no 숩, so it's fine
    "guk": "kook", # no 걱, so it's fine
    "hyuk": "hyeok", # no 휵, so it's fine
    "hyun": "hyeon", # no 휸, so it's fine
    "ju": "joo", # no 저, so it's fine
    "ung": "woong", # no 엉, so it's fine
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
    "duk": "deok", 
    "hack": "hak",
    "gu": "koo", # cases of 거 have been handled (checked both br and st)
    "gang": "kang",
    "gil": "kil",
    "go": "ko",
    "gu": "koo",
    "goo": "koo",
    "gwan": "kwan", # no 좐, so it's fine
    "geun": "keun", # no 즌, so it's fine
    "geon": "keon", # conventional 
    "gwon": "kwon", # no 줜, so it's fine
    "gweon": "kwon", 
    "gyu": "kyu", # conventional
    "gyo": "kyo", # conventional
    "gyeom": "kyeom",
    "gyeong": "kyeong", # conventional
    "gwang": "kwang", # no 좡, so it's fine
    "gyun": "kyun", # no 쥰, so it's fine
    "jip": "jib",
    "ku": "koo",
    "sung": "seong",
    "hyoun": "hyeon",
    "hyok": "hyeok",
    "hyouk": "hyeok",
    "hyuck": "hyeok",
    "no": "noh",
    "back": "baek",
    "youl": "yeol",
    "jung": "jeong", # handled all 중
    "hun": "hoon", # handled all 훈
    "wong": "woong",
    "jee": "ji",
    "tai": "tae",
    "myong": "myeong",
    "kyong": "kyeong",
    "up": "eob",
    "eop": "eob",
    "seog": "seok",
    "du": "doo",
    "pin": "bin",
    "seoung": "seong",
    "suk": "seok",
    "suck": "seok",
    "whoi": "hoi",
    "yil": "il",
    "june": "joon",
    "hee": "hyi", # 희
    "heui": "hyi", # 희
    "hui": "hyi", # 희
    "hei": "hyi", # 희
    "heu": "hyi", # 희
    "whee": "hwi", # 휘
    "hoe": "hoi", # 회
    "ui": "eui", # 의
    "gui": "gwi",
    
    
    
    
    
    
    
    
    
    
    
    
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
    "Jun Rugun": "Chang-Min Jeon", # 전루건 (전창민), flipped format, no -
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
    "Seunghwan Oh": "Seung-Hwan Oh", # 오승환, no - (br)
    
}


'''
1-to-1 correction for unique cases that must be manually handled: usually typo, with some rare names
'''
manual_handle_dict = {
    "aarona ltherr": "aaron altherr", # space typo
    "seok sang ho": "sang ho seok", # flipped format
    "seol jae min": "jae min seol", # flipped format
    "no gun woo": "keon woo noh", # flipped format
    "noh jae won": "jae won noh", # flipped format
    "nam yun sung": "yun sung nam", # flipped format
    "park tae won": "tae won park", # flipped format
    "das sung koo": "dae seong koo", # typo
    "su yeoun kim": "soo yeon kim", # typo
    "jose para": "jose parra", # typo
    "julio cesar depaula": "julio de paula", # missing space
    "rick vandenhurk": "rick van den hurk", # missing space
    "kevin dattolla": "kevin dattola", # typo
    "ki hyo ahn": "ki hyo nam", # typo
    "kwang kuen lee": "kwang keun lee", # typo
    "soo sung kang": "koo seong kang", # typo
    "soung hun kim": "seong hun kim", # typo
    "duck gyoon hwang": "deok kyoon hwang", # unique name, manual match
    "leang keu beul": "matt blank", # ??????? 
    "lang gyun gil": "rang gyun kil", # unique name, manual match
    "hyuk kim": "nyeok kim", # typo
    "mi r jeon": "mi reu jeon", # unique name, manual match
    "michael bowdent": "michael bowden", # typo
    "sangr yul  jeon": "sang ryeol jeon", # space typo WHY NOT WORKING???
    "scoot baker": "scott baker", # typo
    "min guk song": "min kook seong", # typo
    "satohshi iriki": "satoshi iriki", # unique name, manual match
    "tylor wilson": "tyler wilson", # typo
    "wes obermuller": "wes obermueller", # typo
    "tyrone hornes": "tyrone horne", # typo
    "kyung oan park": "kyeong wan park", # typo
    "moung chan kim": "myeong chan kim", # typo
    "seung hye kim": "seung hoi kim",  # typo
    "myeoung jin cha": "myeong jin cha", # typo
    "young hun cho": "yong hoon cho", # typo
    "seong kon kim": "seung kwon kim",  # typo
    "myeong nok oh": "myeong rok oh", # typo
    "myeong jae kim": "myeong je kim",  # typo
    "hwi chan jung": "hoi chan jeong", # typo
    "min je jang": "min jae jang", # typo
    "yu naml": "yool nam", # space typo
    "young jae gp": "young jae ko", # typo
    "soo hyung kjim": "soo hyung kim", # typo
    "lee ju heon": "joo heon lee", # flipped format
    "jun pyo jhun": "jun pyo jeon", # typo
    "kyeong sik chu": "kyeong sik choo", # typo
    "jo sung hyeon": "seong hyeon jo", # flipped format
    "jo hyo won": "hyo won jo", # flipped format
    "hwang sung woong": "seong woong hwang", # flipped format
    "je hwan yu": "hwan yoo je", # flipped format
    "hong ji hun": "ji hoon hong", # flipped format
    "hong jae young": "jae young hong", # flipped format
    "eom tae kyoung": "tae kyeong eom", # flipped format
    "eom tae ho": "tae ho eom", # flipped format
    "kyoung youb youm": "kyeong yeob yeom", # typo
    "kyu jae cho": "kyu je cho", # typo
    "sa min chun": "sa min jeon", # typo
    "yeong jin do": "yeong jin doo", # unique name, manual match
    "il ryung kim": "il yoong kim", # unique name, manual match
    "jung bong": "joong keun bong", # nickname
    "ray choi": "kyeong hwan choi", # nickname
    "jin jong kil": "jong kil jin", # flipped format
    "deuk han yong": "deok han yong", # unique name, manual match
    "yeo seung cheol": "seung cheol yeo", # flipped format
    "choi yun cheol": "yoon cheol choi", # flipped format
    "gil ho song": "gil ho son", # typo
    "kyun eun noh": "kyeong eun noh", # typo
    "sae eop lim": "se eop lim", # typo
    "jeung woo seok": "jeong woo seok", # unique name, manual match
    "lee jung seok": "joong seok lee", # flipped format
    "jo ho pyo": "ho pyo cho", # flipped format
    "sang guk pang": "sang kook park", # typo
    "j.r. philllips": "j.r. phillips", # typo
    "ohkamoto sinya": "okamoto sinya", # typo
    "jae kuk ryu": "je kuk ryu", # typo
    "jae weong seo": "jae eung seo", # typo
    "jae whan bae": "jae hwan bae", # typo
    "wong geun kim": "won keun kim", # typo
    "yoon hee nam": "yoon seong nam", # typo
    "yeun gyu ji": "yeon kyu ji", # typo
    "jo soo kim": "ji soo kim", # typo
    "jong deuk kim": "jong deok kim", # typo
    "wung joung chang": "woong jeong jang", # typo
    "jun kyu ryu": "joon kyu yoo", # typo (류)
    "san gil park": "sang il park", # space typo
    "gang yoo park": "kang woo park", # typo
    "bubba smith": "charles smith", # unique name, manual match
    "luis manuel de los santos martinez": "luis de los santos", # unique name, manual match
    "michael serveneck": "mike cervenak", # typo
    "gustavo karim garcia aguayo": "karim garcia", # unique name, manual match
    "joshua lee josh bell": "josh bell", # unique name, manual match
    "kevin heon ju lee": "kevin lee", # unique name, manual match
    "eum jang yoon": "jang yoon eom", # flipped format
    "gu sun jung" : "goo seon jung", # double u
    "bum jun park": "beom joon park", # double u
    "jun bum koo": "joon beom koo", # double u
    "jun suk choi": "joon seok choi", # double u
    "yun jun song": "yoon joon song", # double u
    "byung hwee lee": "yoo chan lee", # changed name
    "jae hyeon nam": "ha joon nam", # changed name
    "jeong bin kim": "sa yoon kim", # changed name
    "sung ho no": "geon woo noh", # changed name
    "seung hwa lee": "woo min lee", # changed name
    "chang hun choo": "chang hoon joo", # typo
    "dong sik chu": "dong sik joo", # typo
    "jong nam kim": "jeong nam kim", # typo
    "jung heop huh": "jeong hyeop heo", # typo
    "meong man kim": "eok man kim", # typo
    "won jai lee": "won jae lee",  # typo
    "chan seob lee": "chang seob lee", # typo
    "gyeong sik chu": "kyeong sik choo", # typo
    "chung yeol chou": "chung yeol cho", # typo
    "sang un park": "sang eon park", # typo (언)
    "un hak ahn": "eon hak ahn", # typo (언)
    "il yung kim": "il yoong kim", # typo (융)
    "lo han kang": "ro han kang", # typo (로)
    "don hun kwak": "dong hoon kwak", # typo
    "donk keun lee": "dong keun lee", # typo
    "seo owan hong": "se wan hong", # typo
    "geong gyu park": "jeong kyoo park", # typo
    "jun heok huh": "joon hyeok heo", # typo
    "jun hyeung lim": "joon hyeong lim", # typo
    "gyeon eon kim": "kyeong eon kim", # typo
    "kyong hoon lim": "kyeong hoon lim", # typo
    "hei chun lee": "hye cheon lee", # typo
    "heo yong joo": "yong joo heo", # typo
    "hui gon kim": "hwi gon kim", # typo
    "hui gwon kim": "hoi kwon kim", # typo
    "myung woom park": "myeong woon park", # typo
    "nak soo song": "nak soo seong", # typo
    "gyeong eop chu": "kyeong eob joo", # typo
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
    "hsiang pin liu": "sang bin yoo", # typo
    "geun wook lee": "geon wook lee", # typo
    "tae yean kim": "tae yeon kim", # typo
    "tae youn lee": "tae yeon lee", # typo
    "sang gyo chung": "sang kyo jeong", # typo
    "tong keon yeo": "dong keon yeo", # typo
    "jea jung chang": "jae joong jang", # typo
    "ui ji yang": "eui ji yang", # typo
    "beum soo jung":"beom soo jeong", # typo
    "byeong do kim": "byeong doo kim", # typo
    "byeong meong lee":"byeong eok lee", # typo
    "byong yeon choi": "byeong yeon choi", # typo
    "chan sub lee": "chang seob lee", # typo
    "chi ho ha": "ji ho ha", # typo
    "dong weun lee": "dong eun lee", # typo
    "gun cheol song": "koon cheol seong", # typo
    "hae jung yoo": "hye jeong yoo", # typo
    "won jei choi": "won je choi", # typo
    "hyeon doe sin": "hyeon dae shin", # typo
    "hyeong been han": "kyeong bin han", # typo
    "in whan jeon": "in hwan jeon", # typo
    "jae bin kim": "je bin kim", # typo
    "jea gul kim": "jae geol kim", # typo
    "soung hun kim": "seong hoon kim", # typo
    "yeun hun kim": "yeon hoon kim", # typo
    "ji chol park": "ji cheol park", # typo
    "ji guang choi": "ji kwang choi", # typo
    "jin hang choi": "jin haeng choi", # typo
    "ohkamoto sinya": "shinya okamoto", # typo
    "joo on park": "joo eon park", # typo
    "seong hyun son": "seung hyun sohn", # typo
    "joon soon han": "joon soo han", # typo
    "seong min chi": "seung min ji", # typo
    "sung mou an": "seong moo ahn", # typo
    "tae jun shin": "tae joong shin", # typo
    "woo tai hong": "woo tae hong", # typo
    "tae heon kim": "tae hyeon kim",  # typo
    "yeong jae eom": "pyeong jae eom", # typo
    "yeong jae song": "yeong jae seong", # typo
    "young kwon kwon": "yeong koo kwon", # typo
    "hea sung kim": "hoi seong kim", # typo
    "hi sang yoon": "hyi sang yoon", # typo
    "yong sang jeong": "yong saeng jeong", # typo
    "young seok shin": "yong seok shin", # typo
    "yoon sep han": "yoon seob han", # typo
    "yi hyeon hong": "eui hyeon hong", # typo
    "youn suk choi": "yoon seok choi", # typo
    "yeun hun kim": "yeon hoon kim", # typo
    "yeong ll oh": "yeong il oh", # typo
    "young joo seo": "yong joo seo", # typo
    "tae hyon chung": "dae hyeon jeong", # typo
    "yil yeon choi": "il eon choi", # typo
    "jae park song": "jae bak song", # unique name, manual match
    "gap jung kim": "kab joong kim", # unique name, manual match
    "ji hwuon yoo": "ji hwon yoo", # unique name, manual match
    "chan gun lee": "chan geon lee", # mamually resolving u
    "dong kul lee": "dong geol lee", # manually resolving u
    "dong su kim": "dong soo kim", # manually resolving u
    "gun no lee": "koon noh lee", # manually resolving u
    "gun ok lee": "koon ok lee", # manulally resolving u
    "sang yun lee": "sang yoon lee", # manually resolving u
    "seon hun kim": "seon hoon kim", # manually resolving u
    "sun gown cho": "soon kwon cho",  # manually resolving u
    "tae gun kim": "tae koon kim", # manually resolving u
    "young gun cho": "yeong keon cho", # manually resolving u
    "yi sul kim": "yi seul kim", # manually resolving u
    "jun gyu yu": "joon kyu yoo", # manually resolving u
    "kun woo park": "keon woo park", # manually resolving u
    "gun hee kim": "keon hyi kim", # manually resolving u
    "chan moon": "chan jong moon", # nickname
    "chang choi": "chang yang choi", # nickname
    "chang moon": "chang hwan moon", # nickname
    "heishu ohara": "byeong soo kang", # nickname
    "minoru tanaka": "sil kim", # nickname
    "mototomi yoshimura": "won boo ko", # nickname
    "seung song": "seung joon song", # nickname
    "ui jeon": "ui san jeon", # nickname
    "jon mae": "brian mazone", # nickname
    "dae won moon": "won moon", # changed name
    "dong won lee": "tae oh lee", # changed name
    "dong wook park": "keon woo park", # changed name
    "jang hyeok yoo": "ro kyeol yoo", # changed name
    "jong ki park": "so joon park", # changed name
    "ji seon chae": "won hoo chae", # changed name
    "yi hwan kim": "do hyeon kim", # changed name
    "keon choi": "yi joon choi", # changed name
    "sei hyok park": "se hyeok park", # changed name
    "sung ki jung": "jin jeong", # changed name
    "wang gi lee": "jae yool lee", # changed name
    "yong su shin": "yoon hoo shin", # changed name
    "gi hyun yang": "ji yool yang", # changed name
    "pil jung jin": "pil joong jin", # removing 중 to handle jung (st)
    "jung il ryu": "joong il ryu",  # removing 중 to handle jung (st)
    "jung geun cho": "joong keun cho",  # removing 중 to handle jung (st)
    "jung keun bong": "joong keun bong",  # removing 중 to handle jung (st)
    "wang jung baek": "wang joong baek",  # removing 중 to handle jung (st)
    "jung yeol an": "joong yeol ahn",  # removing 중 to handle jung (st)
    "young jung kim": "yeong joong kim",  # removing 중 to handle jung (st)
    "won jung kim": "won joong kim", # removing 중 to handle jung (br)
    "ho jung lee": "ho joong lee", # removing 중 to handle jung (br)
    "jung seok oh": "joong seok oh", # removing 중 to handle jung (br)
    "se jung kim": "se joong kim", # removing 중 to handle jung (br)
    "gap jung kim": "kab joong kim", # removing 중 to handle jung (br)
    "jung hwa lee": "joong hwa lee", # removing 중 to handle jung (br)
    "dae jung kim": "dae joong kim", # removing 중 to handle jung (br)
    "jung seok cho": "joong seok cho", # removing 중 to handle jung (br)
    "hun gon kim": "heon gon kim", # removing 헌 to handle hun (br)
    "hun do park": "heon do park", # removing 헌 to handle hun (br)
    "hun wook park": "heon wook park", # removing 헌 to handle hun (st)
    "ho jun lee": "ho joon lee", # necessary to handle dup names (no 이호전)
    "hyun jun kim": "hyeon joon kim", # necessary to handle dup names (no 김현전)
    "hyeon su kim": "hyeon soo kim", # necessary to handle dup names (no 김현서)
    "jeong su kim": "jeong soo kim", # necessary to handle dup names (no 김정서)
    "ji hun jang": "ji hoon jang", # necessary to handle dup names (no 장지헌)
    "jun heo": "joon heo", # necessary to handle dup names (no 허전)
    "jun ho": "joon heo", # necessary to handle dup names (no 허전)
    "jun ho jeon": "joon ho jeon", # necessary to handle dup names (no 전전호)
    "jun ho lee": "joon ho lee", # necessary to handle dup names (no 이전호)
    "seong hun pak": "seong hoon park", # necessary to handle dup names (no 박성헌)
    "sung jun kim": "seong joon kim", # necessary to handle dup names (no 김숭준, 김숭전, 김승전)
    "seong jun kim": "seong joon kim", # necessary to handle dup names (no 김숭준, 김숭전, 김승전)
    "won jun choi": "won joon choi", # necessary to handle dup names (no 최원전)
    "woo suk go": "woo seok ko", # necessary to handle dup names (no 고우숙)
    "yong hun lee": "yong hoon lee", # necessary to handle dup names (no 이용헌)
    "jae yul lee": "jae yool lee", # necessary to handle dup names (no 이재열)
    "jun hyeok heo": "joon hyeok heo", # necessary to handle dup names (no 허전혁)
    "jun hyuck park": "joon hyeok park", # necessary to handle dup names (no 박전혁)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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