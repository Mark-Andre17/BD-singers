import sqlalchemy
with open('pass.txt', 'r') as filename:
    my_pass = filename.read()


engine = sqlalchemy.create_engine(f'postgresql://postgres:{my_pass}@localhost:5432/music_singers')
connection = engine.connect()
# INSERT заполнение таблиц
connection.execute("""INSERT INTO singer(id,name_singer)VALUES(1,'Макс Корж'),
                                                              (2,'Korn'),
                                                              (3,'Hurts'),
                                                              (4,'Nirvana'),
                                                              (5,'Лолита'),
                                                              (6,'Zivert'),
                                                              (7,'Михаил Круг'),
                                                              (8,'Louis Armstrong');""")
connection.execute("""INSERT INTO genre(id,name_genre)VALUES(1,'Хип-Хоп'),
                                                            (2,'Рок'),
                                                            (3,'Поп'),
                                                            (4,'Шансон'),
                                                            (5,'Джаз');""")
connection.execute("""INSERT INTO singer_genre(singer_id,genre_id)VALUES(1,1),(2,2),(3,2),(4,2),(5,3),(6,3),(7,4),(8,
5);""")
connection.execute("""INSERT INTO album(id,name_album,year)VALUES(1,'Животный мир',2012),
                                                              (2,'See You on the Other Side',2006),
                                                              (3,'Faith',2020),
                                                              (4,'Nevermind',1991),
                                                              (5,'Раневская',2018),
                                                              (6,'Vinyl',2019),
                                                              (7,'Мадам',1998),
                                                              (8,'Jazz Festivall',1967);""")
connection.execute("""INSERT INTO singer_album(singer_id,album_id)VALUES(1,1),
                                                              (2,2),
                                                              (3,3),
                                                              (4,4),
                                                              (5,5),
                                                              (6,6),
                                                              (7,7),
                                                              (8,8);""")
connection.execute("""INSERT INTO song(id,album_id,name_song,duration)VALUES(1,1,'Время',4.11),
                                                                (2,1,'Небо поможет нам',3.28),
                                                                (3,1,'В темноте',3.03),
                                                                (4,2,'Coming Undone',3.19),
                                                                (5,2,'Seen It Al',6.19),
                                                                (6,3,'Redemption',4.18),
                                                                (7,4,'Smells Like Teen Spirit',5.01),
                                                                (8,5,'На Титанике',3.52),
                                                                (9,6,'Beverly Hills',4.13),
                                                                (10,7,'Владимирский централ',4.27),
                                                                (11,8,'What a Wonderful World',2.21),
                                                                (12,6,'Fly',3.13),
                                                                (13,4,'Lithium',3.13),
                                                                (14,3,'All I Have to Give',5.24),
                                                                (15,8,'Let My people go',3.40);""")
connection.execute("""INSERT INTO music_collection(id,name_collection,year)VALUES(1,'Лучшее для спорта',2020),
                                                                    (2,'Лучшие рок хиты',2019),
                                                                    (3,'Лучшее на Maximum',2021),
                                                                    (4,'Pop industry',2018),
                                                                    (5,'90-e',1990),
                                                                    (6,'Грэмми',2000),
                                                                    (7,'Лучшие песни лета',2017),
                                                                    (8,'Русская эстрада',2020);""")
connection.execute("""INSERT INTO song_collection(id,song_id,song,collection_id)VALUES(1,1,'Время',1),
                                                                (2,2,'Небо поможет нам',1),
                                                                (3,3,'В темноте',1),
                                                                (4,4,'Coming Undone',2),
                                                                (5,5,'Seen It Al',2),
                                                                (6,6,'Redemption',3),
                                                                (7,7,'Smells Like Teen Spirit',2),
                                                                (8,8,'На Титанике',8),
                                                                (9,9,'Beverly Hills',7),
                                                                (10,10,'Владимирский централ',5),
                                                                (11,11,'What a Wonderful World',6),
                                                                (12,12,'Fly',4),
                                                                (13,13,'Lithium',3),
                                                                (14,14,'All I Have to Give',2),
                                                                (15,15,'Let my people go',6);""")
# SELECT
name_year = connection.execute("""SELECT name_album,year FROM album WHERE year = 2018;""").fetchmany(10)
# print(name_year)
duration = connection.execute("""SELECT name_song,duration FROM song ORDER BY duration DESC;""").fetchone()
# print(duration)
name_songs = connection.execute("""SELECT name_song FROM song WHERE duration >= 3.5;""").fetchmany(10)
# print(name_songs)
collections = connection.execute("""SELECT name_collection FROM music_collection WHERE year BETWEEN 2018 AND 2020;""").fetchmany(10)
# print(collections)
a = connection.execute("""SELECT name_singer FROM singer WHERE name_singer LIKE '%% %%';""").fetchmany(10)
b = connection.execute("""SELECT name_singer FROM singer WHERE name_singer LIKE '%%%%';""").fetchmany(10)
d = list(set(b)-set(a))
# print(d)
track = connection.execute("""SELECT name_song FROM song WHERE name_song LIKE '%%My%%' OR name_song LIKE '%%мой%%';""").fetchmany(10)
# print(track)