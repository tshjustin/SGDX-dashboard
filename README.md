# SGDX-dashboard

An exchange rate platform to query about different real time rates relative to SGD.


### Requirements 

#### Functional Requirements
Feature | Status | Comments | Response | 
--- | --- | --- | --- |
Query rates every hour  | ✅ | Need to consider DB space. How long are we storing the data for? Need to consider if the free DB that we are using can accomodate so much data | Monitoring 
Query rates every hour  | ✅ | Convert rates to SGD base  | Hard to convert to SGD base. For example if we are scraping USDMYR, and to convert to USDSGD, we need the MYRSGD exchange rate to caculate. But which MYRSGD rate to use? - Not possible to find a suitable rate. | All information from queried rates 

Visuals to see how rate changes per time, time = {day, {1,2...12} months, years}  | If rates are better compared to the previous week or something then we can highlight the rate green? And highlight the rate red vice-versa| Yes |
Allows for switch currency, SGD-> XXX, XXX-> SGD   |  | - | - |
Currency of other bases. Eg: MYR -> USD  |  | - |

#### Known Bugs 
1. Scheduler_status reads False despite it running 