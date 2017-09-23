import sys
sys.path.append('../')
from pages.login_page import LoginPage
import unittest
import ddt
from common.read_data import ReadExcel
from time import sleep

testdata=ReadExcel('../data/user_failed.xlsx', 'user').data_dict()
@ddt.ddt
class LoginFailed(unittest.TestCase):

	def setUp(self):

		self.login_failed=LoginPage()

	@ddt.data(*testdata)
	def test_login_failed(self,data):

		self.login_failed.login(data['username'], data['password'])
		error_msg=self.login_failed.get_login_error_text()
		self.assertEqual(data['error_msg'],error_msg)
		sleep(1)

	def tearDown(self):
		self.login_failed.quit()

if __name__ == '__main__':
	
	unittest.main()

