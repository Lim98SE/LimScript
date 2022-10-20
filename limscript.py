import sys

try:
  sys.argv[1]
 except:
  print("Please give an argument.")
  sys.exit(0)
 
 with open(" ".join(sys.argv[1:])) as cfile:
  code = cfile.read()

var = {}
labels = {}
open_value = 0

lines = code.replace("\n", ";").split(";")
final = []

for i in range(len(lines)):
    lines[i] = lines[i].strip()

def ifvar(variable):
    if variable in var:
        return var[variable]
    else:
        return int(variable)

# ------------------------

pointer = 0

while True:
    try:
        lines[pointer]
    except IndexError:
        break
    line = lines[pointer].replace("openvar", str(open_value))
    line = line.split()
    try:
        line[0]
    except:
        pointer += 1
        continue
    if line[0] == "var":
        i = " ".join(line).replace("var ", "").replace(" ", "")
        d = i.split("=")
        if d[1][0] == "#":
            d[1] = ord(d[1][1])
        var[d[0]] = ifvar(d[1])
    
    if line[0] == "print":
        try:
            print(chr(var[line[1]]), end="")
        except:
            if line[1][0] == "#":
                line[1] = ord(line[1][1])
            print(chr(int(line[1])), end="")
    
    if line[0] == "add":
        try:
            var[line[3]] = ifvar(line[1]) + ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "sub":
        try:
            var[line[3]] = ifvar(line[1]) - ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "mul":
        try:
            var[line[3]] = ifvar(line[1]) * ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "div":
        try:
            var[line[3]] = ifvar(line[1]) // ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "label":
        labels[line[1]] = lines.index(" ".join(line))
    
    if line[0] == "goto":
        pointer = labels[line[1]]
    
    if line[0] == "gotoif":
        pos = labels[line[1]]
        val1 = ifvar(line[2])
        val2 = ifvar(line[4])
        try:
            operation = line[3]
        except IndexError:
            operation = "!="
        
        if val1 != val2 and operation == "!=":
            pointer = pos
        
        if val1 == val2 and operation == "==":
            pointer = pos
        
        if val1 >= val2 and operation == ">=":
            pointer = pos
        
        if val1 <= val2 and operation == "<=":
            pointer = pos
        
        if val1 > val2 and operation == ">":
            pointer = pos
        
        if val1 < val2 and operation == "<":
            pointer = pos
    
    if line[0] == "printval":
        print(ifvar(line[1]))
    
    if line[0] == "get":
        inp = input("? ")
        try:
            var[line[1]] = int(inp)
        except:
            var[line[1]] = ord(inp[0])

    pointer = pointer + 1
