#列表作为参数传递
def arithmetic(args = [],operator="+"):
    x = args[0]
    y = args[1]
    result = {
        "+": x + y ,
        "-": x - y ,
        "*": x * y ,
        "/": x / y 
    }
    return result.get(operator)
print arithmetic([1, 2])
