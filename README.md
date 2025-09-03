# Piauí IA News Analysis

Este projeto realiza coleta, limpeza, análise de sentimentos e visualização de notícias relacionadas à Inteligência Artificial no estado do Piauí, usando feeds RSS do Google News. Ele automatiza o processo de extração de dados, aplica análise de sentimentos baseada em palavras-chave e gera visualizações interativas com Streamlit (gráficos de pizza e nuvens de palavras).

## Funcionalidades Principais

- **Coleta de Dados**: Busca notícias via GoogleNews e salva em XML/CSV.
- **Limpeza de Dados**: Remove tags HTML e caracteres especiais.
- **Análise de Sentimentos**: Classifica notícias como Positiva, Negativa ou Neutra com base em palavras-chave configuráveis.
- **Visualização**: Interface web com Streamlit para gráficos e tabela interativa.

## Requisitos

- Python 3.8+ (testado em 3.12).
- Bibliotecas: `pandas`, `streamlit`, `wordcloud`, `matplotlib`, `GoogleNews`, `beautifulsoup4`, `xml.etree.ElementTree`, `PyYAML`.
- Ambiente virtual recomendado (`venv`).

## Instruções de Git

### Inicialize o Repositório

- Clone o repositório: `git clone <url-do-repo>`.
- Ou, crie um novo: `git init` na raiz do projeto.

### Branching e Commits

- Use branches para features: `git checkout -b feature/nova-funcionalidade`.
- Faça commits atômicos: `git commit -m "Adiciona módulo de coleta de dados"`.
- Merge via Pull Requests no GitHub/GitLab para revisão.

### .gitignore

Inclua: `.venv/`, `data/`, `__pycache__/`, `*.pyc`, para evitar versionar dados e ambientes.

### Versionamento

- Tag releases: `git tag v1.0.0` e `git push --tags`.
- Use Git Flow ou GitHub Flow para workflow.

## Documentação Técnica

### Arquitetura

- **Modularidade**: O código está organizado em módulos dentro de `src/`, permitindo reutilização. Cada módulo foca em uma responsabilidade (coleta, limpeza, análise).
- **Fluxo de Dados**:
  - **Coleta**: `data_collection.py` usa GoogleNews para buscar e salvar em XML/CSV.
  - **Limpeza**: `data_cleaning.py` processa o CSV bruto, removendo HTML com BeautifulSoup e regex.
  - **Análise**: `sentiment_analysis.py` aplica lógica de palavras-chave (carregadas de YAML) e gera CSV final.
  - **Visualização**: `app/app.py` usa Streamlit para renderizar gráficos (Matplotlib) e nuvens de palavras (WordCloud).
- **Configurações**: Palavras-chave em `config/keywords.yaml` para fácil edição sem alterar código.
- **Logging**: Usado para rastrear execuções e erros.
- **Extensibilidade**: Facilmente expansível para ML (ex: integrar Hugging Face para sentimentos mais precisos).

### Decisões Técnicas

Consulte `DECISIONS.md` para justificativas detalhadas.

### Limitações

- Análise de sentimentos é baseada em palavras-chave (simples, mas limitada para contextos nuances).
- Dependente de API GoogleNews (pode ter limites de taxa).

# Setup

## Crie Ambiente Virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

## Instale Dependências:
```bash
pip install -r requirements.txt
```

## Configurações Iniciais:
Edite `config/keywords.yaml` para ajustar palavras-chave positivas/negativas.

# Execução

## Rodar o Pipeline Completo (coleta, limpeza e análise):
```bash
python main.py
```

Isso gera arquivos em `data/raw/` e `data/processed/`.

## Rodar a Aplicação Streamlit:
```bash
streamlit run app/app.py
```

Acesse no navegador (geralmente `http://localhost:8501`).  
Exibe gráfico de pizza, nuvem de palavras e tabela interativa.

## Testes (opcional):
```bash
pytest tests/
```

# Contribuição

- Abra issues no repositório para bugs ou features.
- Pull Requests: Siga o estilo PEP8 e adicione testes.