from file_handle import read_data

def total_expense():
    rows=read_data()
    total=0

    for row in rows[1:]:

        total+=float(row[4])

    print(f"\nTotal Expense:{total}")    