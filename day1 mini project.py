import random
number = random.randint(1,10)
guess = 0
attempt = 0
print('enter a numbet between 1 and 10 ')
while guess !=number:
      guess = int(input("Enter your guess"))
      attempt += 1
      if attempt>5:
            print('game is over !') 
            print('answer is :',number)    
      if guess<number:
            print('too low !')
      elif guess>number:
            print('too high !')
      
      else:
           

                  
            print('correct gessed it')  
            print('your attempt is ',attempt)












