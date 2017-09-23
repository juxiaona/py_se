from common.testrunner import TestRunner
from common.sendmail import SendMail

if __name__ == '__main__':
	
	run_all=TestRunner("./testcases","Auto Test Report","Test case execution")
	run_all.run()


