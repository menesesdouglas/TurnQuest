# 🎮 Guia Detalhado de Gameplay - TurnQuest

## 📖 Índice
- [Introdução](#-introdução)
- [Criação do Personagem](#-criação-do-personagem)
- [Sistema de Combate](#-sistema-de-combate)
- [Progressão e Níveis](#-progressão-e-níveis)
- [Inimigos](#-inimigos)
- [Estratégias](#-estratégias)
- [Comandos e Interface](#-comandos-e-interface)
- [Dicas para Iniciantes](#-dicas-para-iniciantes)

## 🎯 Introdução

TurnQuest é um RPG por turnos onde você controla um herói em crescimento constante. Cada combate é uma oportunidade para ganhar experiência, subir de nível e se tornar mais forte.

## 🧙 Criação do Personagem

Seu personagem é gerado automaticamente com atributos aleatórios:

- **Vida Inicial**: 15-22 pontos
- **Dano Base**: 3 pontos
- **Nível**: 1
- **XP**: 0/100 para próximo nível

*Dica: Reinicie o jogo várias vezes para conseguir atributos iniciais favoráveis!*

## ⚔️ Sistema de Combate

### Fluxo de Combate
1. **Encontro**: Um inimigo aleatório aparece
2. **Iniciativa**: Cara ou coroa decide quem começa
3. **Turnos**: Alternados entre jogador e inimigo
4. **Resolução**: Vitória ou derrota

### Ações Disponíveis

#### ⚔️ Atacar (Opção 1)
- **Dano Base**: Seu dano atual (ex: 3-6)
- **Chance de Erro**: 20% - causa 0 de dano
- **Chance de Crítico**: 15% - dobra o dano
- **Fórmula**: `dano = base_dano * (2 se crítico)`

#### 🛡️ Defender (Opção 2)
- **Efeito**: Reduz dano recebido pela metade
- **Duração**: Apenas para o próximo ataque inimigo
- **Estratégia**: Use antes de turnos inimigos perigosos

#### ℹ️ Ver Status (Opção 3)
- **Novo**: Não consome turno! (atualização recente)
- **Informações**: Vida, dano, nível, XP
- **Uso Tático**: Verifique se pode sobreviver ao próximo ataque

### Exemplo de Combate
```
⚔️ COMBATE INICIADO! ⚔️

👹 Inimigo encontrado: Orc
📊 Nível: 2
❤️  Vida: 23/23
⚔️  Dano: 5

🎲 Cara ou Coroa para determinar quem começa!
Escolha:
1. 👤 Cara
2. 🪙 Coroa

Sua escolha: 1
🎉 Você ganhou a iniciativa! Você começa primeiro.

Sua vez de agir:
1. ⚔️ Atacar
2. 🛡️ Defender
3. ℹ️ Ver status
```

## 📈 Progressão e Níveis

### Sistema de XP
- **Derrotar Inimigos**: Ganhe XP baseado no nível do inimigo
- **Level Up**: A cada 100 XP (com aumento progressivo)
- **Múltiplos Níveis**: Pode subir vários níveis de uma vez

### Bônus por Nível
- **Vida Máxima**: +3-6 pontos por nível
- **Dano Base**: +1-3 pontos por nível
- **Vida Cura**: Cura completa ao subir de nível

### Tabela de Progressão
| Nível | XP Necessário | Vida Média | Dano Médio |
|-------|---------------|------------|------------|
| 1     | 100           | 18         | 3          |
| 2     | 120           | 22         | 5          |
| 3     | 144           | 27         | 7          |
| 4     | 173           | 32         | 9          |
| 5     | 208           | 37         | 11         |

## 👹 Inimigos

### Tipos de Inimigos
1. **Nível 1**: Goblin, Esqueleto, Lobo Fraco
2. **Nível 2**: Orc, Bandido, Lobo Forte  
3. **Nível 3**: Troll, Aranha Gigante, Chefão

### Estatísticas por Nível
| Nível | Vida | Dano | XP |
|-------|------|------|----|
| 1 | 10-18 | 2-3 | 10-23 |
| 2 | 19-27 | 4-6 | 24-38 |
| 3 | 28-56 | 7-10 | 39-70 |

### Comportamento dos Inimigos
- **Chance de Erro**: 15%
- **Chance de Crítico**: 10%
- **IA**: Sempre ataca (não defende)

## 🧠 Estratégias

### Estratégias de Combate
1. **Agressiva**: Sempre atacar (arriscado contra inimigos fortes)
2. **Defensiva**: Defender quando vida baixa (conservadora)
3. **Mista**: Alternar entre ataque e defesa (balanceada)

### Gerenciamento de Vida
- **Defender** quando estiver com menos de 30% de vida
- **Calcular risco**: Inimigo pode te matar no próximo turno?
- **Usar Ver Status** para tomar decisões informadas

### Dicas Avançadas
```python
# Contra inimigos nível 1: Atacar sempre
# Contra inimigos nível 2: Alternar ataque/defesa  
# Contra inimigos nível 3: Defender frequentemente

# Priorize derrotar inimigos fracos para acumular XP
# Use defesa quando o inimigo tem dano alto
# Ataque quando estiver com vida suficiente para sobreviver
```

## ⌨️ Comandos e Interface

### Interface Principal
```
🧙 Status do Jogador:
❤️  Vida: 20/25
⚔️  Dano: 5
📊 Nível: 2
⭐ XP: 85/120
```

### Cores e Símbolos
- ❤️ Vida e estatísticas
- ⚔️ Dano e combate
- 📊 Nível e progresso
- ⭐ XP e recompensas
- 🎯 Ações do inimigo
- 🛡️ Defesas
- 💀 Morte

### Teclas de Atalho
- **Números 1-3**: Selecionar ações
- **Enter**: Confirmar escolhas
- **Ctrl+C**: Sair do jogo (emergência)

## 🚀 Dicas para Iniciantes

### Para Sobreviver Mais
1. **Não subestime inimigos nível 2-3**
2. **Use defesa quando vida estiver baixa**
3. **Verifique status frequentemente**
4. **Calcule se pode sobreviver ao próximo ataque**

### Farm Efficiente
1. **Derrote muitos inimigos nível 1** para XP seguro
2. **Enfrente inimigos nível 2** quando tiver vida suficiente
3. **Evite inimigos nível 3** até estar pelo menos nível 3

### Progressão Ideal
```
Nível 1: Farmar inimigos nível 1
Nível 2: Misturar inimigos nível 1 e 2  
Nível 3+: Enfrentar qualquer inimigo com estratégia
```

## 🎯 Metas e Desafios

### Metas Pessoais
- [ ] Chegar ao nível 5
- [ ] Derrotar 10 inimigos consecutivos
- [ ] Vencer um troll (nível 3) sem defender
- [ ] Acumular 500+ XP total

### Estatísticas para acompanhar
- **Maior nível alcançado**
- **Total de inimigos derrotados**
- **Maior sequência de vitórias**
- **XP total acumulado**

---

**Boa sorte em suas aventuras! Lembre-se: estratégia supera força bruta!** ⚔️🛡️✨

*"O verdadeiro herói não é o mais forte, mas o mais sábio em batalha."*
