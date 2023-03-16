from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        revenue_for_a_race = - 250_000
        sponsors = {
            "Oracle": {1: 1_500_000, 2: 800_000},
            "Honda": {8: 20_000, 10: 10_000},
        }

        for sponsor, values in sponsors.items():
            for position, price in values.items():
                if race_pos <= position:
                    revenue_for_a_race += price
                    break
        self.budget += revenue_for_a_race
        return f"The revenue after the race is {revenue_for_a_race}$. Current budget {self.budget}$"
