use menangrie;
show tables;
create table students
(roll int not null primary key,
name varchar(20) not null,
class integer  check(class>=9 and class<=12),
class_teacher varchar(20),
mobile numeric unique,
maths_marks numeric check(maths_marks>0),
phy_marks numeric check(phy_marks>0),
chem_marks numeric check(chem_marks>0),
eng_marks numeric check(eng_marks>0),
comp_marks numeric check(comp_marks>0)
);

 drop table students;
 desc students;
select * from students;
 where gross is null;
 
 desc employee;
 