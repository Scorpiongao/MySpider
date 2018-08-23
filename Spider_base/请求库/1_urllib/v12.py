from urllib import request


if __name__ == '__main__':

    url = "https://www.zhihu.com/people/feng-zi-42-31-4/following"

    headers = {
        "Cookie": '_zap=d265f226-e444-401f-8837-6a1cf45ca8b0; q_c1=3aa9b22fb31f40d49d5eb91bd0b80b41|1533137064000|1517057362000; __DAYU_PP=7VzvNQNebVAqzNQuvvZV37118d081081; __utma=51854390.1081658639.1521704527.1521704527.1521780852.2; __utmz=51854390.1521780852.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20160526=1^3=entry_date=20160526=1; z_c0="2|1:0|10:1521870028|4:z_c0|80:MS4xWC00VEF3QUFBQUFtQUFBQVlBSlZUY3d5bzF0X3RPOVBiaG54VS1SemxzTTB3OG9DdXdwZnZ3PT0=|cd8ab991912f99d846a4797f735e023178edc244584760caa3256697128fec28"; d_c0="ABBhMOjaig2PTl7wQSCyujeacdw8IWgTAhA=|1525436707"; _xsrf=178ed40b-ff99-49ce-acb0-3f35c10c714f; tgw_l7_route=5bcc9ffea0388b69e77c21c0b42555fe'
    }


    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

    # with open("rsp.html", "w") as f:
    #     f.write(html)
