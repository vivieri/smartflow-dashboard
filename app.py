# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SMARTflow - Dashboard Fixo",
                   layout="wide",
                   initial_sidebar_state="expanded")


PRIMARY = "#021b15" 
ACCENT = "#b8e0c8"  
CARD = "rgba(255,255,255,0.04)"

st.markdown(f"""
    <style>
        .stApp {{ background-color: {PRIMARY}; color: #fff; }}
        .reportview-container .main .block-container{{padding-top:1rem; padding-left:1rem; padding-right:1rem;}}
         h1, h2, h3, .css-1v3fvcr {{ color: #e6fff0; }}
        .card {{ background: {CARD}; border-radius: 10px; padding: 12px; }}
        .small-muted {{ color: rgba(255,255,255,0.7); font-size:12px }}
        .big-number {{ font-size:28px; font-weight:700; color: #eafff0; }}
    </style>
""", unsafe_allow_html=True)


# Tabela 1: Postos, GAP, Descrição e Tempo (resumido)
postos_data = [
    {"Posto": "Posto 1",  "GAP": "TEAM 1", "Descrição": "BCC, UND, KIT 1 E KIT 2", "Tempo_min": 2},
    {"Posto": "Posto 2",  "GAP": "TEAM 1", "Descrição": "Coluna (3kg), parafusamento", "Tempo_min": 2},
    {"Posto": "Posto 3",  "GAP": "TEAM 1", "Descrição": "Chicote + montagem", "Tempo_min": 2},
    {"Posto": "Posto 4",  "GAP": "TEAM 1", "Descrição": "Chicote lado motorista + Airbag", "Tempo_min": 2},
    {"Posto": "Posto 5",  "GAP": "TEAM 1", "Descrição": "DUTO", "Tempo_min": 3},
    {"Posto": "Posto 7",  "GAP": "TEAM 2", "Descrição": "IP + SGG", "Tempo_min": 3},
    {"Posto": "Posto 8",  "GAP": "TEAM 2", "Descrição": "Moldura central, parafusamento IP", "Tempo_min": 3},
    {"Posto": "Posto 9",  "GAP": "TEAM 2", "Descrição": "Conecta rádio, parafusamento IP (2)", "Tempo_min": 3},
    {"Posto": "Posto 10", "GAP": "TEAM 2", "Descrição": "Parafusamento do quadro", "Tempo_min": 2},
    {"Posto": "Posto 11", "GAP": "TEAM 3", "Descrição": "Capa do Duto", "Tempo_min": 2},
    {"Posto": "Posto 12", "GAP": "TEAM 3", "Descrição": "Bracket", "Tempo_min": 2},
    {"Posto": "Posto 13", "GAP": "TEAM 3", "Descrição": "Grelha e KIT 3", "Tempo_min": 2},
    {"Posto": "Posto 14", "GAP": "TEAM 3", "Descrição": "Chave de seta", "Tempo_min": 2},
    {"Posto": "Posto 15", "GAP": "TEAM 3", "Descrição": "Parafusa e encaixa a capa inferior", "Tempo_min": 2},
    {"Posto": "Posto 16", "GAP": "TEAM 4", "Descrição": "GB + porta-objetos", "Tempo_min": 2},
    {"Posto": "Posto 17", "GAP": "TEAM 4", "Descrição": "Tampa LH, miracle do rádio", "Tempo_min": 3},
    {"Posto": "Posto 18", "GAP": "TEAM 4", "Descrição": "Tampão RH, miracle, duto, sensor", "Tempo_min": 3},
    {"Posto": "Posto 20", "GAP": "TEAM 4", "Descrição": "teste elétrico", "Tempo_min": 3},
    {"Posto": "Posto 21", "GAP": "TEAM 4", "Descrição": "teste elétrico", "Tempo_min": 3},
    {"Posto": "Posto 22", "GAP": "TEAM 4", "Descrição": "teste elétrico", "Tempo_min": 3},
    {"Posto": "Posto 23", "GAP": "TEAM 2", "Descrição": "Vistoria", "Tempo_min": 3},
]

df_postos = pd.DataFrame(postos_data)

# Tabela 2: Mix do dia (frequências por modelo) + paradas/causas/esgotamento/dificuldade por posto
mix_models = {
    "Projeto A": 0.05,
    "Projeto B": 0.10,
    "Projeto C": 0.50,
    "Projeto D": 0.25,
    "Projeto E": 0.10
}

paradas_data = [
    {"Posto": "Posto 1", "Paradas por h": 3, "Motivo": "Faltou papel para impressão", "Esgotamento": "esgotado", "Dificuldade":"A,B,C,D,E"},
    {"Posto": "Posto 2", "Paradas por h": 3, "Motivo": "Parada de emergência", "Esgotamento": "péssimo", "Dificuldade":"A,B,C,D,E"},
    {"Posto": "Posto 3", "Paradas por h": 2, "Motivo": "Falta de chicote", "Esgotamento": "ruim", "Dificuldade":"A,B,C,D,E"},
    {"Posto": "Posto 4", "Paradas por h": 3, "Motivo": "Falta de airbag", "Esgotamento": "ruim", "Dificuldade":"A,B,C,D,E"},
    {"Posto": "Posto 5", "Paradas por h": 5, "Motivo": "Falha operacional", "Esgotamento": "ruim", "Dificuldade":"A,B,C,D,E"},
    {"Posto": "Posto 7", "Paradas por h": 7, "Motivo": "Falha do Poka Yoke", "Esgotamento": "ok", "Dificuldade":"A"},
    {"Posto": "Posto 9", "Paradas por h": 4, "Motivo": "Demora no abastecimento", "Esgotamento": "ok", "Dificuldade":"A"},
    {"Posto": "Posto 10","Paradas por h": 5, "Motivo": "Falta de peças", "Esgotamento": "regular", "Dificuldade":"C"},
    {"Posto": "Posto 11","Paradas por h": 4, "Motivo": "Difusor com erro", "Esgotamento": "ok", "Dificuldade":"A"},
    {"Posto": "Posto 12","Paradas por h": 3, "Motivo": "Duto ausente", "Esgotamento": "regular", "Dificuldade":"E"},
    {"Posto": "Posto 13","Paradas por h": 4, "Motivo": "Falta de KIT 3", "Esgotamento": "regular", "Dificuldade":"E"},
    {"Posto": "Posto 14","Paradas por h": 2, "Motivo": "Chave de seta errada", "Esgotamento": "regular", "Dificuldade":"E"},
    {"Posto": "Posto 15","Paradas por h": 4, "Motivo": "Retrabalhos", "Esgotamento": "regular", "Dificuldade":"E"},
    {"Posto": "Posto 16","Paradas por h": 10,"Motivo": "Falta de Glove Box", "Esgotamento": "ruim", "Dificuldade":"A"},
    {"Posto": "Posto 17","Paradas por h": 13,"Motivo": "Ausência de presilhas", "Esgotamento": "esgotado", "Dificuldade":"B,C,D,E"},
    {"Posto": "Posto 18","Paradas por h": 15,"Motivo": "Falta de groomet, mix alto", "Esgotamento": "esgotado", "Dificuldade":"B,C,D,E"},
]

df_paradas = pd.DataFrame(paradas_data)

# Tabela 3: Balanceamento

balanceamento_text = """
Resumo do balanceamento:
- Foi criado o Posto 19 na GAP 4 para diminuir o gargalo entre os postos 17 e 18.
- Objetivo: reduzir o tempo médio de espera e redistribuir tarefas do E-check.
- Resultados esperados: redução de 12% no tempo médio da GAP 4 e queda nas paradas por hora, resultando no aumento do buffer.
"""

# titulo 

st.title("SMARTflow")
st.subheader("Sistema Inteligente de Indicadores de Produção")
st.write("")  # espaçamento

# Menu lateral

menu = st.sidebar.radio("Navegação", ["Painel Geral", "Nível de Esgotamento", "Gargalos", "Balanceamento", "Paradas"])

# Painel Geral 

if menu == "Painel Geral":
    # Cards métricos
    col1, col2, col3, col4 = st.columns([1.3,1.3,1.3,1.3])
    with col1:
        total_prod = 350 
        st.markdown('<div class="card"><div class="small-muted">Produção diária</div><div class="big-number">'+str(total_prod)+' carros/dia</div></div>', unsafe_allow_html=True)
    with col2:
        # Modelo mais frequente (porcentagem)
        most = max(mix_models, key=mix_models.get)
        pct = int(mix_models[most]*100)
        st.markdown(f'<div class="card"><div class="small-muted">Modelo mais frequente</div><div class="big-number">{most} — {pct}%</div></div>', unsafe_allow_html=True)
    with col3:
        # GAP mais exausta: calculo a partir do df_paradas esgotamento "esgotado" ou "ruim"
        gap_counts = df_paradas[df_paradas['Esgotamento'].isin(['esgotado','ruim'])].merge(df_postos[['Posto','GAP']], on='Posto', how='left')
        gap_most = gap_counts['GAP'].mode().iloc[0] if not gap_counts.empty else "—"
        st.markdown(f'<div class="card"><div class="small-muted">GAP mais exausta</div><div class="big-number">{gap_most}</div></div>', unsafe_allow_html=True)
    with col4:
        avg_esgot = df_paradas['Paradas por h'].mean()
        st.markdown(f'<div class="card"><div class="small-muted">Paradas média por posto (h)</div><div class="big-number">{avg_esgot:.1f}</div></div>', unsafe_allow_html=True)

    st.write("")  # espaço

    # Charts: produção por modelo e distribuição (usando mix_models x 350)
    model_labels = list(mix_models.keys())
    model_counts = [int(mix_models[k]*total_prod) for k in model_labels]

    # bar
    fig_bar = px.bar(x=model_labels, y=model_counts, labels={'x':'Projeto','y':'Unidades'}, color=model_labels,
                     color_discrete_sequence=[ACCENT, "#4fbf78", "#86e6b1", "#2e8b57", "#0b5f45"])
    fig_bar.update_layout(plot_bgcolor=PRIMARY, paper_bgcolor=PRIMARY, font_color="white", showlegend=False)
    # pie
    fig_pie = px.pie(names=model_labels, values=model_counts, hole=0.4,
                     color_discrete_sequence=[ACCENT, "#4fbf78", "#86e6b1", "#2e8b57", "#0b5f45"])
    fig_pie.update_layout(plot_bgcolor=PRIMARY, paper_bgcolor=PRIMARY, font_color="white", legend=dict(orientation="v"))

    c1, c2 = st.columns([2,1])
    with c1:
        st.subheader("Produção por Projeto")
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        st.subheader("Distribuição dos Projetos")
        st.plotly_chart(fig_pie, use_container_width=True)

    st.subheader("Resumo dos Postos")
    st.dataframe(df_postos[['Posto','GAP','Descrição','Tempo_min']].rename(columns={'Tempo_min':'Tempo (min)'}), use_container_width=True)


# Nível de Esgotamento

elif menu == "Nível de Esgotamento":
    st.subheader("Nível de Esgotamento por Posto")
    # tabela de paradas + um gráfico de barras com paradas por posto
    fig = px.bar(df_paradas.sort_values('Paradas por h', ascending=False),
                 x='Posto', y='Paradas por h', color='Esgotamento',
                 color_discrete_map={'esgotado':'#ff4d4f','ruim':'#ff7a59','regular':'#f2c94c','ok':'#86e6b1','péssimo':'#b00020'})
    fig.update_layout(plot_bgcolor=PRIMARY, paper_bgcolor=PRIMARY, font_color="white", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.write("Tabela de detalhe (paradas / motivo / esgotamento)")
    st.dataframe(df_paradas, use_container_width=True)


# Gargalos

elif menu == "Gargalos":
    st.subheader("Gargalos – análise por GAP e Posto")
    # Simples heatmap por GAP: média de paradas por GAP
    merged = df_paradas.merge(df_postos[['Posto','GAP']], on='Posto', how='left')
    gap_summary = merged.groupby('GAP')['Paradas por h'].mean().reset_index().rename(columns={'Paradas por h':'Paradas_media_h'})
    st.dataframe(gap_summary, use_container_width=True)

    fig2 = px.bar(gap_summary, x='GAP', y='Paradas_media_h', color='Paradas_media_h',
                  color_continuous_scale=['#86e6b1','#4fbf78','#2e8b57','#0b5f45'])
    fig2.update_layout(plot_bgcolor=PRIMARY, paper_bgcolor=PRIMARY, font_color="white", coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("**Observações:**")
    st.markdown("- GAP 4 apresenta maior concentração de paradas e postos esgotados (Postos 17 e 18)")
    st.markdown("- Criação do posto 19 para reduzir gargalos. Assim, o posto 19 colocará Duto + sensor no projeto C, D e E. Dessa forma o posto 18 não irá parar a linha com frequência")

# Balanceamento

elif menu == "Balanceamento":
    st.subheader("Balanceamento de Linha")
    st.write(balanceamento_text)
    st.write("Resumo de tempos médios por GAP")
    df_times = df_postos.groupby('GAP')['Tempo_min'].mean().reset_index().rename(columns={'Tempo_min':'Tempo Médio (min)'})
    st.dataframe(df_times, use_container_width=True)

# Paradas

elif menu == "Paradas":
    st.subheader("Paradas e motivos por posto")
    st.dataframe(df_paradas, use_container_width=True)
    st.markdown("**Comentários:**")
    st.markdown("- Postos 17 e 18 têm maior número de paradas porque é a GAP final (decorativos), ou seja, é necessário focar na qualidade além da operação")

