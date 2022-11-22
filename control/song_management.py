from model.sql_connect import *

class Song():
    def __init__(self, data):
        self.song_id_list = []
        self.song_title_list = []
        for i in range(len(data)):
            self.song_id_list.append(data[i][0])
            self.song_title_list.append(data[i][1])
        
    def get_song_ids(self):
        return self.song_id_list
    def get_song_title(self):
        return self.song_title_list
    
    @staticmethod
    def get_song(string):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM song WHERE SONG_TITLE like '%" + str(string) +"%'"
        db_cursor.execute(sql)
        data = db_cursor.fetchall()
        if not data:
            return None
        return Song(data)
    
        