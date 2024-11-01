-- 입사일의 마지막 날짜를 출력하세요.
-- 10/01 -> 10/31
select last_day(hire_date) from employees;

-- 가입일
select sdate from students;

-- 가입일 1년후 날짜를 출력하세요.
select add_months(sdate, 12) from students;

-- 현재일 기준으로 가입일이 6개월이내의 회원만 출력하세요.
select sdate, add_months(sysdate, -6) from students
where sdate >= add_months(sysdate, -6) order by sdate;

-- 월별로 가입인원을 출력하세요.
select substr(mdate, 0, 5), count(substr(mdate, 0, 5)) from member
group by substr(mdate, 0, 5)
order by substr(mdate, 0, 5)
;

-- employees 테이블에서 부서별(department_id) 인원을 출력하세요.
select count(*), nvl(to_char(department_id), 'ceo') from employees group by department_id;


-- 그룹함수 : sum, avg, count, min, max, median
create table emp3 as select * from employees;
select * from emp3;
create table emp4 as select * from employees where 1=2;
select * from emp4;

-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법.
insert into emp4 select * from employees;
rollback;
-- insert, update, delete
-- commit, rollback

insert into emp4(employee_id, emp_name, hire_date) select employee_id, emp_name, hire_date from employees;

-- 테이블
-- create : 생성, alter : 변경, drop : 삭제,
select * from emp4;
-- alter add : 컬럼 추가
alter table emp4 add(hire_date2 date);
-- alter modify : 컬럼 타입 변경
-- 컬럼에 데이터가 있다면 제약조건이 있다, ex) 50으로 변경하려고 할 때 65길이의 문자가 있다면 변경 불가.
alter table emp4 modify (email varchar2(70));
alter table emp4 modify (email varchar2(50));
alter table emp4 modify (emp_name varchar2(10));
-- emp_name이 가지고 있는 최대 길이가 17인데 10으로 변경하려고 해서 에러 발생
-- 변경 안되는 예시
select length(emp_name) em from employees order by em desc;

-- email 컬럼에 employee_id 값을 복사
update emp4 set email = employee_id;
select * from emp4;

-- employee_id값을 phone_number에 입력하세요.
-- phone_number 문자형, employee_id 숫자형
update emp4 set phone_number = employee_id;
commit;
-- 문자형 -> 숫자형에 복사
-- 문자형에 숫자 외의 값이 있다면 복사 불가능하다.
update emp4 set manager_id = phone_number;
rollback;
select * from emp4;
update emp4 set phone_number = '198a' where employee_id = 198;

-- 컬럼 이름 변경
-- alter rename column
alter table emp4 rename column phone_number to p_number;
-- 속성 변경
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제
alter table emp4 drop column hire_date2;

desc emp4;

-- 테이블 삭제
drop table emp2;
drop table emp3;

-- 테이블 이름 변경
rename emp4 to emp44;

--
select * from departments;

drop table board;

-- primary eky : 중복불가, null값 불가
create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) not null,
age number(3) default 0,
gender varchar(6) check (gender in ('Male', 'Female')),
nicname varchar2(30),
email varchar(20),
bdate date default sysdate
);

drop table bmember;

insert into bmember (id, pw, name, nicname, age, gender, email, bdate)
values ('aaa', '1111', '홍길동', '길동스', 20, 'Male', 'aaa@aaa.com', sysdate);

insert into bmember (id, pw, name, nicname, gender, email)
values ('bbb', '2222', '유관순', '관순스', 'Female', 'bbb@bbb.com');

insert into bmember (id, pw, name, nicname, age, gender, email, bdate)
values ('ccc', '1111', '홍길동', '길동스', 20, 'Male', 'aaa@aaa.com', sysdate);

create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 values(
1, '홍', '01', '01'
);
insert into emp3 values(
2, '유', '02', '02'
);
insert into emp3 values(
3, '홍', '01', '01'
);

create table board(
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval, '제목1', '내용1', 'aaa', board_seq.currval, 0, 0, 0, sysdate,' '
);
insert into board values(
board_seq.nextval, '제목2', '내용2', 'bbb', board_seq.currval, 0, 0, 0, sysdate,' '
);
insert into board values(
board_seq.nextval, '제목3', '내용3', 'ddd', board_seq.currval, 0, 0, 0, sysdate,' '
);

commit;

select * from mem2;

--update mem2 set id = 'abc', pw='1111', name='안원영', email='ayg1044@naver.com' where id = 'Trineman'


create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) not null,
nicname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in ('Male','Female')),
email varchar2(20),
bdate date default sysdate
);

insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate
);


insert into bmember (id,pw,name,nicname,gender,email) values (
'bbb','2222','유관순','관순스','Female','bbb@bbb.com'
);

-- check - Male, Female 2가지 형태외에는 입력이 안됨.
-- male,MALE,malE 데이터 입력 불가
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'ccc','1111','이순신','순신스',20,'Male','ccc@ccc.com',sysdate
);

-- not null - null허용하지 않음. 빈공백은 가능함.
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'ddd',' ','강감찬','감찬스',20,'Male','ddd@ddd.com','2024/01/01'
);

-- primary key : 중복불가, null불가
insert into bmember (id,pw,name,nicname,age,gender,email,bdate) values (
'eee',' ','김구','구스',20,'Male','eee@eee.com','2024/02/21'
);

commit;

-- 5개만 (5개 * 5개 = 25개 )
select bno,btitle,bcontent,nicname,age,gender,pw,email,bgroup,bstep,bindent,bhit,bfile 
from board, bmember
where
board.id = bmember.id  -- member id:primary key, board.id : foreign key
;
select * from board;
select * from bmember;
-- 조인(join)
select employee_id,emp_name,email,salary,employees.department_id,department_name 
from employees,departments
where employees.department_id = departments.department_id
;

select department_id,department_name from departments
where department_id = 20;

















-----------------------------

insert into member select * from mem2;
select * from member;


create table board2
desc board;
-- 테이블 create할때, foreign key 생성
create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
bcontent clob,
constraint fk_board2_id foreign key(id) references bmember(id)
);
-- 닉네임 : id_fk, foreign key : id, bmember테이블의 primary key : id 등록
alter table board add constraint id_fk foreign key (id) references bmember(id);
-- foreign key 삭제
alter table board drop constraint id_fk;
select * from board;
select * from bmember;  -- aaa,bbb,ccc,ddd,eee
-- abc 글을 등록하면 , 등록이 안됨.
insert into board values(
 board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,''
);
-- [ foreign key 등록된 id 삭제 방법 ]
-- bmember 테이블 id, foreign key로 board,board2에 등록
-- foreign key : 외래키
-- 원본의 primary key데이터를 지우려면, 원칙으로는 foreign key의 데이터를 모두 삭제해야 삭제가 됨.
-- foreign key를 해제해야 삭제 가능
-- primary key : 기본키
delete bmember where id='aaa';
delete board where id='aaa';
select * from bmember;
select * from board;
alter table board drop constraint id_fk;
-- foreign key 로 등록이 되면, primary key를 삭제할때 foreign key에 데이터가 있으면 삭제가 안됨.
-- on delete cascade : primary key가 삭제가 되면, foreign key로 등록된 모든 글을 삭제시킴
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;
-- alter table board add constraint fk_board_id foreign key(id) references bmember (id) on update cascade;
-- check 구문
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female'))
);
-- check 가 지정되어 있는 컬럼에 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
-- salary 범위를 벗어나면 에러,
insert into emp01 values(
2,'유관순',20000,'Female'
);
-- Male,Female 이외 단어 입력시 에러
insert into emp01 values(
3,'이순신',20000,'male'
);
-- default : insert시 값이 입력이 되지 않을시,  문자 , 숫자, 날짜가 넣을수 있음
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female')),
edate date default sysdate
);
--
insert into emp02 (empno,salary,gender) values(
1,5000,'Male'
);
select * from emp02;
commit;
drop table board2;
drop table emp01;
drop table emp3;
drop table emp44;
drop table stu;
drop table chartable;
drop table chartable2;
drop table datetable;






create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date,
gender varchar2(6) check(gender in('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem(id, pw, name, age, birth, gender) values(
'aaa', '1111', '홍길동', '24', '2000/05/05', 'Male'
);
insert into mem(id, pw, name, age, birth, gender) values(
'bbb', '2222', '유관순', '24', '2000/05/05', 'Female'
);
commit;


select count(*), department_id from employees where department_id = 50 group by department_id;
-- employees 테이블의 부서번호와, 부서이름을 가져옴
select b.department_id, department_name
from departments a, employees b
where a.department_id = b.department_id;

select count(*) no, a.department_id dept, department_name deptname
from employees a, departments b
where a.department_id = b.department_id
group by a.department_id,department_name
;

select * from students;
delete students where name ='김유신' ;
commit;
desc students;
