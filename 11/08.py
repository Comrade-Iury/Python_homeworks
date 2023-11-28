url = input()
key = input()
url = url.split("?").pop().split("&")

for i in range(len(url)):
    url[i] = url[i].split("=")
    if url[i][0] == key:
        print(url[i][1])
        break
