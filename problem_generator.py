class Operand:
    def __init__(self):
        self.num_digits = 1
        self.negative = False
        self.whole_number = True
        self.value = 0
        self.decimal_value = 0
    def print_val(self):
        print(self.value)

class Problems:
    def __init__(self):
        self.answer_key = "n"
        self.number_of_problems = 10
        self.number_of_operands = 2
        self.addition = "n"
        self.subtraction = "n" 
        self.multiplication = "n" 
        self.division = "n"
        self.whole = "n"
        self.decimal = "n" 
        self.fraction = "n" 
        self.negative = "n" 

    def show_options(self):
        print("Summary of problem selection")
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)

    def update_options(self):
        print(f"Please update the problem settings")
        for attribute, value in self.__dict__.items():
            if attribute in ["number_of_problems", "number_of_operands"]:
                new_value = int(input(f"Please enter the {attribute}, preferably < 100: "))
            else:
                new_value = input(f"{attribute} (y/n): ").lower()
            setattr(self, attribute, new_value)

def print_problem_selection(problem_settings):
    print("Here is your problem selection")
    for key, value in problem_settings.items():
        if key == "Number of Problems":
            print(f"{key}: {value}")
        else:
            print(f"{key}: {'Yes' if value else 'No'}")

def update_problem_selection(problem_settings):
    for key in problem_settings:
        if key == "Number of Problems":
            user_select = input(f"Please enter the {key}, preferably < 100: ")
            problem_settings[key] = user_select
        else:
            user_select = input(f"{key} (Y/N): ")
            problem_settings[key] = True if user_select.lower() == "y" else False

    print_problem_selection(problem_settings)

def update_operand_selection(operands):
    for index, inst in enumerate(operands):
        inst.num_digits = input(f"Num digits for operand{index+1}:")
        inst.negative = input(f"Is this operand negative (y/n): ")
        inst.whole_number = True if input(f"Is this operand a whole number (y/n): ").lower() == 'y' else False
        print(f"operand{index+1} has {inst.num_digits} digits")
        print(f"operand{index+1} is whole number: {inst.whole_number}")
        print(f"operand{index+1} is negative: {inst.negative}")



def main():
    practice = Problems()
    practice.update_options()
    practice.show_options()

    operands = []
    for index in range(practice.number_of_operands):
        operands.append(Operand())
    print(operands)
         
if __name__ == "__main__":
    print("Welcome to the math problem generator!")
    main()
