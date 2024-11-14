select * from member;

update member set id='abc', pw='1111', name='안원영', email='ayg1044@naver.com'
where id='Tinker';

commit;

update member set pw='1111' where id='Towell';

select hire_date, round(hire_date, 'Month') from employees;
select hire_date, trunc(hire_date, 'month') from employees;

select add_months(trunc(sysdate, 'month'), 1) from dual;

-- vip 요즘제로 변경을 하면 다음달 1일 부터 혜택이 주어진다.
select sysdate, add_months(trunc(sysdate, 'month'), 1) from dual;

-- 입사일 기준 다음달부터 1일부터 혜택을 주겠다고 함.
-- 입사일 다음달 1일 출력하세요.
select emp_name, hire_date, add_months(trunc(hire_date, 'month'), 1) from employees;

-- 입사일 기준 1년 후 날짜를 출력하세요.
select emp_name, hire_date, add_months(hire_date, 12) from employees;

select hire_date, last_day(hire_date) from employees;

-- 입사일 기준 1년 후 날짜와, 1년후 마지막 그달의 날짜를 출력하세요.
select add_months(hire_date, 12), last_day(add_months(hire_date, 12)) from employees;

-- 입력일 기준 1년후 마지막 날짜가 8/31, 9/30, 10/31 인 학생들을 모두 출력하세요.
select sdate from students;
select sdate, add_months(sdate, 12) ydate, last_day(add_months(sdate, 12)) ldate from students
where
last_day(add_months(sdate, 12)) in ('24/08/31', '24/11/30', '25/08/31', '25/09/30', '25/10/31')
order by ydate
;

select sysdate from dual;
select extract(year from sysdate) from dual;
select extract(month from sysdate) from dual;
select extract(day from sysdate) from dual;
select extract(hour from sysdate) from dual;

select systimestamp from dual;
select extract(hour from systimestamp) from dual;

select sdate, extract(month from sdate) from students
where extract(month from sdate) in ('8','9','10');

select sysdate from dual;
-- substr(target, 시작지점, 개수)
select sysdate, substr(sysdate, 4, 2) from dual;

-- 날짜 형변환
select sysdate from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd') from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh24:mi:ss') from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh24:mi:ss day') from dual;
select sysdate, to_char(sysdate, 'yyyy-mm-dd hh24:mi:ss dy') from dual;
select sysdate, to_char(sysdate, 'yy-mm-dd hh24:mi:ss') from dual;

-- 날짜 -> 문자 to_char  날짜포맷
-- 문자 -> 날짜 to_date  날짜 사칙연산
-- 숫자 -> 문자 to_char  천단위, 숫자앞에 0을 표시, 통화 표시
-- 문자 -> 숫자 to_number  천단위 표시, 천단위 삭제해서 사칙연산

select kor from students where kor = 70;

-- 숫자타입 -> 문자타입 변경해서 포맷 천단위 표시
select salary * 1382.86 * 12 from employees;
-- 자릿수 채우기 9: 빈공백으로 채움. 0: 0으로 채움
-- L : 국가통화기호 표시, $ : $가 표기됨
select to_char(salary * 1382.86 * 12, '999,999,999,999') from employees;
select to_char(salary * 1382.86 * 12, 'L000,999,999,999') from employees;
select to_char(1, '000') from dual;

select to_char(123456, '000000000'), to_char(123456, '999,999,999')
from dual;

create table chartable(
no number(4),
kor number(10),
kor_char varchar2(10),
kor_mark varchar2(10)
);
create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);
drop table chartable;

insert into chartable values(
1, 10000, to_char(10000, '00000'), to_char(10000,'000,000')
);
insert into chartable values(
2, 10000, to_char(10000, '00000'), to_char(10000,'000,000')
);
insert into chartable2 values(
3, 3000000, 3000000, 3000000
);
-- 천단위 표시는 숫자형타입에 입력이 안된다.
-- 숫자형 타입은 숫자 앞에 0을 붙여도 안된다. 030 -> 30
-- 숫자형타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능


select '20241031', to_date('24-10-31') + 2 from dual;
select to_date(20231031) from dual;

-- number형 타입 -> 날짜형 타입
select sysdate - to_date(20231031) from dual;
-- 문자형 타입 -> 날짜형 타입
select sysdate - to_date('20231031') from dual;

-- 문자형 타입 -> 숫자형 타입
-- 천단위 문자형타입 -> 천단위 제외 숫자형 타입
select to_number('20,000', '999,999') from dual;

select * from chartable;

delete chartable;

insert into chartable values(
3, 30000,'0030000', '3,000,000'
);
commit;

select * from chartable;
-- 문자형 천단위 타입 -> 숫자형 타입 변환
select kor, to_number(kor_mark, '999,999,999') from chartable;
-- 숫자형타입 사칙연산 가능.
select kor + to_number(kor_mark, '999,999,999') from chartable;



select department_id from employees where department_id is null;

select commission_pct from employees where commission_pct is null;

-- 월급 * 커미션을 계산하시오.
select salary * nvl(commission_pct, 0) from employees;

-- null인 경우 : ceo 로 변경
select nvl(department_id, 0), nvl(to_char(department_id), 'ceo') from employees;

-- 그룹함수
-- sum : 합계, avg : 평균, count : 개수, min : 최소값, max : 최대값
select to_char(sum(salary), '999,999,999') from employees;
select avg(salary) from employees;
-- 반올림
select round(avg(salary), 2) from employees;
-- 버림
select trunc(avg(salary), 3) from employees;

-- 평균값 보다 월급이 높은 사원을 출력하세요.
select avg(salary) from employees;

select emp_name from employees where 6461.83 < salary;
-- 평균값을 select해서 입력함.
select count(salary) from employees where salary >= (select avg(salary) from employees);

-- emp_name : 단일함수, avg : 그룹함수
select emp_name, avg(salary) from employees;
-- department_id : 단일함수, max : 그룹함수
select department_id, max(salary) from employees;

-- students 테이블 모든 학생의 kor점수 합계, 평균, 최대값, 최소값을 구하세요.
select sum(kor), avg(kor), max(kor), min(kor) from students;

-- 부서번호가 50인 사원들의 월급의 합, 평균, 최대값, 최소값을 출력하세요.
select sum(salary), round(avg(salary), 2), max(salary), min(salary) from employees where department_id = 50;

select department_id, max(salary) from employees
group by department_id;

select emp_name, salary from employees;

select department_id, avg(salary) from employees
group by department_id;

-- 단일함수, 그룹함수, 함께 사용하면 ,group by 지정.
select department_id, round(avg(salary), 2) from employees group by department_id order by department_id;

-- 평균월급보다 높은 사람 수를 출력하세요.
select count(salary), min(salary), max(salary) from employees where salary >= (select avg(salary) from employees);

-- 수학함수 - abs : 절대값, ceil : 올림, floor : 버림, round : 반올림, trunc : 절사, mod : 나머지
-- power : 제곱, sqrt : 제곱근
select power(3,3) 제곱 from dual;

-- 문자, 숫자형 타입 -> 날짜형타입 변경가능
-- 숫자, 날짜형 타입 -> 문자형타입 변경가능
-- 문자형 타입 -> 숫자형타입 변경가능
-- 날짜형 타입 -> 숫자형타입 변경불가
select 20240101, to_date(20240101) from dual;

-- 날짜형 -> 문자형 변환 -> 숫자형 변환
select sysdate, to_number(to_char(sysdate, 'yyymmdd')) from dual;

-- 날짜형 -> 문자형 변환 -> 년, 월, 일, 특수문자 입력방법
select sysdate, to_char(sysdate, 'yyyy"년"mm"월"dd"일" day') from dual;
select sysdate, to_char(sysdate, 'yyyy/mm/dd day') from dual;

--------------------------------------------------------------------------------
-- 문자형 함수 (중요함)
select emp_name, email from employees;
-- 문자형타입을 합쳐서 + 기호를 사용하여 합치려고 하면 에러 발생한다.
select emp_name + email from employees;
-- ||, concat 함수를 사용하여야 한다.
-- 속도, 사용량 || 가 높다.
select emp_name || email from employees;
select concat(emp_name, email) from employees;
-- 숫자형 타입 : 사칙연산 계산해서 출력된다.
select kor + math from students;
-- lower() : 소문자 치환, upper() : 대문자 치환, initcap : 첫들자 대문자 치환
select * from member where lower(name)='bryan';
-- lpad : 자리수 왼쪽 채워줌
select 'john', lpad('john', 10, '#') from dual;
-- rpad : 자리수 오른쪽 채워줌
select 'john' , rpad('john', 10, '#') from dual;
-- trim : 빈공백 없애기, ltrim, rtrim
select length('  tt  '), length(trim('  tt  ')) from dual;
select ' a b c ', trim(' a b c ') from dual;
-- replace 치환
-- replace(target, 'target값', '변화값')
select ' a b c ', trim(' a b c '), replace(' a b c ', ' ', '') from dual;
-- substr() : 특정위치 자르기
-- substr(target, 시작점, 개수)
select 'abcdef', substr('abcdef', 0, 3) from dual;
--------------------------------------------------------------------------------
-- 입사일이 3, 8, 10월인 사원을 출력하세요.
select hire_date from employees where substr(hire_date, 4, 2) >= '07';

-- translate 취환 -- 한번에 여러게 바꾸기
select 'axyz', translate('axyzxbbcyaccx', 'xy', 'ab') from dual;
select 'axyz', translate('akxyzxbbkcyakcckx', 'xyk', 'ab') from dual;

-- length() : 문자열 길이
-- students 테이블 name 글자길이가 5자 이상인 학생만 출력하세요.
select count(*) from students where length(name) >= 10;

-- 사원의 월급의 합, 평균을 구하세요.
select sum(salary), round(avg(salary), 2) from employees;
-- 영어점수의 합, 평균, 최대값, 최소값을 구하세요.
select sum(eng), round(avg(eng), 2), max(eng), min(eng) from students;
-- students 테이블에서
-- 홍길동, 등록일 2023년 12월 02일 등록
desc students;
select to_char(sdate, '"등록일 "yyyy"년 " mm"월 " dd"일 "day') from students where name='홍길동';




