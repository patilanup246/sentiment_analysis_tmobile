# Set Directory
import os
os.chdir('C:/Users/A716833/Downloads/Sentiment_Analysis-NLP')


# In[1]: Login to facebook

from Functions import login
#login()


# In[2]: Scrap Data
# Load UDF to Scrap: O/p .html scrap file
from Functions import scrapData
scrapData("https://www.facebook.com/pg/TMobile/community/?ref=page_internal",'T-Mobile_reviews.html')


# In[3]: Fetch Review
# Load UDF to fetch reviews: O/p .txt file
from Functions import fetchReview
reviews_Tmobile = fetchReview("T-Mobile_reviews.html",'review_data_T-Mobile.txt')

from Functions import fetchReviewTwitter
reviews_TmobileTwitter=fetchReviewTwitter()

# In[4]: Analyze review
# Compare with pre-defined +/- words
from Functions import directData
reviews_prediction_Tmobile = directData(reviews_Tmobile)
reviews_prediction_TmobileTwitter = directData(reviews_TmobileTwitter)

# import ast
# reviews_TmobileTwitter=[]
# filepathlang = 'C:/Users/Dell/Downloads/twitter.txt'
# with open(filepathlang, encoding='utf-8') as fpl:
#     for cntlag, linelag in enumerate(fpl):
#         reviews_TmobileTwitter.append(linelag)
#
# reviews_prediction_TmobileTwitter = directData(reviews_TmobileTwitter)

# In[5]: Vader Analysis

# Get +/- rating for each review
from Functions import sentiment_analysis_VADERAnalyser
summary_Tmobile,sentences_Tmobile,label_Tmobile=sentiment_analysis_VADERAnalyser(reviews_Tmobile)
summary_TmobileTwitter,sentences_TmobileTwitter,label_TmobileTwitter=sentiment_analysis_VADERAnalyser(reviews_TmobileTwitter)


from Functions import ExportCSV
ExportCSV(sentences_Tmobile,label_Tmobile,"Facebook")
ExportCSV(sentences_TmobileTwitter,label_TmobileTwitter,"Twitter")
# In[6]: Plot Analysis

# Bar graph for +/-/0 reviews
from Functions import plot_Sentiment
plot_Sentiment(summary_Tmobile, 'T-Mobile Facebook')
plot_Sentiment(summary_TmobileTwitter, 'T-Mobile Twitter')

# In[8]: Clean Sentences

from Functions import cleanup_data
clean_sentences_Tmobile = cleanup_data(sentences_Tmobile)
clean_sentences_TmobileTwitter = cleanup_data(sentences_TmobileTwitter)
