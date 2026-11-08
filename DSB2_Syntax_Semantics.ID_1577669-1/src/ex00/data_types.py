def data_types():
    a = 1
    s = "lol"
    f = 3.14
    b = True
    l = [0,1,2]
    d = {"name": "bob"}
    t = (0,1,2)
    var_set = {0,1,2}

    types = [
        type(a), type(s), type(f), type(b), type(l), type(d), type(t), type(var_set)
    ]
    print(types)

if __name__ == '__main__':
    data_types()