import pandas as pd
import yaml
import logging

logging.basicConfig(level=logging.INFO)

# 🔑 Palavras-chave
positivas = ["destaque", "importância", "conquista", "posição", "transformação", "inovação"]
negativas = ["urgência", "insegurança", "regulamentação", "risco", "vigilância", "problema"]

def analyze_sentiments(input_csv, output_csv='data/processed/analise_sentimentos.csv'):
    """Analisa sentimentos baseado em palavras-chave."""
    df = pd.read_csv(input_csv)

    def analisar_sentimento(texto):
        texto = str(texto).lower()
        score_pos = sum(p in texto for p in positivas)
        score_neg = sum(n in texto for n in negativas)
        if score_pos > score_neg:
            return "Positiva"
        elif score_neg > score_pos:
            return "Negativa"
        else:
            return "Neutra"

    df["Sentimento"] = df.iloc[:, 1].apply(analisar_sentimento)
    df.to_csv(output_csv, index=False)
    logging.info(f"Análise de sentimentos salva em {output_csv}")
    return output_csv