# %%writefile preprocessing_modeling.py  

import datetime as dt
import pandas as pd 
import logging
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from sklearn.preprocessing import LabelEncoder

@dataclass
class Preprocess:
    Continuous : list[str] = field(
        default=None,
        metadata={"help": "A list of names of continuous columns"},
    )
    Character : list[str] = field(
    default=None,
    metadata={"help": "A list of names of character columns"},
    )
    Dummy : List[List[str]] = field(
        default=None,
        metadata={"help": "A list of names of categorical columns to treat as dummy variable"},
    )        
    Embedding : List[List[str]] = field(
    default=None,
    metadata={"help": "A list of names of dummy columns to treat as embeddeding variable"},
    )        

logger = logging.getLogger(__name__)        

def embedding_func(form, data): 
    dict_ls = []
    embedding_df = pd.DataFrame()
    
    for i in form.Embedding:
        merged_list = pd.concat([data[col] for col in i], ignore_index=True)
        unique_lst = list(set(merged_list))
        label_encoder = LabelEncoder()
        encode = label_encoder.fit_transform(unique_lst)
        encode_dict = {element: encoded_value for element, encoded_value in zip(unique_lst, encode)}
        dict_ls.append(encode_dict)
        lst_df = pd.DataFrame()
        for j in i: 
            lst_df[f'{j}'] = data[f'{j}'].map(encode_dict)
        embedding_df = pd.concat([embedding_df,lst_df], axis=1)
    
    return embedding_df, dict_ls

def dummy_func(form, data): 
#     dict_ls = []
    dummy_df = pd.DataFrame()
    for i in form.Dummy:
        dummy_cols = pd.get_dummies(data[i], prefix=i)
        dummy_df = pd.concat([dummy_df, dummy_cols], axis=1)
    return dummy_df

def concat_lst(lstlst):
    concat_lst = []
    for lst in lstlst: 
        concat_lst.extend(lst)
    return concat_lst

def embed_dict(preprocess,data):
    return embedding_func(preprocess, data)[1]

def preprocess_func(form, data):
    #Embedding과 Dummy가 아닌 친구들은 그대로 두고 
    if form.Embedding is not None and form.Dummy is not None:
        embed_lst = concat_lst(form.Embedding)
        dummy_lst = concat_lst(form.Dummy)
        lstlst = [embed_lst,dummy_lst]
        work_lst = concat_lst(lstlst) 
        lig_lst = data.columns.tolist()
        for i in work_lst: 
            lig_lst.remove(i)

        pre_df = data[lig_lst]

        #Embedding실행
    #     preprocess = Preprocess(Embedding=embedding, Dummy=dummy)
        embed_df, embed_dict = embedding_func(form, data)

        #Dummy실행
        dummy_df = dummy_func(form, data)
        #다같이 붙이기 
        if embed_df is not None:
            pre_df = pd.concat([pre_df, embed_df], axis=1)
        if dummy_df is not None:
            pre_df = pd.concat([pre_df, dummy_df], axis=1)
    else: 
        pre_df = data
    return pre_df

# def preprocess(data, Embedding, Dummy):
# let's push by function 
