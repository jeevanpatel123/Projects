question1 = input('Question 1:\nHow many eggs in a dozen?\nA) 3\nB) 8\nC) 12\nD) 9\n\nAnswer: ')
while True:
    if question1 in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        break
    if question1 not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        print("Answer 1: Invalid Response")
        question1 = input('Question 1:\nHow many eggs in a dozen?\nA) 3\nB) 8\nC) 12\nD) 9\n\nAnswer: ')
            
question2 = input('\nQuestion 2:\nHow many fingers on one hand?\nA) 3\nB) 8\nC) 5\nD) 7\n\nAnswer: ')
while True:
    if question2 in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        break
    if question2 not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        print("Answer 1: Invalid Response")
        question2 = input('\nQuestion 2:\nHow many fingers on one hand?\nA) 3\nB) 8\nC) 5\nD) 7\n\nAnswer: ')
            
question3 = input('\nQuestion 3:\nHow many US presidents were there?\nA) 52\nB) 41\nC) 80\nD) 46\n\nAnswer: ')
while True:
    if question3 in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        break
    if question3 not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        print("Answer 1: Invalid Response")
        question3 = input('\nQuestion 3:\nHow many US presidents were there?\nA) 52\nB) 41\nC) 80\nD) 46\n\nAnswer: ')           

question4 = input('\nQuestion 4:\nHow many times has Nick sucked dick?\nA) 4\nB) 0\nC) 12\nD) Too many to count\n\nAnswer: ')
while True:
    if question4 in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        break
    if question4 not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        print("Answer 1: Invalid Response")
        question4 = input('\nQuestion 4:\nHow many times has Nick sucked dick?\nA) 4\nB) 0\nC) 12\nD) Too many to count\n\nAnswer: ')
            
question5 = input('\nQuestion 5:\nWho is on the $1 bill?\nA) Washington\nB) Nixon\nC) Jackson\nD) Lincoln\n\nAnswer: ')
while True:
    if question5 in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        break
    if question5 not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        print("Answer 1: Invalid Response")
        question5 = input('\nQuestion 5:\nWho is on the $1 bill?\nA) Washington\nB) Nixon\nC) Jackson\nD) Lincoln\n\nAnswer: ')
            
question6 = input('\nQuestion 6:\nWhat is API GEN?\nA) yes\nB) a future multi billion dollar company\nC) a horrible API made by chat GPT and pytorch\nD) A company owned by Christopher Fitzgerald and Nick Van Land-shooter\n\nAnswer: ')
while True:
    if question6 in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        break
    if question6 not in ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']:
        print("Answer 1: Invalid Response")
        question6 = input('\nQuestion 6:\nWhat is API GEN?\nA) yes\nB) a future multi billion dollar company\nC) a horrible API made by chat GPT and pytorch\nD) A company owned by Christopher Fitzgerald and Nick Van Land-shooter\n\nAnswer: ')
            
question7 = input('\nQuestion 7:\nAre you picking cotton for $200 an hour?\nA) yes\nB) no\n\nAnswer: ')
while True:
    if question7 in ['A', 'B', 'a', 'b']:
        break
    if question7 not in ['A', 'B', 'a', 'b']:
        print("Answer 1: Invalid Response")
        question7 = input('\nQuestion 7:\nAre you picking cotton for $200 an hour?\nA) yes\nB) no\n\nAnswer: ')
        

print("\nScoring:")

if question1 in ['C', 'c']:
    print("Answer 1: Correct")
    score1 = 1
else:
    print("Answer 1: Incorrect")
    score1 = 0
        

if question2 in ['C', 'c']:
    print("Answer 2: Correct")
    score2 = 1
else:
    print("Answer 2: Incorrect")
    score2 = 0
        

if question3 in ['D', 'd']:
    print("Answer 3: Correct")
    score3 = 1
else:
    print("Answer 3: Incorrect")
    score3 = 0
        

if question4 in ['D', 'd']:
    print("Answer 4: Correct")
    score4 = 1
else:
    print("Answer 4: Incorrect")
    score4 = 0
 

if question5 in ['A', 'a']:
    print("Answer 5: Correct")
    score5 = 1
else:
    print("Answer 5: Incorrect")
    score5 = 0
        

if question6 in ['B', 'b', 'D', 'd']:
    print("Answer 6: Correct")
    score6 = 1
else:
    print("Answer 6: Incorrect")
    score6 = 0
        

if question7 in ['A', 'a']:
    print("Answer 7: Correct")
    score7 = 1
else:
    print("Answer 7: Incorrect")
    score7 = 0

final_score = print("\nYour score: ", str(score1 + score2 + score3 + score4 + score5 + score6 + score7) + "/7")