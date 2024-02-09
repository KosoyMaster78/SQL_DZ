create table if not exists Style (
	id serial primary key,
	name_style varchar(60) not null unique
);

create table if not exists Musician (
	id serial primary key,
	nickname varchar(200) not null
);

create table if not exists Style_Musician (
	musician_id integer references Musician(id),
	style_id integer references Style(id),
	constraint pk primary key (musician_id, style_id)
);

create table if not exists Album (
	id serial primary key,
	name_album varchar(150) not null,
	year_bithday integer check(year_birthday >1800) not null
	
);

create table if not exists Musician_Album (
	id serial primary key,
	musician_id integer references Musician(id),
	album_id integer references Album(id)
	
);

create table if not exists Track (
	id serial primary key,
	name_record varchar(150) not null,
	length float4 check(length>0) not null,
	album_id integer references Album(id)
);

create table if not exists Collection (
	id serial primary key,
	name_collection varchar(150) not null,
	year_bithday integer check(year_birthday >1800) not null
);

create table if not exists Musician_Record (
	id serial primary key,
	collection_id integer references Collection(id),
	record_id integer references Track(id)	
);