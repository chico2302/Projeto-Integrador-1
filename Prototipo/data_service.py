import pandas as pd
import os
from functools import lru_cache

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_CSV = os.path.join(BASE_DIR, 'multiplas_causas.csv')

@lru_cache(maxsize=1)
def obter_dataframe_tratado():
    if not os.path.exists(FILE_CSV):
        print(f"ERRO: Arquivo não encontrado em: {FILE_CSV}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(FILE_CSV)
        return df
    except Exception as e:
        print(f"Erro ao ler CSV: {e}")
        return pd.DataFrame()

def obter_dados_graficos(ano_min=1980, ano_max=2023):
    df_base = obter_dataframe_tratado()
    if df_base.empty:
        return {
            "anos": [], "valores": [], "valores_taxa": [], "valores_cancer": [], "top_nomes": [], "top_valores": [],
            "historico_anos": [], "historico_percentual": [], "historico_eventos": [],
            "ano_recente": 2023, "novos_anos": [], "novos_fumantes_milhoes": [], "novos_ipi": []
        }

    # FILTRO DE ANO: Aplicado nos dados epidemiológicos contínuos do CSV
    df_f = df_base[(df_base['year'] >= ano_min) & (df_base['year'] <= ano_max)]

    # 1. Agrupamento de total de óbitos por ano (Gráfico 1)
    df_agrupado_novo = df_f.groupby('year').sum(numeric_only=True).reset_index()
    anos = df_agrupado_novo['year'].astype(int).tolist()
    valores = [int(v) for v in df_agrupado_novo['val'].tolist()]

    # 2. Linha de controle focada em Câncer de Pulmão (Gráfico 2)
    causa_controle = "Câncer de traqueia, brônquios e pulmão"
    df_cancer = df_f[df_f['cause'] == causa_controle].groupby('year').sum(numeric_only=True).reset_index()
    cancer_map = dict(zip(df_cancer['year'], df_cancer['val']))
    valores_cancer = [int(cancer_map.get(a, 0)) for a in anos]

    # 3. Composição Relativa das Doenças no ano mais recente do período (Gráfico 4)
    ano_recente = df_f['year'].max() if not df_f.empty else ano_max
    df_ano = df_f[df_f['year'] == ano_recente]
    df_causas = df_ano.groupby('cause')['val'].sum().reset_index().sort_values(by='val', ascending=False)
    top_nomes = df_causas['cause'].tolist()
    top_valores = [int(v) for v in df_causas['val'].tolist()]

    # DADOS HISTÓRICOS DE PESQUISAS (Fumantes e Legislações)
    # Mantidos completos para preservar a correlação das eras de políticas públicas
    dados_historicos = {
        "ano": [1989, 1996, 2005, 2011, 2020, 2023],
        "populacao_milhoes": [147.0, 161.0, 184.0, 196.0, 213.0, 203.0],
        "percentual_fumantes": [34.8, 29.0, 22.4, 18.1, 12.6, 13.2],
        "ipi_aproximado": [41.25, 45.0, 60.0, 70.0, 78.0, 78.0],
        "evento": [
            "Campanhas nacionais antitabagismo", "Restrição da propaganda de cigarros",
            "Ratificação da Convenção-Quadro (CQCT)", "Lei antifumo nacional",
            "Consolidação de ambientes livres de fumaça", "Popularização dos cigarros eletrônicos"
        ]
    }
    df_hist = pd.DataFrame(dados_historicos)
    
    fumantes_estimados = [
        round(row['populacao_milhoes'] * (row['percentual_fumantes'] / 100), 1)
        for _, row in df_hist.iterrows()
    ]

    return {
        "anos": anos,
        "valores": valores,
        "valores_cancer": valores_cancer,
        "top_nomes": top_nomes,
        "top_valores": top_valores,
        "ano_recente": int(ano_recente) if not pd.isna(ano_recente) else ano_max,
        "historico_anos": df_hist["ano"].tolist(),
        "historico_percentual": df_hist["percentual_fumantes"].tolist(),
        "historico_eventos": df_hist["evento"].tolist(),
        "novos_anos": df_hist["ano"].tolist(),
        "novos_fumantes_milhoes": fumantes_estimados,
        "novos_ipi": df_hist["ipi_aproximado"].tolist()
    }

def obter_dados_cards(ano_min=1980, ano_max=2023):
    dados = obter_dados_graficos(ano_min, ano_max)
    if not dados["valores"]:
        return {"total_mortes": "0", "ano_ref": f"{ano_max}", "meta_oms": "Menos de 5%"}
    return {
        "total_mortes": f"{dados['valores'][-1]:,}".replace(",", "."),
        "ano_ref": str(dados["anos"][-1]),
        "meta_oms": "Menos de 5%"
    }

def obter_dados_tabela(ano_min=1980, ano_max=2023):
    df_base = obter_dataframe_tratado()
    if df_base.empty: return []
    df = df_base[(df_base['year'] >= ano_min) & (df_base['year'] <= ano_max)]
    df_tabela = df.sort_values(by=['year'], ascending=[False])
    return [{"year": int(r['year']), "cause": str(r.get('cause', 'Geral')), "val": f"{int(r['val'])}".replace(",", ".")} for _, r in df_tabela.iterrows()]