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

# ---------------------------------------
# Optional: Provide a downloadable sample
# ---------------------------------------
st.markdown("### 📁 Example File")
try:
    # Open the sample file and provide a download button
    with open("sample_news.txt", "r", encoding="utf-8") as file:
        sample_text = file.read()
        st.download_button(
            label="📥 Download Sample TXT File",
            data=sample_text,
            file_name="sample_news.txt",
            mime="text/plain"
        )
except FileNotFoundError:
    st.warning("⚠️ Sample file not found. Please make sure 'sample_news.txt' is in the same directory.")

# -------------------------------
# Upload user-provided news file
# -------------------------------
uploaded_file = st.file_uploader("📎 Upload a text file (.txt) containing news content", type=["txt"])

# If a file is uploaded
if uploaded_file is not None:
    # Read the content of the file as a string
    text = uploaded_file.read().decode("utf-8")
    
    # Show a preview of the uploaded text
    st.subheader("📄 News Content Preview")
    st.text_area("📝 Original Text", text, height=200)

    # ---------------------------
    # Sentiment Analysis Section
    # ---------------------------
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

# If no file has been uploaded yet
else:
    st.info("📥 Please upload a text file containing company crisis news for analysis.")
