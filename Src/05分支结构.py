def branch1():
    weight = float(input("体重(KG):"))
    height = float(input("身高(CM):"))
    bmi= weight/(height/100)**2
    if bmi<18.5:
        print(f"bmi={bmi:.1f}  too skinny!")
    elif bmi<20.5:
        print(f"bmi={bmi:.1f}  ok！")
    elif bmi<24:
        print(f"bmi={bmi:.1f}  good!")
    elif bmi<28:
        print(f"bmi={bmi:.1f}over weight!")
    else:print(f"bmi={bmi:.1f}  need to slim!")
def branch2():
    status_code = int(input('响应状态码: '))
    if status_code == 400:
        description = 'Bad Request'
    elif status_code == 401:
        description = 'Unauthorized'
    elif status_code == 403:
        description = 'Forbidden'
    elif status_code == 404:
        description = 'Not Found'
    elif status_code == 405:
        description = 'Method Not Allowed'
    elif status_code == 418:
        description = 'I am a teapot'
    elif status_code == 429:
        description = 'Too many requests'
    else:
        description = 'Unknown status Code'
    print('状态码描述:', description)
def branch3():
    status_code = int(input('响应状态码: '))
    match status_code:
        case 400 | 500:description = 'Bad Request'
        case 401 | 403 | 404: description = 'Not Allowed'
        case 418: description = 'I am a teapot'
        case 429: description = 'Too many requests'
        case _: description = 'Unknown Status Code'
    print('状态码描述:', description)
if __name__== "__main__":
    branch3()