create table if not exists woeid (id SERIAL not null, name varchar(100) not null, created_at timestamp not null default current_timestamp, updated_at timestamp not null default current_timestamp);
create table if not exists twitter_trends (id SERIAL not null, rank smallint not null, name varchar(100) not null, url varchar(255) not null, tweet_volume integer, created_at timestamp not null default current_timestamp, updated_at timestamp not null default current_timestamp);

insert into woeid values (23424856, 'Japan');