import pandas as pd
from typing import Callable, Union
from helper.ref_dict import last_name_dict_kor, first_name_dict_kor, recover_dash_dict, manual_handle_dict, first_name_dict_eng, dob_dict_eng
from collections import defaultdict


'''
Behavior: insert '-' for Korean players whose name miss it.
Usage: used to make sure all Korean players with given name that has more than 1 character have '-'.
'''
def recover_dash(name: str) -> str:
    if name in recover_dash_dict:
        return recover_dash_dict[name]
    return name

'''
Behavior: parse the given full name and return the last name (in terms of character, not word) -> use it for Korean name only.
Usage: used to check if players with rare last name exist (otherwise merge them into the common notation for that last name to resolve naming conflict)
'''
def kor_get_last(name_kor_list: list[str], last_name: str) -> list[str]:
    found = list()
    for name in name_kor_list:
        if name[0] == last_name:
            found.append(name)
    return found


'''
Behavior: parse the given full name and check if the last name is in the last_name_dict_kor and update it.
Usage: used to generalize last names to reduce naming conflict.
'''
def kor_update_last(name: str) -> str:
    
    name_split = name.split(" ")

    if len(name_split) > 1 and name_split[-1] in last_name_dict_kor:
        name_split[-1] = last_name_dict_kor[name_split[-1]]
        return " ".join(name_split)
    else:
        return name

'''
Behavior: parse the given full name and check if the first name is in the first_name_dict and update it.
Usage: used to generalize first names to reduce naming conflict.
'''
def kor_update_first(name: str) -> str:
    
    name_split = name.split(" ")
    if len(name_split) > 1:
        first_name_split = name_split[:-1]
        for i in range(len(first_name_split)):
            if first_name_split[i] in first_name_dict_kor:
                first_name_split[i] = first_name_dict_kor[first_name_split[i]]
        return " ".join(first_name_split) + " " + name_split[-1]
    return name

'''
Bahavior: check if only one candidate exists in the checker. If so, return that candidate. Otherwise, return the default_return.
Usage: used to resolve cases for 'u', which has 2 possible interpretations (eo & oo). If only 1 of them exists, update so. Otherwise leave as it is.
'''
def check_uniqueness(candidate_1: str, candidate_2: str, default_return: str, checker: set[str]) -> str:

    if candidate_1 in checker and candidate_2 in checker:
        # print(f"given name: {default_return} -> both exist")
        return default_return
    if candidate_1 not in checker and candidate_2 not in checker:
        # print(f"given name: {default_return} -> neither exists")
        return default_return
    if candidate_1 in checker:
        # print(f"given name: {default_return} -> found the unique match")
        return candidate_1
    if candidate_2 in checker:
        # print(f"given name: {default_return} -> found the unique match")
        return candidate_2

    
'''
Behavior: specifically handling English notation 'u'
Usage: used to handle common usage of 'u': only 1 'u' in the name and only one of its variation exists on the other side.
'''
def kor_handle_u(row: pd.DataFrame, candidates: set[str]) -> str:

    name_split = row['name_new'].split(" ")
    
    # remove the last name
    if len(name_split) > 1:
        first_name_split = name_split[:-1]

        # if the first name has more than 1 Korean character, need to check if there are several 'u's.
        # if there is no 'u' or more than 1 'u', cannot handle it -> return the original value.
        if len(first_name_split) > 1:
            count = 0
            for name in first_name_split:
                # 'eu' is fine, it has only 1 matching pronuncation ('ㅡ')
                if 'u' in name and 'eu' not in name:
                    count += 1
            if not count:
                return row['name_new']
            if count == len(first_name_split):
                return row['name_new']
        else:
            if 'u' not in first_name_split[0]:
                return row['name_new']
                
        # once confirmed there is only 1 'u', find that character.
        # then substitute that u with 'oo' and 'eo'.
        # if there are both or neither, cannot handle it -> return the original value.
        # if there is only 1 of them, return that name.
        for i in range(len(first_name_split)):
            if 'u' in first_name_split[i] and 'eu' not in first_name_split[i]:

                first_name_copy_oo = first_name_split[:]
                first_name_copy_oo[i] = first_name_copy_oo[i].replace('u', 'oo')
                first_name_copy_oo = " ".join(first_name_copy_oo) + " " + name_split[-1]

                first_name_copy_eo = first_name_split[:]
                first_name_copy_eo[i] = first_name_copy_eo[i].replace('u', 'eo')
                first_name_copy_eo = " ".join(first_name_copy_eo) + " " + name_split[-1]

                return check_uniqueness(first_name_copy_oo, first_name_copy_eo, row['name_new'], candidates)

    return row['name_new']
    
'''
Behavior: update the given row with manual_handle_dict, which has two types of key: str, tuple(str, str) and two types of value: str, tuple(str, str)
Usage: used to handle cases that require 1-to-1 correction for unique cases, such as typo, flipped format, changed name, etc.
'''
def manual_check(row: pd.DataFrame) -> pd.DataFrame: 

    tuple_key = (row["name_new"], row["date_of_birth"])
    str_key = row["name_new"]

    if tuple_key in manual_handle_dict:
        if type(manual_handle_dict[tuple_key]) is tuple:
            row["name_new"] = manual_handle_dict[tuple_key][0]
            row["date_of_birth"] = manual_handle_dict[tuple_key][1]
            return row
        if type(manual_handle_dict[tuple_key]) is str:
            row["name_new"] = manual_handle_dict[tuple_key]
            return row
    if str_key in manual_handle_dict:
        row["name_new"] = manual_handle_dict[str_key]
        return row

    return row

'''
Behavior: update the birthday of non-Korean players (follow BR)
Usage: used for pre-processing before the merge.
       ONLY FOR ST SIDE
'''
def eng_update_birthday(row: pd.DataFrame) -> pd.DataFrame:

    if row['name_eng'] in dob_dict_eng:
        row['date_of_birth'] = dob_dict_eng[row['name_eng']]

    return row

'''
Behavior: remove 'jr' if it exists at the end for non-Korean players.
Usage: used for pre-processing before the merge.
'''
def eng_remove_jr(name: str) -> str:
    
    name_split = name.split(" ")
    if "jr" in name_split[-1]:
        name_split = name_split[:-1]
        return ' '.join(name_split)
        
    return name

'''
Behavior: merge based on the fact that there are not very many non-Korean players, which lowers the change of having two players with the same last name.
          if the given last name only exists once on both side, it means there is a single player with that last name (therefore appears only once on each side).
Usage: first criterion for merging non-Korean players. Used in manual merge.
'''
def eng_handle_rare_last_name(row: pd.DataFrame, last_name_total: dict[str, int], last_name_st: dict[str, int], last_name_br: dict[str, int]) -> str:

    last_name = row['name_new'].split(" ")[-1]

    if last_name_total[last_name] == 2 and last_name_st[last_name] == 1 and last_name_br[last_name] == 1:
        return last_name + " (unique last name)"

    return row['name_new']


'''
Behavior: merge based on the fact that BR usually has a player's abbreviated name or nickname, while ST contains the full legal name.
          based on the length of given name, try several methods for possible matching.
Usage: second criterion for merging non-Korean players. Used in manual merge.
       ONLY WORKS FOR ST SIDE TRYING TO FIND A MATCH IN BR.
'''
def eng_check_possible_match(row: pd.DataFrame, br_candidates: set[str]) -> str:

    # if the english name doesn't contain '-', it is a Korean player.
    if "-" in row['name_eng_y']: 
        return row['name_new']

    name_split = row["name_new"].split(" ")
    

    # this is the case of no middle name for non-Korean players, or a single first name for Korean players.
    if len(name_split) == 2:

        # sometimes names are flipped (usually japanese players)
        name_candidate = name_split[-1] + " " + name_split[0]
        if name_candidate in br_candidates:
            return name_candidate
        

        # Korean players and non-mathcing cases for non-Korean players will be filtered here.
        if name_split[0] in first_name_dict_eng:
            name_split[0] = first_name_dict_eng[name_split[0]]
            name_candidate = ' '.join(name_split)
            
            # if the substituted name (possible nickname) exists, update it.
            if name_candidate in br_candidates:
                return name_candidate
        return row['name_new']

    # this is the case for players whose name contains the middle name.
    elif len(name_split) == 3:

        
        name_candidate_1 = name_split[0] + " " + name_split[-1] # first + last
        name_candidate_2 = name_split[0] + " " + name_split[1] # first + middle

        check_original = check_uniqueness(name_candidate_1, name_candidate_2, row['name_new'], br_candidates)

        # if only one of them exists, return it.
        if check_original != row['name_new']:
            return check_original

        # if both or neither exists, try the same with the first name's possible nickname.
        if name_split[0] in first_name_dict_eng:

            name_split[0] = first_name_dict_eng[name_split[0]]
            name_candidate_1 = name_split[0] + " " + name_split[-1]
            name_candidate_2 = name_split[0] + " " + name_split[1]
            
            return check_uniqueness(name_candidate_1, name_candidate_2, row['name_new'], br_candidates)
    
        else:
            return row['name_new']

    # players from latin-america often have the full names with length 4.
    elif len(name_split) == 4:
        # check the first and third name in BR (the most common case)
        name_candidate = name_split[0] + " " + name_split[2]
        if name_candidate in br_candidates:
            return name_candidate

        return row['name_new']
        
    else:
        return row['name_new']


'''
Behavior:
    1. separate 'outer' into BR and ST (the rows that failed to find its match)
    2. apply manipulation based on 'criterion'.
    3. try merging and concatenate the outcome to 'inner'.
Usage: used for manual merge after the first merge.
'''
def manual_merge(inner: pd.DataFrame, outer: pd.DataFrame, criterion: Callable[[pd.DataFrame, set[str]], str]) -> tuple[pd.DataFrame, pd.DataFrame]:

    # generate new starting points for the next merge.
    df_br = outer[outer['name_eng_y'].isna()].dropna(axis=1)
    df_st = outer[outer['name_eng_x'].isna()].dropna(axis=1)

    # then update those with given criterion.

    # option 1
    if criterion.__name__ == 'kor_handle_u':

        df_br_set = set(df_br["name_new"].to_list())
        df_st_set = set(df_st["name_new"].to_list())
        
        df_br['name_new'] = df_br.apply(kor_handle_u, args=(df_st_set,), axis=1)
        df_st['name_new'] = df_st.apply(kor_handle_u, args=(df_br_set,), axis=1)

    # option 2
    elif criterion.__name__ == 'eng_handle_rare_last_name':

        last_name_total, last_name_st, last_name_br = defaultdict(int), defaultdict(int), defaultdict(int)

        for name in df_br['name_new'].to_list():
            last_name = name.split(" ")[-1]
            last_name_total[last_name] += 1
            last_name_br[last_name] += 1

        for name in df_st['name_new'].to_list():
            last_name = name.split(" ")[-1]
            last_name_total[last_name] += 1
            last_name_st[last_name] += 1
        
        df_br['name_new'] = df_br.apply(eng_handle_rare_last_name, args=(last_name_total, last_name_st, last_name_br), axis=1)
        df_st['name_new'] = df_st.apply(eng_handle_rare_last_name, args=(last_name_total, last_name_st, last_name_br), axis=1)        

    # option 3
    elif criterion.__name__ == 'eng_check_possible_match':
        df_br_set = set(df_br["name_new"].to_list())
        df_st['name_new'] = df_st.apply(eng_check_possible_match, args=(df_br_set,), axis=1)
    
    else:
        raise SystemExit('Not a valid criterion function name')

    
    # merge the updated tables and concatenate its outome to the original merged table.
    new_inner = pd.merge(df_br, df_st, on=['name_new', 'date_of_birth'], how='inner')
    new_outer = pd.merge(df_br, df_st, on=['name_new', 'date_of_birth'], how='outer')
    new_outer = new_outer[new_outer.isna().any(axis=1)]

    return pd.concat([inner, new_inner], axis=0), new_outer

    

    

    







        

    



        



        