from random import randint

def generate_floors():
    floors = []
    
    for _ in range(1000):
        floor = randint(1, 2)
        if floor == 1: floors.append(1)
        else: floors.append(-1)
    return floors 

def check_floor(floors):
    floor_count = 0
    for instruction in floors:
        floor_count += instruction
    print(f"You're on the {floor_count} floor.")

if __name__ == "__main__":
    check_floor(generate_floors())