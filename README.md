# LimScript

## Commands

var \[name] = \[value]: Define a variable. Use # to get the value of an ASCII character. For example, x = #x.

print / printval \[value or variable]: Print out a variable or value. **print** will print as an ASCII character and **printval** will print as an integer with a newline.

add / sub / mul / div \[value 1] \[value 2] \[result variable]: Preform an operation on the specified values and store it into the variable specified. A variable can be created when using this command.

label \[name]: Store that line as a label.

goto \[label]: Jump the pointer to a label.

gotoif \[label] \[value 1] \[operation] \[value 2]: Jump to the label if the operation is true. Operations can be **==**, **!=**, **>**, **<**, **>=**, or **<=**.

get \[variable]: Get input and store it into the variable. If input is a string, it'll get the first character and store the ASCII value.

exit \[code]: Exit program immediately with error code.

**Make sure to mark the end of a line with a semicolon! (;)**

## Usage

`python3 limscript.py code.lim`

## Code Examples

### Hello, World
```
print #H;
print #e;
print #l;
print #l;
print #o;
print #,;
print 32;
print #w;
print #o;
print #r;
print #l;
print #d;
print #!;
print 10;
```
### Truth Machine
```
get val;
label loop;
printval val;
gotoif loop val == 1;
```
### Fibonachi Sequence
```
var a = 1;
var b = 0;
var i = 0;

label loop;
add a b r;
var b = a;
var a = r;
printval r;
add i 1 i;
gotoif loop i <= 10;
```
