import pymysql
from dotenv import load_dotenv
import os 

# load .env
load_dotenv(verbose=True)

class DB():
    def connection(self):
        self.con = pymysql.connect(host=os.getenv('host'), user=os.getenv('user'), password=os.getenv('password'),
                       db=os.getenv('db'), charset='utf8') #env파일에서 db정보를 읽어 연결한다
        self.cur = self.con.cursor(pymysql.cursors.DictCursor)
    def close(self):
        self.con.close()
