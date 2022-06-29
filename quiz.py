def menu():
    title="Welcome to KBC"
    print(title.center(100))
    t1="1) Press 1 to PLAY"
    print(t1.center(99))
    t2="2) Press 2 to EXIT"
    print(t2.center(99))
    
    while True:
        choice=int(input("Enter your choice:"))
        if choice==1:
            play()
            break

        elif choice==2:
            exit()
        else:
            print("Invalid choice,enter again!!")


def play():
    dict = {}
    l1=[]

    def q1():
        score=0
        ques="--> Who is Kapil Sharma? \n a) Bollywood Actor \tb) Comedian\n c) Singer \t\td) Cricketer"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="b"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="a" or ans=="d":
                score-=20
                l1.append((ques,ans,corr_ans))
                break
            
            else:
                print("Invalid answer..")
            
        return score
        
        
    
    
    def q2():
        score=q1()
        ques="\n--> Who is Anushka Sharma married to? \n a) Ranveer Singh \tb) Ranbir Kapoor\n c) Varun Dhawan \td) Virat Kohli"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="d"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="a" or ans=="b":
                score-=20
                l1.append((ques,ans,corr_ans))
                break

            else:
                print("Invalid answer..")
        return score

    def q3():
        score=q2()
        ques="\n--> Which state of India has shortest coastline? \n a) Goa \t\tb) Maharashtra\n c) Andhra Pradesh \td) West Bengal"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="a"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="d" or ans=="b":
                score-=20
                l1.append((ques,ans,corr_ans))
                break

            else:
                print("Invalid answer..")
                
        return score

    def q4():
        score=q3()
        ques="\n--> Alia Bhatt has starred in which of the following movies? \n a) Luka Chuppi \tb) Highway\n c) Pati Patni Aur Woh \td) Son of Sardaar"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="b"
            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="d" or ans=="a":
                score-=20
                l1.append((ques,ans,corr_ans))
                break
            else:
                print("Invalid answer..")
                
        return score

    def q5():
        score=q4()
        ques="--> How many colors are there in rainbow? \n a) 4 \t\t\tb) 9\n c) 7 \t\t\td) 11"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="c"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="b" or ans=="a" or ans=="d":
                score-=20
                l1.append((ques,ans,corr_ans))
                break
            
            else:
                print("Invalid answer..")
            
        return score
        
        
    
    
    def q6():
        score=q5()
        ques="\n--> How many days are there in a year? \n a) 360 \t\tb) 370\n c) 365 \t\td) 300"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="c"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="d" or ans=="a" or ans=="b":
                score-=20
                l1.append((ques,ans,corr_ans))
                break

            else:
                print("Invalid answer..")
        return score

    def q7():
        score=q6()
        ques="\n--> Who is the President of the United States? \n a) Donald Trump \tb) Barack Obama\n c) Melania Trump \td) Hillary Clinton"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="a"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="d" or ans=="b":
                score-=20
                l1.append((ques,ans,corr_ans))
                break

            else:
                print("Invalid answer..")
                
        return score

    def q8():
        score=q7()
        ques="\n--> Python language was invented by? \n a) L. Possum \t\tb) Guido Van Rossum\n c) J.W. Pearson \td) James Gosling"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="b"
            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="d" or ans=="a":
                score-=20
                l1.append((ques,ans,corr_ans))
                break
            else:
                print("Invalid answer..")
                
        return score

    def q9():
        score=q8()
        ques="\n--> In the popular TV Show Taarak Mehta Ka Ooltah Chashmah, Dilip Joshi plays which character? \n a) Jethalal \t\tb) Taarak Mehta\n c) Champaklal \t\td) Sodhi"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="a"

            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="d" or ans=="b":
                score-=20
                l1.append((ques,ans,corr_ans))
                break

            else:
                print("Invalid answer..")
                
        return score

    def q10():
        score=q9()
        ques="\n--> Facebook is owned by? \n a) Bill Gates \t\tb) Sundar Pichai\n c) Steve Jobs \t\td) Mark Zuckerberg"
        print(ques)
        while True:
            ans=input("Enter your answer:")
            corr_ans="d"
            if ans==corr_ans:
                score+=50
                dict[ques] = ans
                break

            elif ans=="c" or ans=="b" or ans=="a":
                score-=20
                l1.append((ques,ans,corr_ans))
                break
            else:
                print("Invalid answer..")
                
        return score


    ###############################################


    score=q10()          
    print("\n~~~~~~~~~~~GAME IS OVER~~~~~~~~~~~")    
    print("\tFinal Score:",score)    


    status=True
    while(status):
        print("\nWould you like to view your answers?:\n1)View Right Questions List\n2)View Wrong Questions List\n3)Exit")
        
        ch=int(input("Enter your choice:"))
        if ch == 1:
            for k,v in dict.items():  
                print("\n",k,"\n-->Correct Answer:",v)
                status=True
                

        elif ch == 2:
            print("YOUR WRONG ANSWERS ARE:")
            for q,a,c in l1:  
                print("\n",q,"\n-->Your Answer:",a,"\tCorrect Answer:",c)
                status=True

        elif ch == 3:
            exit()
            status=False
        
        else:
            print("Invalid choice, try again!")

menu()

