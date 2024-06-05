import sqlite3

connect = sqlite3.connect('admin.db')
c = connect.cursor()
c.execute("SELECT * FROM income WHERE income_resource = ? AND type_of_income = ?;", ('bank', 'cash'))
income_list = c.fetchall()
c.execute("SELECT * FROM cost WHERE cost_resource = ? AND type_of_cost = ?;", ('bank', 'cash'))
cost_list = c.fetchall()

c.close()

income_list.extend(cost_list)
# for item in income_list:
#     if item[1]< 20000:
#         income_list.remove(item)
print(income_list)