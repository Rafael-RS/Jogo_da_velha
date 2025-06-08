# 🕹️ Jogo da Velha

Um simples jogo da velha jogado no terminal (CLI), entre o jogador (**X**) e um robô (**O**).  
Na versão atual, o robô joga de forma aleatória.

> 📌 **Este projeto está na sua primeira versão.**

---

## 🚀 Como Rodar

Certifique-se de estar com o Python instalado. Para iniciar o jogo, execute:

```bash
python main.py
```

> O jogo roda direto no terminal, sem necessidade de instalação adicional — exceto por `windows-curses` no Windows.

---

## 📦 Dependências

Se estiver no Windows, é necessário instalar o pacote abaixo:

```bash
pip install -r requirements.txt
```

**Conteúdo do `requirements.txt`:**

```
windows-curses==2.4.1
```

---

## 🎮 Controles e Ajuda

Durante o jogo, você pode usar as seguintes teclas:

- `A`, `W`, `S`, `D` → Mover o cursor (esquerda, cima, baixo, direita)  
- `Enter` → Marcar a posição atual com "X"  
- `Y` → Reiniciar o jogo  
- `H` → Exibir a tela de ajuda  
- `Q` → Sair do jogo  

---

## 🚧 Roadmap

- [x] Versão inicial com jogo básico (jogador X vs robô O aleatório)  
- [ ] Permitir jogo para 2 jogadores na mesma máquina  
- [ ] Implementar jogo para 2 jogadores via LAN (rede local)  
- [ ] Desenvolver uma IA mais inteligente para o robô  
- [ ] Criar interface gráfica (GUI)  
- [ ] Melhorar ajuda e tutorial dentro do jogo  
- [ ] Suporte multiplataforma aprimorado (Linux, macOS, Windows)  
- [ ] Criar testes automatizados para o código  
- [ ] Documentação detalhada do código e contribuições

---

## 📜 Licença

Este projeto é **livre**. Você pode jogar, modificar e compartilhar à vontade.

---

## 👨‍💻 Autor

Feito por **Rafael Rodrigues**  
GitHub: [@Rafael-RS](https://github.com/Rafael-RS)

---

### 🤖 Sobre este README

Este arquivo foi gerado com auxílio de inteligência artificial (ChatGPT).
