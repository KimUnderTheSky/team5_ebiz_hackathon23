SELECT
    c.first_name,
    c.country,
    s.status
FROM
    Customers AS c
JOIN
    Orders AS o ON c.customer_id = o.customer_id
JOIN
    Shippings AS s ON c.customer_id = s.customer
WHERE
    o.item = 'Keyboard';

