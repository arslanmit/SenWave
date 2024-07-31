# SenWave: A Fine-Grained Multi-Language Sentiment Analysis Dataset Sourced from COVID-19 Tweets
This dataset contains the labeled tweets and a large scale of the unlabeled tweet IDs for fine-grained sentimental analysis about COVID-19. The labeled tweets were organized in two languages (English and Arabic both with 10K) while the unlabeled tweet IDs were represented with only IDs to comply with Twitter’s Terms of Service in five languages (English, Arabic, Spanish, French, and Italian). In order to make use of the labeled data as much as possible, we utilize Google Translate (https://translate.google.com/) to translate the labeled English tweets into Spanish, French, and Italian as the data augmentation. The translated tweets are of good quality with a $0.33$ Bleu Score. The Twitter data was collected from March 1, 2020, with Twint(https://github.com/twintproject/twint). The dataset is licensed under Apache-2.0 license, which allows for the sharing and adaptation of the dataset under certain conditions. These data are only released for non-commercial research use. 


# Data Organization
The tweet IDs are organized as follows:
1) The IDs are separated into the five languages;
2) In each language file, it stores the tweet IDs from March 1, 2020, to May 15, 2020, which are divided line by line.
3) The statistics of each language tweet IDs are shown in file lan_count.txt where the first col represents the date while the second col shows the number of tweets on the corresponding day.
4) Each Txt file named covid19_tweet_id_date.txt stores the tweet IDs.
5) The file statistics.txt counts the statistics of each language including the language, total size of this language, and the ratio in all languages.

For the labeled tweets, we store them in the file folder called labeledTweets where they are organized in five CSV files where English tweets and Arabic tweets were originally annotated by experienced annotators, and the other three language tweets are translated with Google Translate from English tweets. The size of each kind of language tweet is 10K. There are 10 emotions including "Optimistic", "Thankful", "Empathetic", "Pessimistic", "Anxious", "Sad", "Annoyed", "Denial", "Official report", and "Joking". The data cleaning code is attached in tweetClean.py. We remove any information about users for privacy protection.

# Data Usage Agreement
This dataset complies with Twitter’s Terms of Service. If you use this dataset, this means that you agree with the license and terms of Twitter.

# Statistics Summary
The total number of tweets is 104, 830, 630. The tweets will be updated further.
The statistics of five language tweets are shown in the following table:


|Language      |Size      |Ratio      |
| ---------- | :-----------:  | :-----------: |
|En      |68532070      |0.6537408961483872      |
|Es       |20755900       |0.1979946128340543      |
|Ar       |7957489      | 0.07590805282768977      |
|Fr       |4900973       |0.04675134547984687      |
|It       |2684198       |0.02560509271002187      |


# Scope of Data Usage

The SenWave dataset offers a unique resource for various sentiment analysis tasks, such as public opinion analysis and stock market forecast which convey complex sentiments. Besides, researchers can utilize this dataset to explore sentiment dynamics across different languages, investigate cultural variations in emotional responses to the pandemic, identify sentiment triggers, and assess the impact of sentiment on public health behaviors and policy decisions.
