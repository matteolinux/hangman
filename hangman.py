import random
from hangman_words import word_list
from hangman_logo import logo
from hangman_stages import stages

lives = 6

#words = ["autunno","primavera","natale"]
hidden_list = []
chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)

#try with list comprehension instead of list.append()----------------

''' for letter in chosen_word:
        hidden_list.append("_") '''
        
hidden_list = ["_"]*len(chosen_list)
        
            
#---------------------------------------
print()

print(logo)

print()
print(f"The chosen word is: ")
print()
print(chosen_list)
print()
print(f"The hidden list is : ")
print()
print(hidden_list)


start_game = True

while start_game:
    
    print()
    
    chosen_letter = input("Choose a letter: ")
    
    if chosen_letter in hidden_list:
        
        is_guessed = True
        
        while is_guessed:
    
            print("Already Guessed! Try Another One!")
            chosen_letter = input("Choose a letter: ")
            if chosen_letter not in hidden_list:
                is_guessed = False
            else:
                continue
        

    print()
    
    
    # try with index counter ------------------------------------------
    
    ''' index_counter = 0
    
    for letter in chosen_list:
        if letter == chosen_letter:
            index = chosen_list.index(letter, index_counter)
            hidden_list[index] = chosen_letter
            index_counter = (index + 1) '''
     
    # try with enumerate ------------------------------------------        
            
    for index,letter in enumerate(chosen_list):
        if letter == chosen_letter:
            hidden_list[index] = chosen_letter    
            
       
    
    #-------------------------------------------------------------
    print("Updated Hidden List: ") 
    print()
    print(hidden_list) 
    print()
    
    if chosen_letter not in chosen_list:
        if lives > 0:          
            lives -= 1
            print(f"You lose one life! Lives remaining: {lives}")
            print()
            
            match (lives):
                case 5:
                    print(stages[-1])
                case 4:
                    print(stages[-2])
                case 3:
                    print(stages[-3])
                case 2:
                    print(stages[-4])
                case 1:
                    print(stages[-5])
                case 0:
                    print(stages[-6])
                
                
            print()
        else:
            print("You lose!")
            print()
            print(stages[-7])
            print()
            play_again = True
            while play_again:
                new_match = input("Play Again? (y/n): ")
                if new_match == "y":
                    lives = 5
                    chosen_word = ""
                    chosen_word = random.choice(word_list)
                    chosen_list = list(chosen_word)
                    hidden_list = []
                    for letter in chosen_word:
                        #hidden_list.append("_")
                        hidden_list = ["_"]*len(chosen_list)
                    print()    
                    print(f"The chosen word is: ")
                    print()
                    print(chosen_list)
                    print()
                    print(f"The hidden list is : ")
                    print()
                    print(hidden_list)    
                    play_again = False
                elif new_match == "n":
                    print()
                    start_game = False
                    play_again = False
                
                else:
                    continue
                
                
       
                    
    if hidden_list == chosen_list:
        
        print("You Win!")
        print()
        play_again = True
        while play_again:
            new_match = input("Play Again? (y/n): ")
            if new_match == "y":
                lives = 5
                chosen_word = ""
                chosen_word = random.choice(word_list)
                chosen_list = list(chosen_word)
                hidden_list = []
                for letter in chosen_word:
                    #hidden_list.append("_")
                    hidden_list = ["_"]*len(chosen_list)
                print()    
                print(f"The chosen word is: ")
                print()
                print(chosen_list)
                print()
                print(f"The hidden list is : ")
                print()
                print(hidden_list)    
                play_again = False
            elif new_match == "n":
                print()
                start_game = False
                play_again = False
                
            else:
                continue
                      
    
     #END   -----------------------------------------

