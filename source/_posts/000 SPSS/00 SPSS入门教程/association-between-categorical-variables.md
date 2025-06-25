---
title: SPSS：类别变量关联分析教程
date: 2025-06-21 18:34:29
permalink: /2025/06/21/association-between-categorical-variables/
---

[ ![SPSS tutorials website header logo](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/wp-content-themes-spss-tutorials-11-img-spss-tutorials-logo-44.png.png) SPSS TUTORIALS ](..//) [](#) [](#) [](https://www.facebook.com/stats.made.simple/ "Visit Our Facebook Company Page") [](https://www.linkedin.com/company/statistics-made-simple/ "Visit Our LinkedIn Company Page") [VIDEO COURSE](#) [BASICS](../basics/) [ANOVA](../anova/) [REGRESSION](../regression/) [FACTOR](../spss-factor-analysis-tutorials/)

### Beginners[](#)

  * [Basics](../basics/)
  * [Data Preparation](../data-preparation/)



### Statistical Tests - Beginners[](#)

  * [ANOVA](../anova/)
  * [Regression](../regression/)
  * [Correlation](../correlation/)
  * [T-Tests](../t-test/)
  * [Chi-Square Tests](../chi-square-test/)



### Statistical Tests - Intermediate[](#)

  * [Factor Analysis](../spss-factor-analysis-tutorials/)
  * [Nonparametric Tests](../nonparametric-tests/)



### Data Analysis[](#)

  * [SPSS Data Analysis](../spss-data-analysis/)
  * [Charts in SPSS](../charts/)
  * [Tables in SPSS](../tables/)



### Editing Data[](#)

  * [SPSS String Variables](../string-variables/)
  * [SPSS Date & Time Variables](../date-variables/)
  * [SPSS Dictionary Tutorial](../dictionary-tutorial/)



### Python[](#)

  * [SPSS Python Basics](../spss-python-basics/)



### Other[](#)

  * [SPSS A-Z](../spss-glossary/)
  * [Statistics A-Z](../statistics-glossary/)
  * [SPSS Tools](../tools/)
  * [SPSS Blog](../blog/)



# Association between Categorical Variables

By Ruben Geert van den Berg under [SPSS Data Analysis](../spss-data-analysis/)

This tutorial walks through running nice tables and charts for investigating the association between categorical or [dichotomous](../what-is-a-dichotomous-variable/) variables. If statistical assumptions are met, these may be followed up by a [chi-square test](../chi-square-independence-test/). As an example, we'll see whether sector_2010 and sector_2011 in [freelancers.sav](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/downloads-freelancers.sav.sav) are associated in any way.

![SPSS Categorical Variables in Data View](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/cc26a0224b8844437336.png)

## SPSS Quick Data Check

Before doing anything else, let's first just take a quick look at both variables separately. In the [syntax](..///spss-syntax/ ) below, we first ensure we'll see both values and value labels in our output tables (step 1). Next, we run a basic [FREQUENCIES](../spss-frequencies-command/) command.

***1. Set both values and value labels for output tables.** set tnumbers both.***2. Run frequencies.** frequencies sector_2010 sector_2011.

![SPSS FREQUENCIES Output](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/ca3e471332c58d2198d5.png)

## RECODE System Missing Values

Both variables contain values from 1 through 5 plus [system missing values](../spss-missing-values-tutorial/). Since both variables are nominal, we may include these system missings as just another category. This keeps the N nice and constant over analyses and results in cleaner tables.*For nicer tables, you may remove “Valid” with a Python script and apply styling with an SPSS table template (.stt file). The syntax below shows how to do so with [RECODE](..///spss-recode-command/ ).

***1. Recode system missing into value that's not present in variables yet (here: 6).** recode sector_2010 sector_2011 (sysmis = 6).***2. Explain what formerly missing value means.** add value labels sector_2010 sector_2011 6 '(Unknown)'.***3. Show only value labels in output.** set tnumbers labels.***4. Run clean frequency tables.** frequencies sector_2010 sector_2011.

![SPSS FREQUENCIES Output Clean](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/b05dceac9a7f24a2ef09.png)

## SPSS CROSSTABS for Both Variables

Thus far, we only had a look at both variables separately. In order to see how they're associated, we'll inspect their contingency table obtained from [CROSSTABS](../spss-crosstabs-command/). Displaying column percentages without frequencies is our preferred option here.

***Run contingency table with (only) column percentages.** crosstabs sector_2011 by sector_2010/cells column.

![SPSS CROSSTABS Output](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/c800a22ecf2f9f48ff99.png)

**Conclusion** : the variables are strongly related.*Again, note that we're only describing the data at hand. We're not making any attempt to generalize these results to any larger population. Roughly, most people who worked in a sector in 2010 stayed in the same sector in 2011. For example, 60% of respondents who worked in industry in 2010 stayed in industry. Another 20% moved to finance and the final 20% moved to “other”.

## SPSS Clustered Bar Chart Creation

We'll now visualize the contents of the previous table. An option here is a split bar chart but we'll go for a clustered bar chart instead. The screenshots below walk you through the process.

![SPSS Create Clustered Bar Chart](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/e9a102c5c015c29ca59e.png) ![SPSS Create Clustered Bar Chart 2](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/6a7ab8767afdf15fcfda.png)

## SPSS Clustered Bar Chart Syntax

***Run clustered bar chart for sector_2011 by sector_2010.** GRAPH /BAR(GROUPED)=COUNT BY sector_2011 BY sector_2010 /TITLE='Sector in 2010 by sector in 2011 (N = 40)'.

![SPSS Clustered Bar Chart](2025/06/21/000%20SPSS/00%20SPSS入门教程/association-between-categorical-variables/medias/dae32b906332bfedfca9.png)

## SPSS Clustered Bar Chart Styling

Although our chart is technically correct, it looks appalling. Its default color scheme basically just looks like a bad joke from the software developers. A fast way to prettify this and similar charts is building and applying an **SPSS chart template** (.sgt file). Our final result after doing so is shown in the last screenshot.

## SPSS Clustered Bar Chart Example

![SPSS Clustered Bar Chart Styled](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-clustered-bar-chart-styled.png.png)

**Conclusion** : as with the contingency table, we don't see much of a clear pattern here except for people tending to stay in the same sector as the previous year.

# Tell us what you think!

*Required field. Your comment will show up after approval from a moderator.

# THIS TUTORIAL HAS 14 COMMENTS:

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on August 15th, 2018

Hi Salem!

You can download a free 14-day trial version from <http://www.ibm.com>. After that, you'll have to pay as SPSS isn't free software.

Sorry about that.

Expand [comment](#) | [all comments](#)

  * ![](#)

### By Gbeminiyi Oyinloye on February 7th, 2019

The less we speak about the lack of beauty in SPSS charts the better for the good of humanity.

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on February 7th, 2019

Ha ha! Totally agree! Wise words from a wise man...

However, _do_ read up on [SPSS chart templates](../spss-chart-templates/) if you want to create pretty charts fast.

Hope that helps!

SPSS tutorials

Expand [comment](#) | [all comments](#)

  * ![](#)

### By manjari goswami on June 18th, 2023

good




[](../association-between-categorical-variables-comment-page-2/) [1](../association-between-categorical-variables-comment-page-1/) … 3

### Get In Touch!

  * [Ruben Geert van den Berg](../about-us/)
  * ![](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/wp-content-themes-spss-tutorials-11-img-linkedin-icon-white-33a.png.png)[LinkedIn](https://nl.linkedin.com/in/rubenvandenberg1 "Visit my LinkedIn Profile")
  * ![](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/wp-content-themes-spss-tutorials-11-img-facebook-icon-white-33a.png.png) [Facebook](#)



### SPSS Help (Netherlands)

  * Sigma Plus Statistiek
  * [www.sigma-plus-statistiek.nl](#)
  * info@sigma-plus-statistiek.nl



### SPSS Help (International)

  * SPSS tutorials
  * [www.spss-tutorials.com](..//)
  * info@spss-tutorials.com



##  © Copyright Protected 2025  [Disclaimer](..///disclaimer/) [Privacy Policy](#)

