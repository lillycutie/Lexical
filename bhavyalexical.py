# -*- coding: utf-8 -*-
"""Copy of Bhavyastnb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IJgimON1w4eiaMBlXkYOs4LbUpwlgyP2
"""

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="pszemraj/t5-large-for-lexical-analysis")

import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("pszemraj/t5-large-for-lexical-analysis")
model = TFAutoModelForSeq2SeqLM.from_pretrained("pszemraj/t5-large-for-lexical-analysis")

import streamlit as st

import re

def tokenize(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

def main():
    st.title("Lexical Analyzer")

    # Input text area
    text = st.text_area("Enter text for lexical analysis:")

    if st.button("Analyze"):
        tokens = tokenize(text)

        st.header("Tokenized Text:")
        st.write(tokens)

if __name__ == "__main__":
    main()