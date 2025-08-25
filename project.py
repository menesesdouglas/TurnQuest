from random import randint, choice


class Player:
    """
    Representa o jogador do jogo com atributos e métodos para combate e progressão.
    
    Attributes:
        current_life (int): Vida atual do jogador.
        max_life (int): Vida máxima do jogador.
        base_damage (int): Dano base que o jogador causa.
        level (int): Nível atual do jogador.
        xp (int): Experiência acumulada do jogador.
        xp_to_next_level (int): XP necessário para o próximo nível.
    """

    def __init__(self):
        """Inicializa um novo jogador com atributos aleatórios."""
        self.current_life = randint(15, 22)
        self.max_life = self.current_life
        self.base_damage = 3
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def level_up(self):
        """
        Aumenta o nível do jogador se ele tiver XP suficiente.
        O aumento de nível incrementa a vida máxima e o dano base.
        Suporta múltiplos level-ups se XP > xp_to_next_level.
        """
        levels_gained = 0
        
        while self.xp >= self.xp_to_next_level:
            self.level += 1
            levels_gained += 1
            self.base_damage += randint(1, 3)
            self.max_life += randint(3, 6)
            self.current_life = self.max_life
            self.xp -= self.xp_to_next_level
            # Aumenta o XP necessário para o próximo nível
            self.xp_to_next_level = int(self.xp_to_next_level * 1.2)
        
        if levels_gained > 0:
            print(f"Você subiu {levels_gained} nível(s)! Agora é nível {self.level}!")
            print(f"Vida máxima: {self.max_life}, Dano base: {self.base_damage}")
            print(f"Próximo nível em: {self.xp_to_next_level} XP")

    def attack(self):
        """
        Calcula e retorna o dano do ataque do jogador.
        Existe chance de erro (20%) ou de ataque crítico (15%).
        
        Returns:
            int: Dano causado pelo ataque (0 se errou)
        """
        # 20% de chance de errar
        if randint(1, 100) <= 20:
            print("Você errou o ataque!")
            return 0
        
        # 15% de chance de crítico
        is_critical = randint(1, 100) <= 15
        damage = self.base_damage * 2 if is_critical else self.base_damage
        
        if is_critical:
            print("⭐ Ataque crítico! ⭐")
        
        print(f"Você atacou e causou {damage} de dano.")
        return damage

    def defend(self):
        """
        Ativa a defesa do jogador, reduzindo a chance de dano no turno do inimigo.
        
        Returns:
            bool: True indicando que a defesa está ativa
        """
        print("🛡️ Você levantou seu escudo! Dano reduzido no próximo ataque.")
        return True

    def take_damage(self, damage_amount):
        """
        Aplica dano recebido ao jogador e verifica se ele morreu.
        
        Args:
            damage_amount (int): Quantidade de dano recebido.
            
        Returns:
            bool: True se o jogador morreu, False caso contrário.
        """
        if damage_amount <= 0:
            return False
            
        self.current_life -= damage_amount
        
        if self.current_life <= 0:
            self.current_life = 0
            print("💀 Você morreu!")
            return True
        
        print(f"💥 Você recebeu {damage_amount} de dano. Vida restante: {self.current_life}/{self.max_life}")
        return False

    def gain_xp(self, xp_amount):
        """
        Adiciona XP ao jogador e verifica se há necessidade de level up.
        
        Args:
            xp_amount (int): Quantidade de XP recebida.
        """
        if xp_amount <= 0:
            return
            
        self.xp += xp_amount
        print(f"✨ Você recebeu {xp_amount} XP. Total: {self.xp}/{self.xp_to_next_level}")
        self.level_up()
        
    def display_status(self):
        """Exibe o status atual do jogador."""
        print(f"\n🧙 Status do Jogador:")
        print(f"❤️  Vida: {self.current_life}/{self.max_life}")
        print(f"⚔️  Dano: {self.base_damage}")
        print(f"📊 Nível: {self.level}")
        print(f"⭐ XP: {self.xp}/{self.xp_to_next_level}")


class Enemy:
    """
    Representa um inimigo do jogo com atributos baseados no nível.
    
    Attributes:
        name (str): Nome do inimigo.
        level (int): Nível do inimigo.
        current_life (int): Vida atual do inimigo.
        max_life (int): Vida máxima do inimigo.
        base_damage (int): Dano base do inimigo.
        xp_reward (int): Experiência que o inimigo concede ao ser derrotado.
    """

    def __init__(self, name):
        """Inicializa um inimigo com atributos aleatórios conforme seu nível."""
        self.name = name
        self.level = randint(1, 3)

        if self.level == 1:
            self.max_life = randint(10, 18)
            self.base_damage = randint(2, 3)
            self.xp_reward = randint(10, 23)
        elif self.level == 2:
            self.max_life = randint(19, 27)
            self.base_damage = randint(4, 6)
            self.xp_reward = randint(24, 38)
        else:
            self.max_life = randint(28, 56)
            self.base_damage = randint(7, 10)
            self.xp_reward = randint(39, 70)
            
        self.current_life = self.max_life

    def attack(self):
        """
        Calcula e retorna o dano do ataque do inimigo.
        Existe chance de erro (15%) ou de ataque crítico (10%).
        
        Returns:
            int: Dano causado pelo ataque (0 se errou)
        """
        # 15% de chance de errar
        if randint(1, 100) <= 15:
            print(f"🎯 {self.name} errou o ataque!")
            return 0
        
        # 10% de chance de crítico
        is_critical = randint(1, 100) <= 10
        damage = self.base_damage * 2 if is_critical else self.base_damage
        
        if is_critical:
            print(f"💢 {self.name} acertou um ataque crítico!")
        
        print(f"{self.name} atacou e causou {damage} de dano.")
        return damage

    def take_damage(self, damage_amount):
        """
        Aplica dano recebido ao inimigo e verifica se ele morreu.
        
        Args:
            damage_amount (int): Quantidade de dano recebido.
            
        Returns:
            bool: True se o inimigo morreu, False caso contrário.
        """
        if damage_amount <= 0:
            return False
            
        self.current_life -= damage_amount
        
        if self.current_life <= 0:
            self.current_life = 0
            print(f"🎉 {self.name} foi derrotado!")
            return True
            
        print(f"{self.name} recebeu {damage_amount} de dano. Vida: {self.current_life}/{self.max_life}")
        return False

    def display_info(self):
        """Exibe informações sobre o inimigo."""
        print(f"\n👹 Inimigo encontrado: {self.name}")
        print(f"📊 Nível: {self.level}")
        print(f"❤️  Vida: {self.current_life}/{self.max_life}")
        print(f"⚔️  Dano: {self.base_damage}")


def get_player_choice(prompt, valid_choices):
    """
    Solicita ao jogador uma escolha e garante que seja válida.
    
    Args:
        prompt (str): Texto exibido para o jogador.
        valid_choices (list): Lista de opções válidas (inteiros).
        
    Returns:
        int: Escolha válida do jogador.
    """
    while True:
        try:
            print(f"\n{prompt}")
            choice_input = int(input("Sua escolha: "))
            
            if choice_input in valid_choices:
                return choice_input
                
            print(f"❌ Escolha inválida! Opções válidas: {valid_choices}")
            
        except ValueError:
            print("❌ Por favor, digite um número válido.")


def combat_round(player, enemy, is_player_turn, is_defending=False):
    """
    Executa uma rodada de combate.
    
    Args:
        player (Player): O jogador.
        enemy (Enemy): O inimigo.
        is_player_turn (bool): True se for a vez do jogador.
        is_defending (bool): True se o jogador está defendendo.
        
    Returns:
        tuple: (player_died, enemy_died, continue_defending, turn_consumed)
    """
    player_died = False
    enemy_died = False
    continue_defending = False
    turn_consumed = True  # Por padrão, o turno é consumido
    
    if is_player_turn:
        action = get_player_choice(
            "Sua vez de agir:\n1. ⚔️ Atacar\n2. 🛡️ Defender\n3. ℹ️ Ver status",
            [1, 2, 3]
        )
        
        if action == 1:
            damage = player.attack()
            if damage > 0:
                enemy_died = enemy.take_damage(damage)
        elif action == 2:
            continue_defending = player.defend()
        else:
            player.display_status()
            enemy.display_info()
            turn_consumed = False  # Não consome o turno quando apenas visualiza status
            
    else:
        damage = enemy.attack()
        if damage > 0:
            # Reduz dano se o jogador estiver defendendo
            if is_defending:
                damage = max(1, damage // 2)
                print("🛡️ Sua defesa reduziu o dano pela metade!")
                
            player_died = player.take_damage(damage)
    
    return player_died, enemy_died, continue_defending, turn_consumed


def combat(player, enemy, player_starts_first):
    """
    Executa um combate completo entre jogador e inimigo.
    
    Args:
        player (Player): O jogador.
        enemy (Enemy): O inimigo.
        player_starts_first (bool): True se o jogador iniciar primeiro.
        
    Returns:
        bool: True se o jogador morreu no combate, False caso contrário.
    """
    print(f"\n⚔️ COMBATE INICIADO! ⚔️")
    enemy.display_info()
    
    player_died = False
    enemy_died = False
    is_defending = False
    
    # Sequência de turnos
    while not player_died and not enemy_died:
        turns = [player_starts_first, not player_starts_first]
        
        for is_player_turn in turns:
            if player_died or enemy_died:
                break
                
            player_died, enemy_died, is_defending, turn_consumed = combat_round(
                player, enemy, is_player_turn, is_defending
            )
            
            # Se o jogador apenas visualizou status, não avançamos para o próximo turno
            if is_player_turn and not turn_consumed:
                turns.append(is_player_turn)  # Adiciona outro turno do jogador
    
    if enemy_died:
        xp_reward = enemy.xp_reward
        player.gain_xp(xp_reward)
        print(f"🎯 Você derrotou {enemy.name} e ganhou {xp_reward} XP!")
    
    return player_died


def determine_initiative():
    """
    Determina quem começa o combate através de uma escolha de cara ou coroa.
    
    Returns:
        bool: True se o jogador começa primeiro, False se o inimigo começa.
    """
    print("\n🎲 Cara ou Coroa para determinar quem começa!")
    
    player_choice = get_player_choice(
        "Escolha:\n1. 👤 Cara\n2. 🪙 Coroa",
        [1, 2]
    )
    
    coin_flip = randint(1, 2)
    player_won = coin_flip == player_choice
    
    if player_won:
        print("🎉 Você ganhou a iniciativa! Você começa primeiro.")
    else:
        print("😟 Você perdeu a iniciativa. O inimigo começa primeiro.")
    
    return player_won


def main():
    """Loop principal do jogo."""
    print("🎮 Bem-vindo ao RPG de Combate! 🎮")
    print("Você enfrentará inimigos aleatórios e ganhará XP para subir de nível.\n")
    
    player = Player()
    game_running = True
    enemy_names = ["Goblin", "Orc", "Troll", "Esqueleto", "Lobo", "Bandido", "Aranha Gigante"]
    enemies_defeated = 0
    
    while game_running:
        player.display_status()
        
        # Gerar inimigo aleatório
        enemy_name = choice(enemy_names)
        enemy = Enemy(enemy_name)
        
        print(f"\n🌲 Você encontrou um {enemy_name} nível {enemy.level}!")
        
        # Determinar iniciativa
        player_starts_first = determine_initiative()
        
        # Executar combate
        player_died = combat(player, enemy, player_starts_first)
        
        if player_died:
            restart = get_player_choice(
                "💀 Game Over!\nDeseja recomeçar?\n1. ✅ Sim\n2. ❌ Não",
                [1, 2]
            )
            
            if restart == 1:
                player = Player()
                enemies_defeated = 0
                print("\n✨ Novo personagem criado! Boa sorte!")
            else:
                game_running = False
        else:
            enemies_defeated += 1
            continue_playing = get_player_choice(
                f"🏆 Inimigos derrotados: {enemies_defeated}\nDeseja continuar?\n1. ✅ Sim\n2. ❌ Não",
                [1, 2]
            )
            
            if continue_playing == 2:
                game_running = False
    
    print("\n🎯 Obrigado por jogar!")
    print(f"📊 Estatísticas finais:")
    print(f"   Nível alcançado: {player.level}")
    print(f"   Inimigos derrotados: {enemies_defeated}")
    print(f"   XP total acumulado: {player.xp}")


if __name__ == "__main__":
    main()