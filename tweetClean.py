#!/usr/bin/env python
# -*- coding: utf-8 -*-
#cleaning benchmark dataset
import pandas as pd
import numpy as np
import re
try:
    from Loggers import LogerClass
    logger = LogerClass()
except ImportError:  # Fallback to standard logging if custom logger is unavailable
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


# Emotion columns present in the labeled dataset
EMOTION_COLS = [
    "Optimistic",
    "Thankful",
    "Empathetic",
    "Pessimistic",
    "Anxious",
    "Sad",
    "Annoyed",
    "Denial",
    "Official report",
    "Joking",
]

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
    """Load data from ``ori_data_path``, clean it, and return a ``DataFrame``.

    If the cleaned data contains the :data:`EMOTION_COLS`, they are combined
    into a tuple stored in the ``labels`` column. Otherwise a ``label`` column
    is expected. The cleaned tweets are stored in ``text``.
    """

    cleaningBenchmark(ori_data_path, clean_data_path)
    data_df = pd.read_csv(clean_data_path)

    if set(EMOTION_COLS).issubset(data_df.columns):
        # Multi-label format
        data_df["labels"] = list(
            zip(*(data_df[col].tolist() for col in EMOTION_COLS))
        )
    elif "label" in data_df.columns:
        data_df["labels"] = list(data_df["label"].tolist())
    else:
        raise KeyError("Expected 'label' or emotion columns in data")

    data_df["text"] = data_df["Tweet"].apply(lambda x: x.replace("\n", " "))
    return data_df
