# SenWave: The Multi-Language Fine-Grained Sentiment Analysis Dataset for COVID-19 Tweets
This dataset is used for the resource paper submission of NeurPIS 2023, which contains the multiple-language labeled tweets and a large scale of the unlabeled tweet IDs for fine-grained sentimental analysis about Covid-19. The labeled tweets were organized in two languages (English and Arabic both with 10K) while the unlabeled tweet IDs were represented with only IDs to comply with Twitter’s Terms of Service in five languages (English, Arabic, Spanish, French, and Italian in Tweets). In order to make use of the labeled data as much as possible, we utilize Google translate(https://translate.google.com/) to translate the labeled English tweets into Spanish, French, and Italian. The translated tweets are in good quality with $0.33$ Bleu Score. The twitter data was collected from March 1, 2020 with Twint(https://github.com/twintproject/twint). These data is only released for non-commercial research use.

# Data Organization
The tweet IDs are organized as follows:
1) The IDs are seperated on the five languages;
2) In each language file, it stores the tweet IDs from March 1, 2020 to May 15, 2020, which are divided line by line.
3) The statistics of each language tweet IDs are shown in file lan_count.txt where first col represents the date while the second col shows the number of tweets in the corresponding day.
4) Each Txt file named as covid19_tweet_id_date.txt stores the tweet IDs.
5) The file statistics.txt counts the statistics of each language including the language, total size of this language, and the ratio in the all languages.

For the labeled tweets, we store them in the filefolder called labeledTweets where they are organized in five CSV files where English tweets and Arabic tweets are originally annoted by experienced annotators and other three language tweets are translated with Google Translate from English tweets. The size of each kind of language tweets are all 10K. There are 10 emotions including "Optimistic", "Thankful", "Empathetic", "Pessimistic", "Anxious", "Sad", "Annoyed", "Denial", "Official report", and "Joking". The data cleaning code is attached in tweetClean.py. We remove any information about users for privacy protection.

# Data Usage Agreement
This dataset complies with Twitter’s Terms of Service. If you use this dataset, this means that you agree with the license and term of Twitter.

# Statistics Summary
The total number of tweets is 104, 830, 630. The tweets will be updated furthermore. In addition, the unlabeded Chinese data will be released soon whose size is about 1 million.
The statistics of five language tweets are shown in the following table:


|Language      |Size      |Ratio      |
| ---------- | :-----------:  | :-----------: |
|En      |68532070      |0.6537408961483872      |
|Es       |20755900       |0.1979946128340543      |
|Ar       |7957489      | 0.07590805282768977      |
|Fr       |4900973       |0.04675134547984687      |
|It       |2684198       |0.02560509271002187      |


# Scope of data usage

The SenWave dataset offers a unique resource for various sentiment analysis tasks, such as public opinion analysis and stock market forecast which convey complex sentiments. Besides, researchers can utilize this dataset to explore sentiment dynamics across different languages, investigate cultural variations in emotional responses to the pandemic, identify sentiment triggers, and assess the impact of sentiment on public health behaviors and policy decisions.
