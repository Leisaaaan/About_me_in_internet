class Service:

    def __init__(self):
        self.useful_information_db = [
            {"title" : "Постановление 1", "year" : 2024},
            {"title" : "Постановление 2", "year" : 2025}
        ]

    def get_all_information(self):
        return self.useful_information_db



service = Service()