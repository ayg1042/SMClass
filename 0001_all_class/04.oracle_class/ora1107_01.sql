select * from students;

-- 평균 80점 이상, 국어 90점 이상인 학생들을 출력하세요.
select * from students
where avg >= 80 and kor >= 90;

-- 평균 60점이상 또는 총점 100점이상
select * from students
where avg >= 60 or total >= 100;

select * from students
order by kor desc, eng desc;