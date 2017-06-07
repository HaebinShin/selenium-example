from time import strftime, localtime
def put_log(message):
	time = strftime("%Y-%m-%d %H:%M:%S", localtime())
	print("{} | {}".format(time, message))
	

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.chrome.options import Options
import configargparse
import os
parser = configargparse.ArgParser(default_config_files=[os.path.join(os.path.dirname(__file__), "script.conf"), "script.conf"])
parser.add("-c", "--my-config", required=False, is_config_file=True, help="config file parserath")
parser.add("--user-data-dir", dest="user_data_dir", help="user data dir for browser profile", required=True)
parser.add("--dest", dest="dest", help="destination page", required=True)
parser.add("--id", dest="id", help="manipulate html tag id", required=True)
args = vars(parser.parse_args())

capabilities = {'chrome.binary': '/usr/bin/google-chrome'}

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=" + args["user_data_dir"]) #Path to your chrome profile

put_log("start browser")
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", desired_capabilities=capabilities, chrome_options=options)
driver.get(args["dest"])
driver.find_element_by_id(args["id"]).click()
put_log("finish")
#driver.quit()
