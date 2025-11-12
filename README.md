# geoguesser_manaus

# Rodar localmente

# Vantagens
- **Criação automática de site estático.** O index.html apenas chama os arquivos Python. O GitHub Pages atualiza automaticamente a cada commit. Isto permite, entre outras coisas, que qualquer pessoa acesse o app de qualquer dispositivo, ao passo que o Tkinter seria limitado a desktops.

# Desvantagens
- **Lentidão**, é preciso esperar mais de 5 segundos para o site abrir. Isso acontece porque, ao gerar o site estático, o GitHub faz download de todas as imagens da pasta imagens/. Quanto mais imagens o app tiver, mais demorado será carregá-lo. Ele é, portanto, um app não escalável. Todas as imagens tiveram que passar por um processo de redimensionamento para que não fossem tão pesadas.
- **Não intuitivo**. No GeoGuesser original, é possível clicar no mapa e, a partir desse clique, o sistema infere a latidude/altitude, sem que o usuário precise "calibrá-la" para fazer o chute. No entanto, embora o Streamlit tenha a extensão Folium para criar mapas interativos, o Folium não está disponível na [lista de extensões suportadas pelo Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html), então usei a função st.map() nativa do próprio Streamlit, cujo uso é voltado para visualização e não interação, isso é, ela não permite capturar eventos.

# Inspirações:

- [Stlite Template](https://github.com/FredHutch/stlite-template)
- [Streamlit-pydantic](https://github.com/lukasmasuch/streamlit-pydantic)
