---
layout: page
title: Lecture 25
---

<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML" async></script>

Inflation measures the general increase in level of prices. How do we measure cost of living/inflation?

We usually use the _Wholesale Price Index_ (WPI) or _Consumer Price Index_ (CPI) to measure the level of prices or inflation. It consolidates the prices of several goods and services into a single index that measures the overall level of prices. To do this reliably, some options are:
* Compute the average of all prices. This treats all goods and services equally, which need not be the case. For example, food should have a higher weightage than clothing.
* Take a the ratio of weighted averages of the prices while also considering a certain base year. For example, if we buy $$5$$ apples and $$2$$ oranges and take the base year as $$2011$$, we can calculate

$$\text{WPI} = \frac{5\times\text{current price of apples} + 2\times\text{current price of oranges}}{5\times\text{2011 price of apples} + 2\times\text{2011 price of oranges}}$$

On top of this, we assign a weight to each sector, taking into account its share in the market.    
The CPI can be calculated as:
1. Fix the basket and determine which prices are important to the average consumer.
2. Find the prices of each of the goods in the basket at each point in time.
3. Compute the basket's cost.
4. Choose a base year and compute the cost. Compute the index as the ratio of the basket costs between the two times.
<!-- 5. Compute the inflation rate as the percentage change in the CPI. -->

The inflation rate can be measured as the percentage change of CPI or WPI.

The WPI is used to provide estimates of inflation at the wholesale transaction level for the economy as a whole. This allows the government to check for inflation, in essential commodities in particular. It is used as a deflator for many sectors of the economy, including estimating GDP. It is also used for indexation in business contracts. Global investors track the WPI as a key macro indicator for their investment decisions.

We assign less weight to food items that are more volatile over time. As a result, core manufactured products have high weightage. According to purists, core inflation using only manufactured products carries significance as a more accurate predictor in the long term. This weeds out transitory components such as food and energy. Some alternate methods are the trimmed-mean method, which strips the most volatile items off the index each month.

In any index,
* What base year do we choose? The year should be somewhat normal/stable with respect to economic activities and their prices. We should have reliable data and the year should be as recent as possible. The base year for closely related economic indicators should not be wildly different.
* What choice of sample commodity do we choose? We should sample over different varieties of each commodity. Including all these varieties in the index is neither desirable nor feasible. We choose one or two popular varieties consumed by the index population. This popularity is based on family budget data, market intelligence, etc.
* Which price do we choose? We should choose that price which is charged to the consumer, including excise duty, sales tax, etc and excluding rebates.

In the field, price supervisors check the veracity of prices quoted by the price collectors by making spot visits. We further scrutinize in case
* the variation is more than 10% for a non-seasonal item.
* the variation is more than 50% for a seasonal item.
* the variation is more than 3 points in the item level index wrt the previous month.

_Producer Price Index_ (PPI) measures the price of a typical basket of goods bought by firms, not consumers.

<!-- How do we measure cost of living?

We usually use the _Wholesale Price Index_ (WPI) to measure the level of prices or inflation. It consolidates the prices of several goods and services into a single index that measures the overall level of prices. To do this reliably, some options are:
* Compute the average of all prices. This treats all goods and services equally, which need not be the case.
* Take a the ratio of weighted averages of the prices while also considering a certain base year. For example, if we buy $$5$$ apples and $$2$$ oranges and take the base year as $$2011$$, we can calculate

$$\text{WPI} = \frac{5\times\text{current price of apples} + 2\times\text{current price of oranges}}{5\times\text{2011 price of apples} + 2\times\text{2011 price of oranges}}$$

The WPI is used to provide estimates of inflation at the wholesale transaction level for the economy as a whole. This allows the government to check for inflation, in essential commodities in particular. It is used as a deflator for many sectors of the economy, including estimating GDP. It is also used for indexation in business contracts. Global investors track the WPI as a key macro indicator for their investment decisions.

CPI

_Producer Price Index_ (PPI) measures the price of a typical basket of goods bought by firms, not consumers. -->