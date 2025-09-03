import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re


# Setting up the Streamlit page
st.title("Distribuição de Sentimentos no Piauí - Inteligência Artificial")
st.write("Gráfico de pizza mostrando a distribuição dos sentimentos (Positivo, Negativo, Neutro) com base nos dados fornecidos.")

# Loading and processing the CSV data
@st.cache_data
def load_data():
    data = pd.read_csv("../data/processed/analise_sentimentos.csv")
    return data

# Counting sentiments
def process_data(data):
    sentiment_counts = data['Sentimento'].value_counts()
    return sentiment_counts

# Creating the pie chart
def create_pie_chart(sentiment_counts):
    fig, ax = plt.subplots()
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    return fig

# Main execution
data = load_data()
sentiment_counts = process_data(data)

# Displaying the pie chart
st.pyplot(create_pie_chart(sentiment_counts))

# Displaying the raw counts
st.write("Contagem de Sentimentos:")
st.write(sentiment_counts)


# Loading the CSV data
@st.cache_data
def load_data():
    data = pd.read_csv("../data/processed/analise_sentimentos.csv")
    return data

st.write("Esta análise de sentimentos é baseada em um database com poucos dados, por tanto a falta de sentimentos negativos se deve aos falta de um maior volume dados disponíveis")


# Preprocessing text for word cloud
def preprocess_text(text):
    # Convert to lowercase and remove special characters
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text


# Generating word cloud
def generate_word_cloud(text_data):
    # Common Portuguese stopwords
    stopwords = {
        'a', 'o', 'e', 'de', 'do', 'da', 'em', 'para', 'com', 'no', 'na',
        'que', 'é', 'as', 'os', 'um', 'uma', 'dos', 'das', 'se', 'por',
        'nesta', 'neste', 'ao', 'à', 'pelo', 'pela'
    }

    # Preprocess and split into words
    words = []
    for text in text_data:
        cleaned_text = preprocess_text(text)
        words.extend([word for word in cleaned_text.split() if word not in stopwords])

    # Count word frequencies
    word_counts = Counter(words)

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white', min_font_size=10).generate_from_frequencies(
        word_counts)

    return wordcloud


# Main Streamlit app
def main():
    st.title("Análise de Sentimentos - Nuvem de Palavras e Tabela Interativa")

    # Load data
    df = load_data()

    # Display word cloud
    st.subheader("Nuvem de Palavras dos Títulos")
    wordcloud = generate_word_cloud(df['title'])
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    # Display interactive table
    st.subheader("Tabela Interativa de Dados")
    st.dataframe(df, use_container_width=True)

# Nuvem de palavras (código existente, com pré-processamento)
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

stopwords = {'a', 'o', 'e', 'de', 'do', 'da', 'em', 'para', 'com', 'no', 'na', 'que', 'é', 'as', 'os', 'um', 'uma', 'dos', 'das', 'se', 'por', 'nesta', 'neste', 'ao', 'à', 'pelo', 'pela'}
words = []
df = pd.read_csv('../data/processed/analise_sentimentos.csv')
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