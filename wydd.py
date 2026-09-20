import sys
import time
if len(sys.argv) != 2:
    print("Really? REALLY? Well, your brain really seems to need help so here you go:\nUsage:\n   wydd [codefile.wydd]")
    sys.exit()

variables = [0] * 2048

def executeProgram(file):
    global splitted_file
    splitted_file = file.splitlines()
    global count
    count = 0
    while True:
        if count < len(splitted_file):
            if count + 1 < len(splitted_file) and splitted_file[count + 1] != "" and splitted_file[count] != "":
                raise Exception("Exception Occured.")
            if splitted_file[count] != "":
                line = splitted_file[count]
                parseCommand(line, count)
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    args = line.split(":")[1].split()
                    skip = int(args[3])
                    count += (skip * 2) + 1
            count += 1
        else:
            time.sleep(1)

def logicBlockGetLR(arguments):
    left = 0
    right = 0
    if isArgumentVar(arguments[0]):
        left = var2num(arguments[0])
    else:
        left = int(arguments[0])
    if isArgumentVar(arguments[2]):
         right = var2num(arguments[2])
    else:
        right = int(arguments[2])
    
    return [left, right]

def repeatCodeBlocks(logic_comparator, arguments, currentIndex, flip: bool):
    left, right = logicBlockGetLR(arguments)
    if (logic_comparator == "NEQUALS" and not flip) or (logic_comparator == "EQUALS" and flip):
        while left != right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1
            left, right= logicBlockGetLR(arguments)
    elif (logic_comparator == "EQUALS" and not flip) or (logic_comparator == "NEQUALS" and flip):
        while left == right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
            left, right= logicBlockGetLR(arguments)
    elif (logic_comparator == "INFEQ" and not flip) or (logic_comparator == "SUPERIOR" and flip):
        while left <= right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
            left, right= logicBlockGetLR(arguments)
    elif (logic_comparator == "SUPEQ" and not flip) or (logic_comparator == "INFERIOR" and flip):
        while left >= right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
            left, right= logicBlockGetLR(arguments)
    elif (logic_comparator == "INFERIOR" and not flip) or (logic_comparator == "SUPEQ" and flip):
        while left < right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
            left, right= logicBlockGetLR(arguments)
    elif (logic_comparator == "SUPERIOR" and not flip) or (logic_comparator == "SUPEQ" and flip):
        while left > right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
            left, right= logicBlockGetLR(arguments)
    else:
        raise Exception("Exception Occured.")

def ifCodeBlock(logic_comparator, arguments, currentIndex):
    left = logicBlockGetLR(arguments)[0]
    right = logicBlockGetLR(arguments)[1]

    if logic_comparator == "NEQUALS":
        if left != right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1
    elif logic_comparator == "EQUALS":
        if left == right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
    elif logic_comparator == "INFEQ":
        if left <= right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
    elif logic_comparator == "SUPEQ":
        if left >= right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
    elif logic_comparator == "INFERIOR":
        if left < right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
    elif logic_comparator == "SUPERIOR":
        if left > right:
            i = 1
            while i <= int(arguments[3]):
                parseCommand(splitted_file[currentIndex + i * 2], currentIndex + i * 2)
                line = splitted_file[currentIndex + i * 2]
                if ("REPEAT" in line or "EXECUTE CODE IF TRUE" in line) and not line.startswith("END OF"):
                    i += int(line.split(":")[1].split()[3])
                i += 1 
    else:
        raise Exception("Exception Occured.")

                


def parseCommand(splitted, currentIndex):
    command = splitted.split(":")[0]
    arguments = splitted.split(":")[1].split(" ")
    arguments.pop(0)
    match command:
        case "CREATE VARIABLE TYPE INT":
            if arguments[0].isdigit():
                if not isArgumentVar(arguments[1]):
                    if arguments[1].isdigit():
                        variables[int(arguments[0])] = int(arguments[1])
                    elif arguments[1] in "ASKFORUSERINPUT":
                        userInput = input()
                        if userInput.isdigit():
                            variables[int(arguments[0])] = int(userInput)
                        else:
                            raise Exception("Exception Occured.")
                    else:
                       raise Exception("Exception Occured.") 
                else:
                    variables[int(arguments[0])] = int(var2num(arguments[1]))
            else:
                raise Exception("Exception Occured.")
        case "INSERT TO CONSOLE":
            if not isArgumentVar(arguments[0]):
                if arguments[0].isnumeric():
                    print(arguments[0])
                else:
                    raise Exception("Exception Occured.") 
            else:
                print(var2num(arguments[0]))
        case "DECREASE VARIABLE":
            if not isArgumentVar(arguments[0]):
                raise Exception("Exception Occured.")
            else:
                variables[int(arguments[0].replace("VAR!", ""))] -= 1
        case "INCREASE VARIABLE":
            if not isArgumentVar(arguments[0]):
                raise Exception("Exception Occured.")
            else:
                variables[int(arguments[0].replace("VAR!", ""))] += 1
        case "REPEAT UNTIL":
            if not splitted_file[int(arguments[3]) * 2 + 2 + currentIndex].startswith("END OF REPEAT UNTIL"):
                raise Exception("Exception Occured.")
            repeatCodeBlocks(arguments[1], arguments, currentIndex, True)
        case "EXECUTE CODE IF TRUE":
            if not splitted_file[int(arguments[3]) * 2 + 2 + currentIndex].startswith("END OF EXECUTE CODE IF TRUE"):
                raise Exception("Exception Occured.")
            ifCodeBlock(arguments[1], arguments, currentIndex)
        case "REPEAT WHILE":
            if not splitted_file[int(arguments[3]) * 2 + 2 + currentIndex].startswith("END OF REPEAT WHILE"):
                raise Exception("Exception Occured.")
            repeatCodeBlocks(arguments[1], arguments, currentIndex, False)
        case "INSERT TO CONSOLE AS ASCII":
            finalString = ""
            for arg in range(len(arguments)):
                if arguments[int(arg)] != '':
                    if isArgumentVar(arguments[int(arg)]):
                        finalString += chr(int(var2num(arguments[int(arg)]))) 
                    else:
                        finalString += chr(int(arguments[int(arg)]))
            print(finalString)
        case "EXIT THE PROGRAM":
            quit()
        case "COMM":
            pass
        case "":
            pass   


def isArgumentVar(arg):
    if arg.startswith("VAR!"):
        return True
    else:
        return False

def var2num(arg):
    return variables[int(arg.split("!")[1])]
        

if __name__ == "__main__":
    filename = sys.argv[1]
    file = ""
    with open(filename) as f:
        file = f.read()
    executeProgram(file)
