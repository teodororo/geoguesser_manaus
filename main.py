import folium
import streamlit as st
from streamlit_folium import st_folium

from game import GeoGuesserManaus

# Lista de fotos com coordenadas aproximadas
fotos = [
    {"path": "fotos/bernado-ramos.jpg", "lat": -3.119027,
        "lon": -60.021731},
    {"path": "fotos/mercadao.jpg", "lat": -
        3.143505, "lon": -60.013016}
    # {"path": "fotos/3.jpg", "lat": -3.106409,
    #     "lon": -60.027203},
    # {"path": "fotos/4.jpg", "lat": -3.118889,
    #     "lon": -60.013889},
    # {"path": "fotos/5.jpg", "lat": -3.0787, "lon": -59.9935},
    # {"path": "fotos/6.jpg", "lat": -3.147, "lon": -
    #     59.987},
    # {"path": "fotos/7.jpg", "lat": -3.118,
    #     "lon": -60.012},
    # {"path": "fotos/8.jpg", "lat": -3.101, "lon": -60.004},
    # {"path": "fotos/9.jpg", "lat": -3.106,
    #     "lon": -59.986},
    # {"path": "fotos/10.jpg", "lat": -3.135, "lon": -60.012},
]

jogo = GeoGuesserManaus(fotos)

st.title("🌍 GeoGuesser Manaus")
st.write(str(jogo))

foto_atual = jogo[jogo.index]
st.image(foto_atual["path"],
         caption=f"Foto {jogo.index + 1} de {len(jogo)}", width='content')

# Mapa centrado em Manaus
m = folium.Map(location=[-3.119, -60.021], zoom_start=12)
st.write("Clique no mapa para escolher onde acha que a foto foi tirada.")
data = st_folium(m, height=400, width=700)

if data and data.get("last_clicked"):
    lat = data["last_clicked"]["lat"]
    lon = data["last_clicked"]["lng"]
    resultado, dist, pontos = jogo.verificar_chute((lat, lon))
    st.success(f"{resultado} Distância: {dist:.1f} m | +{pontos} ponto(s)")
    if st.button("Próxima imagem ➡️"):
        jogo.proxima()
        st.rerun()
else:
    st.info("Clique em algum ponto no mapa para fazer seu palpite.")
