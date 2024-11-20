import pandas as pd
from typing import Callable, Union
from helper.ref_dict import last_name_dict_kor, first_name_dict_kor, first_name_dict_eng, manual_handle_dict, recover_dash_dict
from collections import defaultdict


def recover_dash(name: str) -> str:
    if name in recover_dash_dict:
        return recover_dash_dict[name]
    return name

def remove_double_dash(name: str) -> str:

    
    if name in recover_dash_dict:
        return recover_dash_dict[name]
    return name

def check_uniqueness(candidate_1: str, candidate_2: str, default_return: str, checker: set[str]) -> str:

    if candidate_1 in checker and candidate_2 in checker:
        print(f"given name: {default_return} -> both exist")
        return default_return
    if candidate_1 not in checker and candidate_2 not in checker:
        print(f"given name: {default_return} -> neither exists")
        return default_return
    if candidate_1 in checker:
        print(f"given name: {default_return} -> found the unique match")
        return candidate_1
    if candidate_2 in checker:
        print(f"given name: {default_return} -> found the unique match")
        return candidate_2

'''
Helper function 1
Behavior: Parse the given name and return the first and last name (in terms of word, not character) -> use it for English name only.
Usage: used to extract first and last name of non-Korean players, which resolved a decent amount of naming conflict.
'''

def eng_get_first_and_last(name: str) -> str:
    split = name.split(" ")

    # 'jr' is not helpful for distinguishing players
    if 'jr' in split[-1]:
        split = split[-1]
    
    if len(split) > 2:
        return split[0] + " " + split[-1]
    else:
        return " ".join(split)



'''
Helper function 2
Behavior: Parse the given full name and return the last name (in terms of character, not word) -> use it for Korean name only.
Usage: used to check if players with rare last name exist (otherwise merge them into the common notation for that last name to resolve naming conflict)
'''
def kor_get_last(name_kor_list: list[str], last_name: str) -> list[str]:
    found = list()
    for name in name_kor_list:
        if name[0] == last_name:
            found.append(name)
    return found


'''
Helper function 3
Behavior: Parse the given full name and check if the last name is in the last_name_dict_kor for generalization (a consistent notation for last names), and if so, update it.
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
Helper function 4
Behavior: Parse the given full name and check if the first name is in the first_name_dict for generalization (a consistent notation for first names), and if so, update it.
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
Helper function 5
Usage: specifically handling 'u'
'''
def kor_handle_u(row: pd.DataFrame, candidates: set[str]) -> str:

    name_split = row['name_new'].split(" ")
    
    # remove the last name
    if len(name_split) > 1:
        first_name_split = name_split[:-1]

        # 'eu' is fine, it has only 1 matching pronuncation ('ㅡ')
        # if the first name has more than 1 Korean character, need to check if there are several 'u's.
        # if there is no 'u' or more than 1 'u', cannot handle it -> return the original value.
        if len(first_name_split) > 1:
            count = 0
            for name in first_name_split:
                if 'u' in name and 'eu' not in name:
                    count += 1
            if not count:
                # print(f"given name: {row['name_new']} -> at least than 2 charcters, no 'u'")
                return row['name_new']
            if count == len(first_name_split):
                print(f"given name: {row['name_new']} -> at least than 2 charcters, all 'u' (count: {count})")
                return row['name_new']
        else:
            if 'u' not in first_name_split[0]:
                # print(f"given name: {row['name_new']} -> 1 character with no 'u'")
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

                # print(f"given name: {row['name_new']} -> oo: {first_name_copy_oo}, eo: {first_name_copy_eo}")

                # if first_name_copy_oo not in candidates and first_name_copy_eo not in candidates:
                #     print(f"given name: {row['name_new']} -> neither exists")
                #     return row['name_new']
                # if first_name_copy_oo in candidates and first_name_copy_eo in candidates:
                #     print(f"given name: {row['name_new']} -> both exist")
                #     return row['name_new']
                # if first_name_copy_oo in candidates:
                #     print(f"given name: {row['name_new']} -> found the unique match")
                #     return first_name_copy_oo
                # if first_name_copy_eo in candidates: 
                #     print(f"given name: {row['name_new']} -> found the unique match")
                #     return first_name_copy_eo

                return check_uniqueness(first_name_copy_oo, first_name_copy_eo, row['name_new'], candidates)

        # print(f"given name: {row['name_new']} -> what case is this???") -> never happens

    return row['name_new']
    
    
def manual_check(name: str) -> str: 

    if name in manual_handle_dict:
        return manual_handle_dict[name]

    return name

def eng_remove_jr(name: str) -> str:
    
    name_split = name.split(" ")
    if "jr" in name_split[-1]:
        name_split = name_split[:-1]
        return ' '.join(name_split)
        
    return name


def eng_handle_rare_last_name(row: pd.DataFrame, last_name_total: dict[str, int], last_name_st: dict[str, int], last_name_br: dict[str, int]) -> str:

    last_name = row['name_new'].split(" ")[-1]

    # if the last name only appears once per each side and therefore total of 2, then it is a single player with that last name.
    if last_name_total[last_name] == 2 and last_name_st[last_name] == 1 and last_name_br[last_name] == 1:
        return last_name + " (unique last name)"

    return row['name_new']

# only works from the statiz side, because it made sure that all Korean players has '-' in their name (single first name doesn't apply, but still can be handled by checking the number of letters inside the function)
# use dict unlike handle u function, because non-Korean players
def eng_check_possible_match(row: pd.DataFrame, br_candidates: set[str]) -> str:

    # if the english name doesn't contain '-', it is a Korean player.
    if "-" in row['name_eng_y']: 
        # print(f"given name: {row['name_new']} -> not a valid input")
        return row['name_new']

    name_split = row["name_new"].split(" ")
    

    # this is the case of no middle name for non-Korean players, or a single first name for Korean players.
    if len(name_split) == 2:

        # sometimes names are flipped (usually japanese players)
        name_candidate = name_split[-1] + " " + name_split[0]
        if name_candidate in br_candidates:
            print(f"given name: {row['name_new']} -> found the unique match")
            return name_candidate
        

        # Korean players and non-mathcing cases for non-Korean players will be filtered here.
        if name_split[0] in first_name_dict_eng:
            name_split[0] = first_name_dict_eng[name_split[0]]
            name_candidate = ' '.join(name_split)
            
            # if the substituted name exists, up date it.
            if name_candidate in br_candidates:
                print(f"given name: {row['name_new']} -> found the unique match")
                return name_candidate
        return row['name_new']

    elif len(name_split) == 3:

        
        name_candidate_1 = name_split[0] + " " + name_split[-1]
        name_candidate_2 = name_split[0] + " " + name_split[1]

        check_original = check_uniqueness(name_candidate_1, name_candidate_2, row['name_new'], br_candidates)

        if check_original != row['name_new']:
            return check_original

        if name_split[0] in first_name_dict_eng:

            name_split[0] = first_name_dict_eng[name_split[0]]
            name_candidate_1 = name_split[0] + " " + name_split[-1]
            name_candidate_2 = name_split[0] + " " + name_split[1]
            
            return check_uniqueness(name_candidate_1, name_candidate_2, row['name_new'], br_candidates)

        else:
            return row['name_new']


        # if name_candidate_1 not in br_candidates and name_candidate_2 not in br_candidates:
        #     print(f"given name: {row['name_new']} -> neither exists, repeat the same with nicknames")

        #     if name_split[0] in first_name_dict_eng:
        #         name_candidate_1[0] = first_name_dict_eng[name_split[0]]
        #         name_candidate_2[0] = first_name_dict_eng[name_split[0]]
                
            
        #     return row['name_new']
        # if name_candidate_1 in br_candidates and name_candidate_2 in br_candidates:
        #     print(f"given name: {row['name_new']} -> both exist")
        #     return row['name_new']
        # if name_candidate_1 in br_candidates:
        #     potential_dup = name_candidate_1.split(" ")
        #     if potential_dup[0] in first_name_dict_eng:
        #         potential_dup[0] = first_name_dict_eng[potential_dup[0]]
        #         potential_dup = ' '.join(potential_dup)
        #         if potential_dup in br_candidates:
        #             print(f"given name: {row['name_new']} -> potential dup (nickname) exists!!!!!!!!!!")
        #             return row['name_new']
        #     print(f"given name: {row['name_new']} -> found the unique match")
        #     return name_candidate_1        
        # if name_candidate_2 in br_candidates:
        #     potential_dup = name_candidate_2.split(" ")
        #     if potential_dup[0] in first_name_dict_eng:
        #         potential_dup[0] = first_name_dict_eng[potential_dup[0]]
        #         potential_dup = ' '.join(potential_dup)
        #         if potential_dup in br_candidates:
        #             print(f"given name: {row['name_new']} -> potential dup (nickname) exists!!!!!!!!!!")
        #             return row['name_new']
        #     print(f"given name: {row['name_new']} -> found the unique match")
        #     return name_candidate_2  
            
    elif len(name_split) == 4:
        name_candidate = name_split[0] + " " + name_split[2]
        if name_candidate in br_candidates:
            print(f"given name: {row['name_new']} -> found the unique match")
            return name_candidate

        return row['name_new']
        
    
    else:
        print(f"given name: {row['name_new']} -> has not been implemented yet")
        return row['name_new']


def manual_merge(inner: pd.DataFrame, outer: pd.DataFrame, criterion: Callable[[pd.DataFrame, set[str]], str]) -> tuple[pd.DataFrame, pd.DataFrame]:

    df_br = outer[outer['name_eng_y'].isna()].dropna(axis=1)
    df_st = outer[outer['name_eng_x'].isna()].dropna(axis=1)


    if criterion.__name__ == 'kor_handle_u':

        df_br_set = set(df_br["name_new"].to_list())
        df_st_set = set(df_st["name_new"].to_list())
        
        df_br['name_new'] = df_br.apply(kor_handle_u, args=(df_st_set,), axis=1)
        df_st['name_new'] = df_st.apply(kor_handle_u, args=(df_br_set,), axis=1)

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

    elif criterion.__name__ == 'eng_check_possible_match':
        df_br_set = set(df_br["name_new"].to_list())
        df_st['name_new'] = df_st.apply(eng_check_possible_match, args=(df_br_set,), axis=1)
    
    else:
        raise SystemExit('Not a valid criterion function name')
    
    
    new_inner = pd.merge(df_br, df_st, on='name_new', how='inner')
    new_outer = pd.merge(df_br, df_st, on='name_new', how='outer')
    # new_outer = new_outer.drop(columns=['url'])
    new_outer = new_outer[new_outer.isna().any(axis=1)]

    return pd.concat([inner, new_inner], axis=0), new_outer

    

    

    







        

    



        



        