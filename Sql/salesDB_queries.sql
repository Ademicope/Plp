use salesDb;

select checkNumber, paymentDate, amount
from payments;

select orderDate, requiredDate
from orders
where status like "In Process"
order by orderDate desc
;

select firstName, lastName, email
from employees
where jobTitle = "Sales Rep"
order by employeeNumber desc;

select * from offices;

select productName, quantityInStock
from products
order by buyPrice
limit 5;