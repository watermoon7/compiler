# Task

Mathematical expression calculator
Using this framework: [Building a simple interpreter, by Ruslan](https://ruslanspivak.com/lsbasi-part1/)

# Features

## Supports these operations
    - adding, subtracting, multiplying, dividing
    - brackets
    - powers

    - factorial (only works on integers)

## Supports these modes
    - decimal output
    - rational output (fractions)

    - variable output (includes unspecified variables)

## Supports these types of numbers
    - whole numbers
    - decimal numbers
    
    - pi (3.14), e (2.718)

## Extra things
    - multiline calculations (using results from previous lines)
    - variables
    - functions

    - big numbers
    - infinite precision

    - trigonometric functions: sin, cos, tan, arsin, arcos, artan
    - summation formulas

    - latex gui

## Symbol table
    add: +
    subtract: -
    multiply: *
    divide: /
    brackets: ()
    factorial: !
    power: ^
    pi: pi
    e: e

    previous result: ans
    variables: any alphabetic character (lower and uppercase) except for e, pi or ans


# Syntax Rules

1. Any number of + and - signs
e.g. `-+1*++++----5 = -5`
e.g. `(+1) - (-1) = 2`

2. Any number of brackets
e.g. `(((1)+(((((2))))))) = 3`
e.g. `-((((((((((((((0)))))))))))))) = 0`

3. Precedence: power > divide = multiply (* has been replaced with x)
e.g. `2/2x3 = (2/2)x3 = 2/(2x3)`
e.g. `3/5^7 = 3/(5^7)`
e.g. `4x2/6 = (4x2)/6 = 4x(2/6)`

4. Implied multiplication
e.g. `3(2+1) = 3*(2+1)`
e.g. `3pi= 3*pi`
e.g. `8(x+1) = 8*x+8 = 8x+8`

5. Fraction simplification
e.g. `30/45 = 2/3`
e.g. `(12+6)/20 = 9/10`
e.g. `6x/9 = 2x/3`

# Simple rules

1. `++ = +`
2. `-+ = -`
3. `+- = -`
4. `-- = +`
5. `+n = n`
6. `-0 = 0`
7. `((expression)) = (expression)`

# Tests

## Example expressions

1. `1+2-3*4/5`
2. `1*(1+3)-3*(8/(1+1))^3`
3. `+1+-8---6+(+0)^(1!/(8/(2/1)))`
4. `8*3.5/6^2`
5. `3!*5!/2!+1!-2!`

### Extra

6. `(1+x^2)^2`
7. `(pi/7)^2+3pi^6/(9pi)`
8. `3y+12z/(9ans)`

## Expexted outputs

1. `3/5`
2. `-188`
3. `-13`
4. `7/9`
5. `359`

### Extra

6. `1+2x^2+x^4`
7. `pi^2/49+pi^5/3`
8. `3y+4z/(3ans)`
In the last one, replace 'ans' with the previous result and simplify

# Java to Pygyatt compiler

do it you nerd!
