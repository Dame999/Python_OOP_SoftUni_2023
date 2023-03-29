from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("some name", "some type", "some sound")

    def test_if_initialization_is_correct(self):
        self.assertEqual(self.mammal.name, "some name")
        self.assertEqual(self.mammal.type, "some type")
        self.assertEqual(self.mammal.sound, "some sound")

    def test_make_sound_func_returns_correct_string(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "some name makes some sound")

    def test_get_kingdom_is_returning_correct_value(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info_returns_the_correct_string(self):
        result = self.mammal.info()
        self.assertEqual(result, "some name is of type some type")


if __name__ == "__main__":
    main()