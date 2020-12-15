-- window function :
analytic_function_name ( [ argument_list ] ) OVER over_clause

over_clause:
  { named_window | ( [ window_specification ] ) }

window_specification:
  [ named_window ]
  [ PARTITION BY partition_expression [, ...] ]
  [ ORDER BY expression [ { ASC | DESC }  ] [, ...] ]
  [ window_frame_clause ]

window_frame_clause:
  { rows_range } { frame_start | frame_between }

rows_range:
  { ROWS | RANGE }
---
AVG ( [ALL ] expression ) OVER ([ PARTITION BY expr_list ][ ORDER BY order_list   frame_clause ]) 
/*
avg nearby rows:
avg(weight) over (order by weight ROWS between 1 preceding and 1 following) as average_weight
*/
---
SUM ( [ALL ] expression ) OVER ([ PARTITION BY expr_list ][ ORDER BY order_list   frame_clause ]) 
/*
running totals :
sum(weight) over (order by weight DESC ROWS between unbounded preceding and current row) as running_total_weight
*/
---
COUNT ( * | [ ALL ] expression) OVER ([ PARTITION BY expr_list ][ ORDER BY order_list   frame_clause ]) 
/*
       SUM(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_total,
       COUNT(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_count,
       AVG(duration_seconds) OVER
         (PARTITION BY start_terminal) AS running_avg
*/
---
MAX ( [ ALL ] expression ) OVER ( [ PARTITION BY expr_list ] [ ORDER BY order_list frame_clause ] ) 

MIN ( [ ALL ] expression ) OVER ( [ PARTITION BY expr_list ] [ ORDER BY order_list frame_clause ] ) 
---
ROW_NUMBER () OVER ( [ PARTITION BY expr_list ] [ ORDER BY order_list ] ) 
/*
unique number : 
row_number() over (order by color,name) as unique_number
*/
---
RANK () OVER ( [ PARTITION BY expr_list ] [ ORDER BY order_list ] ) 
/*
order by weight : 
rank() over (order by weight desc) as ranking
*/
---
DENSE_RANK () OVER ( [ PARTITION BY expr_list ] [ ORDER BY order_list ] ) 
/*
sequentially ordering :
dense_rank() over (order by age DESC) as r
*/
---
FIRST_VALUE | LAST_VALUE ( expression [ IGNORE NULLS | RESPECT NULLS ] ) OVER ( [ PARTITION BY expr_list ] [ ORDER BY order_list frame_clause ] )
/*
split to quartiles:
ntile(4) over ( order by weight) as weight_quartile // split to groups of 4 by weight
first of each group : 
first_value(weight) over (partition by color order by weight) as weight_by_color
The cats have decided the correct weight is the same as the 4th lightest cat :(nth_value() allows us to select the an arbitrary position in a subgroup)
coalesce(nth_value(weight, 4) over (order by weight), 99.9)
*/
---
--It is useful for looking for strange step ups/downs in data

LEAD (value_expr [, offset ]) [ IGNORE NULLS | RESPECT NULLS ] OVER ( [ PARTITION BY window_partition ] ORDER BY window_ordering )
/*
compare to row overall weight: 
coalesce(weight - lag(weight, 1) over (order by weight), 0) as weight_to_lose
compare to row overall weight and split by breed: 
coalesce(weight - lag(weight, 1) over (partition by breed order by weight), 0) as weight_to_lose_by_breed
the next heaviest cat's weight or 'fattest cat' :
coalesce(cast(lead(weight, 1) over (partition by breed order by weight) as varchar), 'fattest cat') as next_heaviest
second lightest cats : 
nth_value(weight, 2) over ( partition by breed order by weight RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING ) 

*/
    
--FILTER & array_agg :
-- Filter is to be used with aggregate functions or window functions. It allows us to filter out values
--average weight of cats grouped by breed whose age is over 1
avg(weight) filter (where age > 1) average_old_weight
-- Array Agg allows us to select several entries into one. Think of it as compressing the values into an Array object
--3 rows, each row containing a color and a list of cat names :
array_agg(name) as names

--- time & date & string functions :
--date :
SELECT CURRENT_DATE() as the_date
EXTRACT(part FROM date_expression) // DAY , WEEK , MONTH , YEAR
DATE_ADD(date_expression, INTERVAL int64_expression date_part)
DATE_SUB(date_expression, INTERVAL int64_expression date_part)
DATE_DIFF(date_expression_a, date_expression_b, date_part)
--time :
SELECT CURRENT_TIME() as now;
EXTRACT(part FROM time_expression) // MILLISECOND , SECOND , MINUTE , HOUR
TIME_ADD(time_expression, INTERVAL int64_expression part)
TIME_SUB(time_expression, INTERVAL int64_expression part)
TIME_DIFF(time_expression_a, time_expression_b, part)
-- string :
CHAR_LENGTH(value)
CONCAT(value1[, ...])
ENDS_WITH(value1, value2)
STARTS_WITH(value1, value2)
LENGTH(value)
LOWER(value)
UPPER(value)
REGEXP_CONTAINS(value, regexp)
REGEXP_EXTRACT(value, regexp)
REGEXP_REPLACE(value, regexp, replacement)
REVERSE(value)
SUBSTR(value, position[, length])
TRIM(value1[, value2])


--- other :
 CAST(raw_events.event_timestamp AS DATE) = CAST(TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR) AS DATE)
 ---
 raw_events.hour_of_day = EXTRACT(HOUR FROM TIMESTAMP_SUB(CURRENT_TIMESTAMP(),INTERVAL 1 HOUR))
---
 AND event_name IN ("picked_answer")
---
AND NOT ENDS_WITH(raw_events.answer_id, "_next")
---
TIMESTAMP(FORMAT_TIMESTAMP('%Y-%m-%d %H:00:00', CAST(Raw_Events.event_timestamp AS TIMESTAMP))) AS timestamp,
---
    COALESCE(`data`.`interaction_id`,
      `inative`.`interaction_id`,
      `display`.`interaction_id`,
      'no_value') AS `interaction_id`,
---
   CAST(IFNULL(SUM(`video_income`),
        0.0) + IFNULL(SUM(`inative_income`),
        0.0) + IFNULL(SUM(`display_income`),
        0.0) AS FLOAT64) AS `estimated_income`,
---
    AND COALESCE(CAST(`data`.`timestamp` AS STRING),
      'no_value') = COALESCE(CAST(`inative`.`timestamp` AS STRING),
      'no_value')
---
      CASE
        WHEN `Raw_Events`.`platform` = "desktop" THEN "Desktop"
        WHEN `Raw_Events`.`platform` = "mobile_web" THEN "Mobile"
        WHEN `Raw_Events`.`platform` = "mobile_app" THEN "Mobile"
        ELSE "Other"
      END AS `platform`,
--- 
      IF (`Raw_Events`.`application` = 'unknown'
        OR `Raw_Events`.`application` IS NULL,
        'web & other apps',
        `Raw_Events`.`application`) AS application,
---
      SUM(IF( (`Raw_Events`.`mon_type` IN ('rtk', 'gpt')
            AND `Raw_Events`.`mon_provider` = 'co'
            AND `Raw_Events`.`Event_Name` = 'player_mon_impression' ),
          IFNULL(`Raw_Events`.`companion_custom_param_float`,
            0),
          0)) AS `companion_gross_income`,
---
      COUNTIF(`Raw_Events`.`mon_type` IN ('rtk', 'gpt')
        AND `Raw_Events`.`mon_provider` IN ('co')
        AND `Raw_Events`.`event_name` = 'player_mon_impression') AS `companion_impressions`,
---
    SUM(CASE
        WHEN `programmatic_billing_method` = "revenueShare" THEN `in_unit_gross_income` / 1000 * (programmatic_billing_value / 100.0)
        WHEN `programmatic_billing_method` = "flatRate" THEN 0
        ELSE `in_unit_gross_income` / 1000 * 0.5 END) AS `in_unit_income`,
---
  COUNTIF(Raw_Events.event_name = "interaction_loaded"
    AND (Raw_Events.feed_sequence = 0
      OR Raw_Events.feed_sequence IS NULL)) AS page_views,
---
  MAX(IF(`data`.`event_name` = 'picked_answer',
      `count_events`,
      NULL)) AS `picked_answer`,
---
  CONCAT('aggs-v4-', FORMAT_TIMESTAMP('%Y-%m-%d', CAST(`data`.`timestamp` AS TIMESTAMP))) AS `index`
---
  CAST(Raw_Events.event_timestamp AS DATE) >= CAST(TIMESTAMP_SUB(TIMESTAMP(FORMAT_TIMESTAMP('%Y-%m-%d %H:00:00', CURRENT_TIMESTAMP())), INTERVAL 5 HOUR) AS DATE)
  AND CAST(Raw_Events.event_timestamp AS DATE) <= CAST(TIMESTAMP(FORMAT_TIMESTAMP('%Y-%m-%d %H:00:00', CURRENT_TIMESTAMP())) AS DATE)
---
    TIMESTAMP_DIFF(MAX(event_timestamp), MIN(event_timestamp), SECOND) AS session_duration,
---

-- important queries : 
  --// Write a query to return the number of actors whose first name starts with 'A', 'B', 'C', or others :
WITH
  tmp AS (
  SELECT
    actor_id,
    (
      CASE
        WHEN STARTS_WITH(first_name, 'A') THEN 'a_acotrs'
        WHEN STARTS_WITH(first_name, 'B') THEN 'b_acotrs'
        WHEN STARTS_WITH(first_name, 'C') THEN 'c_acotrs'
      ELSE
      'other_actors'
    END
      )AS cat
  FROM
    actor
  GROUP BY
    1)
SELECT
  cat,
  COUNT(*) AS count
FROM
  tmp
GROUP BY
  1
  --// Write a query to return the number of good days and bad days in May 2020 based on number of daily rentals : 
   WITH
  tmp AS (
  SELECT
    DATE(rental_ts) AS date,
    COUNT(DISTINCT rental_id) AS total_daily_rental
  FROM
    rental
  WHERE
    EXTRACT(month
    FROM
      rental_ts ) = 5
    AND EXTRACT(year
    FROM
      rental_ts ) = 2020
  GROUP BY
    1 )
SELECT
  sum (CASE
      WHEN total_daily_rental > 100 THEN 1
  END
    ) AS good_day,
  SUM(CASE
      WHEN total_daily_rental <= 100 THEN 1
  END
    ) AS bad_day
FROM
  tmp
--// Write a query to return the first name and the last name of the actor who appeared in the most films :
SELECT
  first_name,
  last_name
FROM
  actor
JOIN (
  SELECT
    actor_id,
    COUNT(DISTINCT film_id) AS total_mov
  FROM
    film_actor
  GROUP BY
    1
  ORDER BY
    total_mov DESC
  LIMIT
    1 ) AS tmp
ON
  tmp.actor_id = actor.actor_id
--// Write a query to return the first and last name of the customer who spent the most on movie rentals in Feb 2020 : 
SELECT
  first_name,
  last_name
FROM
  customer
JOIN (
  SELECT
    customer_id,
    SUM(amount) AS total
  FROM
    payment
  WHERE
    EXTRACT(month
    FROM
      payment_ts ) = 2
    AND EXTRACT(year
    FROM
      payment_ts ) = 2020
  GROUP BY
    1
  ORDER BY
    2 DESC
  LIMIT
    1) AS tmp
ON
  tmp.customer_id = customer.customer_id
--//Write a query to return the average cost on movie rentals in May 2020 per transaction : 
SELECT
  AVG(amount) OVER (PARTITION BY EXTRACT(month FROM payment_ts ))
FROM
  payment
WHERE
  EXTRACT(month
  FROM
    payment_ts ) = 5
  AND EXTRACT(year
  FROM
    payment_ts ) = 2020
LIMIT
  1
--//Write a query to return the titles of the films with >= 10 actors :
SELECT
  title
FROM
  film
JOIN (
  SELECT
    film_id,
    COUNT(DISTINCT actor_id) AS total_act
  FROM
    film_actor
  GROUP BY
    1
  HAVING
    COUNT(DISTINCT actor_id) >=10 ) AS tmp
ON
  tmp.film_id = film.film_id
  --// Write a query to return the title of the second shortest film based on its duration/length : 
  WITH
  tmp AS (
  SELECT
    film_id,
    title,
    length,
    DENSE_RANK() OVER (ORDER BY length) AS rank
  FROM
    film )
SELECT
  title
FROM
  tmp
WHERE
  rank = 2
--// Write a query to return the total number of customers who didn't rent any movies in May 2020 : 
SELECT
  COUNT(DISTINCT customer.customer_id) AS count
FROM
  customer
WHERE
  customer_id NOT IN (
  SELECT
    customer_id
  FROM
    rental
  WHERE
    EXTRACT(month
    FROM
      rental_ts ) = 5
    AND EXTRACT(year
    FROM
      rental_ts ) = 2020)
-- // Any customers who made at least 10 movie rentals are happy customers, write a query to return the dates when the following customers became happy customers: customer_id in (1,2,3,4,5,6,7,8,9,10).
WITH
  tmp AS (
  SELECT
    customer_id,
    DATE(rental_ts) AS date,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY rental_ts) AS ROW
  FROM
    rental
  WHERE
    customer_id IN (1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10))
SELECT
  customer_id,
  date
FROM
  tmp
WHERE
  ROW = 10
-- // Return the city ids where we have the most and least number of customers (Append a column to indicate whether this city id has has the most customers or least customers with 'most' or 'least' category): 
WITH city_cust_cnt AS (
	SELECT     
	    A.city_id,
	    COUNT(*) cust_cnt,
	    ROW_NUMBER() OVER(ORDER BY COUNT(*) ASC) AS cust_asc_idx,
	    ROW_NUMBER() OVER(ORDER BY COUNT(*) DESC) AS cust_desc_idx
	FROM customer C
	INNER JOIN address A
	ON A.address_id = C.address_id
	GROUP BY A.city_id
)
SELECT 
    city_id,
    'least' AS city_cat
FROM city_cust_cnt
WHERE cust_asc_idx = 1
UNION
SELECT 
    city_id,
    'most' AS city_cat
FROM city_cust_cnt
WHERE cust_desc_idx = 1
;
--// Write a query to return the cumulative daily spend for the following customers: customer_id in (1, 2, 3).
WITH
  tmp AS (
  SELECT
    DATE(payment_ts) AS date,
    customer_id,
    SUM(amount) AS daily_spend
  FROM
    payment
  WHERE
    customer_id IN (1,
      2,
      3)
  GROUP BY
    1,
    2)
SELECT
  date,
  customer_id,
  daily_spend,
  SUM(daily_spend) OVER (PARTITION BY customer_id ORDER BY date) AS cum_spend
FROM
  tmp
-- // Write a query to return percentile distribution for the following movies by their total rental revenues in the entire movie catalog :
  SELECT  
    F.film_id,        
    SUM(P.amount) revenue,
    NTILE(100) OVER(ORDER BY SUM(P.amount)) AS percentile
  FROM payment P
  INNER JOIN rental R
  ON R.rental_id = P.rental_id
  INNER JOIN inventory I
  ON I.inventory_id = R.inventory_id  
  INNER JOIN film F
  ON F.film_id = I.film_id  
  GROUP BY F.film_id
-- // Write a query to return quartiles for the following movies by number of rentals among all movies :
WITH
  movie_rentals AS (
  SELECT
    F.film_id,
    COUNT(*) AS num_rentals,
    NTILE(4) OVER(ORDER BY COUNT(*)) AS quartile
  FROM
    rental R
  INNER JOIN
    inventory I
  ON
    I.inventory_id = R.inventory_id
  INNER JOIN
    film F
  ON
    F.film_id = I.film_id
  GROUP BY
    F.film_id )
SELECT
  *
FROM
  movie_rentals
WHERE
  film_id IN (1,
    10,
    11,
    20,
    21,
    30);
--// Write a query to return the first name and last name of actors who only appeared in movies :
SELECT M.first_name, M.last_name
FROM actor_movie M
LEFT JOIN actor_tv T
ON M.actor_id = T.actor_id
WHERE T.actor_id IS NULL;












