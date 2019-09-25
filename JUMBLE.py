class Jumble:
    def playplay(): 
        import random
        
        def choose():
            words=['rainbow','class','friendship','trust','relationship']
            pick=random.choice(words)
            return pick
        def jumble(words):
            jumbled=" ".join(random.sample(words,len(words)))
            return jumbled
        def thank(player1,player2,pp1,pp2):
            print(player1,"your score", pp1)
            print(player2,"your score",pp2)
            
        
        def play():
            player1=input("enter your name,player 1")
            player2=input("enter your name,player 2")
            pp1=0
            pp2=0
            turn=0
            while(1):
                picked_word=choose()
                qn=jumble(picked_word)
                print(qn)
                if turn%2==0:
                    print(player1,"this is your chance")
                    ans=input("what is in your mind")
                    
                    if ans==picked_word:
                        pp1+=1
                        print("the score of player 1 is",pp1)
                    else:
                        print("better luck next time i thought word is ",picked_word)
                        
                else:
                    print(player2,"this is your chance")
                    ans=input("what is in your mind")
                    if ans==picked_word:
                        pp2+=1
                        print("the score of player 2 is",pp2)
                    else:
                        print("better luck next time i thought word is ",picked_word)
                    
                c=int(input("take 1 for the continue,0 to quit"))
                if c==0:
                    thank(player1,player2,pp1,pp2)
                    break
                turn=turn+1
                
        play()       
