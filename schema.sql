DROP TABLE IF EXISTS posts;
    CREATE TABLE POSTS (
            id int primary key autoincrement,
            name text not null,
            content text not null,
);
