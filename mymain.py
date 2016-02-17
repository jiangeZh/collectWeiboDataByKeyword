# -*- coding: utf-8 -*-

import login
import collectWeiboDataByKeyword
import urllib
import urllib2
import sys

uid = 'your weibo username'
psw = 'your password'

reload(sys)
sys.setdefaultencoding('utf8')

simLogin = login.WeiboLogin(uid, psw)
simLogin.login()

collectWeiboDataByKeyword.main();
