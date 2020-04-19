import sys
from fractions import Fraction

import numpy as np

from simplex import standarize_rows, optimize


def menu():
    print("""
        EKR-SIMPLEX CALCULATOR

    what type of problem do you want to solve?	
        1 :maximization (<=).
        2 :minimization (>=).

        0 :For Help.
        """)
    try:
        prob_type = int(input("enter the number problem type: >"))
    except ValueError:
        print("please enter a number from choices above")
        prob_type = int(input("enter the number problem type: >"))
    if prob_type not in (0, 1, 2):
        sys.exit("you enter a wrong problem choice ->" + str(prob_type))
    elif prob_type == 0:
        print(r"""
            --HELP:
            USING SIMPLEX CALCULATOR

            ----- requirements -----

            1 -> python - install python (https://www.python.org)
            2 -> pip    - install pip (google for your Operating System)
            3 -> numpy  - pip install numpy  - required!!
            4 -> pandas - pip install pandas - optional - makes the tableus more beautiful and orderly

            ----- choices -----

            1 -> Simplex maximization problems like maximization of profits
            2 -> Simplex minimization problem like minimization of expenditure in company
            0 -> Help on using the calculator

            ----- best data -----

            please rename your products to X1, X2, X3...Xn
            for easy feeding of data

            n - being the number of products you have

            example: computers - X1
                     printers  - X2

            you can use: - whole numbers
                         - decimal numbers
                         - fractions
                    Entering the value you are prompted to. the decimal are not 
                    rounded off on entering. this ensures high accuracy.
                    for recurring and long fractions, ie. (1/3). the decimal places are ronded of 
                    to default of python

            you are advised to use values less than 10000000
            you can standardize the data by dividing it to small values
            and re-converting after getting solution

            big values are used for slack in this program.
            so using big values may lead to confusion of data with the
            slack variables in some cases


            ----- assumptions -----

            I assume that you know how to read the simplex table.
            I also assume that you know how to interpret the data in the table and So 
            I did not interpret the data 

            This program is to be used by statisticians and also those with
            an idea about the simplex problems

            This programs though need no much knowledge on mathematics/statistics

            ----- mixed simplex problem -----

            I have not make a choice for mixed simplex problem and so for now 
            the program may not provide a solution for such problems

            ----- declaimer -----

            Only the console  option of this program is available yet but the GUI might be available
            at some point and when available, I will update on how to use the GUI.

            The program has been tested with several examples but maybe all the exception 
            may not have been countered fully. using this program will be an alternative
            you chose and so we I am not expecting a complain in failure to meet your expectation as indicated in the LICENCE.

            #You can suggest additions or even send me bugs in the program in the email below.#

            kimrop20@gmail.com



            ----- licence -----

            This program is to be used freely. You can also re-edit or modify or even add to
            this program.
            you can also share but you should not change the developer ownership.

            I will appreciate credit given to me

            ----- developer -----

            developed by [ELPHAS KIMUTAI ROP] .
            Student Bsc. Statistics and programming.
            Machakos University, Kenya.
            Email   : kimrop20@gmail.com
            Website : http://bestcoders.herokuapp.com



            """)
        sys.exit()
    print('\n##########################################')
    return prob_type


def main():
    prob_type = menu()

    product_names = []
    z_equation = []
    col_values = []

    # TODO is it reversed?
    # solutions = []
    x = 'X'
    # final_rows = []

    const_num = int(input("how many products do you have: >"))
    prod_nums = int(input("how many constrains do you have: >"))
    const_names = [x + str(i) for i in range(1, const_num + 1)]
    for i in range(1, prod_nums + 1):
        prod_val = input("enter constrain {} name: >".format(i))
        product_names.append(prod_val)
    print("__________________________________________________")

    is_max = True if prob_type == 1 else False

    for i in const_names:
        try:
            val = float(Fraction(input("enter the value of %s in Z equation: >" % i)))
        except ValueError:
            print("please enter a number")
            val = float(Fraction(input("enter the value of %s in Z equation: >" % i)))
        if is_max:
            # TODO should be int?
            z_equation.append(0 - int(val))
        else:
            # TODO should be int?
            z_equation.append(val)
    z_equation.append(0)

    while len(z_equation) <= (const_num + prod_nums):
        z_equation.append(0)
    print("__________________________________________________")

    # TODO should be an API instead
    for prod in product_names:
        for const in const_names:
            try:
                val = float(Fraction(input("enter the value of %s in %s: >" % (const, prod))))
            except ValueError:
                print("please ensure you enter a number")
                val = float(Fraction(input("enter the value of %s in %s: >" % (const, prod))))
            col_values.append(val)
        equate_prod = float(Fraction(input('equate %s to: >' % prod)))
        col_values.append(equate_prod)

    z2_equation, final_cols = standarize_rows(col_values, is_max, const_num, prod_nums)
    i = len(const_names) + 1

    if is_max:
        while len(const_names) < len(final_cols[0]) - 1:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        const_names.append('Solution')
        final_cols.append(z_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("_____________________________________________")
        decimals = int(input('Number of roundoff decimals : '))
        print('\n##########################################')
        maximization(final_cols, final_rows)

    else:
        while len(const_names) < prod_nums + const_num:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        solutions[:] = []
        add_from = len(const_names) + 1
        while len(const_names) < len(final_cols[0][:-1]):
            removable_vars.append('X' + str(add_from))
            const_names.append('X' + str(add_from))
            add_from += 1
        removable_vars.append(' Z')
        removable_vars.append('Z1')
        const_names.append('Solution')
        for ems in removable_vars:
            solutions.append(ems)
        while len(z_equation) < len(final_cols[0]):
            z_equation.append(0)
        final_cols.append(z_equation)
        final_cols.append(z2_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("________________________________")
        decimals = int(input('Number of roundoff decimals : '))
        print('\n##########################################')
        minimization(final_cols, final_rows)


if __name__ == "__main__":
    main()

# I use python list and arrays(numpy) in most of this program
# it became simple coz python has a strong power in list and array manipulation and solution
