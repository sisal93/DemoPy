var_string = input("enter the string")
var_upper = 0
var_lower = 0
var_space = 0

for i in range(len(var_string)):
    if 'a' <= var_string[i] <= 'z':
        var_lower = var_lower + 1

    if 'A' <= var_string[i] <= 'Z':
        var_upper = var_upper + 1

    if var_string[i] == " ":
        var_space = var_space + 1

print(var_lower)
print(var_upper)
print(var_space)
