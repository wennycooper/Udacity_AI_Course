def update(mean1, var1, mean2, var2):
    new_mean = (var2*mean1 + var1*mean2) / (var2 + var1) 
    new_var  = 1. / (1./(var2) + 1./(var1))
    return [new_mean, new_var]

print update(10., 8., 13., 2.)

