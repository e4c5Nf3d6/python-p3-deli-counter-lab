katz_deli = []

def line(l):
    if len(l) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for person in l:
            message = message + " " + f"{l.index(person) + 1}. {person}"
        print(message)
        
def take_a_number(l, name):
    l.append(name)
    print(f"Welcome, {name}. You are number {len(l)} in line.")

def now_serving(l):
    if len(l) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {l[0]}.")
        l.pop(0)
