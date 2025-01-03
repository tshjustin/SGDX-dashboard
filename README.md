﻿# SGDX-dashboard

An exchange rate platform to query about different real time rates relative to SGD.


### Requirements 

#### Functional Requirements
1. Query rates every hour  ✅
- OK! 
- Need to consider DB space. How long are we storing the data for? Need to consider if the free DB that we are using can accomodate so much data.

2. Convert rates to SGD base ✅
- Hard to convert to SGD base. For example if we are scraping USDMYR, and to convert to USDSGD, we need the MYRSGD exchange rate to caculate. But which MYRSGD rate to use? - Not possible to find a suitable rate.

3. Visuals to see how rate changes per time, time = {day, {1,2...12} months, years}
- Possible! If rates are better compared to the previous week or something then we can highlight the rate green? And highlight the rate red vice-versa

4. Allows for switch currency, SGD-> XXX, XXX-> SGD 

5. Currency of other bases. Eg: MYR -> USD 

#### Non Functional Requirements 
1. Scalability -> More currency from different sources 
- I think possible? Can incorporate multi-threading.

2. Peformance -> How fast should rates be updated upon query 
- After we have scraped the rates from the all websites, we can do a query immediately after to query the updated rates and display on the website. 

3. Monitoring / Alerts -> If significant drop is encountered 
- Possible! Perhaps alert through email / SMS when significant drop

### To-do
1. Verify Periodic Queries and check if updates to DB are successful ✅

2. Set up endpoints 