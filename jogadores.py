import copy
from random import randint
class Jogadores(object):
    def __init__(self, controle, posicoes):
        self.controle = controle
        self.posicoes = posicoes
        self.fim_de_partida = False
        self._vencedor = None

    @property.getter
    def vencedor(self):
        return self.vencedor
    
    @property.setter
    def vencedor(self, vencedor):
        self.vencedor = vencedor

    def jogador(self):
        if self.posicoes[self.controle.pos_y][self.controle.pos_x] == "":
            self.posicoes[self.controle.pos_y][self.controle.pos_x] == 'x'
            return True
        return False
    
    def robo(self):
        vazias = []
        for i in range(0,3):
            for j in range(0,3):
                if self.posicoes[i][j] == '':
                    vazias.append([i,j])
        
        n_escolhas = len(vazias)
        if n_escolhas != 0:
            j, i = vazias[randint(0, n_escolhas - 1)]
            self.posicoes[j][i] = "o"