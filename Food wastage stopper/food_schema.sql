
drop table if exists posts;
	create table posts (
		id integer primary key autoincrement,
		price text not null,
		content text not null,
		user_name text
);
