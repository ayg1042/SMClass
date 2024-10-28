
-- 검색
--select * from employees;
--select * from customers;
--select * from products;

-- 테이블 생성
-- no, name, kor, eng, math, total, avg, rank
create table students (
no number(4),
name varchar2(20),
eng number(3),
kor number(3),
math number(3),
total number(3),
avg number(10),
rank number(4)
);
-- 테이블 삭제
--drop table students;

insert into students (no, name, kor, eng, math, total, avg, rank) values(
1,'홍길동', 100, 100, 99, 299, (299)/3, 1
);

insert into students (no, name, kor, eng, math, total, avg, rank) values(
2,'유관순', 100, 90, 99, 289, (289)/3, 1
);

select * from students;

-- 데이터를 저장함
commit;

-- 커밋 전으로 돌림
rollback;

select * from students;

select * from employees;

create table member(
id varchar2(20) primary key,
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);

-- insert into 테이블 values 입력값
-- update 테이블 set 변경 컬럼 = 변경 데이터 where 변경 컬럼 = 변경될 데이터
-- delete 테이블 where 컬럼=데이터
-- aaa, 111, 홍길동, 010-1111-1111
insert into member(id, pw, name, phone) values(
'aaa', '1111', '홍길동', '010-1111-1111'
);

insert into member(id, pw, name, phone) values(
'bbb', '1111', '유관순', '010-2222-2222'
);

commit;

insert into member(id, name) values(
'ccc', '이순신'
);

select id, phone from member;

select emp_name, salary from employees;

select * from member;

update member set name = '홍길자' where id = 'aaa';

delete member where id = 'ccc';
