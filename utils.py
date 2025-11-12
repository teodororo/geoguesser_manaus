import math


def distancia(coord1, coord2):
    """Calcula a distância em metros entre duas coordenadas (lat, lon)."""
    R = 6371000  # raio da terra em metros
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c


def ler_pontuacao():
    """Lê pontuação salva. No stlite, retorna sempre 0."""
    try:
        with open("pontuacao.txt", "r") as f:
            conteudo = f.read().strip()
            return int(conteudo) if conteudo else 0
    except (FileNotFoundError, PermissionError):
        return 0


def salvar_pontuacao(pontos):
    """Salva pontuação. No stlite, pode não funcionar."""
    try:
        with open("pontuacao.txt", "w") as f:
            f.write(str(pontos))
    except (PermissionError, OSError):
        pass  # Silenciosamente ignora erros de escrita no stlite
