def string_splosion(str):
    newstr = []
    for i in range(1, len(str)+1):
        newstr.append(str[:i])
    return "".join(newstr)
