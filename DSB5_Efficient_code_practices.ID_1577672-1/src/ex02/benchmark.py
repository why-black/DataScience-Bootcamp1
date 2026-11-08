import timeit
import sys

def loop(emails):
    res = []
    for email in emails:
        if email.split('@')[1]== 'gmail.com':
            res.append(email)
    return res

def comprehension(emails):
    return [email for email in emails if email.split('@')[1]== 'gmail.com']

def use_map(emails):
    return list(map(lambda email: email if email.split('@')[1] == 'gmail.com' else None, emails))
    #если без нан, но грраздо дольше даже loop
    #return [email for email in map(lambda email: email if is_gmail(email) else None, emails) if email is not None]

def use_filter(emails):
    return list(filter(lambda email: email.split('@')[1]=='gmail.com', emails))

def main():
    if len(sys.argv)!=3:
        raise Exception('must be 3 arguments')

    func = sys.argv[1]
    num_of_steps = int(sys.argv[2])

    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5

    functions  = {
        'loop': loop,
        'list_comprehension': comprehension,
        'map': use_map,
        'filter': use_filter,
    }

    if func not in functions:
        raise Exception('incorrect function name')

    res = timeit.timeit(lambda: functions[func](emails), number=num_of_steps)
    print(loop(emails))
    print(comprehension(emails))
    print(use_map(emails))
    print(res)

if __name__ == '__main__':
    main()