'''
Used to merge uncommon notations for a given name into the most common notation.
criteria for chooing the standard notation for Korean name:
    1. Avoided 'u' as much as I could because it is one of the main reasons for the naming conflict, which can be pronounced in various ways.
        1.1. if 'u' was used to represent 'ㅜ', replace it to "oo".
        1.2. if 'u' was used to represent 'ㅓ', replace it to 'eo'.
    2. Avoided negative words or common word ex) 'no', 'an', 'go', 'im'.
        2-1. 'park' and 'moon' are exceptions, because they have already been too popular and common.
    3. Avoided 'g', as much as I could because it may confuse english speakers (great and giant sound different).
        3-1. if 'g' was used to represent 'ㄱ' (the case of great), replace it to 'k'.
        3-2. if 'g' was used to represent 'ㅈ' (the case of giant), replace it to 'j'.
'''

# merge various notations for a given Korean character's last name into its standard notation.
last_name_dict_kor = {
    "an": "ahn",
    "pae": "bae",
    "paek": "baek",
    "back": "baek",
    "beak": "baek", # only 1 case
    "baik": "baek", # only 1 case
    "byun": "byeon",
    "pyon": "byeon", # only 1 case
    "chei": "chae", # only 1 case
    "chen": "cheon",
    "chun": "cheon",
    "tian": "cheon", # only 1 case
    "jo": "cho",
    "chou": "choi",
    "to": "doh", # only 2 cases
    "do": "doh", # only 1 case
    "tong": "dong",
    "uhm": "eom", # only 1 case
    "um": "eom", # only 1 case
    "aum": "eom",
    "hur": "heo",
    "her": "heo",
    "hor": "heo",
    "huh": "heo",
    "ho": "heo", # check 호 -> no such last name (good)
    "chang": "jang", #check 창 -> no such last name (good)
    "jun": "jeon", # check 준 -> no such last name (good)
    "jeun": "jeon",
    "chung": "jeong",
    "jong": "jeong", # only 1 case
    "joung": "jeong", # only 1 case
    "jung": "jeong", # check 중 -> no such last name (good)
    "chi": "ji",
    "chin": "jin",
    "ju": "joo",
    "ga": "ka", # only 1 case
    "gam": "kam", # only 1 case
    "kum": "keum",
    "geum": "keum",
    "gi": "ki", # might cause problem... hasn't been checked
    "gil": "kil",
    "go": "ko",
    "koh": "ko", # only 1 case
    "gong": "kong",
    "gu": "koo",
    "ku": "koo",
    "kuk": "kook", # only 1 case
    "gwak": "kwak",
    "gye": "kye",
    "gwon": "kwon",
    "kweon": "kwon", # only 1 case
    "yi": "lee", # only 1 case
    "im": "lim",
    "mun": "moon",
    "mon": "moon", # only 1 case
    "no": "noh",
    "roh": "noh",
    "ro": "noh", # only 1 case
    "o": "oh", # only 1 case
    "bang": "pang",
    "pak": "park", # pak is never 백? not sure -> manually check, no conflict (good)
    "ryou": "ryu", # only 2 cases
    "sok": "seok", # only 1 case
    "sun": "seon",
    "sung": "seong",    
    "senyu": "seonwoo",
    "seonu": "seonwoo",
    "sim": "shim",
    "sin": "shin",
    "son": "sohn",
    "shon": "sohn", # only 1 case
    "dang": "tang", # only 1 case
    "wee": "wi",
    "weon": "won", # only 1 case
    "wu": "woo",
    "yo": "yeo", # only 2 cases
    "youm": "yeom",
    "in": "yin", # only 2 cases
    "yu": "yoo",
    "you": "yoo",
    "liu": "yoo", # only 1 case
    "yuk": "yook", # only 1 case
    "yun": "yoon", # check 연 -> no conflict (good)
}

# merge various notations for a given Korean character into its standard notation.
first_name_dict_kor = {
    "back": "baek",
    "been": "bin",
    "pin": "bin",
    "bu": "boo", # no 버, so it's fine
    "chul": "cheol", # no 출, so it's fine
    "dai": "dae",
    "deog": "deok",
    "duk": "deok", 
    "du": "doo",
    "up": "eob",
    "eop": "eob",
    "ui": "eui", # 의
    "gui": "gwi",
    "hai": "hae",
    "hack": "hak",
    "whoi": "hoi", 
    "hoe": "hoi", # 회
    "hun": "hoon", # handled all 훈
    "whee": "hwi", # 휘
    "hyeop": "hyeob",
    "hyub": "hyeob", # no 흅, so it's fine
    "hyuk": "hyeok", # no 휵, so it's fine
    "hyok": "hyeok",
    "hyouk": "hyeok",
    "hyuck": "hyeok",
    "hyun": "hyeon", # no 휸, so it's fine
    "hyoun": "hyeon",
    "hee": "hyi", # 희
    "heui": "hyi", # 희
    "hui": "hyi", # 희
    "hei": "hyi", # 희
    "heu": "hyi", # 희
    "ick": "ik",
    "yil": "il",
    "jung": "jeong", # handled all 중
    "jee": "ji",
    "jip": "jib",
    "ju": "joo", # no 저, so it's fine
    "june": "joon",
    "gap": "kab", 
    "gab": "kab",
    "kap": "kab",
    "gang": "kang", # conventional
    "geon": "keon", # conventional
    "geun": "keun", # no 즌, so it's fine
    "gi": "ki", # conventional
    "gil": "kil", # conventional
    "go": "ko", # conventional
    "ku": "koo",
    "gu": "koo", # conventional
    "goo": "koo", # conventional
    "gu": "koo", # cases of 거 have been handled (checked both br and st)
    "gook": "kook",
    "guk": "kook", # no 걱, so it's fine
    "gwan": "kwan", # no 좐, so it's fine
    "gwang": "kwang", # no 좡, so it's fine
    "gwon": "kwon", # no 줜, so it's fine
    "gweon": "kwon", 
    "gyeol": "kyeol", # no 졀, so it's fine
    "gyeom": "kyeom",
    "kyong": "kyeong",
    "gyeong": "kyeong", # conventional
    "gyo": "kyo", # conventional
    "gyu": "kyu", # conventional
    "gyun": "kyun", # no 쥰, so it's fine
    "myong": "myeong",
    "no": "noh",
    "o": "oh",
    "pill": "pil",
    "suh": "seo",
    "sub": "seob", # no 숩, so it's fine
    "seop": "seob",
    "sup": "seob",
    "suk": "seok",
    "suck": "seok",
    "seog": "seok",
    "sung": "seong",
    "seoung": "seong",
    "see": "si",
    "sig": "sik",  
    "sin": "shin",
    "tai": "tae",
    "ttaum": "tteum",
    "wahn": "wan",
    "u": "woo",
    "oug": "wook",
    "uk": "wook", # cases of 억 have been handled (checked both br and st)
    "un": "woon", # cases of 언 have been handled (checked both br and st)
    "ung": "woong", # no 엉, so it's fine
    "wong": "woong",
    "yeop": "yeob",
    "yup": "yeob",
    "yeup": "yeob",
    "yub": "yeob",
    "yuop": "yeob", 
    "youb": "yeob",  
    "yol": "yeol",
    "youl": "yeol",
    "i": "yi",
    "yu": "yoo",
}

# recover '-' for Korean players who don't have it in their name.
# Necessary to distinguish Korean players and non-Korean pleyers.
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
1-to-1 correction for unique cases.
If the change is artificial that may cause problems, double check with birthday to specify the certain player.
'''
manual_handle_dict = {

    # Korean player whose birthday is different between websites. Follow the statiz side.
    ("myeong jin oh", "2001-04-09"): ("myeong jin oh", "2001-09-04"), # mismatching birthday
    ("joon hyoung kim", "2002-12-07"): ("joon hyeong kim", "2002-07-12"), # mismatching birthday
    ("hyeon seung jung", "2001-10-24"): ("hyeon seung jeong", "2001-01-24"), # mismatching birthday
    ("jong soo chung", "1980-06-08"): ("jong soo jeong", "1980-05-08"), # mismatching birthday
    ("jin soo lim", "1972-02-01"): ("jin soo lim", "1972-02-21"), # mismatching birthday
    ("ji heon jung", "2003-12-11"): ("ji heon jeong", "2003-01-01"), # mismatching birthday
    ("ho jung lee", "1992-10-13"): ("ho joong lee", "1992-10-03"), # mismatching birthday
    ("dong hun lee", "1996-07-24"): ("si won lee", "1996-07-24"), # mismatching birthday
    ("do been kim", "2001-01-05"): ("do been kim", "2001-01-15"), # mismatching birthday
    ("chul woo park", "1991-01-19"): ("cheol woo park", "1991-01-29"), # mismatching birthday
    ("won kuk lee", "1948-05-10"): ("won kuk lee", "1949-05-10"), # mismatching birthday
    ("yong ho lee", "2012-01-01"): ("yong ho lee", "1988-05-07"), # wrong birthday

    # players who changed the name -> check birthday.
    ("byung hwee lee", "1998-08-05"): "yoo chan lee", # changed name
    ("jae hyeon nam", "1996-09-13"): "ha joon nam", # changed name
    ("jeong bin kim", "1994-06-08"): "sa yoon kim", # changed name
    ("sung ho no", "1989-10-22"): "geon woo noh", # changed name
    ("seung hwa lee", "1982-05-04"): "woo min lee", # changed name
    ("dae won moon", "1998-08-22"): "won moon", # changed name
    ("dong won lee", "1993-12-15"): "tae oh lee", # changed name
    ("dong wook park", "1985-04-06"): "keon woo park", # changed name
    ("jang hyeok yoo", "2000-05-30"): "ro kyeol yoo", # changed name
    ("jong ki park", "1995-01-21"): "so joon park", # changed name
    ("ji seon chae", "1995-07-11"): "won hoo chae", # changed name
    ("yi hwan kim", "2000-09-15"): "do hyeon kim", # changed name
    ("keon choi", "1999-04-10"): "yi joon choi", # changed name
    ("sei hyok park", "1990-01-09"): "se hyeok park", # changed name
    ("sung ki jung", "1979-08-06"): "jin jeong", # changed name
    ("wang gi lee", "1986-05-28"): "jae yool lee", # changed name
    ("yong su shin", "1996-01-05"): "yoon hoo shin", # changed name
    ("gi hyun yang", "1998-12-16"): "ji yool yang", # changed name
    ("yeong hwan choi", "1992-02-20"): "seol woo choi", # changed name
    ("tae woo kim", "1997-10-19"): "soo in kim", # changed name
    ("min su kim", "1998-07-16"): "soo yoon kim", # changed name
    ("ju hong park", "1999-08-20"): "seong woong park", # changed name
    ("hyun min kim", "2000-02-23"): "geon kim", # changed name


    # flipped format (last name + first name instead of first name + last name) -> check birthday
    ("eum jang yoon", "2003-10-07"): "jang yoon eom", # flipped format
    ("jo ho pyo", "1958-12-02"): "ho pyo cho", # flipped format
    ("seok sang ho", "2000-04-14"): "sang ho seok", # flipped format
    ("seol jae min", "1997-05-01"): "jae min seol", # flipped format
    ("no gun woo", "1989-10-22"): "keon woo noh", # flipped format
    ("noh jae won", "2001-07-26"): "jae won noh", # flipped format
    ("nam yun sung", "1987-08-04"): "yoon seong nam", # flipped format
    ("park tae won", "1992-02-17"): "tae won park", # flipped format
    ("jo sung hyeon", "2002-08-06"): "seong hyeon cho", # flipped format
    ("jo hyo won", "1999-03-10"): "hyo won cho", # flipped format
    ("hwang sung woong", "1986-06-12"): "seong woong hwang", # flipped format
    ("je hwan yu", "2000-09-30"): "hwan yoo je", # flipped format
    ("hong ji hun", "1998-05-17"): "ji hoon hong",# flipped format
    ("hong jae young", "1990-09-25"): "jae young hong", # flipped format
    ("eom tae kyoung", "2003-05-03"): "tae kyeong eom", # flipped format
    ("eom tae ho", "2001-01-03"): "tae ho eom", # flipped format
    ("lee ju heon", "1969-11-17"): "joo heon lee",  # flipped format
    ("yeo seung cheol", "1984-05-29"): "seung cheol yeo", # flipped format
    ("choi yun cheol", "1989-10-24"): "yoon cheol choi", # flipped format
    ("jin jong kil", "1981-09-23"): "jong kil jin", # flipped format
    ("lee jung seok", "1998-07-27"): "joong seok lee", # flipped format
    ("choi seol woo", "1992-02-20"): "seol woo choi", # flipped format
    ("heo yong joo", "2003-06-05"): "yong joo heo", # flipped format

    # English name is valid but does not match Korean name -> check birthday
    ("young hun cho", "1987-10-29"): "yong hoon cho", # wrong name
    ("young ho lee", "1970-05-06"): "yong ho lee", # wrong name
    ("tae soo kim", "1982-09-27"): "tae goo kim", # wrong name
    ("seung min choi", "1990-07-31"): "seong min choi", # wrong name
    ("keong soo min", "1981-05-19"): "kyeong soo min", # wrong name
    ("jong ho kim", "1973-05-24"): "dong ho kim", # wrong name
    ("hyeon jong choi", "1992-12-03"): "hyeon jeong choi", # wrong name
    ("ki hyo ahn", "1996-06-19"): "ki hyo nam", # wrong name
    ("min guk song", "1982-02-09"): "min kook seong", # wrong name 
    ("soo sung kang", "1993-06-09"): "koo seong kang", # wrong name
    ("hyuk kim", "1968-02-28"): "nyeok kim", # wrong name
    ("seung hye kim", "1981-02-11"): "seung hoi kim",  # wrong name
    ("seong kon kim", "1976-05-01"): "seung kwon kim", # wrong name
    ("myeong jae kim", "1987-01-05"): "myeong je kim",  # wrong name
    ("hwi chan jung", "1987-02-07"): "hoi chan jeong", # wrong name
    ("min je jang", "1990-03-19"): "min jae jang", # wrong name
    ("kyu jae cho", "1967-10-07"): "kyu je cho", # wrong name
    ("gil ho song", "1967-08-03"): "gil ho sohn", # wrong name
    ("kyun eun noh", "1984-03-11"): "kyeong eun noh", # wrong name
    ("sae eop lim", "1983-09-01"): "se eop lim", # wrong name
    ("sang guk pang", "1960-09-06"): "sang kook park", # wrong name
    ("jae kuk ryu", "1983-05-30"): "je kuk ryu", # wrong name
    ("jae whan bae", "1995-02-24"): "jae hwan bae", # wrong name
    ("yoon hee nam", "1987-08-04"): "yoon seong nam", # wrong name
    ("jo soo kim", "1986-08-23"): "ji soo kim", # wrong name
    ("jong deuk kim", "1993-05-12"): "jong deok kim", # wrong name
    ("san gil park", "1976-07-30"): "sang il park", # wrong name
    ("gang yoo park", "1980-07-19"): "kang woo park", # wrong name
    ("jong nam kim", "1986-11-22"): "jeong nam kim", # wrong name
    ("chan seob lee", "1987-03-10"): "chang seob lee", # wrong name
    ("don hun kwak", "1981-07-13"): "dong hoon kwak", # wrong name
    ("hei chun lee", "1979-03-12"): "hye cheon lee", # wrong name
    ("hui gon kim", "1984-07-28"): "hwi gon kim", # wrong name
    ("hui gwon kim", "1986-04-10"): "hoi kwon kim", # wrong name
    ("nak soo song", "1957-08-12"): "nak soo seong", # wrong name
    ("gyeon eon kim", "1982-12-07"): "kyeong eon kim", # wrong name
    ("sung heon hong", "1977-02-28"): "seong heun hong", # wrong name
    ("seong jae yang", "1980-12-16"): "seong je yang", # wrong name
    ("chan sub lee", "1987-03-10"): "chang seob lee", # wrong name
    ("chi ho ha", "1984-12-16"): "ji ho ha", # wrong name
    ("seong woo choo", "1979-09-24"): "seung woo choo", # wrong name
    ("geun wook lee", "1995-02-13"): "geon wook lee", # wrong name
    ("tong keon yeo", "2005-08-04"): "dong keon yeo", # wrong name
    ("byeong do kim", "1972-01-23"): "byeong doo kim", # wrong name
    ("gun cheol song", "1968-05-25"): "koon cheol seong", # wrong name
    ("hae jung yoo", "1982-06-20"): "hye jeong yoo", # wrong name
    ("hyeong been han", "1998-12-11"): "kyeong bin han", # wrong name
    ("in whan jeon", "1990-06-04"): "in hwan jeon", # wrong name
    ("jae bin kim", "1982-03-31"): "je bin kim", # wrong name
    ("seong min chi", "1978-09-12"): "seung min ji", # wrong name
    ("joo on park", "1973-07-13"): "joo eon park", # wrong name
    ("seong hyun son", "1982-07-08"): "seung hyeon sohn", # wrong name
    ("joon soon han", "1999-02-13"): "joon soo han", # wrong name
    ("tae jun shin", "1955-06-27"): "tae joong shin", # wrong name
    ("tae heon kim", "1998-03-21"): "tae hyeon kim",  # wrong name
    ("yeong jae eom", "1960-10-24"): "pyeong jae eom", # wrong name
    ("yeong jae song", "1971-03-09"): "yeong jae seong", # wrong name
    ("young kwon kwon", "1971-08-20"): "yeong koo kwon", # wrong name
    ("yong sang jeong", "1964-04-29"): "yong saeng jeong", # wrong name
    ("young seok shin", "2003-10-11"): "yong seok shin", # wrong name
    ("yi hyeon hong", "1978-03-12"): "eui hyeon hong", # wrong name
    ("young joo seo", "1990-06-30"): "yong joo seo", # wrong name

    # last name doesn't follow the translation convention -> check birthday 
    ("gyeong eop chu", "1968-09-02"): "kyeong eob joo", # manual last name interpretation
    ("chang hun choo", "1981-12-17"): "chang hoon joo", # manual last name interpretation
    ("dong sik chu", "1948-08-23"): "dong sik joo", # manual last name interpretation
    ("sa min chun", "1999-07-06"): "sa min jeon", # manual last name interpretation
    ("gyeong sik chu", "1983-11-19"): "kyeong sik choo", # manual last name interpretation
    ("chung yeol chou", "1959-02-25"): "chung yeol cho", # manual last name interpretation
    ("sang wahn chu", "1971-01-28"): "sang wan choo", # manual last name interpretation
    ("sang ryul chun", "1972-06-12"): "sang ryul jeon", # manual last name interpretation
    ("sung geon chu", "1970-08-05"): "seong keon choo", # manual last name interpretation

    # manual handling for g and u -> check birthday
    ("chan gun lee", "1996-05-14"): "chan keon lee", # mamually resolving g, u
    ("gun hee kim", "2004-11-07"): "keon hyi kim", # manually resolving g, u
    ("gun no lee", "1961-02-27"): "koon noh lee", # manually resolving g, u
    ("gun ok lee", "1971-12-27"): "koon ok lee", # manulally resolving g, u
    ("jun gyu yu", "2002-08-16"): "joon kyoo yoo", # manually resolving g, u
    ("geong gyu park", "1983-04-17"): "jeong kyoo park", # manually resolving g + u
    ("tae gun kim", "1989-12-30"): "tae koon kim", # manually resolving g, u
    ("young gun cho", "1999-02-04"): "yeong keon cho", # manually resolving g, u
    ("dong geol lee", "1983-08-12"): "dong keol lee", # manually resolving g
    ("sang gyo chung", "1991-10-01"): "sang kyo jeong", # manually resolving g
    ("yi sul kim", "1984-06-15"): "yi seul kim", # manually resolving u
    ("sang yun lee", "1960-12-21"): "sang yoon lee", # manually resolving u
    ("gu sun jung", "1956-12-15") : "koo seon jung", # double u
    ("bum jun park", "2004-05-28"): "beom joon park", # double u
    ("jun bum koo", "1995-03-18"): "joon beom koo", # double u
    ("jun suk choi", "1983-02-15"): "joon seok choi", # double u
    ("yun jun song", "1992-07-16"): "yoon joon song", # double u
    ("su yun kim", "1998-07-16"): "soo yoon kim", # double u

    # handle common 'u' case by removing one way of interpretation so that the rest can be only one case that can be handled by first_name_dict_kor -> check birthday.
    ("pil jung jin", "1972-10-13"): "pil joong jin", # removing 중 to handle jung (st)
    ("jung il ryu", "1963-04-28"): "joong il ryu",  # removing 중 to handle jung (st)
    ("jung geun cho", "1982-12-20"): "joong keun cho",  # removing 중 to handle jung (st)
    ("jung keun bong", "1980-07-15"): "joong keun bong",  # removing 중 to handle jung (st)
    ("wang jung baek", "1992-08-06"): "wang joong baek",  # removing 중 to handle jung (st)
    ("jung yeol an", "1995-09-01"): "joong yeol ahn",  # removing 중 to handle jung (st)
    ("young jung kim", "1998-04-27"): "yeong joong kim",  # removing 중 to handle jung (st)
    ("won jung kim", "1993-06-14"): "won joong kim", # removing 중 to handle jung (br)
    ("ho jung lee", "1992-10-03"): "ho joong lee", # removing 중 to handle jung (br)
    ("jung seok oh", "1973-08-05"): "joong seok oh", # removing 중 to handle jung (br)
    ("se jung kim", "1979-10-20"): "se joong kim", # removing 중 to handle jung (br)
    ("gap jung kim", "1970-08-15"): "kab joong kim", # removing 중 to handle jung (br)
    ("jung hwa lee", "1964-02-11"): "joong hwa lee", # removing 중 to handle jung (br)
    ("dae jung kim", "1963-03-16"): "dae joong kim", # removing 중 to handle jung (br)
    ("jung seok cho", "1972-03-02"): "joong seok cho", # removing 중 to handle jung (br)
    ("hun gon kim", "1988-11-09"): "heon gon kim", # removing 헌 to handle hun (br)
    ("hun do park", "1987-01-01"): "heon do park", # removing 헌 to handle hun (br)
    ("hun wook park", "1993-04-11"): "heon wook park", # removing 헌 to handle hun (st)   
    ("sang un park", "1997-03-03"): "sang eon park", # removing 언 to handle un (st)
    ("un hak ahn", "1962-01-06"): "eon hak ahn", # removing 언 to handle un (st)

    # Non-Korean Players (fix to match the BR name)
    "aarona ltherr": "aaron altherr", # space typo
    "julio cesar depaula": "julio de paula", # missing space
    "rick vandenhurk": "rick van den hurk", # missing space
    "kevin dattolla": "kevin dattola", # name typo
    "jose para": "jose parra", # name typo
    "michael bowdent": "michael bowden", # name typo
    "tylor wilson": "tyler wilson", # name typo
    "wes obermuller": "wes obermueller", # name typo
    "tyrone hornes": "tyrone horne", # name typo
    "scoot baker": "scott baker", # name typo
    "michael serveneck": "mike cervenak", # name typo
    "j.r. philllips": "j.r. phillips", # name typo
    "satohshi iriki": "satoshi iriki", # japanese h handling
    "ohkamoto sinya": "shinya okamoto", # japanese h handling
    "heishu ohara": "byeong soo kang",  # japanese kanji read in Korean
    "minoru tanaka": "sil kim", # japanese kanji read in Korean
    "mototomi yoshimura": "won boo ko",  # japanese kanji read in Korean
    "bubba smith": "charles smith", # unique name, manual match
    "luis manuel de los santos martinez": "luis de los santos", # unique name, manual match
    "gustavo karim garcia aguayo": "karim garcia", # unique name, manual match
    "joshua lee josh bell": "josh bell", # unique name, manual match
    "leang keu beul": "matt blank", # English read in Korean then read in English again

    # uncertain for translation standard (both seem fine, just go with one of them for matching) 
    "myeong nok oh": "myeong rok oh", # notation clarification
    "kyeong sik chu": "kyeong sik choo", # notation clarification
    "jun kyu ryu": "joon kyoo yoo", # notation clarification
    "won jai lee": "won jae lee",  # notation clarification
    "lo han kang": "ro han kang", # notation clarification
    "seung rak son": "seung lak sohn", # notation clarification
    "tae lyong kim": "tae ryong kim", # notation clarification
    "woo tai hong": "woo tae hong", # notation clarification

    # English name is not valid.
    "tae yeoung kim": "tae yeong kim", # name typo
    "das sung koo": "dae seong koo", # name typo
    "su yeoun kim": "soo yeon kim", # name typo
    "jae weong seo": "jae eung seo", # name typo
    "wong geun kim": "won keun kim", # name typo
    "yu naml": "yool nam", # space typo
    "kwang kuen lee": "kwang keun lee", # name typo
    "soung hun kim": "seong hun kim", # name typo
    "sangr yul  jeon": "sang ryeol jeon", # space typo 
    "yeun gyu ji": "yeon kyu ji", # name typo
    "young jae gp": "young jae ko", # name typo
    "wung joung chang": "woong jeong jang", # name typo
    "kyung oan park": "kyeong wan park", # name typo
    "moung chan kim": "myeong chan kim", # name typo
    "myeoung jin cha": "myeong jin cha", # name typo
    "soo hyung kjim": "soo hyung kim", # name typo
    "jun pyo jhun": "jun pyo jeon", # name typo
    "jung heop huh": "jeong hyeop heo", # name typo
    "meong man kim": "eok man kim", # name typo
    "donk keun lee": "dong keun lee", # name typo
    "seo owan hong": "se wan hong", # name typo
    "jun heok huh": "joon hyeok heo", # name typo
    "jun hyeung lim": "joon hyeong lim", # name typo
    "kyong hoon lim": "kyeong hoon lim", # name typo
    "myung woom park": "myeong woon park", # name typo
    "myuong ki lee": "myeong ki lee", # name typo
    "seong bhin park": "seong bin park", # name typo
    "seong mou ahn": "seong moo ahn", # name typo
    "hsiang pin liu": "sang bin yoo", # name typo
    "tae yean kim": "tae yeon kim", # name typo
    "tae youn lee": "tae yeon lee", # name typo
    "jea jung chang": "jae joong jang", # name typo
    "beum soo jung":"beom soo jeong", # name typo
    "byeong meong lee":"byeong eok lee", # name typo
    "byong yeon choi": "byeong yeon choi", # name typo
    "dong weun lee": "dong eun lee", # name typo
    "won jei choi": "won je choi", # name typo
    "hyeon doe sin": "hyeon dae shin", # name typo
    "jea gul kim": "jae geol kim", # name typo
    "soung hun kim": "seong hoon kim", # name typo
    "yeun hun kim": "yeon hoon kim", # name typo
    "ji chol park": "ji cheol park", # name typo
    "ji guang choi": "ji kwang choi", # name typo
    "jin hang choi": "jin haeng choi", # name typo
   "sung mou an": "seong moo ahn", # name typo
    "hea sung kim": "hoi seong kim", # name typo
    "hi sang yoon": "hyi sang yoon", # name typo
    "yoon sep han": "yoon seob han", # name typo
    "youn suk choi": "yoon seok choi", # name typo
    "yeun hun kim": "yeon hoon kim", # name typo
    "yeong ll oh": "yeong il oh", # name typo
    "tae hyon chung": "dae hyeon jeong", # name typo
    "yil yeon choi": "il eon choi", # name typo

    # manual handling for rare names
    "jae park song": "jae bak song", # unique name, manual match
    "gap jung kim": "kab joong kim", # unique name, manual match
    "ji hwuon yoo": "ji hwon yoo", # unique name, manual match
    "yeong jin do": "yeong jin doo", # unique name, manual match
    "il ryung kim": "il yoong kim", # unique name, manual match
    "deuk han yong": "deok han yong", # unique name, manual match
    "jeung woo seok": "jeong woo seok", # unique name, manual match
    "duck gyoon hwang": "deok kyoon hwang", # unique name, manual match
    "lang gyun gil": "rang gyun kil", # unique name, manual match
    "mi r jeon": "mi reu jeon", # unique name, manual match
    "kevin heon ju lee": "kevin lee", # unique name, manual match
    "il yung kim": "il yoong kim", # unique name, manual match

    # nickname matching -> no need birthday
    "chan moon": "chan jong moon", # nickname
    "chang choi": "chang yang choi", # nickname
    "chang moon": "chang hwan moon", # nickname
    "seung song": "seung joon song", # nickname
    "ui jeon": "ui san jeon", # nickname
    "jon mae": "brian mazone", # nickname
    "jung bong": "joong keun bong", # nickname
    "ray choi": "kyeong hwan choi", # nickname
}

# Non-Korean players' nicknames for more flexible matching. Only includes the cases that do not cause confusions.
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
    "roberto": "robert",
    "raymond": "ray",
    # "daniel": "dan",
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

# birthday correction for non-Korean players (match BR birthday)
dob_dict_eng = {
    "Israel Alcantara": "1973-05-06",
    "Michael Anderson": "1966-07-30",
    "Boi Rodriguez": "1966-04-14",
    "George Anthony Canale": "1965-08-11",
    "Michael Serveneck": "1976-08-17",
    "Gerrod Jay Davis": "1970-10-03",
    "Julio Franco": "1958-08-23",
    "Luther Hackman": "1974-10-10",
    "Ken Kadokura": "1973-07-29",
    "Doug Linton": "1965-02-09",
    "Mendy Lopez": "1973-10-15",
    "Alessandro Maestri": "1985-06-01",
    "Roberto Antonio Petagine": "1971-06-07",
    "Bienvenido Rivera": "1968-01-11",
    "Runelvys Hernandez": "1978-04-27",
    "Jacob Edward Turner": "1991-05-21",
    "Efrain Valdez": "1966-07-11",
    "Darrin Winston": "1966-07-06",
    "Julian Yan": "1965-07-24",
}