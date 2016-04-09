# This program will disply how much a loan payment will be given an interest rate
# compounded monthly. And how much  it would be at +/-0.5%.

global rate
global months

def main():
    print()
    print("Welcome to Metro Bank, this program will help you to calculate how ")
    print("much your loan payment will be.")
      
    # This section gathers information from the user, and does a few unit conversions
    print()
    principal = float(input("Please enter the loan amount. "))
    years = float(input("Please enter the duration of the loan in years. "))
    rateInitial = float(input("Please enter the interest rate in percent. "))
    rate = rateInitial/100/12 # convert percent to decimal and apr to monthly percentage rate
    months = years*12 # convert years to months

    # This section contains all of the functions for calculating the minimum
    # payment, and total interest paid.

    # The payRate function calculates the monthly payment
    def payRate(p,r,t): #p,r,t are principal, rate, and time respectively
        payment = (p*r)/(1-(1+r)**(-t))
        print("Your monthly payment will be: $",format(payment,'.2f'))
        return payment   

    # The interest function calculates the total interest that will be paid
    # over the lifetime of the loan.
    def interest(t,pay,p): # t, pay, and p are time, payment and principal respectively
        total = t*pay-p
        print("The total amount of interest paid will be: $", format(total,'.2f'))
        return interest
        
    # This section displays the results, and includes what the results would be
    # with both .5% higher and lower apr.

    print("Your loan amount is. $",principal)
    print("The loan duration will be ",years,"years." )
    print("At an intrest rate of ",rateInitial)
    print()
    payment = payRate(principal,rate,months)
    interest(months,payment,principal)
    print()
    print("If your initial rate is increased by .5%:")
    payment = payRate(principal,rate+.005/12,months)
    interest(months,payment,principal)
    print()
    print("If your initial rate is decreased by by .5%:")
    payment = payRate(principal,rate-.005/12,months)
    interest(months,payment,principal)

main()

# Test cases:
#
# Test 1: Student loan
#
# $483, 20 months left, 4.3% apr.
# payRate:
# 483*(.043/12) = 1.72914
# 1.72914/(1-(1+.043/12)**-20) = 25.07 program produces 25.02
# interest:
# 25.07*20-483 = 18.40 program produces 18.41
#
# Test 2: 
#
# $3000, 1 year, 6.5% apr
# payRate:
# 3000*(.065/12) = 15
# 15/(1-(1+.06/12)**-12) = 258.20  program produces 258.20
# interest:
# 258.20*12-3000 = 98.4 program produces 98.39
#
# Report:
#
# I started by writing up the input statments and basic outputs, then I wrote up
# the equations, and checked them, and finally worked on getting the functions 
# up and running.
#
# I started testing my program with the equations.  Once I got those close enough
# to working, I started putting in the functions, which broke everything for a
# while there. I had some trouble with local variables, and it took me a while to 
# figure out that you can assign a variable as a function.
#
# I learned a lot about how local variables can be applied, and variable declaration
# in Python. I also learned a lot about functions, arguments and parameters.
# Next time I will probably spend a lot less time wondering how to use a variable
# generated in one function in a different function.
