
import sys
import sqlite3
from loggingmodule import init_logging

URL = r"static/db/article.sqlite"


class DbController:
    def __init__(self, url=URL):

        self.url = url

        self.logger = init_logging(__name__)
        self.logger.info(f"Connect : {self.url}")

        self.conn = sqlite3.connect(self.url)
        self.db = self.conn.cursor()

        self.commit_flag = False

        self._create_table()



        # self._create_tabl

    def _create_table(self):
        """
        ArticleID: 記事のID(未入力でよい)
        Create_DateTime: 投稿日時(サーバ時間)
        Post_User: 投稿者(デフォルト値: NoName)
        Image_URL: 画像ファイルパス
        Category: タグ
        Content: 投稿内容
        """
        try:
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS article(
                    ArticleID INTEGER PRIMARY KEY,
                    Create_DateTime TIMESTAMP DEFAULT (DATETIME('now','localtime')),
                    Post_User TEXT DEFAULT 'NoName',
                    Image_URL TEXT DEFAULT 'NotImage',
                    Category TEXT DEFAULT '未分類',
                    Content TEXT NOT NULL
                );
            """)

            self.logger.info("Success Create Table.")

        except Exception as e:
            self.logger.error(" ----- Error Information -----")
            self.logger.error(f"type : {str(type(e))}")
            self.logger.error(f"about: {str(e)}")

    def insert_record(self, datetime=None, username=None, image=None, category=None, content=None):
        if content is None:
            self.logger.error(f"Not Data List:[datetime: {datetime}, username: {username}, content: {content}]")
            self.logger.info("本文がありません。")
            return

        counter = len([x for x in self.db.execute("select * from 'article'")])
        counter += 1
        counter = str(counter)

        sql = f"insert into article values ({counter}, ?, ?, ?, ?, ?);"
        try:
            self.db.execute(sql, (datetime, username, image, category, content))
            self.commit_flag = True
        except Exception as e:
            self.logger.error(f"Error Message: {e}")
            self.logger.info("Failed Insert date")
        finally:
            self.db.close()

    def close_db(self):
        try:
            if self.commit_flag:
                self.conn.commit()
                self.logger.info("Success Commit.")
        except:
            self.logger.error("Failed Commit. Please Check System.")
        finally:
            self.db.close()
            self.logger.info("Close DataBase.")

    def insert_test_data(self):
        """ArticleID: Create_DateTime: Post_User: Image_URL: Category: Content: """
        counter = len([x for x in self.db.execute("select * from 'article'")])
        counter += 1
        counter = str(counter)
        self.db.execute(f"""insert into article values ({counter}, 20190113, "kujira_go", "URL", "未分類", "test_data");""")

    def check_data(self):
        result = len([x for x in self.db.execute("select * from 'article'")])
        self.close_db()

        return result

    def __del__(self):
        self.logger.info("call del")


if __name__ == "__main__":
    db = DbController(URL)
    db.insert_test_data()
    db.check_data()
    db.close_db()

    while 1:
        d = input("wait")
        if d == "exit":
            sys.exit(0)
