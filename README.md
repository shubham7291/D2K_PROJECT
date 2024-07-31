# D2K_PROJECT
### Customer Attrition Prediction

1) Create a new enviroment
```
conda create  -p venv python=3.12.2 -y
```
Insights

1) Attrition_Flag data is imbalanced with about 84% of records being that of existing customers and only 16% of the records representing attrited customers.
2) Customer_Age data is normally distributed with a few data points represented as outliers.
3) Gender data distribution is not quite but close to a uniform distribution with majority of the records representing female customers.
4) Dependent_count vary between 0 to 5 with majority of the customers having 2 or 3 dependents.
5) Most of the customers, about 31% of them, are graduates.
6) Number of customers who are married and number of customers who either are single or divorced, is almost the same.
7) Majority of about 35.2% of the customers fall under the low Income_Category, earning less than 40k anually.
8) 'Blue' category cards seems to be the most popular among the customers with about 93.2% of them using it.
9) Months_on_book data has a few outliers with most of the customers having been associated with the bank for about 3 years.
10) Majority of about 22.8% of the customers use 3 of the bank's products. The number of customers using 4, 5 and 6 products is approximately the same.
11) Only 0.3% of the customers were active throughout the year and about 7.3% of the customers were inactive for more than 3 months.
12) About 16% of the customers contacted the bank for more 3 times in the past year.
13) Credit_Limit data is sharply right skewed with many data points indicated as outliers. Very few customers have been given a credit limit of more than 10k.
14) Most of the customers have a timely payment record with 0 revolving balance.
15) Avg_Open_To_Buy data is right skewed with many outliers. Majority of the customers seem to utilize most of their credit limit.
16) Total_Amt_Chng_Q4_Q1 data appears to be normally distributed until to an extent but is then right skewed with many outliers. Expenditure in Q4 over that in Q1 has decreased for most of the customers.
17) Total_Trans_Amt data distribution is right skewed with records of more than 9k in the amount of transaction considered as outliers.
18 )Total_Trans_Ct data distribution has two peaks with few outliers.
19) Total_Ct_Chng_Q4_Q1 data appears to be normally distributed until to an extent but is then right skewed with many outliers. In case of most of the customers, the number of transactions made has decresed in Q4 over that in Q1.
20) Avg_Utilization_Ratio data is right skewed with most of the customers not utilizing their credit limit effectively.

Another Insights
1) Attrition_Flag appears to have a weak negative correlation with the Total_Trans_Ct indicating that to a small extent, decrease in the number of transactions can hint towards a greater likelihood of attrition.
2) Months_on_book has a strong positive correlation with the Customer_Age. Greater the age of a customer, longer is the customer's association with the bank.
3) Total_Relationship_Count has a weak negative correlation with the Total_Trans_Amt and Total_Amt_Chng_Q4_Q1 has a weak positive correlation with the Total_Ct_Chng_Q4_Q1.
4) Avg_Utilization_Ratio has a negative correlation with the attributes Credit_Limit and Avg_Open_To_Buy which is expected from its definition although the degree of correlation is not very high.
5) Avg_Utilization_Ratio also has a positive correlation with the Total_Revolving_Bal indicating that the customers who are on-time with their payments are more likely to effectively utilize their credit limit.
6) Credit utilization is higher in female customers than in male customers in the age group of 30 to 60.
7) There is a steep increase in the utilization by male customers over the age of 60 whereas a steep decrease in the utitlization by female customers under the age of 30.
8) Male customers of the age between 40 to 50 have a decreased credit utilization.
ajority of the customers are existing customers.
9) Attrition_Flag data is imbalanced with only 1627 Attrited customers against 8500 Existing customers.
10) Most of the customers are Female.
11) Customers are predominantly Graduates.
12) Majority of the customers are married.
13) Annual income of the majority of the customers is less than $40K.
14) There are 1112 records under Income_Category labelled as 'Unknown' which possibly be considered as missing entries.
15) There are 749 records under Martial Sattus labelled as 'Unknown' which possibly be considered as missing entries.
16) There are 1519 records under Education_Level labelled as 'Unknown' which possibly be considered as missing entries.
17) Most of the customers hold a 'Blue' category card and only 20 of the customers hold a 'Platinum' category card.
18) CLIENTNUM: Client number is a unique identifier and does not convey any information on customer behavior.
19) Customer_Age: The customers in the dataset are in the age group of 26 to 73 with about 75% of the customers less than or equal to 52 years old.
20) Dependent_count: Average number of dependents is 2 with a maximum of 5 dependents for a customer.
21) Months_on_book: The customers have been associated with the bank for atleast 13 months and about 25% of them for more than 40 months.
22) Total_Relationship_Count: The number of banking products held by the customers range between 1 and 6 with about 50% of the customers using atleast    4 products.
23) Months_Inactive_12_mon: On an average, in the past 12 months, customers have been inactive for about 2 months with 25% of the customers inactive      for more than 3 months and upto 6 months. It could provide us with information on whether high inactivity can lead to churning by the customers.
24) Contacts_Count_12_mon: On an average, customers have interacted with the bank only twice in the past 12 months and a maximum of 6 times.
25) Credit_Limit: The credit limit set for the customers averages at 8632 units with only 25% of the customers enjoying more than 11068 units of          credit limit upto a maximum of 34516 units.
26) Total_Revolving_Bal: The revolving balance carried by the customers range between 0 to 2517 averaging at 1163.
27) Avg_Open_To_Buy: Average amount of unused credit of the customers over the past 12 months has a large variation ranging between 3 to 34516 with a     mean of 7469.
28) Total_Amt_Chng_Q4_Q1: Expenditure of about 75% of the customers has decreased in Q4 compared to their expenditure in Q1. A maximum of 3.4 times       increase in expenditure observed in Q4 over Q1.
29) Total_Trans_Amt: The total transaction amount in the past 12 months varies over a wide range between 510 and 18484 with an average of 4404. About     75% of the customers have spent less than 4742.
30) Total_Trans_Ct: On an average, in the past 12 months, about 65 transactions are made by the customers ranging between as low as 10 and upto 139.
31) Total_Ct_Chng_Q4_Q1: In case of about 75% of the customers, the number of transactions have decreased in Q4 compared to Q1.
32) Avg_Utilization_Ratio: On an average, customers have utilized about 27.5% of their credit limit with about 25% of them utilizing atmost of 2.3%       and about 75% of them utilizing atmost of 50.3% of their credit limit.