-- dual 가상 테이블
select sysdate from dual;

-- employees 테이블 hire_date 컬럼
select hire_date, hire_date - 1 from employees;
-- 날짜는 -, + 가능 (일수가 변경이 된다.)

-- 날짜 범위계산, 정렬 order by - asc(순차), desc(역순)
select * from employees where hire_date >= '02-01-01' and hire_date <= '04-12-31' order by hire_date desc;

-- like 중요함
select * from employees where emp_name like '%a%';

-- 정렬
-- desc - Null이 제일 위로, asc - Numll 제일 아래로
select department_id from employees order by department_id desc;
select department_id from employees order by department_id asc;

-- 월급 salary 역순정렬
select emp_name, salary from employees order by salary desc;

-- students 테이블에서 total 역순정렬
select no, name, total from students order by total desc;
select name, kor, eng, math, total from students order by kor desc, eng desc, math desc;

-- hire_date 기준, 순차정렬
select emp_name, hire_date from employees order by hire_date desc;

-- 입사일이 빠른 순으로 정렬하는데, 이름은 역순으로 정렬하세요.
select emp_name, hire_date from employees order by hire_date asc, emp_name desc;

-- abs 절대값
select -10, abs(-10) as abs from dual;

select kor, kor - eng, abs(kor - eng) abs from students order by abs desc; 

-- floor 소수점 이하 버림
select 3.141592, floor(3.141952) from dual;

-- round 반올림, 자리수 범위 지정
select 34.5678, round(34.5678) from dual;
select 34.5678, round(34.5678, 2) from dual;
-- 소수점 자리에서 앞쪽으로 한칸 위치 반올림
select 34.5678, round(35.5678, -1) from dual;

-- trunc : 버림, 자리수 지정
select 34.5678, trunc(34.5678, 2) from dual;
select 34.5678, trunc(34.5678, -1) from dual;

-- seil 소수점 이하 올림
select 3.141592, ceil(3.141592) from dual;

-- mod : 나머지
select 27/2 from dual;
select mod(27,2) from dual;
select 30/3, mod(31, 3) from dual;

-- 사원번호가 홀수인 사원을 출력하세요.
select * from employees where mod(employee_id, 2) = 1 order by employee_id asc;

-- 최종연봉 : 월급 * 12 + (월급 * 12) * 커미션 , 소수점 2자리에서 반올림, 첫째자리로 만드세요.
select emp_name, round(salary * 12 + (salary * 12) * nvl(commission_pct, 0) * 1381.86, 2)  from employees;

select * from students;

-- 시퀀스 : 자동으로 번호부여
-- 시퀀스 생성 방법
create sequence stu_seq
start with 1 -- 시작번호
increment by 1 -- 증가번호
minvalue 1 -- 최소번호
maxvalue 9999 -- 최대번호
nocycle
nocache;

-- 시퀀스.currval 현재번호
select stu_seq.currval from dual;

-- 시퀀스.nextval 다음번호
select stu_seq.nextval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000), -- 최대 4000, 한글 한개에 3byte
id varchar2(20),
bhit number(10),
bdate date
);

insert into board values(
1, '제목입니다.', '내용입니다.', 'aaa', 1, sysdate
);

insert into board values(
stu_seq.nextval, '2제목입니다.', '2내용입니다.', 'bbb', 1, sysdate
);

commit;
select * from board;


select * from board;

create sequence board_seq
start with 14 -- 시작번호
increment by 1 -- 증감번호
minvalue 1 -- 최소값
maxvalue 9999 -- 최대값
nocycle -- 1 ~ 9999 이상이 되면, 다시 1로 돌아가는 것 넘으면 에러남
nocache -- 메모리에 시퀀스값 미리할당
;

desc board

insert into board values(
board_seq.nextval, '제목14', '내용14', 'aaa', 1, sysdate
);
update board set btitle='제목을 다시 변경' where bno='14';

drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob, -- clob 대용량 글자타입
id varchar2(20),
bgroup number(4), -- 답변달기 그룹핑
bstep number(4), -- 답변달기 경우 순서정의
bindent number(4), -- 답변달기 드려쓰기
bhit number(10), -- 조회수
bdate date -- 등록일
);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval, '제목1', '내용1', 'aaa',board_seq.currval, 0, 0, 1, sysdate
);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100번까지 있음
-- 101, 홍길순, 99, 99, 90, total, avg, rnak, date

desc students;

create sequence students_seq
start with 101
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache
;

select students_seq.currval from dual;

insert into students values(
students_seq.nextval, '홍길순', 99, 99, 90, (99+99+90), (99+99+90)/3, 0, sysdate
);

select no, name, kor, eng, math, total, round(avg, 2), rank, sdate from students order by no;
delete students where name='홍길순';
commit;

select dept_seq.nextval from dual;

-- s_seq
-- 시작 1, 증가 1, 최대값 99999
create sequence s_seq
start with 1
increment by 1
maxvalue 99999
minvalue 1
nocycle
nocache
;

select s_seq.nextval from dual;



-- 시퀀스 생성, nextval : 다음 시퀀스번호 생성, currval: 현재시퀀스 번호 보여줌
select emp_seq.nextval from dual;




-- 타입
-- 문자형, 숫자형, 날짜형
-- char, varchar2, nchar, nvarchar2, 대용량 타입 : long, clob
-- char, varchar2 : 한글문자 입력시 3byte 사용.
-- varchar2(6) : 한글 2글자
-- nvarchar2(5) : 한글 5자리까지 입력가능 - 2byte
-- number
-- date - 초단위 까지 입력, timestamp - 밀리세컨드 까지 입력

select '홍길동' from dual;
-- length 문자길이
select length('홍길동') from dual;

-- 이름의 길이로 역순정렬
select name, length(name) n from students order by n desc;
-- lengthb : byte 크기
select lengthb('홍길동') from dual;

select * from students;
-- 합계가 200점 이상이면서, 번호 10이상, 50이하, 이름 2번째 자리에 E가 들이었는 학생출력하세요.
select * from students where total >= 200 and no >= 10 and no <= 50 and name like '_e%';

select * from students
where total >= 200;

-- 2중 쿼리문
select * from (
select * from students
where total >= 200
) where name like '_e%' and no >= 30;




rollback;

select * from students;

select no, name, total, rank from students;

-- rank() over(기준점) 입력
-- no는 중복이 없음, 유일키, 기본키, 프라이머리 키(primary key)
select no, rank() over(order by total desc) ranks from students;
select no, name, total, rank from students
order by total desc;
select ranks from (select no, rank() over(order by total desc) ranks from students);

update students set rank = (select ranks from (select no, rank() over(order by total desc) ranks from students))
where no = (select no from (select no, rank() over(order by total desc) ranks from students));

update students a
set rank = (
select ranks from (
select no, rank() over(order by total desc) ranks from students
) b
where a.no = b.no
);

select * from students order by rank;
rollback;
select no, rank() over(order by total desc) as ranks from students;

update students set rank = 1 where no = 64;
update students set rank = 1 where no = 96;
update students set rank = 3 where no = 49;
update students set rank = 4 where no = 14;
update students set rank = 5 where no = 72;

select * from students order by rank desc;

-- 사원번호가 높은순으로 등수를 생성하세요.
-- 사원번호, 사원명, 등수
select employee_id, emp_name, rank() over(order by employee_id desc) as rank
from employees;

-- emp2 테이블 복사, employees 테이블
drop table emp2;
create table emp2 as select * from employees;

-- 테이블 컬럼 추가
alter table emp2 add rank number(4);
desc emp2

update emp2 e set rank = (
select ranks from (select employee_id, rank() over(order by employee_id desc) ranks from employees) e2
where e.employee_id = e2.employee_id
);


-- 컬럼의 순서 변경
-- modify 컬럼 invisible; 컬럼 숨김
desc emp2;
alter table emp2 modify email invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify COMMISSION_PCT invisible;
alter table emp2 modify RETIRE_DATE invisible;
alter table emp2 modify DEPARTMENT_ID invisible;
alter table emp2 modify JOB_ID invisible;
alter table emp2 modify CREATE_DATE invisible;
alter table emp2 modify UPDATE_DATE invisible;

select * from emp2;

-- 숨긴 컬럼 다시 나타내기
-- modify 컬럼 visible;
alter table emp2 modify email visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify COMMISSION_PCT visible;
alter table emp2 modify RETIRE_DATE visible;
alter table emp2 modify DEPARTMENT_ID visible;
alter table emp2 modify JOB_ID visible;
alter table emp2 modify CREATE_DATE visible;
alter table emp2 modify UPDATE_DATE visible;

alter table emp2 modify rank invisible;
alter table emp2 modify rank visible;

select * from emp2;

-- 컬럼 삭제
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column hire_date;
alter table emp2 drop column salary;
alter table emp2 drop column commission_pct;
alter table emp2 drop column retire_date;
alter table emp2 drop column create_date;
alter table emp2 drop column update_date;
desc emp2;

select * from departments;
desc departments;
alter table emp2 add department_name varchar2(80);

-- 부서명이 없음
select * from emp2;
-- 부서명은 departments
select * from departments;

select department_id, department_name from emp2;
select department_id, department_name from departments;

update emp2 e
set department_name = 
(
select d_name from(select department_name d_name, department_id from departments) e2
where e.department_id = e2.department_id
);
select department_id, department_name from emp2;


drop table stu;

-- 테이블 복사
create table stu as select * from students;

desc stu;
alter table stu drop column total;
alter table stu drop column avg;

desc stu;
alter table stu add total number(3);
alter table stu add avg number;

alter table stu modify rank invisible;
alter table stu modify sdate invisible;
alter table stu modify rank visible;
alter table stu modify sdate visible;
desc stu;
select * from stu;
update stu set total = kor + eng + math;
update stu set avg = total/3;

update stu s
set rank = (
select ranks from (select no, rank() over(order by total desc) ranks from stu) s2
where s.no = s2.no
)
;
select no, name, total, rank from stu order by rank;

commit;

---- 날짜 함수
-- 현재날짜 : sysdate
select sysdate from dual;
select sysdate - 1 from dual;
select sysdate + 30 from dual;

create table datetable(
no number(4),
predate date,
today date,
nextdate date
);

-- 회원가입 1달치, 6개월, 1년
insert into datetable values(
1, sysdate - 30, sysdate, sysdate + 180
);
select today 가입일, nextdate 만기일 from datetable;

select * from member2;

select id, name, mdate, sysdate-mdate from member2
where sysdate >= mdate + 180;

-- 입사일 현재날짜와 입사일 몇일 지났는지 출력하세요.
-- employees, hire_date
select hire_date, round(sysdate - hire_date) from employees;
-- 15일 이상이면 1달을 올림
select hire_date, round(hire_date, 'month') from employees;

-- 일의 숫자를 1로 초기화
select hire_date, trunc(hire_date, 'month') from employees;

-- 입사일 현재일 기준의 달수
select hire_date, sysdate, months_between(sysdate, hire_date) from employees;
select hire_date, sysdate, round(months_between(sysdate, hire_date)) 달수, round(sysdate - hire_date) 일수 from employees;


-- add_months 개월수 추가
select hire_date, add_months(hire_date, 3) from employees;

-- next_day : 다음주 수요일 날짜를 알려준다.
select sysdate, next_day(sysdate, '수요일') from dual;
select sysdate, next_day(sysdate, '토요일') from dual;

-- lsat_date : 그달의 마지막 날짜를 알려줌
select sysdate, last_day(sysdate) from dual;

-- 형변환 함수
select sysdate from dual;
select to_char(sysdate, 'yy-mm-dd hh24:mi:ss') from dual;
select to_char(hire_date, 'yyyy-mm-dd') from employees;
select to_char(to_day('24-01-01'), 'yyyy-mm-dd') from dual;

select * from member2 where id='aaa' and pw='1111';

select * from member2;

update member set id = 'abc', pw='1111', name='안원영', email='ayg1044@naver.com'
where id = 'Trineman';

select * from member where id='eee';










