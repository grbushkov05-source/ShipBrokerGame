def print_header(title):
    print("="*len(title))
    print(title)
    print("="*len(title))

def choose_from_list(items, prompt="Выберите:"):
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    choice = 0
    while choice < 1 or choice > len(items):
        try:
            choice = int(input(prompt + " "))
        except ValueError:
            choice = 0
    return choice - 1
