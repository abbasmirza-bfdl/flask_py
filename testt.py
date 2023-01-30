from flask import request
from random import randint
url='https://www.guru99.com/linux-redirection.html#1'

urlid=request.host_url(url)+str(randint(0,9))
print(urlid)