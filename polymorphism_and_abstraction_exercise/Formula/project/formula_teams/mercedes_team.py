from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int):
        revenue_for_a_race = - 200_000
        sponsors = {
            "Petronas": {1: 1_000_000, 3: 500_000},
            "TeamViewer": {5: 100_000, 7: 50_000},
        }

        for sponsor, values in sponsors.items():
            for position, price in values.items():
                if race_pos <= position:
                    revenue_for_a_race += price
                    break
        self.budget += revenue_for_a_race
        return f"The revenue after the race is {revenue_for_a_race}$. Current budget {self.budget}$"
