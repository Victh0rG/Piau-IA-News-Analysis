import pandas as pd
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(level=logging.INFO)

def clean_data(input_csv, output_csv='data/processed/dados.csv'):
    """Limpa texto: remove HTML e caracteres especiais."""
    df = pd.read_csv(input_csv)

    def limpar_html(texto):
        if pd.isna(texto):
            return ""
        soup = BeautifulSoup(str(texto), "html.parser")
        texto_limpo = soup.get_text()
        texto_limpo = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", texto_limpo)
        return texto_limpo.strip()

    df["description"] = df["description"].apply(limpar_html)
    df.drop(columns=["link"], inplace=True, errors='ignore')
    df.to_csv(output_csv, index=False)
    logging.info(f"Dados limpos salvos em {output_csv}")
    return output_csv