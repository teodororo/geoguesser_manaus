import pandas as pd
import streamlit as st

from game import GeoGuesserManaus

# Lista de fotos com coordenadas aproximadas
fotos = [
    {"path": "fotos/bernardo-ramos.jpg", "lat": -3.134000, "lon": -60.028000},
    {"path": "fotos/mercadao.jpg", "lat": -3.140000, "lon": -60.024000}
]

# Inicializar o jogo no session_state
if 'jogo' not in st.session_state:
    st.session_state.jogo = GeoGuesserManaus(fotos)
if 'chute_feito' not in st.session_state:
    st.session_state.chute_feito = False
if 'resultado' not in st.session_state:
    st.session_state.resultado = None

jogo = st.session_state.jogo

st.title("🌍 GeoGuesser Manaus")

# Instruções logo abaixo do título
with st.expander("ℹ️ Como jogar"):
    st.write("""
    1. Observe a foto exibida
    2. Ajuste a latitude e longitude para onde você acha que a foto foi tirada
    3. Use o mapa como referência (ponto azul = seu chute)
    4. Clique em "Confirmar localização"
    5. Veja o resultado e a localização correta (ponto verde = resposta)

    **Pontuação:**
    - 🎯 Até 500m = 2 pontos
    - 👍 Até 1500m = 1 ponto
    - ❌ Mais de 1500m = 0 pontos
    """)

st.write(str(jogo))

foto_atual = jogo[jogo.index]
st.image(foto_atual["path"],
         caption=f"Foto {jogo.index + 1} de {len(jogo)}",
         width='stretch')

st.write("**Escolha onde você acha que a foto foi tirada:**")

# Layout em duas colunas
col1, col2 = st.columns(2)

with col1:
    lat_input = st.number_input(
        "Latitude",
        min_value=-3.3,
        max_value=-2.9,
        value=-3.119,
        step=0.001,
        format="%.6f",
        disabled=st.session_state.chute_feito
    )

with col2:
    lon_input = st.number_input(
        "Longitude",
        min_value=-60.2,
        max_value=-59.8,
        value=-60.021,
        step=0.001,
        format="%.6f",
        disabled=st.session_state.chute_feito
    )

# Preparar dados para o mapa com cores diferentes
map_data = []

# Adicionar ponto do chute do usuário (azul)
if lat_input and lon_input:
    map_data.append({
        'lat': lat_input,
        'lon': lon_input,
        'color': '#0044FF',  # Azul para o chute
        'size': 100
    })

# Se o chute foi feito, mostrar o local correto (verde)
if st.session_state.chute_feito:
    map_data.append({
        'lat': foto_atual['lat'],
        'lon': foto_atual['lon'],
        'color': '#00FF00',  # Verde para o correto
        'size': 150
    })

# Criar DataFrame para o mapa
df_map = pd.DataFrame(map_data)

# Exibir mapa com cores customizadas
if not df_map.empty:
    st.map(df_map, latitude='lat', longitude='lon',
           color='color', size='size', zoom=12)

# Botão de enviar chute
if not st.session_state.chute_feito:
    if st.button("✅ Confirmar localização", type="primary"):
        resultado, dist, pontos = jogo.verificar_chute((lat_input, lon_input))
        st.session_state.chute_feito = True
        st.session_state.resultado = (resultado, dist, pontos)
        st.rerun()

# Mostrar resultado
if st.session_state.chute_feito and st.session_state.resultado:
    resultado, dist, pontos = st.session_state.resultado

    if pontos == 2:
        st.success(f"{resultado} Distância: {dist:.1f} m | +{pontos} pontos")
    elif pontos == 1:
        st.info(f"{resultado} Distância: {dist:.1f} m | +{pontos} ponto")
    else:
        st.error(f"{resultado} Distância: {dist:.1f} m | +{pontos} pontos")

    st.write(
        f"**Local correto:** Lat: {foto_atual['lat']:.6f}, Lon: {foto_atual['lon']:.6f}")

    # Botão para próxima imagem
    if jogo.index < len(jogo) - 1:
        if st.button("➡️ Próxima imagem", type="primary"):
            jogo.proxima()
            st.session_state.chute_feito = False
            st.session_state.resultado = None
            st.rerun()
    else:
        st.balloons()
        st.success(
            f"🎉 Parabéns! Você completou o jogo com {jogo.pontos} pontos!")
        if st.button("🔄 Jogar novamente"):
            # Zerar pontos ao jogar novamente
            st.session_state.jogo = GeoGuesserManaus(fotos, pontos_iniciais=0)
            st.session_state.chute_feito = False
            st.session_state.resultado = None
            st.rerun()
            st.rerun()
