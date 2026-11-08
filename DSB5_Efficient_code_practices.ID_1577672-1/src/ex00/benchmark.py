import timeit

def loop(emails):
    res = []
    for email in emails:
        if email.split('@')[1]== 'gmail.com':
            res.append(email)
    return res

def comprehension(emails):
    return [email for email in emails if email.split('@')[1]== 'gmail.com']

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']*5
    loop_time = timeit.timeit(lambda: loop(emails), number=900000)
    comp_time = timeit.timeit(lambda: comprehension(emails), number=900000)
    print(loop(emails))
    print(comprehension(emails))
    if comp_time <= loop_time:
        print('It is better to use a list comprehension')
        print(f"{comp_time} vs {loop_time}")   
    else:
        print('It is better to use a loop')
        print(f"{loop_time} vs {comp_time}")

if __name__ == '__main__':
    main()