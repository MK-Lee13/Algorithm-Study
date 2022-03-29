-- 코드를 입력하세요
set @hour = - 1;
SELECT (@hour := @hour + 1) AS HOUR,
  (
    SELECT COUNT(*)
    FROM ANIMAL_OUTS
    WHERE date_format(DATETIME, "%H") = @hour
  ) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;