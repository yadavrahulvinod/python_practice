import random

computer_score=0
user_score=0

options=["rock","paper","scissors"]

while computer_score < 3 and user_score <3 :
 user_input= input("select one options/rock(r)/paper(p)/scissors(s) or q for Quit").lower()
 
 if user_input in ["q","quit"]:
   print("you quit")
   break
 
 if user_input not in options:
   print("please select a right options")
   continue  

 random_val = random.randint(0,2)
 computer_input =options[random_val]
 
 if user_input == "scissors"  and computer_input == "paper" :
  user_score+=1
  print("you won!")
  print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
  print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
  continue
 if user_input =="paper" and computer_input == "scissors":
   computer_score+=1
   print("computer won !")
   print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
   print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
   continue
 if user_input =="paper" and computer_input == "rock" :
   user_score +=1
   print("you won!")
   print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
   print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
   continue
 if user_input == "rock" and computer_input =="paper":
   computer_score+=1
   print("computer won !")
   print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
   print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
   continue
 if user_input =="rock" and computer_input =="scissors":
   user_score +=1
   print("you won!")
   print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
   print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
   continue
 if user_input =="scissors" and computer_input=="rock":
   computer_score+=1
   print("computer won !")
   print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
   print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
   continue
 else :
   print("its a draw")
   print("computer picked : "+str(computer_input)+" "+"user picked : "+str(user_input))
   print("User Score : "+ str(user_score)+" "+"Computers Score : "+str(computer_score))
   continue 