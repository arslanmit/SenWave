import os
import sys
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import tweetClean as tc


def test_cleaning_emoji_chars():
    sample = "This is a test @user http://example.com #hash pic.twitter.com/abc\n"
    cleaned = tc.cleaningEmojiChars(sample)
    assert cleaned == "This is a test hash"


def test_load_data(tmp_path):
    data = pd.DataFrame({
        "Tweet": ["hello @user http://example.com #tag"],
        "Optimistic": [1],
        "Thankful": [0],
        "Empathetic": [0],
        "Pessimistic": [0],
        "Anxious": [0],
        "Sad": [0],
        "Annoyed": [0],
        "Denial": [0],
        "Official report": [0],
        "Joking": [0],
    })
    ori = tmp_path / "input.csv"
    des = tmp_path / "clean.csv"
    data.to_csv(ori, index=False)
    df = tc.loadData(str(ori), str(des))
    assert df["text"].iloc[0] == "hello tag"
    assert df["labels"].iloc[0] == tuple([1,0,0,0,0,0,0,0,0,0])
