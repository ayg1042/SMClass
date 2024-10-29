--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;

-- create 테이블 생성
-- alter 테이블 수정
-- drop 테이블 삭제

create table member(
no number(4),
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20),
mdate date
);

-- insert, select, update, delete
-- 데이터 입력
insert into member values(
1, 'aaa', '1111', '홍길동', '010-1111-1111', '2024-10-29'
);

-- 데이터 수정
update member set name='홍길자' where name='홍길동';

-- 데이터 검색
select * from member;


-- 테이블 생성
create table students(
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);


-- 테이블 복사
create table emp2 as select * from employees;

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;

-- 테이블이 존재 할 경우 데이터만 복사
-- 테이블 구조 복사
create table member2 as select * from member where 1=2;


-- 테이블이 존재 할 경우 데이터만 복사
insert into member2 select * from member;


-- 컬럼 데이터 타입, 길이 변경
desc member;
alter table member modify no number(10);
update member set no='';
alter table member modify no varchar2(10);
-- alter변경, 컬럼의 이름 변경
alter table member rename column no to memberNo;

-- employees 테이블에서 사원번호, 사원 이름, 입사일 출력하세요. hire_date
desc employees;
select employee_id, emp_name, hire_date from employees;

drop table member;

create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
select * from member;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

--drop table students;

commit;

select kor, eng, (kor + eng) from students;
select kor, eng, (kor - eng) from students;


-- concat 명령어, ||
select concat(employee_id, emp_name) from employees;
select employee_id || emp_name from employees;

-- 달러 환산
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary * 1384, '999,999,999') from employees;

select emp_name, salary, salary * 1384 from employees;

create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values(1, '홍길동', 100);
insert into stu values(2, '유관순', 99);

commit;

insert into stu values(3, '', 0);
insert into stu values(4,null,null);
select * from stu;
commit;

-- null 값 찾는 방법
select * from stu where name is null;
-- null이 아닌것 출력 : is not null
select commission_pct from employees where commission_pct is not null;

-- 년봉계산
select salary, salary*12 from employees;
select salary, salary*12, salary*12*1384 from employees;

-- 커미션이 없는 사원은 null값이 있는데, null +,-,*,/ null값으로 변경
select salary, salary*12, salary*12+(salary*12)*commission_pct*0.01 from employees;
select salary, salary*12, salary*12+(salary*12)*nvl(commission_pct, 0)*0.01 from employees;
-- as 별칭, "" 특수문자, 사이공간까지 컬럼명으로 사용가능
select salary, salary*12 as 년봉, salary*12+(salary*12)*commission_pct*0.01 from employees;
select salary, salary*12 as "년 봉", salary*12+(salary*12)*commission_pct*0.01 from employees;

-- nvl() 함수 -- null이면 0으로 변경
select * from stu;
select no, name, kor, kor + 100 from stu;
select no, name, kor, nvl(kor, 0) + 100 from stu;

-- 번호, 이름, 국어, 영어, 수학, 합계
-- 입력일 컬럼명 별칭을 사용해서 출력하세요.
select no as 번호, name as 이름, kor as 국어, eng as 영어, math as 수학, total as 합계 from students;

-- 사원번호, 이름, 이메일을 합쳐서 출력하시오.
desc employees;
select employee_id || emp_name || email from employees;
select concat(concat(employee_id, emp_name), email) from employees;
select employee_id || ' is a ' || email from employees;

-- 중복제거 distinct
select DEPARTMENT_ID from employees;
select distinct DEPARTMENT_ID from employees;

-- 정렬 order by - 순차정렬 asc(생략가능), 역순정렬 desc
select distinct DEPARTMENT_ID from employees order by department_id desc;
select distinct DEPARTMENT_ID from employees order by department_id;

-- job_id 중복제거 출력하세요.
select distinct job_id from employees;

-- 문자열 자르기 substr(0, 2)
select substr(job_id, 0, 2) from employees;

-- 4번째 컬럼데이터를 가져와서 중복을 제거 함.
select distinct substr(job_id, 4) from employees;

-- where : 조건비교연산자
select * from employees;

select * from employees where manager_id = 124;
select * from employees where job_id = 'SH_CLERK';

select * from students;
-- students 합계 250이상 출력하세요.
select * from students where total >= 250;

-- 합계가 250, kor 90점 이상 출력하세요.
select * from students where total >= 250 and kor >= 90;

-- 영어 70이상, 90이하 출력하세요.
select * from students where eng >= 70 and eng <= 90;

-- employees에서 월급이 5000이상 8000이하 검색하세요.
select * from employees where salary >= 5000 and salary <= 8000;

-- 5000이 아닌것을 출력하세요.
select * from employees where salary != 5000;

-- 부서(department_id) = 50, 50번이 아닌것 출력하세요.
select count(*) from employees where department_id = 50; -- 45개
select count(*) from employees where department_id != 50; -- 61개

select count(*) from employees where department_id is null; -- 1개
select count(employee_id) from employees;
select count(department_id) from employees;

-- 급여 4000이하 사원번호, 사원명, 급여 컬럼만 출력하세요.
desc employees;
select employee_id as 사원번호, emp_name as 사원명, salary as 급여 from employees where salary <= 4000;

-- 숫자, 날짜 비교연산자 가능
select * from employees where hire_date >= '2002/01/01';

-- 1999/12/31 이전에 입사한 사람을 출력하세요.
select * from employees where hire_date <= '1999/12/31';

-- 2001/0101 부터 2004/12/31 까지 출력하세요.
select * from employees where hire_date >= '2001/01/01' and hire_date <= '2004-12-31';

-- 논리연산자 and, or, not
select count(*) from students where kor >= 90 or eng >= 90;
select count(*) from students where kor >= 90 and eng >= 90;
select count(*) from students where not kor >= 90;

-- 부서번호 - 10, department_id, job - man
select * from employees where DEPARTMENT_ID = 80 and substr(JOB_ID, 4) = 'MAN';
select * from employees where DEPARTMENT_ID = 80 and JOB_ID = 'SA_MAN';

select commission_pct from employees where commission_pct is not null;

-- 커미션이 0.2, 0.3, 0.5 인 경우만 출력하세요.
select * from employees where commission_pct is not null and commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;

-- 사원번호 110, 120, 130 출력하세요.
select * from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;
select * from employees where employee_id in (110, 120, 130);

-- 150 ~ 170
select * from employees where employee_id >= 150 and employee_id <= 170;

-- between - and : <= 포함이 되어 있는 경우 해당
select * from employees where employee_id between 150 and 170;
--date in, between
select * from employees where hire_date in ('2004/02/17','2002/06/07');
select * from employees where hire_date between '2004/02/17' and '2004/12/31';

-- job man 출력하시오.
select * from employees where substr(job_id, 4) = 'MAN' ;
-- like 연산자 : 포함되어 있는 글자.
select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';

-- emp_name에 a 가 들어가 있는 이름을 출력하세요.
select * from employees where emp_name like '%a%';

-- emp_name에 두번째 자리에 t가 들어가 있는 이름을 출력하세요.
select * from employees where emp_name like '__t%';

-- emp_name에 4번째 자리에 v가 들어가 있는 이름을 출력하세요.
select * from employees where emp_name like '___v%';

-- emp_name에 뒤에서 2번째 자리에 l이 들어가 있는 이름을 출력하세요.
select * from employees where emp_name like '%l_';

-- emp_name에 첫번째 대문자 d가 들어가 있는 이름을 출력하세요.
select * from employees where emp_name like 'D%';

desc employees;








