
delimiter //
create trigger user_add_post after insert on article
  for each row
  begin
    update user
    set num_post = num_post + 1
    where user.ID = new.author;
    update classification
    set last_article_time = new.post_time, discussion = discussion + 1
    where classification.name = new.class;
  end;
//
delimiter ;


delimiter //
create trigger user_add_comment after insert on comment
  for each row
  begin
    update classification
    set num_comment = num_comment + 1
    where classification.name = (select article.class from article where article.serial_num = new.article_num);
  end;
//
delimiter ;
