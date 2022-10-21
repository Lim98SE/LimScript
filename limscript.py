#!/usr/bin/env python3

from math import sqrt
import sys
import yaml
import time

try:
    sys.argv[1]
except:
    print("Please give an argument.")
    sys.exit(0)
 
with open(" ".join(sys.argv[1:])) as cfile:
    code = cfile.read()

#code = """
#var x = 7;
#arr hello = 68, x, #E;
#append hello #F;
#remove hello #E;
#printarr hello;
#getitem hello char 0;
#print char;
#pop hello char;
#print char;
#"""

var = {}
strings = {}
arrays = {}
labels = {}
functions = {}
open_value = 0

lines = code.replace("\n", ";").split(";")

stack = []

for i in range(len(lines)):
    lines[i] = lines[i].strip()

def ifvar(variable):
    if variable in var:
        return var[variable]
    elif variable == "pop":
        try:
            return stack.pop()
        except:
            return -1
    elif variable == "time":
        return int(time.time())
    elif not isinstance(variable, int):
        if variable[0] == "#":
            return ord(variable[1])
    return int(variable)

# ------------------------

for i in lines:
    i = i.strip().split()
    try:
        i[0]
    except:
        continue

    if i[0] == "include":
        file = " ".join(i[1:])

        print("Importing", file)

        try:
            with open(file) as code_file:
                code += code_file.read()
        except FileNotFoundError:
            print("Could not import", file)

lines = code.replace("\n", ";").split(";")

# print(code)

for i in range(len(lines)):
    lines[i] = lines[i].strip()

for i in lines:
    i = i.strip().split()
    try:
        i[0]
    except:
        continue
    if i[0] == "label":
        labels[i[1]] = lines.index(" ".join(i))
    if i[0] == "subr":
        functions[i[1]] = lines.index(" ".join(i))

pointer = 0

while True:
    try:
        lines[pointer]
    except IndexError:
        break
    line = lines[pointer][:lines[pointer].find("//")] if "//" in lines[pointer] else lines[pointer]
    line = line.split()

    try:
        line[0]
    except:
        pointer += 1
        continue
    if line[0] == "var":
        i = " ".join(line).replace("var ", "").replace(" ", "")
        d = i.split("=")
        var[d[0]] = ifvar(d[1])
    
    if line[0] == "str":
        i = " ".join(line).replace("str ", "")
        d = i.split("=")
        strings[d[0].strip()] = " ".join(d[1:]).strip()
    
    if line[0] == "arr":
        i = " ".join(line).replace("arr ", "")
        d = i.split("=")
        arrays[d[0].strip()] = (" ".join(d[1:]).strip()).split(",")
        
        for i in range(len(arrays[d[0].strip()])):
            arrays[d[0].strip()][i] = ifvar(arrays[d[0].strip()][i].strip())
    
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
    
    if line[0] == "sqrt":
        try:
            var[line[2]] = int(sqrt(ifvar(line[1])))
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "goto":
        pointer = labels[line[1]]
    
    if line[0] == "gotoif":
        pos = labels[line[1]]
        val1 = ifvar(line[2])
        val2 = ifvar(line[4])
        operation = line[3]
            
        if eval(f"{val1} {operation} {val2}"):
            pointer = pos
    
    if line[0] == "printval":
        print(ifvar(line[1]))
    
    if line[0] == "get":
        inp = input("? ")
        try:
            var[line[1]] = int(inp)
        except:
            var[line[1]] = ord(inp[0])

    if line[0] == "exit":
        exit(ifvar(line[1]))
    
    if line[0] == "save":
        try:
            with open("prefs.yml") as prefs:
                data = yaml.load(prefs, yaml.Loader)
        except FileNotFoundError:
            with open("prefs.yml", "w") as prefs:
                yaml.dump({}, prefs, yaml.Dumper)
                data = {}
        
        data[line[1]] = ifvar(line[2])

        with open("prefs.yml", "w") as prefs:
            yaml.dump(data, prefs, yaml.Dumper)
    
    if line[0] == "load":
        try:
            with open("prefs.yml") as prefs:
                data = yaml.load(prefs, yaml.Loader)
            
            var[line[2]] = data[line[1]]
        except FileNotFoundError:
            print("Could not load file.")
    
    if line[0] == "subj":
        stack.append(pointer)
        pointer = functions[line[1]]
    
    if line[0] == "subjif":
        pos = functions[line[1]]
        val1 = ifvar(line[2])
        val2 = ifvar(line[4])
        operation = line[3]
        
        if eval(f"{val1} {operation} {val2}"):
            stack.append(pointer)
            pointer = pos

    if line[0] == "return":
        try:
            pointer = stack.pop()
        except:
            pass
    
    if line[0] == "push":
        stack.append(ifvar(line[1]))
    
    if line[0] == "mod":
        try:
            var[line[3]] = ifvar(line[1]) % ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "exp":
        try:
            var[line[3]] = pow(ifvar(line[1]), ifvar(line[2]))
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "flipstack":
        stack.reverse()
    
    if line[0] == "shir":
        try:
            var[line[3]] = ifvar(line[1]) >> ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
   
    if line[0] == "shil":
        try:
            var[line[3]] = ifvar(line[1]) << ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)

    if line[0] == "bxor":
        try:
            var[line[3]] = ifvar(line[1]) ^ ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "band":
        try:
            var[line[3]] = ifvar(line[1]) & ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "bor":
        try:
            var[line[3]] = ifvar(line[1]) | ifvar(line[2])
        except Exception as e:
            print("ERROR:", e)
    
    if line[0] == "printstr":
        try:
            print(strings[line[1]])
        except Exception as e:
            print("ERROR:",e)
    
    if line[0] == "getitem":
        if line[1].strip() in arrays:
            var[line[2]] = arrays[line[1]][ifvar(line[3])]
    
    if line[0] == "append":
        value = ifvar(line[2])
        arrays[line[1].strip()].append(value)
    
    if line[0] == "pop":
        var[line[2]] = arrays[line[1].strip()].pop()
    
    if line[0] == "remove":
        arrays[line[1].strip()].remove(ifvar(line[2]))
    
    if line[0] == "printarr":
        print(arrays[line[1].strip()])

    pointer = pointer + 1
