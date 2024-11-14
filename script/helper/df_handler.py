import pandas as pd
from typing import Callable, Union
from helper.ref_dict import last_name_dict_kor, first_name_dict_kor, manual_handle_dict

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

                if first_name_copy_oo not in candidates and first_name_copy_eo not in candidates:
                    print(f"given name: {row['name_new']} -> neither exists")
                    return row['name_new']
                if first_name_copy_oo in candidates and first_name_copy_eo in candidates:
                    print(f"given name: {row['name_new']} -> both exist")
                    return row['name_new']
                if first_name_copy_oo in candidates:
                    return first_name_copy_oo
                if first_name_copy_eo in candidates:
                    return first_name_copy_eo

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


# def eng_handle_rare_last_name(row: pd.DataFrame,  



def manual_merge(inner: pd.DataFrame, outer: pd.DataFrame, criterion: Callable[[pd.DataFrame, set[str]], str]) -> tuple[pd.DataFrame, pd.DataFrame]:

    df_br = outer[outer['name_eng_y'].isna()].dropna(axis=1)
    df_st = outer[outer['name_eng_x'].isna()].dropna(axis=1)
    df_br_set = set(df_br["name_new"].to_list())
    df_st_set = set(df_st["name_new"].to_list())
    # print(df_br.head(3))
    # print(df_st.head(3))

    if criterion.__name__ == 'kor_handle_u':
        df_br['name_new'] = df_br.apply(kor_handle_u, args=(df_st_set,), axis=1)
        df_st['name_new'] = df_st.apply(kor_handle_u, args=(df_br_set,), axis=1)
        print('successful calling function')
    
    
    new_inner = pd.merge(df_br, df_st, on='name_new', how='inner')
    new_outer = pd.merge(df_br, df_st, on='name_new', how='outer')
    # new_outer = new_outer.drop(columns=['url'])
    new_outer = new_outer[new_outer.isna().any(axis=1)]

    return pd.concat([inner, new_inner], axis=0), new_outer

    

    

    







        

    



        



        