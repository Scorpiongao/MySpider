import requests
from lxml import etree
from pyquery import PyQuery as pq

class Login():
    def __init__(self):
        self.headers={
            'Host': 'github.com',
            'Referer': 'https://github.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        self.login_url='https://github.com/login'
        self.post_url='https://github.com/session'
        self.logined_url='https://github.com/settings/profile'
        self.session=requests .session()


    def token(self):
        response=self.session .get(self.login_url,headers=self .headers )
        selector=etree .HTML(response .text )
        token=selector .xpath('//*[@id="login"]/form/input[2]/@value')[0]
        print('token:',token )
        return token


    def login(self,email,password):
        post_data={
            'commit': 'Sign in',
            'utf8':' ✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response=self.session.post(self.post_url ,data=post_data ,headers=self.headers )
        if response .status_code ==200:
            self.get_repositories(response .text )

        response =self.session .get(self.logined_url ,headers=self.headers )
        if response .status_code ==200:
            self.profile(response.text  )

    def get_repositories(self,html):
        doc=pq(html)
        repositories=doc('div.Box-body ul.list-style-none li').items()
        for item in repositories :
            href=item('a').attr('href')
            base_url='https://github.com/'
            # //*[@id="dashboard"]/div[1]/div[2]/div[2]/ul/li[1]
            # //*[@id="dashboard"]/div[1]/div[2]/div[2]/ul/li[2]
            #//*[@id="dashboard"]/div[1]/div[2]/div[2]/ul/li[3]
            print(base_url+href)

    def profile(self,html):
        selector=etree.HTML(html)
        image_url=selector .xpath('//*[@id="profile_37337566"]/dl/dd/img/@src')[0]
        resp=requests .get(image_url )
        with open('pic.jpg','wb')as f:
            f.write(resp .content )


EMAIL = '1456586096@qq.com'
PASSWORD = 'mlf1456586096@'

if __name__ =='__main__':
    app=Login ()
    app.login(EMAIL ,PASSWORD )