SELECT c.first_name, c.last_name, o.item, o.amount
  FROM customers c
  LEFT
  JOIN orders o 
    ON c.customer_id = o.customer_id // customer_id를 기준으로 LEFT_JOIN
 WHERE o.amount IS NOT NULL; // 주문하지 않은 사람의 정보
