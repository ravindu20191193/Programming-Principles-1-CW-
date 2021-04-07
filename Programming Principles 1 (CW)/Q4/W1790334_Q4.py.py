# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20191193
# UOW ID : W1790334 
# Date: 17.04.2020
# Part 4 - Alternative Staff Version (optional extension)

no_of_Progress = 0
no_of_Trailing = 0
no_of_Retriever = 0
no_of_Excluded = 0

#dictionary (list type)                
marks = { 1:[120,0,0],
         2:[100,20,0],
         3:[100,0,20],
         4:[80,20,20],
         5:[60,40,20],
         6:[40,40,40],
         7:[20,40,60],
         8:[20,20,80],
         9:[20,0,100],
         10:[0,0,120]  }
student=0
count=1
while count !=11:
    student +=1
    Pass=marks.get(student) [0]
    Defer=marks.get(student) [1]
    Fail=marks.get(student) [2]

    count+=1

    if Pass==120 and Defer==0 and Fail==0:
        print('Progress')
    elif Pass==100 and Defer==20 and Fail==0:
        print()
    elif Pass==100 and Defer==0 and Fail==20:
        print('Progress-module trailer')
    elif Pass==80 and Defer==20 and Fail==20:
        print('Do not Progress-module retriever')
    elif Pass==60 and Defer==40 and Fail==20:
        print('Do not Progress-module retriever')
    elif Pass==40 and Defer==40 and Fail==40:
        print('Do not Progress-module retriever')
    elif Pass==20 and Defer==40 and Fail==60:
        print('Do not Progress-module retriever')
    elif Pass==20 and Defer==20 and Fail==80:
        print('Exclude')
    elif Pass==20 and Defer==0 and Fail==100:
        print('Exclude')
    elif Pass==0 and Defer==0 and Fail==120:
        print('Exclude')
                                                                                
        
        
    
          

print(" ")



    



























       
