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



def main():
    print("Please select the type of problems you want to generate")
    problem_settings = {
        "Answer Key": False, 
        "Number of Problems": 10, 
        "Addition": False, 
        "Subtraction": False, 
        "Multiplication": False, 
        "Division": False, 
        "Whole" : False, 
        "Decimal": False, 
        "Fraction": False, 
        "Negative": False, 
    }

    update_problem_selection(problem_settings)
         
if __name__ == "__main__":
    print("Welcome to the math problem generator!")
    main()
