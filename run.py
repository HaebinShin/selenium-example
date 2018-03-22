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
parser.add("--dest", dest="dest", help="destination page", required=True)
parser.add("--id", dest="id", help="manipulate html tag id", required=True)
parser.add("--chromedriver-path", dest="chromedriver_path", help="chromedriver path", required=True)
parser.add("--profile-path", dest="profile_path", help="user data dir for browser profile", default=None)
parser.add("--browser-bin-path", dest="browser_bin_path", help="browser binary path", default=None)
args = vars(parser.parse_args())

if args["browser_bin_path"] != None:
    capabilities = {'chrome.binary': args["browser_bin_path"]}
else:
    capabilities = None

if args["profile_path"] != None:
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=" + args["profile_path"]) #Path to your chrome profile
else:
    options = None

put_log("start browser")
driver = webdriver.Chrome(executable_path=args["chromedriver_path"], desired_capabilities=capabilities, chrome_options=options)
driver.get(args["dest"])

# Manipulate what you want.
# e.g. how to fill form tag value?
#   : driver.find_element_by_id("example").send_keys("blahblah")

driver.find_element_by_id(args["id"]).click()
put_log("finish")
driver.quit()
