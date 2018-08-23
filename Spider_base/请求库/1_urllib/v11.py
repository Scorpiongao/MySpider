from urllib import request

if __name__ == '__main__':

    url = "https://www.zhihu.com/people/feng-zi-42-31-4/following"

    rsp = request.urlopen(url)

    html = rsp.read().decode()
    print(html)
    # with open("rsp.html", "w") as f:
    #     f.write(html)