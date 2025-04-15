import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy

# Set the page title
st.set_page_config(page_title="Custom NER App", layout="wide")
st.title("Custom Named Entity Recognition (NER) App")


# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Add EntityRuler and patterns
nlp.add_pipe("entity_ruler", before="ner")
ruler = nlp.get_pipe("entity_ruler")
ruler.add_patterns([
    {"label": "ORG", "pattern": "Tesla"},
    {"label": "GPE", "pattern": "USA"},
])

# Sample text
sample_text = "Where Does Tesla Face the Most Sales Risk: China, USA, or Europe?"

# User inputs or uploads text
st.subheader("Step 1: Input or upload text")
text_input_method = st.radio("Select input method：", ["Manual Input", "Upload File (.txt)"])

if text_input_method == "Manual Input":
    user_text = st.text_area("Please enter text：", sample_text, height=150)
else:
    uploaded_file = st.file_uploader("upload your own text：", type=["txt"])
    if uploaded_file is not None:
        user_text = uploaded_file.read().decode("utf-8")
    else:
        user_text = ""

st.subheader("Step 2: Add custom entity rules")
with st.form("entity_form"):
    label = st.text_input("entity lables (e.g. ORG, PRODUCT, LOCATION)")
    pattern = st.text_input("entity words（e.g. Tesla、USA）")
    submitted = st.form_submit_button("Add rules")

    if submitted and label and pattern:
        new_pattern = [{"label": label.upper(), "pattern": pattern}]
        ruler.add_patterns(new_pattern)
        st.success(f"Entities added：{label.upper()} -> '{pattern}'")

# ---- Process text and display the results ----
if user_text:
    st.subheader("Step 3: Entity recognition results")
    doc = nlp(user_text)

    # Highlight recognized entities
    html = displacy.render(doc, style="ent", minify=True, jupyter=False)
    st.markdown(
        f'<div style="background-color:#f9f9f9; padding:15px; border-radius:10px;">{html}</div>',
        unsafe_allow_html=True
    )

    # List recognized entities
    if doc.ents:
        st.subheader("Recognized entities: ")
        for ent in doc.ents:
            st.write(f"• **{ent.text}** — _{ent.label_}_")
    else:
        st.info("No entities recognized.")