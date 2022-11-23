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
            return Song([])
        return Song(data)
    
        

class Lyric_data:
    def __init__(self, lyric, senti_data):
        self.lyric = lyric
        self.mapping_score = []
        for data in senti_data:
            self.mapping_score.append(data)
            
    def get_lyrics(self):
        return self.lyric
    def get_score(self):
        return self.mapping_score
            
    @staticmethod
    def get_lyric(song_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM song_info_lyrics WHERE SONG_ID = '%s'" % str(song_id)
        db_cursor.execute(sql)
        data = db_cursor.fetchone()
        if not data:
            return None
        print(data)
        return Lyric_data(data[1], data[2:])
        
        

class Sound_data:
    def __init__(self, mp3_path, senti_data):
        self.mp3_path = mp3_path
        self.mapping_score = []
        for data in senti_data:
            self.mapping_score.append(data)
            
    def get_mp3_path(self):
        return self.mp3_path
    def get_score(self):
        return self.mapping_score
    
    @staticmethod
    def get_sound(song_id):
        mysql_db = conn_mysqldb()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * FROM song_info_sound WHERE SONG_ID = '%s'" % str(song_id)
        db_cursor.execute(sql)
        data = db_cursor.fetchone()
        if not data:
            return None
        return Lyric_data(data[1], data[2:])