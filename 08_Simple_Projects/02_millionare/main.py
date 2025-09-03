#v0.1
questions = [
    ["Who painted Mona Lisa?", "Claude Monet", "Pablo Picasoo", "Leonardo Da Vince", "Vincent van Gogh", 3],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", 2],
    ["Who wrote 'Hamlet'?", "Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen", 2],
    ["What is the largest mammal?", "Elephant", "Blue Whale", "Giraffe", "Hippopotamus", 2],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Silver", "Iron", 2]
]

prizes = [100, 200, 300, 500, 1000, 2000]
init_prize = 0

for question in questions:
    print(question[0])
    print(f"A: {question[1]}")
    print(f"B: {question[2]}")
    print(f"C: {question[3]}")
    print(f"D: {question[4]}")

    ans = int(input("1->A, 2->B, 3->C, 4->D"))
    if (question[5] == ans):
        print("Correct!")
    else:
        print(f"Incorrect!, the correct answer was {question[5]}")
        break
    print(f"You won {prizes[init_prize]}")
    init_prize += 1