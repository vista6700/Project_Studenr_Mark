def Main():
    print("*************** Enter information ***************")
    Mark[1][1][0] = False
    while Mark[1][1][0] == False:
        Mark[1][2][0] = input("Enter student name:")
        if str.isalpha(Mark[1][2][0]) == True:
            Mark[1][1][0] = True
        else:
            print("Invalid name, please try again.")
    while Mark[1][1][0] == True:
        Mark[1][2][1] = input("Enter student ID:")
        if len(Mark[1][2][1]) == 8 and str.isdigit(Mark[1][2][1]) == True :
            Mark[1][1][0] = False
        else:
            print("Please enter Student ID again")
    for i in range(0,4):
        found = False
        while found == False:
            try:
                Mark[0][0][0][i] = input("Enter " + Mark[0][0][1][i] + ": ")
                if float(Mark[0][0][0][i]) <= 100 and float(Mark[0][0][0][i]) >= 0:
                    found = True
                else:
                    print("Invalid " + Mark[0][0][1][i] + ", please try again.")
            except:
                print("Invalid " + Mark[0][0][1][i] + ", please try again.")
    Mark[0][0][0][4] = float(Mark[0][0][0][0]) * 0.4 + float(Mark[0][0][0][1]) * 0.3 + float(Mark[0][0][0][2]) * 0.3
    Mark[0][0][0][5] = float(Mark[0][0][0][4]) * 0.5 + float(Mark[0][0][0][3]) * 0.5
    if float(Mark[0][0][0][3]) < 40 or float(Mark[0][0][0][4]) < 40:
        Mark[1][0][6] = 0
    elif Mark[0][0][0][5] >= 75.0:
        Mark[1][0][6] = 1
    elif Mark[0][0][0][5] >= 65.0:
        Mark[1][0][6] = 2
    elif Mark[0][0][0][5] >= 40.0:
        Mark[1][0][6] = 3
    else:
        Mark[1][0][6] = 4
    print("*************** Result ***************")
    print("Student name: " + Mark[1][2][0])
    print("Student ID: " + Mark[1][2][1])
    print(Mark[0][0][1][0] + ": " + Mark[0][0][0][0] + " ," + Mark[0][0][1][1] + ": " + Mark[0][0][0][1] + " ," + Mark[0][0][1][2] + ": " + Mark[0][0][0][2] + " ," +Mark[0][0][1][3] + ": " + str(Mark[0][0][0][3]))
    print("Module Marks: " + str(Mark[0][0][0][5]) + " ,Madule Grade: " + Mark[0][1][0][Mark[1][0][6]] + " ,Remarks: " + Mark[0][1][1][Mark[1][0][6]])
    print(Mark[0][1][2][Mark[1][0][6]])
    print("*************** Result ***************")
global Mark
Mark = [[[0,0,0,0.0,0,0],["Test Marks","Project Marks","Workshop Marks","Exam Marks"]],[["F","A","B","C","Others"],["Restudy","Pass with A grade","Pass with B grade","Pass with C grade","Invalid Module Grade"],["Don't get discouraged, keep trying!","Well done!","Almost canget an A grade, work harder!","Please be careful, you only qualified for a C.","Please double-check the input marks"]]],[[0,0,0,0,0,"",0,0.0],[False,True],["",""]]
while Mark[1][1][1] == True:
    Main()
    Mark[1][0][7] += Mark[0][0][0][5]
    match Mark[1][0][6]:
        case 0:
            Mark[1][0][3] += 1
        case 1:
            Mark[1][0][0] += 1
        case 2:
            Mark[1][0][1] += 1
        case 3:
            Mark[1][0][2] += 1
    Mark[1][0][4] += 1
    while Mark[1][1][0] == False:
        Mark[1][0][5] = input("Do you want to enter another student record? [Y/y] for Yes, [N/n] for No: ")
        if Mark[1][0][5] == "Y" or Mark[1][0][5] == "y" or Mark[1][0][5] == "N" or Mark[1][0][5] == "n":
            if Mark[1][0][5].upper() == "N":
                    Mark[1][1][1] = False
            Mark[1][1][0] = True
        else:
            print("Invalid, please try again.")
print("There is/are " + str(Mark[1][0][4]) + " students' record(s) inputted, and the average marks is: " + str(Mark[1][0][7]/Mark[1][0][4]))
for x in range(0,3):
    print("Total number of " + chr(65 + x) + " grade: " + str(Mark[1][0][x]))
print("Total number of F grade: " + str(Mark[1][0][3]))