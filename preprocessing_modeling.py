
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
    Dummy : List[List[int]] = field(
        default=None,
        metadata={"help": "A list of names of categorical columns to treat as dummy variable"},
    )        
    Embedding : List[List[int]] = field(
    default=None,
    metadata={"help": "A list of names of dummy columns to treat as embeddeding variable"},
    )        

logger = logging.getLogger(__name__)        

def embedding(lst, data): 
    dict_ls = []
    embedding_df = pd.DataFrame()
    for embedding_list in lst:
        merged_list = pd.concat([data[col] for col in embedding_list], ignore_index=True)
        unique_lst = list(set(merged_list))
        label_encoder = LabelEncoder()
        encode = label_encoder.fit_transform(unique_lst)
        encode_dict = {element: encoded_value for element, encoded_value in zip(unique_lst, encode)}
        dict_ls.append(encode_dict)
        lst_df = pd.DataFrame()
        for i in embedding_list: 
            lst_df[f'{i}'] = res[f'{i}'].map(encode_dict)
        embedding_df = pd.concat([embedding_df,lst_df], axis=1)
    
    return embedding_df, dict_ls

def dummy(lst, data): 
#     dict_ls = []
    dummy_df = pd.DataFrame()
    for dummy_list in lst:
        for i in lst:
            dummy_cols = pd.get_dummies(data[i], prefix=i)
            dummy_df = pd.concat([dummy_df, dummy_cols], axis=1)
    return dummy_df

print("you working?")
print("you working?")
print("for sure?")
print("study session")
# def preprocess(data, Continuous, Character, Embedding, Dummy):
# let's push by function 
