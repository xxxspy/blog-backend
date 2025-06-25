---
title: SPSS因子分析结果的APA格式报告指南
date: 2025-06-21 18:34:26
permalink: /2025/06/21/apa-reporting-factor-analysis/
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



# APA Reporting SPSS Factor Analysis

By Ruben Geert van den Berg under [Factor Analysis](../spss-factor-analysis-tutorials/) & [Tables in SPSS](../tables/)

  * [Introduction](#introduction)
  * [Creating APA Tables - the Easy Way](#creating-apa-tables-the-easy-way)
  * [Table I - Factor Loadings & Communalities](#table-i-factor-loadings-communalities)
  * [Table II - Total Variance Explained](#table-ii-total-variance-explained)
  * [Table III - Factor Correlations](#table-iii-factor-correlations)



## Introduction

Creating APA style tables from SPSS factor analysis output can be cumbersome. This tutorial therefore points out some tips, tricks & pitfalls. We'll use the results of [SPSS Factor Analysis - Intermediate Tutorial](../spss-factor-analysis-intermediate-tutorial/).

All analyses are based on [20-career-ambitions-pca.sav](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/downloads-20-career-ambitions-pca.sav.sav) (partly shown below).

![SPSS Factor Analysis Promax Rotation Variable View](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/da058c810fc7939d99b6.png)

![](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/01a3971f98e5ddd55c2b.png) Note that some items were reversed and therefore had “(R)” appended to their variable labels; ![](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/f9b2af41bdafb04a626f.png) We'll [FILTER](../spss-filter-command/) out cases with 10 or more missing values. 

After opening these data, you can replicate the final analyses by running the [SPSS syntax](../spss-syntax/) below.

***ACTIVATE FILTER VARIABLE.** filter by filt01.***PCA VI - AS PREVIOUS BUT REMOVE TOU04.** FACTOR /VARIABLES Car01 Car02 Car03 Car04 Car05 Car06 Car07 Car08 Conf01 Conf02 Conf03 Conf05 Conf06 Comp01 Comp02 Comp03 Tou01 Tou02 Tou05 Succ01 Succ02 Succ03 Succ04 Succ05 Succ06 Succ07 /MISSING PAIRWISE /PRINT INITIAL EXTRACTION ROTATION /FORMAT SORT BLANK(.3) /CRITERIA FACTORS(5) ITERATE(25) /EXTRACTION PC /ROTATION PROMAX /METHOD=CORRELATION.

## Creating APA Tables - the Easy Way

For a wide variety of analyses, the easiest way to create [APA](#) style tables from SPSS output is usually to

  1. adjust your analyses in **SPSS** so the output is as close as possible to the desired end results. Changing table layouts (which variables/statistics go into which rows/columns?) is also best done here.
  2. copy-paste one or more tables into **Excel** or Googlesheets. This is the easiest way to set decimal places, fonts, alignment, borders and more;
  3. copy-paste your table(s) from Excel into **WORD**. Perhaps adjust the table widths with “autofit”, and you'll often have a perfect end result.

![Word Autofit Tables Example](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/a48756ba735cb8565b9a.png) Autofit to Contents, then Window results in optimal column widths

## Table I - Factor Loadings & Communalities

The figure below shows an APA style table combining factor loadings and communalities for our example analysis.

![Apa Reporting Factor Analysis Factor Loadings Table](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/90fe5503ea2c0290eedb.png) Example APA style factor loadings table

If you take a good look at the [SPSS](../spss-what-is-it/) output, you'll see that you _cannot_ simply copy-paste these tables for combining them in Excel. This is because the factor loadings (pattern matrix) table follows a different variable order than the communalities table. Since the latter follows the variable order as specified in your syntax, the easiest fix for this is to

  * make sure that only variable names (not labels) are shown in the output;
  * copy-paste the correctly sorted pattern matrix into Excel;
  * copy-paste the variable names into the FACTOR syntax and rerun it.



Tip: try and replace the line breaks between variable names by spaces as shown below.

![SPSS Find Replace In Syntax Example](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/9c6a40d567e38bb2091d.png) Replace line breaks by spaces in an SPSS syntax window

Also, you probably want to see only variable labels (not names) from now on. And -finally- we no longer want to hide any small absolute factor loadings shown below. 

![SPSS Pca Pattern Matrix](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/f54eae9af4dd1d73ea93.png) This table is fine for an exploratory analysis but not for reporting

The syntax below does all that and thus creates output that is ideal for creating APA style tables.

***SHOW ONLY VARIABLE LABELS, NOT NAMES.** set tvars labels.***RERUN PREVIOUS ANALYSIS WITH VARIABLE ORDER AS IN PATTERN MATRIX TABLE.** FACTOR /VARIABLES Car02 Car04 Car05 Car03 Car01 Car08 Car07 Car06 Succ01 Succ02 Succ03 Succ05 Succ07 Succ04 Succ06Conf03 Conf01 Conf05 Conf02 Conf06 Tou02 Tou05 Tou01 Comp02 Comp03 Comp01 /MISSING PAIRWISE /PRINT INITIAL EXTRACTION ROTATION /FORMAT SORT /CRITERIA FACTORS(5) ITERATE(25) /EXTRACTION PC /ROTATION PROMAX /METHOD=CORRELATION.

You can now safely combine the communalities and pattern matrix tables and make some final adjustments. The end result is shown in [this Googlesheet](#), partly shown below.

![Apa Style Factor Loadings Table Googlesheets](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/90ac7f35ff5dbfdb308e.png) An APA table for WORD is best created in a Googlesheet or Excel

Since decimal places, fonts, alignment and borders have all been set, this table is now perfect for its final copy-paste into WORD.

## Table II - Total Variance Explained

The screenshot below shows how to report the Eigenvalues table in APA style.

![Apa Reporting Factor Analysis Eigenvalues Table](2025/06/21/000%20SPSS/00%20SPSS入门教程/apa-reporting-factor-analysis/medias/215513c9ae98f6404c58.png) APA style Eigenvalues example table

The corresponding SPSS output table comes fairly close to this. However, an annoying problem are the missing percent signs.

![SPSS Pca Total Variance Explained Table](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-pca-total-variance-explained-table.png.png)

If we copy-paste into Excel and set a percentage format, 34.57 is converted into 3,457%. This is because Excel interprets these numbers as proportions rather than percentage points as SPSS does. The easiest fix is setting a percent format for these columns in SPSS before copy-pasting into Excel.

The OUTPUT MODIFY example below does just that for all Eigenvalues tables in the output window.

***APPLY PERCENTAGE FORMAT TO PERCENT COLUMNS IN ALL TOTAL VARIANCE EXPLAINED TABLES.** output modify/select tables/tablecells select = ["% of Variance"] format = 'pct6.2'/tablecells select = ["Cumulative %"] format = 'pct6.2'.

After this tiny fix, you can copy-paste this table from SPSS into Excel. We can now easily make some final adjustments (including the removal of some rows and columns) and copy-paste this table into WORD.

## Table III - Factor Correlations

If you used an oblique factor rotation, you'll probably want to report the correlations among your factors. The figure below shows an APA style factor correlations table.

![Apa Reporting Factor Analysis Correlations Among Factors Table](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-apa-reporting-factor-analysis-correlations-among-factors-table.png.png)

The corresponding SPSS output table (shown below) is pretty different from what we need.

![SPSS Pca Component Correlation Matrix](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-pca-component-correlation-matrix.png.png) APA style factor correlation table

Adjusting this table manually is pretty doable. However, I personally prefer to use an SPSS Python script for doing so.

You can download my script from [LAST-FACTOR-CORRELATION-TABLE-TO-APA.sps](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/downloads-LAST-FACTOR-CORRELATION-TABLE-TO-APA.sps.sps). This script is best run from an INSERT command as shown below.

***Run Python script for adjusting factor correlation table.** insert file = 'D:\DOWNLOADS\LAST-FACTOR-CORRELATION-TABLE-TO-APA.sps'.

I highly recommend trying this script but it does make some assumptions:

  * the above syntax assumes the script is located in D:\DOWNLOADS so you probably need to change that;
  * the script assumes that you've the SPSS Python3.x essentials properly installed (usually the case for recent SPSS versions);
  * the script assumes that no SPLIT FILE is in effect.



If you've any trouble or requests regarding my script, feel free to contact me and I'll see what I can do.

## Final Notes

Right, so these are the basic routines I follow for creating APA style factor analysis tables. I hope you'll find them helpful.

If you've any feedback, please throw me a comment below.

**Thanks for reading!**

# Tell us what you think!

*Required field. Your comment will show up after approval from a moderator.

# THIS TUTORIAL HAS 5 COMMENTS:

  * ![](#)

### By Iris on July 15th, 2022

Hi, quick question. Where can you find the sig levels from the correlation table? Or do you just have to report it without them?

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on July 16th, 2022

Hi Iris!

They're not usually reported.

You could obtain them by saving the factor scores as new variables and running correlations over them as covered in [SPSS Correlation Analysis](../spss-correlation-analysis/). 

However, this only works if you use listwise exclusion of missing values which is a bad idea for the data used in this tutorial. 

With pairwise exclusion (used here) the correlations from FACTOR may differ from those from CORRELATIONS due to missing values on the created factor score variables.

Hope that helps!

SPSS tutorials

Expand [comment](#) | [all comments](#)

  * ![](#)

### By Mihiretu Wondimu on January 2nd, 2025

It is a good guide for students and new researchers. But is this your own style or is it a standard that we have to follow as an APA standard of reporting? Thank You!

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on January 2nd, 2025

No, the tables I presented in this tutorial are the ones that the APA suggests. 

I'd like to add that I often disagree with the APA standards but that's a whole different story. Let's not go into that.

  * ![](#)

### By Xavier on March 21st, 2025

Informative.




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

