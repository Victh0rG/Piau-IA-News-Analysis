import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re
from src.sentiment_analysis import analyze_sentiments  # Importe se precisar reanalisar

st.title("Análise de Sentimentos no Piauí - Inteligência Artificial")

# Carrega dados processados
df = pd.read_csv('data/processed/analise_sentimentos.csv')

# Gráfico de pizza (código existente mantido)
sentiment_counts = df['Sentimento'].value_counts()
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
ax.axis('equal')
st.pyplot(fig)

st.write("Contagem de Sentimentos:")
st.write(sentiment_counts)
st.write("Esta análise de sentimentos é baseada em um database com poucos dados, por tanto a falta de sentimentos negativos se deve aos falta de um maior volume dados disponíveis")


# Nuvem de palavras (código existente, com pré-processamento)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

stopwords = {'a', 'o', 'e', 'de', 'do', 'da', 'em', 'para', 'com', 'no', 'na', 'que', 'é', 'as', 'os', 'um', 'uma', 'dos', 'das', 'se', 'por', 'nesta', 'neste', 'ao', 'à', 'pelo', 'pela'}
words = []
for text in df['title']:
    cleaned = preprocess_text(text)
    words.extend([word for word in cleaned.split() if word not in stopwords])
word_counts = Counter(words)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

st.subheader("Tabela Interativa")
st.dataframe(df, use_container_width=True)