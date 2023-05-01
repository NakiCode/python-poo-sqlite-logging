# importation des modules
import os
import sqlite3
from sqlite3 import Error
import logging

class data:
    
    def __init__(self):
        self.database = os.path.abspath(os.path.join(os.path.dirname(__file__), 'db/database.db'))
        self.conn = sqlite3.connect(self.database)
        logging.basicConfig(filename=os.path.abspath(os.path.join(os.path.dirname(__file__), "journal/journal.log")), format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    #############################################################################################
    def sql_request(self):
        try:
            sql = """
                PRAGMA foreign_keys=True;

                -- CREATION D'UNE TABLE DE Todo List
                CREATE TABLE IF NOT EXISTS Todo (
                    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                    'name' TEXT(50) NOT NULL,
                    'desc' TEXT (150) NOT NULL
                );
                -- CREATION DE LA VIEW
                CREATE VIEW IF NOT EXISTS selectAll
                AS 
                    SELECT * FROM Todo;
                
            """
            query = self.conn.cursor()
            query.executescript(sql)
            return True
        except Error as e:
            logging.error(f"Niveau : SQL REQUEST | Type : {e}", exc_info=True)
        finally:
            self.conn.commit()
            self.conn.close()
    ##########################################################"
    # INSERT DATA
    def insert(self, donnees):
        try:
            query = self.conn.cursor()
            query.executemany(""" INSERT INTO Todo (name, desc) VALUES (?, ?)""", donnees)
            return True
        except Error as e:
            logging.error(f"Niveau : INSERT | Type : {e}", exc_info=True)
        finally:
            self.conn.commit()
            self.conn.close()
    ##############################################################
    # SELECT
    def select(self):
        try:
            query = self.conn.cursor()
            query.execute(""" SELECT * FROM selectAll """)
            return query.fetchall()
        except Error as e:
            logging.error(f"Niveau :SELECT | Type : {e}", exc_info=True)
        finally:
            self.conn.commit()
            self.conn.close()
    ###########################################################
    # SELECT BY ID
    def select_id(self, id):
        try:
            query = self.conn.cursor()
            query.execute(""" SELECT * FROM selectAll WHERE id=? """, id)
            return query.fetchone()
        except Error as e:
            logging.error(f"Niveau :SELECT BY ID | Type : {e}", exc_info=True)
        finally:
            self.conn.commit()
            self.conn.close()
    #########################################################☺
    # SELECT BY ID
    def update(self, donnees):
        try:
            query = self.conn.cursor()
            query.execute("""UPDATE Todo SET desc=? WHERE id=? """, donnees)
            return True
        except Error as e:
            logging.error(f"Niveau : UPDATE | Type : {e}", exc_info=True)
        finally:
            self.conn.commit()
            self.conn.close()
    ################################################################
    # DELETE
    def delete(self, id):
        try:
            query = self.conn.cursor()
            query.execute("""DELETE FROM Todo WHERE id=? """, id)
            return True
        except Error as e:
            logging.error(f"Niveau : DELETE | Type : {e}", exc_info=True)
        finally:
            self.conn.commit()
            self.conn.close()


if __name__ == '__main__':
    data()
