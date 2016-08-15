from robobrowser import RoboBrowser

import random
DEBUG=True
def dbg(message):
    if DEBUG:
        print(message)
        return
    else:
        return
fbbrowser = RoboBrowser(history=True,parser="html.parser")
def login(username,password):
    global fbbrowser
    USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
                   'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
                   'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
                   ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                    'Chrome/19.0.1084.46 Safari/536.5'),
                     ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                    'Safari/536.5'),)

    fbbrowser.session.headers['User-Agent'] = random.choice(USER_AGENTS)
    dbg("Pointing browser to facebook.com...")
    fbbrowser.open('https://m.facebook.com/')
    login_form=fbbrowser.get_form(0)
    dbg("Typing username...")
    login_form['email']=username
    dbg("Typing password...")
    login_form['pass']=password
    dbg("Logging in....")
    fbbrowser.submit_form(login_form)
    try:
        links=fbbrowser.get_links()
        if(links[0].text=='Not Now'):
            dbg("Remember browser...")
            form=fbbrowser.get_form(0)
            fbbrowser.submit_form(form)
    except Exception as e:
        pass
    links=fbbrowser.get_links()
    for link in links:
        if(link.text=='Chat'):
            print("Login success...")
            return 0
    dbg("login failure...")
    return 1


def postfb("message"):
    


if __name__ == '__main__':