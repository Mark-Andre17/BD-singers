import sqlalchemy

with open('pass.txt', 'r') as filename:
    my_pass = filename.read()

engine = sqlalchemy.create_engine(f'postgresql://postgres:{my_pass}@localhost:5432/music_singers')
c = engine.connect()
singers = c.execute("""SELECT genre_id, COUNT(singer_id) FROM singer_genre GROUP BY genre_id;""").fetchmany(10)

track = c.execute("""SELECT COUNT(s.id) FROM song s
                     JOIN album a ON a.id = s.album_id
                     WHERE a.year BETWEEN 2019 AND 2020;""").fetchmany(10)

avr_duration = c.execute("""SELECT a.name_album, AVG(duration) FROM song s JOIN album a ON s.album_id = a.id GROUP BY 
a.name_album;""").fetchmany(10)

other_singers = c.execute("""SELECT s.name_singer FROM singer s 
                            JOIN singer_album sa ON s.id = sa.singer_id 
                            JOIN album a ON a.id = sa.album_id 
                            WHERE year != 2020;""").fetchmany(10)

name_coll = c.execute("""SELECT mc.name_collection FROM music_collection mc
                        JOIN song_collection sc ON mc.id = sc.collection_id
                        JOIN song s ON s.id = sc.song_id
                        JOIN album a ON a.id = s.album_id
                        JOIN singer_album sa ON sa.album_id = a.id
                        JOIN singer si ON si.id = sa.singer_id
                        WHERE name_singer = 'Макс Корж';""").fetchmany(10)

genre = c.execute("""SELECT a.name_album FROM album a 
                     JOIN singer_album sa ON sa.album_id = a.id
                     JOIN singer s ON s.id = sa.singer_id
                     JOIN singer_genre sg ON sg.singer_id = s.id
                     GROUP BY a.name_album
                     HAVING COUNT(sg.genre_id)>1;""").fetchmany(10)

song = c.execute("""SELECT s.name_song FROM song s
                    LEFT JOIN song_collection sc ON sc.song_id = s.id
                    WHERE collection_id IS NULL;""").fetchmany(10)

min_duration = c.execute("""SELECT s.name_singer FROM singer s
                            JOIN singer_album sa ON sa.singer_id = s.id
                            JOIN album a ON a.id = sa.album_id
                            JOIN song so ON so.album_id = a.id
                            WHERE duration = (SELECT min(duration) FROM song);""").fetchmany(10)

album = c.execute("""SELECT DISTINCT a.name_album FROM album a
                     JOIN song s ON s.album_id = a.id
                     WHERE s.album_id IN(SELECT album_id FROM song
                     GROUP BY album_id
                     HAVING COUNT(id)=(SELECT COUNT(id) FROM song
                     GROUP BY album_id
                     ORDER BY COUNT
                     LIMIT 1));""").fetchmany(10)

