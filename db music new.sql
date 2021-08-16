CREATE TABLE IF NOT EXISTS singer(id serial primary key,name_singer text not null);
CREATE TABLE IF NOT EXISTS genre(id serial primary key,name_genre text not null);
CREATE TABLE IF NOT EXISTS singer_genre(singer_id integer references singer(id),genre_id integer references genre(id),
										constraint sg primary key(singer_id,genre_id));
CREATE TABLE IF NOT EXISTS album(id serial primary key,name_album text not null,year integer not null);
CREATE TABLE IF NOT EXISTS singer_album(singer_id integer references singer(id),album_id integer references album(id),
									   constraint sa primary key(singer_id,album_id));
CREATE TABLE IF NOT EXISTS song(id serial primary key,album_id integer references album(id),name_song text not null,duration numeric);
CREATE TABLE IF NOT EXISTS music_collection(id serial primary key,name_collection text not null,year integer not null);
CREATE TABLE IF NOT EXISTS song_collection(id serial primary key,song_id integer references song(id),
										   collection_id integer references music_collection(id),song text not null);