import random
class Operand:
    def __init__(self):
        self.num_digits = 1
        self.num_decimal_digits = 0
        self.negative = "n"
        self.whole_number = "n"
        #self.value = 0
        #self.decimal_value = 0

    def print_operand_settings(self):
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)

    def update_operand_settings(self, whole_numbers, negatives):
        self.num_digits = int(input(f"Number of digits: "))
        self.whole_number = whole_numbers
        if self.whole_number != "y":
            self.num_decimal_digits = int(input(f"Number of decimal digits: "))
        self.negative = negatives
        #self.negative = input(f"Is negative (y/n): ")
        #self.whole_number = input(f"Is whole number (y/n): ")

    def generate_val(self):
        value, decimal_value = 0, 0
        for i in range(self.num_digits):
            min_val = 1 if i == 0 else 0
            d = random.randint(min_val,9)
            value *= 10
            value += d



        if self.whole_number != "y":
            for i in range(self.num_decimal_digits):
                decimal_d = random.randint(0,9)
                decimal_value *= 10
                decimal_value += decimal_d
            decimal = f"0.{decimal_value}"
            value += float(decimal)

        if self.negative == "y":
            value *= random.choice([1, -1])

        return value

class Problems:
    def __init__(self):
        self.answer_key = "n"
        self.number_of_problems = 10
        self.number_of_operands = 2
        self.addition = "y"
        self.subtraction = "n" 
        self.multiplication = "n" 
        self.division = "n"
        self.whole = "n"
        self.fraction = "n" 
        self.negative = "n" 
        self.operators = []
        self.operands = Operand()

    def show_options(self):
        print("Summary of problem selection")
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)

    def update_options(self):
        print(f"Please update the problem settings")
        for attribute, value in self.__dict__.items():
            if attribute == "operands":
                continue
            if attribute in ["number_of_problems", "number_of_operands"]:
                new_value = int(input(f"Please enter the {attribute}, preferably < 100: "))
            else:
                new_value = input(f"{attribute} (y/n): ").lower()
            setattr(self, attribute, new_value)

    def update_operators(self):
        if self.addition == 'y':
            self.operators.append('+')
        if self.subtraction == 'y':
            self.operators.append('-')
        if self.multiplication == 'y':
            self.operators.append('*')
        if self.division == 'y':
            self.operators.append('/')

    def update_operands(self):
        self.operands.update_operand_settings(self.whole, self.negative)
        self.operands.print_operand_settings()


def main():
    practice = Problems()
    practice.update_options()
    practice.update_operands()
    #practice.show_options()

    problems = []
    for i in range(practice.number_of_problems):
        operands = []
        for j in range(practice.number_of_operands):
            operands.append(practice.operands.generate_val())
        problems.append(operands)

    for prob in problems:
        print(prob)



         
if __name__ == "__main__":
    print("Welcome to the math problem generator!")
    main()
