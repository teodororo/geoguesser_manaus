from utils import distancia, ler_pontuacao, salvar_pontuacao


class GeoGuesserManaus:
    def __init__(self, fotos):
        self.fotos = fotos
        self.index = 0
        self.pontos = ler_pontuacao()

    def __len__(self):
        return len(self.fotos)

    def __getitem__(self, idx):
        return self.fotos[idx]

    def __str__(self):
        return f"Rodada {self.index+1}/{len(self.fotos)} - Pontos: {self.pontos}"

    def proxima(self):
        if self.index < len(self.fotos) - 1:
            self.index += 1
        else:
            self.index = 0

    def verificar_chute(self, chute_latlon):
        """Verifica se o chute está próximo do local real."""
        foto = self.fotos[self.index]
        real = (foto["lat"], foto["lon"])
        d = distancia(real, chute_latlon)
        if d <= 500:
            pontos = 2
            resultado = "🎯 Acertou em cheio!"
        elif d <= 1500:
            pontos = 1
            resultado = "👍 Quase acertou!"
        else:
            pontos = 0
            resultado = "❌ Errou!"
        self.pontos += pontos
        salvar_pontuacao(self.pontos)
        return resultado, d, pontos
