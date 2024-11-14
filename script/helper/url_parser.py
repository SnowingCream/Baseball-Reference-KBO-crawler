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
