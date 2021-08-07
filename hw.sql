CREATE TABLE IF NOT EXISTS singer(id serial primary key,name_singer text not null);
CREATE TABLE IF NOT EXISTS album(id serial primary key,album_id integer references singer(id),name_album text not null,year integer)
CREATE TABLE IF NOT EXISTS song(id serial primary key,song_id integer references album(id),name_song text not null,duration numeric)
CREATE TABLE IF NOT EXISTS genre(id serial primary key,name_genre text not null)
ALTER TABLE singer ADD COLUMN genre_id integer references genre(id)