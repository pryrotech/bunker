##################################################
#     Bunker Parser & Lexer by Colby Pryor       #
##################################################
import os
import linecache
print("******                    **")                   
print("/*////**                  /**")                   
print("/*   /**  **   ** ******* /**  **  *****  ******")
print("/******  /**  /**//**///**/** **  **///**//**//*")
print("/*//// **/**  /** /**  /**/****  /******* /** / ")
print("/*    /**/**  /** /**  /**/**/** /**////  /**")  
print("/******* //****** ***  /**/**//**//******/***") 
print("///////   ////// ///   // //  //  ////// /// \n\n\n")

operation = False
get_command = ''

while(operation == False):
    get_command = input("BUNKER >")
    if(get_command[0:5].upper() == "CLEAR"):
        os.system("cls")
        operation == True
    if(get_command.upper() == "EXIT"):
        os.system("exit")
        operation == True
    if(get_command.upper() == "HELP"):
        print("Hello")
    if(get_command[0:5].upper() == "PRINT"):
        print(get_command[6:])
        operation == True
    if(get_command[0:5].upper() == "BMATH"):
        if(get_command[6:7] == "."):
            get_command = get_command[7:]
            a,b = get_command.split("!")
            x= eval(b)
            print(x)
    if("=" in get_command):
        b,c = get_command.split("=")
        d,e = get_command.split("=")
        b = len(b)
        c = len(c)
        print(d[0:b])
        print(e[0:c])
        b= d[0:b],e[0:c]
        print(b)
        file = open("variable_store"+str(b)+".txt", "w")
        file.write(str(b))
        file.close()

    if(get_command[0:6].upper() == "GETVAR"):
        file = open("variable_store"+str(b)+".txt", "r")
        if("'"+get_command[7:]+"'" in file.read()):
                file = open("variable_store"+str(b)+".txt", "r")
                data = file.read()
                data2,data3 = data.split(",")
                variable_1= data3[2:].strip("')")
                print(variable_1)
                file.close()
                
    if(get_command[0:6].upper() == "COMVAR"):
        get_command = get_command.replace('COMVAR.','')
        data4,data5 = get_command.split("+")
        file2 = open("variable_store"+str(data4)+".txt", "r")
        print(file2)


