from tvextractor import TVExtractor
from dotenv import load_dotenv
import os

load_dotenv()

extractor = TVExtractor(['FCPOF2023', 'FCPOG2023'], os.environ['tv_username'], os.environ['tv_password'], "C:/Users/Mohamad Fadil/Downloads", "JqgggM9t")

driver = None
while driver == None:
    driver = extractor.init_driver()

authed = False
while authed == False:
    authed = extractor.authenticate(driver)

extracted = False
while extracted == False:
    extracted = extractor.pull_data(driver)

extractor.deinit(driver)
