-- Total Number of Customers
select count(customerid) as num_of_customers
from customers;

-- Total Number of Orders
select count(orderid) as num_of_orders
from orders;

-- Total Revenue
SELECT sum(totalamount) AS TotalRevenue
from orders;

--	Average Order Value
select avg(totalamount) as average_ordered_value 
from Orders;

-- Total Number of Products
select count(productid) as num_of_products
from products;

--⦁	Total Products Sold
select productid, sum(quantity) as totalsold
from OrderDetails
group by ProductID

--Most Expensive Product
select top 1 productid, max(UnitPrice) as mostexpensive
from OrderDetails
group by ProductID
order by mostexpensive desc

--Least Expensive Product
select top 1 productid, min(UnitPrice) as leastexpensive
from OrderDetails
group by ProductID
order by leastexpensive


--⦁	Number of Orders Per Customer
select customerid, count(orderid) as num_of_orders
from orders
group by CustomerID

--⦁	Total Stock Quantity
select sum(StockQuantity) as totalstock
from Products

--⦁	Products Out of Stock
Select ProductName from Products
Where StockQuantity= 0 ;


--⦁	Total Orders in ‘2024-04-12’
select count(orderid) as ordersinday
from Orders
where YEAR(orderdate) = 2024 and MONTH(OrderDate) =	04 and DAY(OrderDate) = 12 

--⦁	Most Recent Order
select top 1 orderid, max(orderdate) as mostrecent
from orders
group by OrderID
order by mostrecent desc

--Number of Orders by Month
select month(OrderDate) as months, count(orderid) as numberoforders
from orders
group by month(OrderDate)
order by months

--⦁	Find all products that cost less than $50 
select productid, Price
from Products
where price < 50
order by Price desc

-- Best Selling Product (by quantity)
select top 1 productid, max(quantity) as bestselling
from OrderDetails
group by ProductID

--Find all products that are out of stock:
Select ProductName from Products
Where StockQuantity= 0;

--	Number of Orders by Day of Week
select datename(weekday, OrderDate) as Dayy, count (orderid) as ordersinday
from orders
group by datename(weekday, OrderDate)
order by ordersinday;

------Average Order Value by Custome
----Select customerid, avg(totalamount) as averageamount
----from orders
----group by customerid
--order by averageamount

----Products with Price Above Average
--select productid, AVG(price) as average
--from products
--where price > average