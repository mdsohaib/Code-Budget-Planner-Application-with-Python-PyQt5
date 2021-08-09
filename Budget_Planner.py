# importing time module to make use of the sleep function in it.
import smtplib 
  
import time

# Declaring empty lists to store data as required


need_d={}
sorted_need_d={}
want_d={}
sorted_want_d={}
diff=0
saving=0
l=[]


# Defining need_wants function which builds a complete list of user's needs,wants

def needs_wants(diff,sav):
    print("\n\n*****Please enter the list of your NEEDS acoording to your priority*****")
    print("\n Don't forget to provide the price and priority value ")
    print("\n The priority will be marked on a scale of 1-10, 10 means it has the highest priority")
    size = int(input("\n\n Enter the number of needs you have = "))
    
    for i in range(1, size + 1):
        

        print("Enter the need , priority and the cost required for the need: ")
        need,priority,price = (map(str,input().split()))

        need_d[int(priority)] = [need,int(price)]
        
        
    
   
    
    print("\n\n*****Please enter the list of your WANTS acoording to your priority*****")
    print("\n Don't forget to provide the price and priority value ")
    print("\n The priority will be marked on a scale of 1-10, 10 means it has the highest priority")
    size = int(input("\n\n Enter the number of wants you have = "))
    
    for i in range(1, size + 1):
        
        print("Enter the wants:\n")

        want,priority,cost = (map(str,input().split()))
        
        want_d[int(priority)] = [want,int(cost)]
        
    
    


# define start() function which takes budget and savings as inputs and connects all the other functions

def start():
    s = "\n ******** Welcome to the Monthly Budget Planner ********"
    for i in s:
        print(i, end=" ")
        time.sleep(0.05) # Adding a pause 3 milli seconds 
    budget = float(input("\n\nPlease enter your Monthly budget = "))
    saving = float(input("\nPlease enter the amount you want to save = "))
    diff = budget - saving
    
    # checking if saving is greater than budget then re-enter
    
    if(saving > budget):
        print("\nYou can't save more than your budget .... Please provide your inputs again!!! ")
        start()

        
    needs_wants(diff,saving)



    need_k=sorted(need_d.keys(),reverse=True)

    for i in need_k:
        sorted_need_d[i]=need_d[i]
     

    want_k=sorted(want_d.keys(),reverse=True)


    for i in want_k:
        sorted_want_d[i]=want_d[i]
    


   
    print("\n You have provided all your inputs!")
    print("\n Calculating your finalized Budget")
    
    calculation(diff,saving)

 


     #Defining calc() function which calculates the budget based on needs and wants
def calculation(diff,sav):
   
    spent=0
    print("\n So As per The given data your Monthly Budget will be as followed :")
    print("\n :::::::::::Your Need's List::::::::::: ")
    print("\n | Name |         |Priority|        |Price|   \n")
    for i in sorted_need_d:
        print("\n ",sorted_need_d[i][0],"\t\t", i,"\t\t", sorted_need_d[i][1],"\n")
    print("\n\n :::::::::::Your Want's List::::::::::: ")
    print("\n | Name |         |Priority|        |Price|   \n")
    for j in sorted_want_d:
        print("\n ",sorted_want_d[j][0],"\t\t", j,"\t\t", sorted_want_d[j][1])
    for i in sorted_need_d:
        if((diff-sorted_need_d[i][1])>=0):
            diff=diff-sorted_need_d[i][1]
            spent+=sorted_need_d[i][1]
            l.append(sorted_need_d[i][0])
            print("\n Amount left after fulfilling your ",sorted_need_d[i][0]," need is: ",diff) 
        else:
            print("\n So Sorry but Your ", sorted_need_d[i][0], " need can't be satisfied as it exceeds your Budget")

    for j in sorted_want_d:
        if((diff-sorted_want_d[j][1])>=0):
            diff=diff-sorted_want_d[j][1]
            spent+=sorted_want_d[j][1]
            l.append(sorted_want_d[j][0])
            print("\n Amount left after fulfilling your ",sorted_want_d[j][0]," want is: ",diff)
            
        else:
            print("\n So Sorry but Your ", sorted_want_d[j][0], " want can't be satisfied as it exceeds your Budget")

    # Printing the final results
    
    print("\n\n So, The total Amount You are spending = ", spent )
    print("\n Total Amount that you are saving = ",(sav + diff))
    mailr=input("\n\nPlease enter your Mail Id = ")   
    # Asking the user to re-run if he didn't like the results
    a="Please Buy These Items For these month"+'\n'
    for i in l:
        a=a+" "+str(i)
    # creates SMTP session 
    email = smtplib.SMTP('smtp.gmail.com', 587) 

    # TLS for security 
    email.starttls() 

    # authentication
    # compiler gives an error for wrong credential. 
    email.login("budgetcalcpy@gmail.com", "zqprcutbzhlsbhzd") 

    # message to be sent 
    message = a

    # sending the mail 
    email.sendmail("budgetcalcpy@gmail.com", mailr, message) 

    # terminating the session 
    email.quit()
    print("MAIL SENT PLEASE CHECK")


# calling to the start() function to initiate the program from beginning

print(start())


    
    

