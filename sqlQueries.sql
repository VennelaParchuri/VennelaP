SELECT phone from address
WHERE address='259 Ipoh Drive';

SELECT customer_id FROM payment 
WHERE amount>0.00 
ORDER BY payment_date ASC 
LIMIT 10

SELECT title from film
ORDER BY length ASC
LIMIT 5

SELECT COUNT(title) from film
WHERE length<=50

SELECT COUNT(*) FROM payment
WHERE amount>5.00

SELECT COUNT(*) FROM actor
WHERE first_name ILIKE '%P'; 

SELECT DISTINCT district FROM address;

SELECT COUNT(title) FROM film
WHERE rating = 'R' 
AND replacement_cost BETWEEN 5 AND 15

SELECT COUNT(title) FROM film
WHERE title ILIKE '%Truman%';

SELECT MIN(replacement_cost) FROM film;
SELECT MAX(replacement_cost) FROM film;
SELECT MIN(replacement_cost), MAX(replacement_cost)  FROM film;
SELECT round(AVG(replacement_cost),2) FROM film;
SELECT SUM(replacement_cost) FROM film;
SELECT SUM(replacement_cost), MIN(replacement_cost),
MAX(replacement_cost), COUNT(*),round(AVG(replacement_cost),2) FROM film;

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id ORDER BY customer_id

SELECT customer_id, COUNT(amount) FROM payment
GROUP BY customer_id ORDER BY COUNT(amount)

SELECT customer_id,staff_id, SUM(amount) FROM payment
GROUP BY staff_id,customer_id
ORDER BY customer_id;

SELECT DATE(payment_date), SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount)

SELECT staff_id, count(amount) FROM payment
GROUP BY staff_id 
ORDER BY count(amount) DESC

SELECT rating, ROUND(AVG(replacement_cost),3) FROM film
GROUP BY rating

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC LIMIT 5

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
HAVING SUM(amount)>100

SELECT store_id, COUNT(customer_id) FROM customer
GROUP BY store_id
HAVING COUNT(customer_id)>300

SELECT customer_id,COUNT(amount) FROM payment
GROUP BY customer_id
HAVING COUNT(amount)>=40

SELECT customer_id, SUM(amount) FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount)>=110

SELECT COUNT(title) FROM film
WHERE title ILIKE 'J%'

SELECT customer_id, first_name, last_name FROM customer 
WHERE first_name ILIKE 'E%' AND address_id < 500
ORDER BY customer_id DESC LIMIT 1

SELECT customer_id,first_name, last_name FROM customer 
WHERE customer_id = (SELECT MAX(customer_id) FROM customer
WHERE first_name ILIKE 'E%' AND address_id < 500)


SELECT payment_id,payment.customer_id,first_name 
FROM customer INNER JOIN payment
ON customer.customer_id = payment.customer_id

SELECT * FROM customer 
FULL OUTER JOIN payment
ON customer.customer_id=payment.customer_id
WHERE customer.customer_id IS NULL OR
payment.payment_id IS NULL

SELECT email FROM customer
INNER JOIN address ON customer.address_id = address.address_id
WHERE address.district = 'California'

SELECT title FROM film 
WHERE film_id IN (SELECT film_id FROM actor INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id WHERE actor.first_name='Nick' 
AND actor.last_name='Wahlberg')

SELECT title,first_name,last_name FROM actor INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film.film_id = film_actor.film_id
WHERE first_name='Nick' AND last_name = 'Wahlberg'

SHOW ALL
SHOW TIMEZONE
SELECT NOW()
SELECT TIMEOFDAY()
SELECT CURRENT_TIME
SELECT CURRENT_DATE


SELECT TO_CHAR(payment_date,'MONTH') FROM payment
SELECT TO_CHAR(payment_date,'DAY') FROM payment

SELECT COUNT(*) FROM payment 
WHERE EXTRACT(dow FROM payment_date) = 1