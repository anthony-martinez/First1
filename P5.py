def absolute(N):
    if N < 0:
        return -1 * N
    else:
        return N

print "|-1| = ", absolute(-1)
print "|100| = ", absolute(100)
print "|0| = ", absolute(0)

x = 9
if x < 0:
    print 'Negative'
elif x== 0:

    print 'Zero'
else:
    print 'Positive'

###################### TAX EXAPLE ###########################
def get_tax_amount(salary):
    if salary < 20000:
        return 0
    elif salary >= 20000 and salary < 50000:
        return 0.15 * salary
    elif salary >= 50000 and salary < 100000:
        return 0.20 * salary
    else:
        return 0.33 * salary




