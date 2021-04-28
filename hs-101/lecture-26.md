---
layout: page
title: Lecture 26
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

The _HSBC Purchasing Manager Index_ (PMI) measures the factory production based on the monthly responses of purchasing executives in around 500 manufacturing companies. A value over 50 means expansion and a value under 50 means contraction.

Now, should we use the WPI or the GDP deflator?    
The GDP deflator measures the prices of all goods produced, whereas the WPI measures only the prices of goods/services bought by consumers. In particular, an increase in the price of goods bought by firms/government shows up in the former but not the latter. Also, imported goods are not part of the GDP and do not show up in the GDP deflator. Lastly, the WPI assigns fixed weights to the prices of different goods whereas the GDP deflator assigns changing weights (a fixed basket of goods v. a changing basket of goods).

We use two indices in general, the _Laspeyres index_ (which works with a fixed basket of goods) and the _Paasche index_ (which works with a changing basket of goods).     
The Laspeyres price index is equal to

$$P = \frac{\sum p_t q_0}{\sum p_0 q_0} \times 100 $$

and the Paasche price index is equal to

$$P = \frac{\sum p_t q_t}{\sum p_0 q_t} \times 100, $$

where $$P$$ is the price index, $$p_t$$ is the current price, $$q_t$$ is the quantity used in the current period, $$p_0$$ is the price of the base period, and $$q_0$$ is the quantity used in the base period.

Laspeyres requires quantity data from only the base period, which allows a more meaningful comparison because changes in the index can be attributed to changes in price, but may overweight goods whose prices increase and does not reflect changes in buying patterns over time.    
Paasche reflects current buying habits because it uses current quantities, but it requires quantity data from the current year, which may be difficult to obtain. It is difficult to attribute changes in the index to price changes alone and tends to overweight goods whose prices have declined. The prices need to be recomputed each year.    
_Fischer's ideal index_ is equal to the geometric mean of these two indices.

When the prices of different goods are changing differently, the Laspeyres index tends to overstate the increase in cost of living. This is because it does not take into account that consumers can replace more expensive items with less expensive items.    
Conversely, the Paasche index tends to understate the increase in cost of living. While it takes the substitution effect into account, but does not take into account the decrease in the consumers' welfare resulting from this substitution (because we take a fixed basket of goods). This issue is known as _substitution bias_.

As new goods are introduced, consumers have more choice so the dollar is worth more.    
Some quality change may be unmeasured. If the quality of a good deteriorates while its price remains the same, the value of a dollar is dropping.

Therefore, it is difficult to compare WPI (Laspeyres) and the GDP deflator (Paasche), since they are both bad in their own ways. They follow similar trends.

We can compare today's prices with that of a different year's as

$$\text{Amount in today's dollars} = \text{Amount in other year's dollars} \times \frac{\text{Price level today}}{\text{Price level in other year}}.$$

When we perform the above correction, we are said to _index_ the amount for inflation. Approximately, when we put our money in a bank, the real interest rate is equal to the nominal interest rate minus the inflation rate.

_Unemployment rate_ is the statistic that measures the percentage of people who want to work but do not have jobs, reflecting the performance of the economy.

_Labor force_ is the sum of the employed and unemployed, and the _unemployment rate_ is the percentage of the labor force that is unemployed. The _labor force participation rate_ is the percentage of the adult population that is in the labor force.    
The average rate of unemployment around which the economy fluctuates is called the _natural rate of unemployment_. It is the rate of unemployment towards which the economy gravitates. It should be noted that natural does not mean desirable.

<!-- The _HSBC Purchasing Manager Index_ (PMI) measures the factory production based on the monthly responses of purchasing executives in around 500 manufacturing companies. A value over 50 means expansion and a value under 50 means contraction.

The GDP deflator measures the prices of all goods produced, whereas the WPI measures only ht prices of goods/services bought by consumers. In particular, an increase in the price of goods bought by firms/government shows up in the former but not the latter. Also, imported goods are not part of the GDP and do not show up in the GDP deflator. Lastly, the WPI assigns fixed weights to the prices of different goods whereas the GDP deflator assigns changing weights.

We use two indices in general, the _Laspeyres index_ (which works with a fixed basket of goods) and the _Paasche index_ (which works with a changing basket of goods)

The Laspeyres price index is equal to

$$P = \frac{\sum p_t q_0}{\sum p_0 q_0} \times 100 $$

and the Paasche price index is equal to

$$P = \frac{\sum p_t q_0}{\sum p_0 q_t} \times 100, $$
where $$P$$ is the price index, $$p_t$$ is the current price, $$q_t$$ is the quantity used in the current period, $$p_0$$ is the price of the base period, and $$q_0$$ is the quantity used in the base period.

Laspeyres requires quantity data from only the base period, which allows a more meaningful comparison, but may overweight goods whose prices increase and does not reflect changes in buying patterns over time.    
Paasche reflects current buying habits because it uses current quantities, but it requires quantity data from the current year. It is difficult to attribute changes in the index to price changes alone and tends to overweight goods whose prices have declined. The prices need to be recomputed each year.

The Fischer index is equal to the geometric mean of these two indices.

_Unemployment rate_ is the statistic that measures the percentage of people who want to work but do not have jobs, reflecting the performance of the economy.

_Labor force_ is the sum of the employed and unemployed, and the _unemployment rate_ is the perecentage of the labor force that is unemployed.    
The average rate of unemployment around which the economy fluctuates is called the _natural rate of unemployment_. It is the rate of unemployment towards which the economy gravitates. -->