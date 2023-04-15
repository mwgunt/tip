#!/bin/python3

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollar):
    # Remove "$" from string.
    dollar = dollar.replace("$", "")
    # Convert string to float.
    dollar = float(dollar)
    return dollar

def percent_to_float(percent):
    # Remove "%" from string
    percent = percent.replace("%", "")
    # Convert string to float
    percent = float(percent)
    # Convert percentage to decimal
    percent = percent * 0.01
    return percent

main()
