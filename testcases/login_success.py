import sys
sys.path.append("../")

from pages.login_page import LoginPage
import unittest
from time import sleep
from common.read_data import ReadExcel
import ddt

testdata=ReadExcel('../data/user.xlsx', 'user').data_dict()

@ddt.ddt
class LoginSuccess(unittest.TestCase):
	
	def setUp(self):

		self.login_success=LoginPage()

	@ddt.data(*testdata)
	def test_login_success(self,data):

		self.login_success.login(data["username"],data["password"])
		text=self.login_success.get_login_success_text()
		self.assertIn(data["username"], text)

		url=self.login_success.get_login_success_url()
		self.assertIn('wp-admin', url)

	def tearDown(self):
		self.login_success.quit()



if __name__ == '__main__':
	unittest.main()