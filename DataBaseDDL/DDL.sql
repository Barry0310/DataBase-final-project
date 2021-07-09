create table user
  (ID           char(20),
   password     char(20),
   name         char(20),
   gender       char(6),
   education   	char(20),
   create_time  date,
   num_post  	 	int,
   primary key (ID)
  ) ENGINE=INNODB;

create table classification
  (name 	    	char(20),
   discussion  	int,
   num_comment  int,
   last_article_time  date,
   primary key (name)
 ) ENGINE=INNODB;

create table article
  (serial_num		int,
   author		    char(20),
   class			  char(20),
   title    		char(30),
   content      varchar(100),
   post_time   	date,
   primary key (serial_num),
   foreign key (author) references user (ID) on delete cascade,
   foreign key (class) references classification (name) on delete cascade
 ) ENGINE=INNODB;

create table comment
  (serial_num    int,
   userID		     char(20),
   article_num	 int,
   comment_time  date,
   content       varchar(50),
   primary key (serial_num),
   foreign key (userID) references user (ID) on delete cascade,
   foreign key (article_num) references article (serial_num)
 ) ENGINE=INNODB;

insert into classification values('Sport', 0, 0, NULL);
insert into classification values('Joke', 0, 0, NULL);
insert into classification values('Graduate', 0, 0, NULL);
insert into classification values('NTNU', 0, 0, NULL);
