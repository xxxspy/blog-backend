---
title: ANOVA方差分析入门教程
date: 2025-06-21 18:34:24
permalink: /2025/06/21/anova-what-is-it/
---

Processing math: 100%

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



# ANOVA – Super Simple Introduction

By Ruben Geert van den Berg under [ANOVA](../anova/) & [Statistics A-Z](../statistics-glossary/)

  * [ANOVA - Null Hypothesis](#null-hypothesis)
  * [Test Statistic - F](#test-statistic)
  * [Assumptions for ANOVA](#assumptions)
  * [Effect Size - (Partial) Eta Squared](#effect-size)
  * [ANOVA - Post Hoc Tests](#post-hoc-tests)



ANOVA -short for “analysis of variance”- is a statistical techniquefor testing if 3(+) population means are all equal. The two simplest scenarios are 

  * one-way ANOVA for comparing **3(+) groups on 1 variable** : do all children from school A, B and C have equal mean IQ scores? *For 2 groups, one-way ANOVA is identical to an [independent samples t-test](..///spss-independent-samples-t-test/ ).
  * [repeated measures ANOVA](../spss-repeated-measures-anova/) for comparing **3(+) variables in 1 group** : is the mean rating for beer A, B and C equal for all people?*For 2 variables, repeated measures ANOVA is identical to a [paired samples t-test](../spss-paired-samples-t-test/).



The figure below visualizes the basic question for one-way ANOVA.

![ANOVA - What Is It?](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/a6d1636006450f7fb68d.png)

## Simple Example - One-Way ANOVA

A scientist wants to know if all children from schools A, B and C have equal mean IQ scores. Each school has 1,000 children. It takes too much time and money to test all 3,000 children. So a simple random sample of n = 10 children from each school is tested. Part of these data -available from [this Googlesheet](#) are shown below.

![ANOVA What Is It Data View](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/941515827f7f197cc182.png)

## Descriptives Table

Right, so our data contain 3 samples of 10 children each with their IQ scores. Running a simple descriptives table immediately tells us the mean IQ scores for these samples. The result is shown below.

![ANOVA What Is It Descriptives](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/ad9234c97f26bf186af3.png)

For making things clearer, let's visualize the mean IQ scores per school in a simple bar chart.

![ANOVA - What Is It? Means Chart](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/0c0cad69acb5e96f16e7.png)

Clearly, our sample from school B has the highest mean IQ - roughly 113 points. The lowest mean IQ -some 93 points- is seen for school C. Now, here's the problem: our mean IQ scores are only based on tiny samples of 10 children per school. So couldn't it be that _all_ 1,000 children per school have the same mean IQ? Perhaps we just happened to sample the smartest children from school B and the dumbest children from school C?*“Dumbest” isn't really appropriate here: these children may have terrific talents that -unfortunately for them- aren't measured by the test adminstered. However, a discussion of the usefulness of IQ tests is beyond the scope of this tutorial. Is that realistic? We'll try and show that this statement -our null hypothesis- is not credible given our data.

## ANOVA - Null Hypothesis

The null hypothesis for (any) ANOVA is that all population means are exactly equal. If this holds, then our _sample means_ will probably differ a bit. After all, samples always differ a bit from the populations they represent. However, the sample means probably shouldn't differ too much. Such an outcome would be unlikely under our null hypothesis of equal population means. So if we _do_ find this, we'll probably no longer believe that our population means were really equal. 

## ANOVA - Sums of Squares Between

So precisely how different are our 3 sample means? How far do these numbers lie apart? A number that tells us just that is the variance. So we'll basically compute the variance among our 3 sample means. As you may (or may not) understand from the [ANOVA formulas](#formulas), this starts with the sum of the squared deviations between the 3 sample means and the overall mean. The outcome is known as the “sums of squares between” or SSbetween. So sums of squares between expresses the total amount of dispersion among the sample means. Everything else equal, larger SSbetween indicates that the sample means differ more. And the more different our sample means, the more likely that our population means differ as well. 

![ANOVA Sums Of Squares Between Bar Chart Means](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/8c71cffb6adfe594de51.png)

## Degrees of Freedom and Mean Squares Between

When calculating a “normal” variance, we divide our sums of squares by its degrees of freedom (df). When comparing k means, the degrees of freedom (df) is (k - 1). Dividing SSbetween by (k - 1) results in mean squares between: MSbetween. In short, _mean squares between_ is basically the variance among sample means. MSbetween thus indicates how far our sample means differ (or lie apart). The larger this variance between means, the more likely that our population means differ as well. 

## ANOVA - Sums of Squares Within

If our population means are really equal, then what difference between sample means -MSbetween- can we reasonably expect? Well, this depends on the variance _within_ subpopulations. The figure below illustrates this for 3 scenarios.

![ANOVA What Is It Variance Within Groups Histograms](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/b1c7db229982fe0ee5e8.png)

The 3 leftmost histograms show population distributions for IQ in schools A, B and C. Their narrowness indicates a **small variance within** each school. If we'd sample n = 10 students from each school, should we expect very different sample means? Probably not. Why? Well, due to the small variance within each school, the sample means will be close to the (equal) population means. These narrow histograms don't leave a lot of room for their sample means to fluctuate and -hence- differ. The 3 rightmost histograms show the opposite scenario: the histograms are wide, indicating a **large variance within** each school. If we'd sample n = 10 students from each school, the means in these samples may easily differ quite a lot. In short, larger variances _within_ schools probably result in a larger variance _between_ sample means per school. We basically estimate the within-groups population variances from the within-groups sample variances. Makes sense, right? The exact calculations are in [the ANOVA formulas](#formulas) and [this Googlesheet](#). In short: 

  * **sums of squares within** (SSwithin) indicates the total amount of dispersion within groups;
  * **degrees of freedom within** (DFwithin) is (n - k) for n observations and k groups and
  * **mean squares within** (MSwithin) -basically the variance within groups- is SSwithin / DFwithin.



## ANOVA Test Statistic - F

So how likely are the population means to be equal? This depends on 3 pieces of information from our samples:

  * the variance between sample means (MSbetween);
  * the variance within our samples (MSwithin) and
  * the sample sizes.



We basically combine all this information into a single number: our **test statistic F**. The diagram below shows how each piece of evidence impacts F.

![ANOVA Test Statistic F Combines Between Within Variance](2025/06/21/000%20SPSS/00%20SPSS入门教程/anova-what-is-it/medias/13c26b9bc0796422f522.png)

Now, F itself is not interesting at all. However, we can obtain the [statistical significance](../statistical-significance/) from F if it follows an F-distribution. It will do just that if 3 assumptions are met.

## ANOVA - Assumptions

The assumptions for ANOVA are

  * independent observations;
  * **normality** : the outcome variable must follow a [normal distribution](../normal-distribution/) in each subpopulation. Normality is really only needed for small sample sizes, say n < 20 per group.
  * **homogeneity** : the variances within all subpopulations must be equal. Homogeneity is only needed if sample sizes are very unequal. In this case, [Levene's test](../levenes-test-in-spss/) indicates if it's met.



If these assumptions hold, then F follows an F-distribution with DFbetween and DFwithin degrees of freedom. In our example -3 groups of n = 10 each- that'll be F(2,27).

## ANOVA - Statistical Significance

In our example, F(2,27) = 6.15. This huge F-value is strong evidence that our null hypothesis -all schools having equal mean IQ scores- is not true. If all assumptions are met, F follows the F-distribution shown below.

![F Distribution with DF\(2,27\)](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-f-distribution-2-27.png.png)

Given this distribution, we can look up that the [statistical significance](../statistical-significance/). We usually report: F(2,27) = 6.15, **p = 0.006**. If our schools have equal mean IQ's, there's only a 0.006 chance of finding our sample mean differences or larger ones. We usually say something is “statistically significant” if p < 0.05. Conclusion: our population means are very _unlikely_ to be equal. The figure below shows how [SPSS](../spss-what-is-it/) presents the output for this example. 

![ANOVA What Is It SPSS Output](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-anova-what-is-it-spss-output.png.png)

## Effect Size - (Partial) Eta Squared

So far, our conclusion is that the population means are not all exactly equal. Now, “not equal” doesn't say much. What I'd like to know is exactly _how different_ are the means? A number that estimates just that is the [effect size](../effect-size/). An effect size measure for ANOVA is [partial eta squared](../spss-partial-eta-squared/), written as η2.*η is the Greek letter “eta”, pronounced as a somewhat prolonged “e”. For a one-way ANOVA, partial eta-squared is equal to simply eta-squared. Technically, (partial) eta-squared is the proportion of variance accounted for by a factor. Some rules of thumb are that 

  * η2 > 0.01 indicates a **small** effect;
  * η2 > 0.06 indicates a **medium** effect;
  * η2 > 0.14 indicates a **large** effect.



The exact calculation of eta-squared is shown in the [formulas section](#formulas). For now, suffice to say that **η 2 = 0.31** for our example. This huge -_huge_ - effect size explains why our F-test is statistically significant despite our very tiny sample sizes of n = 10 per school.

## Post Hoc Tests - Tukey's HSD

So far, we concluded from our F-test that our population means are very unlikely to be (all) equal. The effect size, η2, told us that the difference is large. An unanswered question, though, is precisely _which_ means are different? Different patterns of sample means may all result in the exact same F-value. The figure below illustrates this point with some possible scenarios. 

![ANOVA - Post Hoc Tests for Different Patterns of Sample Means](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-anova-post-hoc-tests-means-plots-different-scenarios.png.png)

One approach would be running [independent samples t-tests](..///spss-independent-samples-t-test/ ) on all possible _pairs_ of means. For 3 means, that'll be A-B, A-C and B-C. However, as the number of means we compare grows, the number of all possible pairs rapidly increases.*Precisely, k means result in 0.5 * k * (k - 1) distinct pairs. Like so, 3 means have 3 distinct pairs, 4 means have 6 distinct pairs and 5 means have 10 distinct pairs. And each t-test has its own chance of drawing a wrong conclusion. So the more t-tests we run, the bigger the risk of drawing at least one wrong conclusion. The most common solution to this problem is using **Tukey's HSD** (short for “Honestly Significant Difference”) procedure. You could think of it as running all possible t-tests for which the results have been corrected with some sort of [Bonferroni correction](#) but less conservative. The figure below shows some output from Tukey's HSD in SPSS.

![ANOVA - Results of Tukey's HSD in SPSS Output](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-tukey-hsd-output-school-data.png.png)

Tukey's HSD is known as a **[post hoc test](../anova/-what-is-it/#post-hoc-tests)**. “Post hoc” is Latin and literally means “after that”. This is because they are run only _after_ the main F-test has indicated that not _all_ means are equal. I don't entirely agree with this convention because

  * post hoc tests **may not** indicate differences while the main F-test **does** ;
  * post hoc tests **may** indicate differences while the main F-test **does not**.



Say I'm comparing 5 means: A, B, C and D are equal but E is much larger than the others. In this case, the large difference between E and the other means will be strongly diluted when testing if all means are equal. So in this case an overall F-test may not indicate any differences while post hoc tests _will_.

Last but not least, there's many other post hoc tests as well. Some require the homogeneity assumption and others don't. The figure below shows some examples.

![ANOVA - Overview Different Post Hoc Tests in SPSS ANOVA Dialog](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/img-spss-anova-overview-post-hoc-tests-dialog.png.png)

## ANOVA - Basic Formulas

For the sake of completeness, we'll list the main formulas used for the one-way ANOVA in our example. You can see them in action in [this Googlesheet](#). We'll start off with the **between-groups** variance: SSbetween=Σnj(¯Xj−¯X)2 where

  * ¯Xj denotes a group mean;
  * ¯X is the overall mean;
  * nj is the sample size per group.



For our example, this results in SSbetween=10(99.2−101.7)2+10(112.6−101.7)2+10(93.3−101.7)2=1956.2 Next, for m groups, dfbetween=m−1 so dfbetween = 3 - 1 = 2 for our example data. MSbetween=SSbetweendfbetween For our example, that'll be 1956.22=978.1 We now turn to the **within-groups** variance. First off, SSwithin=Σ(Xi−¯Xj)2 where

  * ¯Xj denotes a group mean;
  * Xi denotes an individual observation (“data point”).



For our example, this'll be SSwithin=(90−99.2)2+(87−99.2)2+...+(96−93.3)2=4294.1 for n independent observations and m groups, dfwithin=n−m So for our example that'll be = 30 - 3 = 27. MSwithin=SSwithindfwithin For our example, this results in 4294.127=159 We're now ready to calculate the **F-statistic** : F=MSbetweenMSwithin which results in 978.1159=6.15 Finally, P=P(F(2,27)>6.15)=0.0063 Optionally, the **effect size** η2 is calculated as Effectsizeη2=SSbetweenSSbetween+SSwithin For our example, that'll be 1956.21956.2+4294.1=0.31 Thanks for reading.

# Tell us what you think!

*Required field. Your comment will show up after approval from a moderator.

# THIS TUTORIAL HAS 61 COMMENTS:

  * ![](#)

### By Babak on January 13th, 2023

honestly, I think this article is very educative. l learnt a great deal about ANOVA and its respective effect size both conceptually and technically. Thank you so much!




[](../anova/-what-is-it/comment-page-12/#comments) [1](../anova/-what-is-it/comment-page-1/#comments) … 13

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

