create table my_student_info(
	stu_id int unsigned not null primary key auto_increment comment '学号',
	stu_name varchar(10) not null comment '姓名',
	stu_class int unsigned not null comment '班级',
	stu_age int unsigned not null comment '年龄',
	stu_gender bit default 0 comment '性别',
	stu_IDcard char(18) not null comment '身份证号',
	unique(stu_IDcard)
) ENGINE=InnoDB default charset=utf8 comment='学生信息表'; 
/**
create table my_teacher_info(
	tea_id int unsigned not null primary key auto_increment,
	tea_name varchar(10) not null comment '姓名',
	stu_gender bit default 0 comment '性别',
	stu_sub varchar(20) not null comment '科目'
) ENGINE= InnoDB default charset=utf8 comment='老师信息表';
**/
create table my_subject_info(
	sub_id int unsigned not null primary key auto_increment comment '科目ID',
	sub_name varchar(20) not null comment '科目名称'
) ENGINE=InnoDB default charset=utf8 comment '科目表';

create table my_score_info(
	sco_id int unsigned not null primary key auto_increment comment '科目ID',
	stu_id int unsigned comment '学生ID',
	sub_id int unsigned comment '科目ID',
	score int comment '成绩',
	foreign key(stu_id) references my_student_info(stu_id),
	foreign key(sub_id) references my_subject_info(sub_id)
) ENGINE=InnoDB default charset=utf8 comment '成绩表';
alter table my_student_info add isDelete unsigned not null default 0;
alter table my_subject_info add isDelete unsigned not null default 0;
alter table my_score_info add isDelete unsigned not null default 0;

insert into my_student_info(stu_name,stu_class,stu_age,stu_gender,stu_IDcard) 
	VALUES
	('张兰',1,18,1,'141024199811250032'),
	('张岁',0,18,1,'142314199811250032'),
	('张可',0,18,1,'140984199811250032'),
	('张年',1,18,1,'141024199811255532'),
	('lk',1,13,1,'142314199111250032'),
	('ks',0,14,1,'142314199511250032'),
	('fk',1,16,1,'142314199411250032'),
	('bn',0,17,1,'142314199311250032'),
	('ml',1,18,1,'142314199211250032');
update my_student_info set stu_class=2 where stu_class=0;
/**
insert into my_subject_info(sub_name) VALUES('语文');
insert into my_subject_info(sub_name) VALUES('数学');
insert into my_subject_info(sub_name) VALUES('英语');
**/
insert into my_subject_info(sub_name) VALUES('语文'),('数学'),('英语');

select * from my_student_info inner join my_score_info on my_student_info.stu_id=my_score_info.stu_id inner join my_subject_info on my_subject_info.sub_id=my_score_info.sub_id;

/**
left join 以左表为准
right join 以right表为准
inner join 以两者共同部分为准
**/


