import mysql.connector

class sql_connector():
    @staticmethod
    def send_score_easy(wpm, time, cpm):
        #connects to db
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sml12345",
            database="highscore"
        )
        mycursor = mydb.cursor()
        # sql command
        sql = "INSERT INTO highscore (wpm, time, cpm) VALUES (%s, %s, %s)"
        val = (wpm, time, cpm)
        mycursor.execute(sql, val)
        mydb.commit()

    @staticmethod
    def recive_score_easy():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sml12345",
            database="highscore"
        )
        mycursor = mydb.cursor()

        mycursor.execute("select * from highscore where wpm = (select max(wpm) from highscore)")

        data_highscore = mycursor.fetchone()
        highscore = ""
        # this returns a str with the id wpm time cpm
        for i, name in enumerate(['id: ', 'WPM: ', 'Time: ', 'CPM: ']):
            highscore += name + str(data_highscore[i]) + ' '

        return highscore

    @staticmethod # send/recive score easy/ hard is the same just diffrent table
    def send_score_hard(wpm, time, cpm):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sml12345",
            database="highscore"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO highscore_hard (wpm_hard, time_hard, cpm_hard) VALUES (%s, %s, %s)"
        val = (wpm, time, cpm)
        mycursor.execute(sql, val)
        mydb.commit()

    @staticmethod
    def recive_score_hard():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sml12345",
            database="highscore"
        )
        mycursor = mydb.cursor()

        mycursor.execute("select * from highscore_hard where wpm_hard = (select max(wpm_hard) from highscore_hard)")

        data_highscore = mycursor.fetchone()
        highscore = ""
        for i, name in enumerate(['id: ', 'WPM: ', 'Time: ', 'CPM: ']):
            highscore += name + str(data_highscore[i]) + ' '

        return highscore