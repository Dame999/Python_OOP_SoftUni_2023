from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("hero", 1, 100, 100)
        self.enemy_hero = Hero("enemy", 1, 50, 50)

    def test_if_initialization_is_correct(self):
        self.assertEqual(self.hero.username, "hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 100)

    def test_battle_func_enemy_username_is_the_same_as_my_hero_username_raises_exception(self):
        with self.assertRaises(Exception) as error:
            self.hero.battle(self.hero)

        self.assertEqual(str(error.exception), "You cannot fight yourself")

    def test_battle_func_if_self_health_is_less_or_equal_to_zero_raises_exception(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(error.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_func_if_enemy_health_is_less_or_equal_to_zero_raises_exception(self):
        self.enemy_hero.health = 0

        with self.assertRaises(ValueError) as error:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(str(error.exception), "You cannot fight enemy. He needs to rest")

    def test_battle_func_battle_finished_draw_returns_correct_string(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(result, "Draw")

    def test_battle_func_your_hero_wins_and_func_returns_correct_string(self):
        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, "You win")

    def test_battle_func_enemy_hero_wins_and_func_returns_correct_string(self):
        self.hero.health = 30
        self.hero.damage = 30

        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(self.enemy_hero.level, 2)
        self.assertEqual(self.enemy_hero.health, 25)
        self.assertEqual(self.enemy_hero.damage, 55)
        self.assertEqual(result, "You lose")

    def test_string_method_returns_the_correct_message(self):
        self.assertEqual(str(self.hero), "Hero hero: 1 lvl\n" +
                         "Health: 100\n" +
                         "Damage: 100\n")


if __name__ == "__main__":
    main()
