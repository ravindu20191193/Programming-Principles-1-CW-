# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20191193
# UOW ID : W17903334
# Date: 17.04.2020
# Part 2-Staff Version

no_of_Progress = 0
no_of_Trailing = 0
no_of_Retriever = 0
no_of_Excluded = 0

while True:
    try :
        print(" ")
        Pass = int(input ("Enter Pass mark   :"))
        Defer = int(input ("Enter Defer mark   :"))
        Fail = int(input ("Enter Fail mark      :"))
        print(" ")

        if (((Pass%20) == 0) and ((Defer%20) == 0) and ((Fail%20) == 0)) and ((Pass <= 120) and (Defer <= 120) and (Fail <= 120)) and ((Pass >= 0) and (Defer >= 0) and (Fail >= 0)) and ((Pass+Defer+Fail) == 120) :
            if Pass==120:
                print(">>> Progress")
                no_of_Progress += 1
            elif Pass==100:
                print(">>> Progress-module trailer")
                no_of_Trailing += 1
            elif Fail>=80:
                print(">>>Exclude")
                no_of_Excluded += 1
            else:
                print(">>> Do not -module retriever")
                no_of_Retriever += 1
                
            print (" ")
            end_program = input ("Enter 'q' to exit from the program or enter any key to continue : ")
            if end_program == "q" :
                break

        
        if (((Pass%20) != 0) or((Defer%20) != 0) or((Fail%20) != 0)) or ((Pass > 120) or (Defer > 120) or (Fail > 120)) or ((Pass < 0) or (Defer < 0) or (Fail < 0)) :
            print("----- Range Error -----")
            print(" ")


        if (Pass+Defer+Fail) != 120:
            print("----- Total Incorrect -----")
            print(" ")

        
               
    except ValueError:
        print(" ")
        print("----- Integer required -----")
        Value1 = False

print (" ")
print (" .............................................................................................................................................................. ")
print (" ")

print ("Progress    ", no_of_Progress , "   :   " ,  "*"*no_of_Progress)
print ("Trailing      ", no_of_Trailing ,    "   :   " ,  "*"*no_of_Trailing)
print ("Retriever    ", no_of_Retriever ,  "   :   " ,  "*"*no_of_Retriever)
print ("Excluded   ", no_of_Excluded , "    :   " ,  "*"*no_of_Excluded)

total_outcomes = no_of_Progress + no_of_Trailing + no_of_Retriever + no_of_Excluded
if total_outcomes == 1:
    print (total_outcomes,"outcome in total.")
else:
    print (total_outcomes,"outcomes in total.")



























       
