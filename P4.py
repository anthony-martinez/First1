def pay_raise(current_salary):
    new_salary = 0
    if current_salary < 20000:
        new_salary = current_salary * 1.10
    else:
        new_salary = current_salary * 1.07
    return new_salary

pete_salary = 19000
bob_salary = 40000

print "New pete salary - ", pay_raise(pete_salary)
print "New bob salary - ", pay_raise(bob_salary)

name = 'Joe'
if name == 'joe':
    print 'Name: ' + name


x = 10
if x < 100:
    print x
else:
    print 100













