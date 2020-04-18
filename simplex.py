import pandas as pd
import numpy as np


product_names = []
col_values = []
final_rows = []
solutions = []
x = 'X'
z2_equation = []
removable_vars = []
NO_SOLUTION_STR = """
        ---unboundedness ----
Your problem might not be having solution due to wrong 
formulation of constrains,

This mostly occurs when you leave out some relevant constrains 
please check again the formulation of constrains
            """


def maximization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print(" 1 TABLEAU")
    try:
        final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(final_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element != 1 and min_manager == 1 and count < 6:
        print("*********************************************************")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col

            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows

        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('pivot element: %s' % pivot_element)
        print('pivot column: ', pivot_row)
        print('pivot row: ', pivot_col)
        print("\n")
        solutions[index_pivot_col] = const_names[index_pivot_row]

        print(" %d TABLEAU" % count)
        try:
            final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(final_pd)
        except:
            print("%d TABLEAU" % count)
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)
    if not pandas_av:
        print("""
        Please install pandas to make your tables look good
        install using command $pip install pandas 
        """)


def minimization(final_cols, final_rows):
    row_app = []
    last_col = final_cols[-1]
    min_last_row = min(last_col)
    min_manager = 1
    print("1 TABLEAU")
    try:
        fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        print(fibal_pd)
    except:
        print('  ', const_names)
        i = 0
        for cols in final_cols:
            print(solutions[i], cols)
            i += 1
    count = 2
    pivot_element = 2
    while min_last_row < 0 < pivot_element and min_manager == 1:
        print("*********************************************************")
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0
        print('pivot element: %s' % pivot_element)
        print('pivot column: ', pivot_row)
        print('pivot row: ', pivot_col)
        print("\n")
        removable = solutions[index_pivot_col]
        solutions[index_pivot_col] = const_names[index_pivot_row]
        if removable in removable_vars:
            idex_remove = const_names.index(removable)
            for colms in final_cols:
                colms.remove(colms[idex_remove])
            const_names.remove(removable)
        print("%d TABLEAU" % count)
        try:
            fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
            print(fibal_pd)
        except:
            print('  ', const_names)
            i = 0
            for cols in final_cols:
                print(solutions[i], cols)
                i += 1
        count += 1
        final_rows[:] = []
        new_final_rows = np.array(final_cols).T.tolist()
        for _list in new_final_rows:
            final_rows.append(_list)

        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col[:-1])
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        if pivot_element < 0:
            print(no_solution)

    if not pandas_av:
        print("""
        Please install pandas to make your tables look good
        install using command $pip install pandas 
        """)


def standarize_rows(column_values, is_max, const_num, prod_nums):
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]

    if not is_max:
        sum_z = (0 - np.array(final_cols).sum(axis=0)).tolist()
        for _list in sum_z:
            z2_equation.append(_list)

    for cols in final_cols:
        if is_max:
            while len(cols) < (const_num + prod_nums):
                cols.insert(-1, 0)
        else:
            while len(cols) < (const_num + (2 * prod_nums) - 1):
                cols.insert(-1, 0)

    i = const_num

    if not is_max:
        for sub_col in final_cols:
            sub_col.insert(i, -1)
            z2_equation.insert(-1, 1)
            i += 1

    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    if not is_max:
        while len(z2_equation) < len(final_cols[0]):
            z2_equation.insert(-1, 0)

    return final_cols
