import csv

#In this question first csv is imported 

dict = {}
# now first dict named empty dictionary is created to store the sum of salary according to the employee id

with open('Salaries.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] in dict:
            dict[row[0]] = dict.get(row[0])+int(row[2])
        else:
            dict[row[0]] = int(row[2])

    # print(dict)


departmentDict = {}

#now here departmentDict name empty dictionary is created to store the  sum of all employees working in department

with open('Employees.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader: 
        if row[2] in departmentDict:
            departmentDict[row[2]] = dict[row[0]]+departmentDict[row[2]]
        else:
            departmentDict[row[2]] = dict[row[0]]
    # print(departmentDict)

finalDictOp = {}

#now finalDictop name empty Dictionary is created to store the avg salary with department Name and avg(salary) is calculated using 
# divide by 12 method 

with open('Departments.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader: 
        finalDictOp[row[1]] = int(departmentDict[row[0]]/12)

sortedDict = sorted(finalDictOp.items(), key=lambda x: x[1], reverse=True)[:3]
#now at the last sortedDict Name Dictionary is created with reversely sorted values of finalDictOp 


#Now at the last values of sortedDict are Printed
print(f'{"DEPT_NAME": <12} AVG_MONTHLY_SALARY (USD)')
for item in sortedDict:
    k,v = item
    print('{0: <12} {1}'.format(k,v))
