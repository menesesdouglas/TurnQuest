from random import randint as rand, choice


class Player:
    """
    Representa o jogador do jogo.

    Attributes:
        life (int): Vida atual do jogador.
        base_life (int): Vida base máxima do jogador.
        base_damage (int): Dano base que o jogador causa.
        level (int): Nível atual do jogador.
        xp (int): Experiência acumulada do jogador.
    """

    def __init__(self):
        """Inicializa um novo jogador com vida, dano, nível e XP aleatórios."""
        self.life = rand(15, 22)
        self.base_life = self.life
        self.base_damage = 3
        self.level = 1
        self.xp = 0

    def level_up(self):
        """
        Aumenta o nível do jogador se ele tiver XP suficiente (100 ou mais).
        O aumento de nível incrementa a vida base e o dano base.
        Suporta múltiplos level-ups se XP > 100.
        """
        while self.xp >= 100:
            self.level += 1
            self.base_damage += rand(1, 3)
            self.base_life += rand(3, 6)
            self.life = self.base_life
            self.xp -= 100
            print(f"Você subiu para o nível {self.level}!")

    def attack(self):
        """
        Calcula e retorna o dano do ataque do jogador.
        Existe chance de erro ou de ataque crítico.
        """
        if rand(0, 1):
            print("Você errou o ataque.")
            return 0
        damage = self.base_damage * 2 if rand(0, 1) else self.base_damage
        if damage > self.base_damage:
            print("Ataque crítico!")
        print(f"Você atacou e causou {damage} de dano.")
        return damage

    def defend_yourself(self):
        """Ativa a defesa do jogador, reduzindo a chance de dano no turno do inimigo."""
        print("Você levantou seu escudo.")
        return True

    def get_hit_dead(self, damage_taken):
        """
        Aplica dano recebido ao jogador e verifica se ele morreu.

        Args:
            damage_taken (int): Quantidade de dano recebido.

        Returns:
            bool: True se o jogador morreu, False caso contrário.
        """
        if self.life <= 0:
            return True
        self.life -= damage_taken
        if self.life <= 0:
            self.life = 0
            print("Você morreu.")
            return True
        print(f"Você recebeu {damage_taken} de dano. Vida restante: {self.life}")
        return False

    def receive_xp(self, xp):
        """
        Adiciona XP ao jogador e verifica se há necessidade de level up.

        Args:
            xp (int): Quantidade de XP recebida.
        """
        self.xp += xp
        print(f"Você recebeu {xp} XP. Total de XP: {self.xp}")
        self.level_up()


class Enemy:
    """
    Representa um inimigo do jogo.

    Attributes:
        name (str): Nome do inimigo.
        level (int): Nível do inimigo.
        life (int): Vida atual do inimigo.
        base_damage (int): Dano base do inimigo.
        xp (int): Experiência que o inimigo concede ao ser derrotado.
    """

    def __init__(self, name):
        """Inicializa um inimigo com atributos aleatórios conforme seu nível."""
        self.name = name
        self.level = rand(1, 3)

        if self.level == 1:
            self.life = rand(10, 18)
            self.base_damage = rand(2, 3)
            self.xp = rand(10, 23)
        elif self.level == 2:
            self.life = rand(19, 27)
            self.base_damage = rand(4, 6)
            self.xp = rand(24, 38)
        else:
            self.life = rand(28, 56)
            self.base_damage = rand(7, 10)
            self.xp = rand(39, 70)

    def attack(self):
        """
        Calcula e retorna o dano do ataque do inimigo.
        Existe chance de erro ou de ataque crítico.
        """
        if rand(0, 1):
            print(f"O {self.name} errou o ataque.")
            return 0
        damage = self.base_damage * 2 if rand(0, 1) else self.base_damage
        if damage > self.base_damage:
            print("Ataque crítico!")
        print(f"{self.name} atacou e causou {damage} de dano.")
        return damage

    def get_hit_dead(self, damage_taken):
        """
        Aplica dano recebido ao inimigo e verifica se ele morreu.

        Args:
            damage_taken (int): Quantidade de dano recebido.

        Returns:
            bool: True se o inimigo morreu, False caso contrário.
        """
        if self.life <= 0:
            return True
        self.life -= damage_taken
        if self.life <= 0:
            self.life = 0
            print(f"{self.name} morreu.")
            return True
        return False

    def give_xp(self):
        """Retorna a quantidade de XP que o inimigo concede ao jogador."""
        return self.xp


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
            choice_input = int(input(prompt))
            if choice_input in valid_choices:
                return choice_input
            print(f"Escolha inválida! Digite uma das opções: {valid_choices}")
        except ValueError:
            print("Entrada inválida! Digite um número.")


def combat(player, enemy, player_first):
    """
    Executa um combate entre jogador e inimigo.

    Args:
        player (Player): O jogador.
        enemy (Enemy): O inimigo.
        player_first (bool): True se o jogador iniciar primeiro.

    Returns:
        bool: True se o jogador morreu no combate, False caso contrário.
    """
    player_dead = False
    enemy_dead = False
    defend = False

    while not player_dead and not enemy_dead:
        turns = (
            [(player, enemy, True), (enemy, player, False)]
            if player_first
            else [(enemy, player, False), (player, enemy, True)]
        )

        for attacker, defender, _ in turns:
            if attacker == player:
                choice_input = get_player_choice(
                    "\nSua vez.\nEscolha:\n1. Atacar\n2. Defender\n", [1, 2]
                )
                if choice_input == 1:
                    damage = player.attack()
                    enemy_dead = enemy.get_hit_dead(damage) if damage > 0 else enemy_dead
                    if enemy_dead:
                        xp = enemy.give_xp()
                        player.receive_xp(xp)
                        break
                else:
                    defend = player.defend_yourself()
            else:
                damage = enemy.attack()
                player_dead = player.get_hit_dead(damage) if not defend else player_dead
                defend = False

            if player_dead or enemy_dead:
                break

    return player_dead


# ----------------- Game Loop -----------------
def main():
    """Loop principal do jogo."""
    player = Player()
    game_status = 0
    enemy_names = ["Goblin", "Orc", "Troll", "Esqueleto", "Lobo"]

    while game_status == 0:
        print(
            f"\nStatus: Player\nVida: {player.life}\nLevel: {player.level}\nXP: {player.xp}"
        )

        enemy_name = choice(enemy_names)
        enemy = Enemy(enemy_name)
        print(f"\nVocê encontrou um inimigo!\n{enemy.name} - Level: {enemy.level}")

        # Iniciativa
        cara_coroa = get_player_choice("Cara ou Coroa?\n1. Cara\n2. Coroa\n", [1, 2])
        coin = rand(1, 2)
        player_first = coin == cara_coroa
        print("Você começa primeiro." if player_first else f"{enemy.name} começa primeiro.")

        player_dead = combat(player, enemy, player_first)

        continue_game = get_player_choice("\nContinuar?\n1. Sim\n0. Não\n", [0, 1])
        if not continue_game:
            game_status = 1
        elif player_dead:
            print("Você vai recomeçar com um novo personagem.")
            player = Player()

    print("\nObrigado por jogar!")


if __name__ == "__main__":
    main()
