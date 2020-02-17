from function import *
from jdSeckill import *
import json

def main():

	jd = JDSecKill()
	jd.cookies = build_cookies('cookiesDate.txt')
	print(json.dumps(jd.cookies))
	print(loginValidation(jd.sess, jd.cookies))


if __name__ == "__main__":
	main()