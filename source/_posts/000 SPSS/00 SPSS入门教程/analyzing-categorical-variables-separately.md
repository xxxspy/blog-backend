---
title: SPSS：分类变量的单独分析
date: 2025-06-21 18:34:22
permalink: /2025/06/21/analyzing-categorical-variables-separately/
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



# Analyzing Categorical Variables Separately

By Ruben Geert van den Berg under [SPSS Data Analysis](../spss-data-analysis/)

When analyzing your data, you sometimes just want to gain some insight into variables separately. The first step in doing so is creating appropriate tables and charts. This tutorial shows how to do so for [dichotomous](../what-is-a-dichotomous-variable/) or categorical variables. We recommend you follow along by downloading and opening [smartphone_users.sav](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/downloads-smartphone_users.sav.sav).

![SPSS Smartphone Users Data - Data View](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/521399eabd6c1ed64b2c.png)

## SPSS Frequency Tables

We'd like to know which smartphone brands were most popular in 2011. Our data contains a variable brand_2011 holding the relevant data. Since this is a categorical variable, a suitable table here is a simple frequency table as obtained with [FREQUENCIES](../spss-frequencies-command/). The [syntax](..///spss-syntax/ ) below shows how to run it.

***1. Show value labels and variable labels in output.** set tnumbers labels tvars labels.***2. Create frequency table.** frequencies brand_2011.

## Result

![SPSS Frequency Table Categorical Variable](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/9d15b54acb88a619e9f2.png)

Note that there's some [system missing values](../spss-missing-values-tutorial/). Presuming these occurred due to respondents not using a smartphone in the first place, we'll report the figures under “Percent”. **Conclusion** : in 2011, 33% of our respondents used a Samsung smartphone, making it the most popular brand during that year.

## SPSS Bar Charts for Categorical Variable

Our frequency table provides us with the necessary information but we need to look at it carefully for drawing conclusions. Doing so is greatly facilitated by creating a simple bar chart with bars representing frequencies. The fastest way to do so is including it in our FREQUENCIES command but this doesn't allow us to add a title. We'll therefore do it differently as shown by the screenshots below.

![SPSS Create Bar Chart with Title 1](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/bd62f1fd385f21cf8e0c.png) ![SPSS Create Bar Chart with Title 2](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/c0938b0156e6b6827bd7.png)

## SPSS Bar Chart Syntax Example

***Bar chart with title for brand_2011.** GRAPH /BAR(SIMPLE)=COUNT BY brand_2011/title 'All Respondents (n = 566)'.

## Result

![SPSS Bar Chart with Title](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/ecd035d4e660b6f2177d.png)

We now have our basic bar chart. For a serious report, however, you probably want a better looking chart. A great way for prettifying charts is discussed in [SPSS Chart Templates - Quick Introduction](../spss-chart-templates/).

## System Missing Values

Thus far, we simply ignored the system missing values we saw in our frequency table. For nominal variables, an alternative approach is including them as just another answer category. The syntax below does just that for all brand variables. We'll first inspect which values are present. Next, we'll [RECODE](..///spss-recode-command/ ) system missing values into a value that wasn't present yet. In our case that will be 6.

## SPSS RECODE Syntax Example

***1. Show values and value labels in output tables.** set tnumbers both.***2. Inspect which values are present in brand variables.** frequencies brand_2011 to brand_2015.***3. Change system missing values to 6.** recode brand_2011 to brand_2015 (sysmis = 6).***4. Apply value label to new value.** add value labels brand_2011 to brand_2015 6 '(No answer)'.***5. Show only value labels in output tables.** set tnumbers labels.***6. Rerun frequency tables.** frequencies brand_2011 to brand_2015.

## Result

![SPSS Frequency Table 2](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/620effb0b1ba47dd895b.png)

Note that our frequency table no longer includes any missing values. They've been converted to 6, which is labeled “(No answer)” and occurs 30 times for this variable. We see that recoding system missing values make our frequency tables look better but there's another advantage: because the brand variables don't contain missing values anymore, their bar charts will all be based on the same number of respondents. This circumvents the need for specifying different numbers of respondents in their titles; we can create them very easily by copy-pasting-editing the syntax we used previously. The syntax below illustrates the idea.

## SPSS Bar Charts Syntax Example

***Create bar charts for several brand variables.** GRAPH /BAR(SIMPLE)=COUNT BY brand_2011 /TITLE='All Respondents (n = 596)'.GRAPH /BAR(SIMPLE)=COUNT BY brand_2012 /TITLE='All Respondents (n = 596)'.GRAPH /BAR(SIMPLE)=COUNT BY brand_2013 /TITLE='All Respondents (n = 596)'.

## Result

![SPSS Bar Chart with Title](2025/06/21/000%20SPSS/00%20SPSS入门教程/analyzing-categorical-variables-separately/medias/cb3c2eda960d1ca009f2.png)

# Tell us what you think!

*Required field. Your comment will show up after approval from a moderator.

# THIS TUTORIAL HAS 15 COMMENTS:

  * ![](#)

### By Chris on March 9th, 2016

Great website! After many years off, I need to purchase SPSS again. Not sure where to place my question...

I know that the SPSS Tables Original (Basic Tables, General Tables, Multiple Response Tables, Tables of Frequencies) user interface is no longer available and no longer supported. However, some sources on the internet note that the "existing TABLES syntax should continue to work". Do you know if the TABLES syntax will work in SPSS Statistics Base. I would download a trial, but the trial version is not SPSS Statistics Base. More to the point, I don't need to purchase a CUSTOM TABLES module if I can use the TABLES command in SPSS Statistics Base.

Expand [comment](#) | [all comments](#)

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on March 11th, 2016

Hi Chris!

I obviously can't guarantee that TABLES will keep on working. However, SPSS seems almost obsessed with backward compatibility so I find it highly unlikely they'll discontinue support.

More importantly, the TABLES command demonstrated here is the only one I found useful so far. Since it can be replaced by VARSTOCASES followed by [CROSSTABS](../spss-crosstabs-command/), I don't see any need for TABLES in the first place.

Alternatively, we may (or may not) start working on a workaround for CUSTOM TABLES: create the actual table data as a dataset and convert it into an SPSS output table by means of Python scripting. Like so, you can easily create any table you can imagine but the conversion to an output table will take some effort to set up.

Exactly what kind of table do you need anyway? Could you perhaps upload an example screenshot for us?

Expand [comment](#) | [all comments](#)

  * ![](#)

### By Adekunle Adurapemi on July 8th, 2016

Please can u send this tutorial to my email address? Thanks

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on July 8th, 2016

Hi Adekunie! Our tutorials are available online only. You can save it via your web browser if you want to but you may lose some functionality such as hyperlinks and hidden comments.

  * ![](#)

### By Pooja on October 23rd, 2018

Helpful for us!




[](../analyzing-categorical-variables-separately-comment-page-2/) [1](../analyzing-categorical-variables-separately-comment-page-1/) … 3

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

