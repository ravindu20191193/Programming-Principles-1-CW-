# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20191193
# UOW ID : W1790334
# Date: 17.04.2020
# Part 1-Student Version

# Enter Pass,Defer,Fail


while True :
    try :
        print(" ")
        Pass = int(input ("Enter Pass mark   :"))
        Defer = int(input ("Enter Defer mark   :"))
        Fail = int(input ("Enter Fail mark      :"))
        print(" ")

        if (((Pass%20) == 0) and ((Defer%20) == 0) and ((Fail%20) == 0)) and ((Pass <= 120) and (Defer <= 120) and (Fail <= 120)) and ((Pass >= 0) and (Defer >= 0) and (Fail >= 0)) and ((Pass+Defer+Fail) == 120) :
            break    
        
        if (((Pass%20) != 0) or((Defer%20) != 0) or((Fail%20) != 0)) or ((Pass > 120) or (Defer > 120) or (Fail > 120)) or ((Pass < 0) or (Defer < 0) or (Fail < 0)) :
            print("----- Range Error -----")
            print(" ")


        if (Pass+Defer+Fail) != 120:
            print("----- Total Incorrect -----")
            print(" ")

    except ValueError:
        print(" ")
        print("----- Integers required -----")
        Value1 = False

    
if Pass==120:
    print(">>> Progress")
elif Pass==100:
    print(">>> Progress-module trailer")
elif Fail>=80:
    print(">>>Exclude")
else:
    print(">>> Do not progress-module retriever")
       
