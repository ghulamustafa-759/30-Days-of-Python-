import random
import words
import stage


stages = stage.stages
display = []
word_list = words.word_list
chosen_word = random.choice(word_list).lower()
leng = len(chosen_word)
lives = 6
#print(chosen_word)
for _ in range(leng):
    display += "_"
print(*display)

endOfGame =  False
while not endOfGame:
    guess = input("Guess an alphabet : ").lower()
    if guess in display:
      print("Letter already guessed")
    for i in range(leng):
        a = chosen_word[i]
        if guess == a:
            display[i] = a
                

    if guess not in display:
      print(stages[lives])
      print("You guessed the letter wrong, you lose a life.")
      lives-=1
      
      
    if lives == -1:
      endOfGame = True
      print("You Lose.")
      print(f"the word was : {chosen_word}")
    print(*display)
    #print(lives)
    if  "_" not in display:
      endOfGame = True
      print("You win.")