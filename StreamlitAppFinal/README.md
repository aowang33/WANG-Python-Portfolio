## 📉 Company Crisis News Sentiment Analyzer  
This is a simple and clean Streamlit web app designed to analyze the sentiment of news related to company crises. The app uses TextBlob for sentiment analysis and spaCy for Named Entity Recognition (NER), providing intuitive visualizations for both.

### 🧠 Background  
My academic background is in organizational crisis management. In this field, understanding how the public reacts to corporate crises is crucial. Natural Language Processing (NLP), especially sentiment analysis, plays a key role in tracking public opinion in news media. I developed this app to provide an accessible interface for analyzing the sentiment of crisis-related news. The integrated NER visualization further helps to clearly identify key entities in the news, aiding interpretation and analysis.

### 🔍 Features  
Text File Upload: Upload .txt files containing news articles or reports.

#### Sentiment Analysis:

Calculates polarity (positive–negative) and subjectivity (objective–subjective).

Displays interpretation of the sentiment result (positive / negative / neutral).

#### Visualization:

Bar chart of polarity and subjectivity scores.

Inline rendering of Named Entity Recognition results.

## 📸 Screenshots

### 📰 News Content Preview
![News Content Preview](images/News_content_preview.png)
### 📊 Sentiment Analysis
![Sentiment Analysis](images/sentiment_analysis.png)
### 🧠 Named Entity Recognition
![NER](images/NER.png)

## 🚀 How to Use

Sample File: A downloadable .txt file is provided for testing.

📁 File Structure 

📦 StreamlitAppFinal  
 ┣ 📄 main.py  
 ┣ 📄 sample_news.txt  
 ┣ 📁 images  
 ┃ ┣ 📄 news_content_preview.png  
 ┃ ┣ 📄 sentiment_analysis.png  
 ┃ ┗ 📄 ner.png  
 ┗ 📄 README.md  

🚀 How to Use
Run the Streamlit app:
streamlit run main.py
Upload a .txt file with news content.

View sentiment analysis results and named entities directly in the browser.