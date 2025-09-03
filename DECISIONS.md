# Architecture Decision Records (ADRs)

Este arquivo documenta decisões técnicas tomadas no projeto, seguindo o formato ADR para registrar o contexto, opções consideradas, decisão final e justificativas. Isso ajuda na manutenção e compreensão futura.

## ADR 001: Estrutura de Pastas e Modularidade

**Contexto**: O código original estava em arquivos soltos, misturando responsabilidades, o que dificulta manutenção e escalabilidade.

**Opções Consideradas**:
- Manter arquivos soltos: Simples, mas desorganizado para crescimento.
- Usar uma estrutura monolítica: Fácil para pequenos projetos, mas não reutilizável.
- Adotar estrutura modular com pacotes (`src/`, `app/`, `config/`): Padrão em projetos Python médios, como recomendado pela Python Packaging Authority.

**Decisão**: Adotar estrutura modular com `src/` como pacote (incluindo `__init__.py`), `app/` para Streamlit e `data/` para outputs.

**Justificativa**: Facilita importações reutilizáveis (ex: `from src.data_collection import collect_news`), separa preocupações (SRP - Single Responsibility Principle), e segue convenções como Cookiecutter Data Science. Reduz acoplamento e melhora testabilidade. **Custo**: Leve overhead inicial, mas benefícios em longo prazo para colaboração.

## ADR 002: Análise de Sentimentos Baseada em Palavras-Chave

**Contexto**: Precisa classificar sentimentos em notícias, mas sem dependências pesadas ou custos de API.

**Opções Consideradas**:
- Modelos ML avançados (ex: Hugging Face Transformers): Mais preciso, mas requer GPUs e aumenta complexidade.
- Bibliotecas como VADER/TextBlob: Fáceis, mas focadas em inglês (notícias em PT-BR).
- Lógica simples com palavras-chave: Básica, usando listas positivas/negativas.

**Decisão**: Usar lógica de palavras-chave em listas.

**Justificativa**: Simples e sem dependências externas, alinhado ao escopo inicial do projeto (prova de conceito). **Custo**: Menos preciso em sarcasmos, mas suficiente para análise inicial.

## ADR 003: Uso de Streamlit para Visualização

**Contexto**: Necessidade de interface interativa para gráficos e tabela.

**Opções Consideradas**:
- Flask/Django: Mais flexível, mas requer mais boilerplate para web.
- Jupyter Notebooks: Bom para exploração, mas não para apps finais.
- Streamlit: Focado em data apps, com suporte nativo a Pandas/Matplotlib.

**Decisão**: Usar Streamlit.

**Justificativa**: Rápido prototipagem (código Python puro vira app web), integra bem com Pandas e visualizações. Ideal para análise de dados sem expertise em frontend. **Custo**: Menos customizável que React, mas suficiente para este MVP. Alinha com ecossistema data science (usado em projetos como Uber's data apps).

## ADR 004: Armazenamento de Dados em CSV/XML

**Contexto**: Gerenciar dados brutos e processados sem banco de dados.

**Opções Consideradas**:
- Banco SQL (SQLite): Estruturado, mas overkill para arquivos pequenos.
- JSON: Flexível, mas menos legível para tabelas.
- CSV/XML: Simples para tabular e feeds RSS.

**Decisão**: Usar XML para coleta inicial (compatível com RSS) e CSV para processamento.

**Justificativa**: CSV é leve, compatível com Pandas e ferramentas como Excel. XML preserva estrutura original de feeds. Evita overhead de DB para um projeto de análise offline. **Futuro**: Migrar para Parquet se volumes crescerem. Justificado por simplicidade e performance em datasets pequenos.

## ADR 005: Configurações em YAML

**Contexto**: Palavras-chave precisam ser editáveis sem alterar código.

**Opções Consideradas**:
- Hardcoded no código: Rápido, mas inflexível.
- JSON: Simples, mas menos legível para listas.
- YAML: Humano-legível, suporta listas e hierarquias.


## ADR 006: Logging em Vez de Prints

**Contexto**: Rastrear execuções e erros sem poluir console.

**Opções Consideradas**:
- Prints: Simples, mas não configurável.
- Logging module: Nativo, com níveis (INFO, ERROR).

**Decisão**: Usar logging básico.

**Justificativa**: Permite controle de verbosity, salva em arquivos se necessário. Padrão em apps profissionais. **Custo mínimo**, melhora depuração.

Essas decisões são revisáveis. Novas ADRs serão adicionadas conforme o projeto evolui.