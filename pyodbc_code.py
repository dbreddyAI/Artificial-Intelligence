import csv
import pyodbc
print("____________________ checking below the list of available drivers ___________________")
print(pyodbc.drivers())
print("_____________________________________________________________________________________")
conn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                      "Server=DBREDDY-PC;"  # localhost windows authentication
                      "Database=venolearn;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()
print(dir(cursor))
print("________________________________________________________________________________________________")
cursor.tables()
table_names = cursor.fetchall()
final = []
for i in table_names:
    # print(i)
    # print(type(i))
    if i[1] == 'dbo':  # dbo means database owner
        req_table = i[2]
        print(req_table)
        final.append(req_table)
        print(final)
print("______________________________________________")
print(final)
for k in final:
    print(k)
    query = "select * from" + ' ' + k
    print(query)
    cursor.execute(query)
    data_rows = cursor.fetchall()
    print(data_rows)
    with open(k + '.csv', 'w', newline='') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(data_rows)



'''with open('training.csv', 'w', newline='') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(["Reg_ID", "Person_Name", "Skill", "Expr", "Gender", "city", "Email_ID", "Ph_No", "Batch", "Age", "Reg_Date"])
    a.writerows(rows)'''

cursor.close()
conn.close()







