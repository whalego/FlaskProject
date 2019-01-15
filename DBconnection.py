
import sys
import sqlite3
from loggingmodule import init_logging

URL = r"static/db/article.sqlite"


class DbController:
    def __init__(self, url):

        self.url = url

        self.logger = init_logging(__name__)
        self.logger.info(f"Connect : {self.url}")

        self.conn = sqlite3.connect(self.url)
        self.db = self.conn.cursor()

        self._create_table()

        print([x for x in self.db.execute("select * from 'article'")])

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
            # self.db.execute("""
            #     CREATE TABLE IF NOT EXISTS article(
            #         ArticleID INTEGER PRIMARY KEY,
            #         Create_DateTime TIMESTAMP DEFAULT (DATETIME('now','localtime')),
            #         Post_User TEXT DEFAULT 'NoName',
            #         Image_URL TEXT DEFAULT 'NotImage',
            #         Category TEXT DEFAULT '未分類',
            #         Content TEXT NOT NULL
            #     );
            # """)
            self.db.execute("""
                CREATE TABLE IF NOT EXISTS article(
                    ArticleID INTEGER PRIMARY KEY,
                    Content TEXT NOT NULL
                );
            """)

            self.logger.info("Success Create Table.")

        except Exception as e:
            self.logger.error(" ----- Error Information -----")
            self.logger.error(f"type : {str(type(e))}")
            self.logger.error(f"about: {str(e)}")


    def insert_record(self, datetime=None, username=None, image=None, category=None, content=None):
        if datetime is None and username is None and content is None:
            self.logger.error(f"Not Data List:[datetime: {datetime}, username: {username}, content: {content}]")
            self.logger.info("日付、投稿者名、本文がありません。")
            return

        sql = "insert into article values (None, ?, ?, ?, ?, ?);"
        try:
            self.db.execute(sql, (datetime, username, image, category, content))
        except Exception as e:
            self.logger.error(f"Error Message: {e}")
            self.logger.info("Failed Insert date")

    def _commit(self):

        try:
            self.conn.commit()
            self.logger.info("Success Commit.")
        except:
            self.logger.error("Failed Commit. Please Check System.")

    def close_db(self, commit_flag=False):

        if commit_flag:
            self._commit()

        self.db.close()
        self.logger.info("Close DataBase.")


    def insert_test_data(self):
        # self.db.execute("""
        #     insert into article values(1, None, "kujira_go", "URL", "未分類", "test_data");
        # """)
        self.db.execute("""
            insert into article values(2, "test_data");       
        """)



if __name__ == "__main__":
    db = DbController(URL)
    db.insert_test_data()
    db.close_db(commit_flag=True)

