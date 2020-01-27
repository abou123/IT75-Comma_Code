def comma_code(argList):
    string = ""

    for i in range(len(argList) - 1):
        string = string + argList[i] + ', '

    string = string + 'and ' + argList[i+1] + 'foo'

    return string
