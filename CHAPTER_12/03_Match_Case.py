def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Error"
        case _:
            return "Unknown Status"

a=http_status(200)
print(a)
b=http_status(404)
print(b)
c=http_status(500)
print(c)
d=http_status(5)
print(d)