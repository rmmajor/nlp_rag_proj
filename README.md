---
title: rag
app_file: main.py
sdk: gradio
sdk_version: 5.8.0
---
# RAG project for NLP course

1. Task this project aims to translate from English to French

2. Hosted service: 
 - huggingface spaces:  https://huggingface.co/spaces/Rmajor/rag
 - gradio: https://1f3b5ea8e182e47b3b.gradio.live

3. Source code: https://github.com/rmmajor/nlp_rag_proj

## How to run locally:
1. docker way: 
 - build with `docker build -t english-to-french-translator .
 - run with `docker run -p 7860:7860 english-to-french-translator`

2. local way:
 - run the script: `python main.py`
 