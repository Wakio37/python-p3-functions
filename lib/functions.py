#!/usr/bin/env python3

def greet_programmer():
    return "Hello, programmer!\n"


def greet(name):
    return f"Hello, {name}!"

def greet_with_default(name="programmer"):
    return f"Hello, {name}!"

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number/2

print(greet_programmer())               
print(greet("Naureen"))                 
print(greet_with_default())              
print(greet_with_default("Sunny"))       
print(add(1, 2))                        
print(halve(4))                       
print(halve("two"))       
