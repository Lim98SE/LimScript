# LimScript

## Commands

### Variables

 - `var [name] = [value]`
   - Define a variable. Use # to get the value of an ASCII character. For example, `x = #x`.

### Input / Output

 - `print [name / value]` / `printval [name / value]`
   - Print out a variable / value.
     - `print` will print an ASCII character (e.g, `print 65` will print a capital A)
     - `printval` will print the value as an integer (e.g, `printval 65` will actually print `65`)

 - `get [name]`
   - Get input and store the first ASCII character value in the variable. (e.g, when you input `Andromeda`, the ASCII value of `A` will be stored.)

### Arithmetic / Bitwise operations
*It is possible to create new variables using these commands.*

#### Arithmetic

 - `add [value 1] [value 2] [result variable]`
   - Add value 1 to value 2 and store in result variable.

 - `sub [value 1] [value 2] [result variable]`
   - Subtract value 2 from value 1 and store in result variable.

 - `mul [value 1] [value 2] [result variable]`
   - Multiply value 1 times value 2 and store in result variable.

 - `div [value 1] [value 2] [result variable]`
   - Divide value 1 by value 2 and store in result variable.

 - `mod [value 1] [value 2] [result variable]`
   - Calculate remainder from value 1 divided by value 2 and store in result variable.

 - `exp [value 1] [value 2] [result variable]`
   - Calculate value 1 to the power of value 2 and store in result variable.

#### Bitwise operations

 - `band [value 1] [value 2] [result variable]` (**b**itwise **and**)
   - Calculate value 1 & value 2, and store in result variable.

 - `bor [value 1] [value 2] [result variable]`
   - Calculate value 1 | value 2, and store in result variable.

 - `bxor [value 1] [value 2] [result variable]`
   - Calculate value 1 ^ value 2, and store in result variable.

 - `shir [value 1] [value 2] [result variable]`
   - Shift right value 1 by value 2 bits, and store in result variable.

 - `shil [value 1] [value 2] [result variable]`
   - Shift left value 1 by value 2 bits, and store in result variable.

### Control flow

#### Goto / Jumps

 - `label [name]`
   - Assign a label to this line.

 - `goto [label]`
   - Jump to a label.

 - `gotoif [label] [value 1] [operation] [value 2]`
   - Jump to a label under a condition.
     - Available operations are: `==`, `!=`, `>`, `<`, `>=` and `<=`.
     - Example: Jump to label `myLabel` if variable `myVar` is more than the ASCII value of `A`.  
       `gotoif myLabel myVar > #A`

#### Subroutines

 - `subr [name]`
   - Define a subroutine here.

 - `subj [subroutine]`
   - "Call" a subroutine.

 - `subjif [subroutine] [value 1] [operation] [value 2]`
   - "Call" a sobroutine under a condition.
     - Same syntax as [gotoif](#goto--jumps).

 - `return`
   - Return from a subroutine.

~~subroutines example needed~~

### Stack

 - `push [value]`
   - Push a value or a variable to the stack.

 - `[variable] = pop` (~~weird syntax, will change in the future~~)
   - Store and then remove the top value on the stack in a variable.

 - `flipstack`
   - Flip the stack.

### Miscellaneous

 - `include [file]`
   - Import another LimScript file.
     - Essentially copies the file's content to this position.

 - `exit [code]`
   - Exit program immediately with error code.
  
 - `str [name] = [string]`
   - Define a string variable.
 
 - `printstr [string]`
   - Print a string to the console.
 
 - `arr [name] = [ints seperated by ,]`
   - Define an array variable.

### Array Functions

 - `getitem [array] [output] [index]`
   - Get an item from an array.

 - `append [array] [data]`
   - Append data to an array.
 
 - `pop [array] [output]`
   - Pop the top value of an array into an output variable.
 
 - `delete [array] [data]`
   - Delete a value from an array.
  
 - `printarr [array]`
   - Prints the array's contents to the console.

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
