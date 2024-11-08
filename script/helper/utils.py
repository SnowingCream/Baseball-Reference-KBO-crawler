'''
Used to merge uncommon notations for a given last name into the most common notation.
criteria for chooing the standard notation:
    1. Avoided 'u' as much as I could because it is one of the main reasons for the naming conflict, which can be pronounced in various ways.
        1.1. if 'u' was used to represent 'ㅜ', replace it to "oo".
        1.2. if 'u' was used to represent 'ㅓ', replace it to 'eo'.
    2. Avoided negative words or common word ex) 'no', 'an', 'go', 'im'.
        2-1. 'park' and 'moon' are exceptions, because they have already been too popular and common.
    3. Avoided 'g', as much as I could because it may confuse english speakers (great and giant sound different).
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
    
}

given_name_dict_kor = {
    "u": "woo",
    "been": "bin",
    "see": "si",
    "wahn": "wan",
}

non_korean_name_dict_eng = {
    "aarona ltherr" = "aaron altherr",
    "andrew" = "andy
}

'''
Helper function 1
Behavior: Parse the given URL and return its ct_code and year.
Usage: called in team_url_to_back_number_url to pre-process the URL. Also Used in st_player.ipynb to keep track of the appending process.
'''
def get_ct_code_and_year(team_url: str) -> tuple[int, int]:

    ct_code, year = int(team_url.split("&")[1].split("=")[1]), int(team_url.split("&")[2].split("=")[1])
    return ct_code, year

'''
Helper function 2
Behavior: Convert urls from the team overviews page: https://statiz.sporki.com/team/ to each team's backnumber list page, which has links to the page of each player in which the player's English name can also be found.
Usage: called to transit to players' individuals pages from team's URL.
'''

def team_url_to_back_number_url(team_url: str) -> str:

    # ct_code(input) = 1 digit, t_code(output) = 4 digit
    ct_code, year = get_ct_code_and_year(team_url)

    # Samsung Lions (삼성 라이온즈), 1982 - 2024
    if ct_code == 1:
        t_code = 1001 

    # Haitai Tigers (해태 타이거즈), 1982 - 2000
    # Kia Tigers (KIA 타이거즈), 2001 - 2024
    elif ct_code == 2:
        if year <= 2000:
            t_code = 2001
        else:
            t_code = 2002

    # Lotte Giants (롯데 자이언츠), 1982 - 2024
    elif ct_code == 3:
        t_code = 3001

    # Sammi Superstars (삼미 슈퍼스타즈), 1982 - 1984
    # Chungbo Pintos (청보 핀토스), 1985 - 1987
    # Pacific Dolphins (태평양 돌핀스), 1988 - 1995
    # Hyundai Unicorns (현대 유니콘스), 1996 - 2007
    elif ct_code == 4:
        if year <= 1984:
            t_code = 4001
        elif year <= 1987:
            t_code = 4002
        elif year <= 1995:
            t_code = 4003
        else:
            t_code = 4004

    # MBC Blue Dragons (MBC 청룡), 1982 - 1989
    # LG Twins (LG 트윈스), 1990 - 2024
    elif ct_code == 5:
        if year <= 1989:
            t_code = 5001
        else:
            t_code = 5002

    # OB Bears (OB 베어스), 1982 - 1998
    # Doosan Bears (두산 베어스), 1999 - 2024
    elif ct_code == 6:
        if year <= 1998:
            t_code = 6001
        else:
            t_code = 6002

    # Binggre Eagles (빙그레 이글스), 1986 - 1993
    # Hanwha Eagles (한화 이글스), 1994 - 2024
    elif ct_code == 7:
        if year <= 2000:
            t_code = 7001
        else:
            t_code = 7002

    # Ssangbangwool Raiders (쌍방울 레이더스), 1991 - 1999
    elif ct_code == 8:
        t_code = 8001 

    # SK Wyverns (SK 와이번스), 2000 - 2020
    # SSG Landers (SSG 랜더스), 2021 - 2024
    elif ct_code == 9:
        if year <= 2020:
            t_code = 9001
        else:
            t_code = 9002

    # No idea why there is no ct_code 10.
    # Before Kiwoom Heroes, The previous team names were Woori Heroes (우리 히어로즈) and Nexen Heroes (넥센 히어로즈),
    # but those names are not in KBO website and Statiz.
    
    # Kiwoom Heroes (키움 히어로즈), 2008 - 2024
    elif ct_code == 11:
        t_code = 10001 

    # NC Dinos (NC 다이노스), 2013 - 2024
    elif ct_code == 12:
        t_code = 11001 

    # KT Wiz (KT 위즈), 2015 - 2024
    elif ct_code == 13:
        t_code = 12001 

    back_number_url = f"https://statiz.sporki.com/team/?m=seasonBacknumber&t_code={t_code}&year={year}"
    return back_number_url

'''
Helper function 3
Behavior: Parse the given name and return the first and last name (in terms of word, not character) -> use it for English name only.
Usage: used to extract first and last name of non-Korean players, which resolved a decent amount of naming conflict.
'''

def eng_get_first_and_last(name: str) -> str:
    split = name.split(" ")

    # 'jr' is not helpful for distinguishing players
    if split[-1].contains["jr"]:
        split = split[-1]
    
    if len(split) > 2:
        return split[0] + " " + split[-1]
    else:
        return " ".join(split)



'''
Helper function 4
Behavior: Parse the given name and return the last name (in terms of character, not word) -> use it for Korean name only.
Usage: used to check if players with rare last name exist (otherwise merge them into the common notation for that last name to resolve naming conflict)
'''
def kor_get_last(name_kor_list: list[str], last_name: str) -> list[str]:
    found = list()
    for name in name_kor_list:
        if name[0] == last_name:
            found.append(name)
    return found


'''
Helper function 5
Behavior: Parse the given name and check if the last name is in the last_name_dict for generalization (a consistent notation for last names), and if so, update it.
Usage: used to generalize last names to reduce naming conflict.
'''
def kor_update_last(name: str) -> str:
    
    name_split = name.split(" ")

    if len(name_split) > 1 and name_split[-1] in last_name_dict:
        name_split[-1] = last_name_dict[name_split[-1]]
        return " ".join(name_split)
    else:
        return name


def kor_update_given(df, name: str) -> str:

    df_br = df[df['name_eng_y'].isna()]
    df_st = df[df['name_eng_x'].isna()]

    df_br_set = set(df_br["name_new"].to_list())
    df_st_set = set(df_st["name_new"].to_list())


def kor_update_given_2(name_input: str, opposite_set: set[str]) -> str:

    name_split = name_input.split(" ")

    if len(name_split) > 1:
        given_name = name_split[:-1]

        for i in range(len(given_name)):
            if given_name[i] in given_name_dict_kor:
                given_name[i] = given_name_dict_kor[given_name[i]]

            if given_name[i].contains('u'):
                chr_cdd_1 = given_name[i][:].replace('u', 'eo')
                chr_cdd_2 = given_name[i][:].replace('u', 'oo')

                name_cdd = given_name[:]
                
    
    else:
        return name_input

    
    
    




        

    



        



        