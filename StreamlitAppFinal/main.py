import streamlit as st
from textblob import TextBlob
import spacy
from spacy import displacy
import pandas as pd

# Load the English spaCy model for NLP tasks (like Named Entity Recognition)
nlp = spacy.load("en_core_web_sm")

# Set up the Streamlit page with a title and wide layout
st.set_page_config(page_title="Company Crisis News Sentiment Analyzer", layout="wide")

# Page title and description
st.title("📉 Company Crisis News Sentiment Analyzer")
st.markdown(
    "This tool analyzes public sentiment in news articles related to company crises. "
    "It also visualizes the Named Entity Recognition (NER) results to highlight people, organizations, locations, and more."
)

# -------------------------------
# Text input field with example content
# -------------------------------
example_text = """
On May 5, 2025, XYZ Corporation announced a significant layoff of 10% of its workforce due to economic downturns and declining sales. 
The CEO, John Doe, stated, "This was a difficult decision, but necessary to ensure the long-term stability of the company." 
The announcement was met with mixed reactions from employees and investors. While some analysts are optimistic that the company will recover, 
others fear that the layoffs might harm its public image and employee morale.

XYZ's stock price fell by 8% on the day of the announcement, reflecting the negative sentiment in the market. Investors are concerned about 
the company's ability to rebound after such a major decision. The company has been facing increasing competition from newer, tech-driven firms 
and has struggled to adapt its product offerings to meet changing consumer demands. Despite these challenges, the leadership team remains committed 
to driving growth and improving profitability over the next few quarters.
"""

# -------------------------------
# Upload file option
# -------------------------------
uploaded_file = st.file_uploader("📎 Upload a text file (.txt) containing news content", type=["txt"])

# If a file is uploaded, read its content
if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.subheader("📄 Uploaded News Content")
    st.text_area("📝 Original Text", text, height=200)
else:
    # If no file is uploaded, provide a text area for user input with example content
    text = st.text_area("📄 Enter News Content for Sentiment Analysis", example_text, height=200)

# ---------------------------
# Sentiment Analysis Section
# ---------------------------
if text:  # Only run sentiment analysis if text is provided
    st.subheader("💬 Sentiment Analysis Results")
    
    # Use TextBlob to perform sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment  # returns polarity (-1 to 1) and subjectivity (0 to 1)

    # Display numeric sentiment scores
    st.write(f"**Polarity**: {sentiment.polarity:.2f}")       # Positive vs. Negative
    st.write(f"**Subjectivity**: {sentiment.subjectivity:.2f}")  # Objective vs. Subjective

    # Give interpretation based on polarity value
    if sentiment.polarity > 0:
        st.success("🔍 Analysis: The sentiment is **positive**.")
    elif sentiment.polarity < 0:
        st.error("🔍 Analysis: The sentiment is **negative**.")
    else:
        st.info("🔍 Analysis: The sentiment is **neutral**.")

    # -------------------------------
    # Sentiment Visualization Section
    # -------------------------------
    st.subheader("📊 Sentiment Visualization")

    # Create a DataFrame for bar chart visualization
    sentiment_df = pd.DataFrame({
        "Sentiment Type": ["Polarity", "Subjectivity"],
        "Value": [sentiment.polarity, sentiment.subjectivity]
    }).set_index("Sentiment Type")

    # Display a bar chart
    st.bar_chart(sentiment_df)

    # -------------------------------
    # Named Entity Recognition (NER)
    # -------------------------------
    st.subheader("🧠 Named Entity Recognition (NER)")

    # Process the text with spaCy's NLP pipeline
    doc = nlp(text)

    # Render the NER visualization as HTML using spaCy's displacy
    html = displacy.render(doc, style="ent", page=True)

    # Embed the HTML into the Streamlit app
    st.components.v1.html(html, height=500, scrolling=True)

# If no text has been provided (neither from upload nor input)
else:
    st.info("📥 Please either upload a text file or enter news content related to a company crisis for analysis.")