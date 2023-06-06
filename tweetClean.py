#!/usr/bin/env python
# -*- coding: utf-8 -*-
#cleaning benchmark dataset
import pandas as pd
import numpy as np
import re
from Loggers import LogerClass

#load log
logger = LogerClass()

#The number of classes we will use
CLASS_NUM = 10

#cleaning emoji and some special chars, like url, username, hashtag and blank
def cleaningEmojiChars(line_twitter):
    line_twitter = str(line_twitter)
    line_twitter = line_twitter.encode('ascii', 'ignore').decode('ascii')
    line_twitter = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', line_twitter) # remove URLs #URL
    line_twitter = re.sub('@[^\s]+', 'AT_USER', line_twitter) # remove usernames #AT_USER
#     line_twitter = re.sub(r'#([^\s]+)', r'', line_twitter) # remove the # in #hashtag
    line_twitter = re.sub(r'pic.twitter.com/([^\s]+)', r'', line_twitter)
    line_twitter = line_twitter.replace('\n', ' ').replace('URL', ' ').replace('AT_USER', ' ').replace('|', ' ').replace('&amp;', '').replace('#', ' ').strip()
    line_twitter = re.sub(' +', ' ', line_twitter)
    return line_twitter

#read data from original data and then clean them and next write them into files
def cleaningBenchmark(ori_path, des_path):
    x_data = pd.read_csv(ori_path)
    x_data['Tweet'] = x_data['Tweet'].apply(lambda x : cleaningEmojiChars(x))
    x_data.to_csv(des_path, index=False)
    logger.info('Data have been cleaned!')

def loadData(ori_data_path, clean_data_path):
    cleaningBenchmark(ori_data_path, clean_data_path)
    data_df = pd.read_csv(clean_data_path)
    if CLASS_NUM == 11:
        head = ["Optimistic", "Thankful", "Empathetic","Pessimistic","Anxious","Sad","Annoyed","Denial","Official report","Joking"]
        data_df['labels'] = list(zip(data_df[head[0]].tolist(), data_df[head[1]].tolist(), data_df[head[2]].tolist(), data_df[head[3]].tolist(),
                        data_df[head[4]].tolist(), data_df[head[5]].tolist(), data_df[head[6]].tolist(), data_df[head[7]].tolist(),
                        data_df[head[8]].tolist(), data_df[head[9]].tolist(), data_df[head[10]].tolist()))
    else:
        head = ['label']
        data_df['labels'] = list(data_df[head[0]].tolist())
    data_df['text'] = data_df['Tweet'].apply(lambda x: x.replace('\n', ' '))
    return data_df
