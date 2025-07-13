import os
from cleam_table import CleanTable
from model import Model
from test_model import TestTable
from naive_bayes import ProbabilityCalculating

class UI:
    def __init__(self):
        self.user_table = None
        self.model = None
        self.test = None

    def login_menu(self):
        print("----Naive Bayesian classifier----")

        while True:
            path = input("Enter A Dataset Path: ").strip('\'"')
            if os.path.exists(path) and path.endswith('.csv'):
                break
            else:
                print("File not found or not a CSV file. Please try again.")

        self.user_table = CleanTable(path)
        self.model = Model(self.user_table.table)

    def menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Check the success rate")
            print("2. Insert a line for prediction")
            print("3. Exit")

            user_input = input("Enter your choice between 1-3: ")
            match user_input:
                case "1":
                    self.test = TestTable(self.user_table.table)
                    print(f"Success rate: {self.test.test()}")
                case "2":
                    self.choice()
                case "3":
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please enter 1, 2, or 3.")




    def choice(self):

        user_input = {}

        for feature in self.model.features:
            print(f"\nChoose a value for '{feature}':")

            unique_values = list(self.user_table.table[feature].unique())

            for idx, value in enumerate(unique_values):
                print(f"{idx + 1}. {value}")

            while True:
                try:
                    choice = int(input("Enter the number of your choice: ")) - 1
                    if 0 <= choice < len(unique_values):
                        user_input[feature] = unique_values[choice]
                        break
                    else:
                        print("Invalid number. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        prediction = ProbabilityCalculating.result(user_input, self.model.model, self.model.target_variable())
        print("\nPrediction result:", prediction)




u = UI()
u.login_menu()
u.menu()