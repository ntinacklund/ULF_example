from random import randint

def generate_list():
    numbers = []
    
    for _ in range(1000):
        numbers.append(randint(1, 25))
    return numbers    

def larger_than_in_list(numbers):
    
    counter = 0
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]: counter +=1
    
    return counter

def count_uniques(numbers):
    uniques = set(numbers)
    return len(uniques)

if __name__ == "__main__":
    generated_numbers = generate_list()
    larger_count = larger_than_in_list(generated_numbers)
    uniques = count_uniques(generated_numbers)
    print(f"Uniques in list: {uniques}. \nItems larger than next: {larger_count}")