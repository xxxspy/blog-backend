---
title: SPSS：从Excel应用字典信息
date: 2025-06-21 18:34:27
permalink: /2025/06/21/apply-dictionary-information-from-excel/
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



# Apply Dictionary Information from Excel

By Ruben Geert van den Berg under [SPSS Python Basics](../spss-python-basics/)

## Question

_“I have an Excel workbook whose three sheets contain data values, variable labels and value labels. How can I apply the dictionary information from these last two sheets to the SPSS dataset after importing the data values?”_

## Option A: Python

A nice and clean option is to have [Python](..///python-for-spss-what-is-it/ ) read the dictionary information from the Excel sheets. The cell contents can then be inserted into standard `VARIABLE LABELS` and `ADD VALUE LABELS` commands. Running these commands applies the [variable labels](../spss-set-variable-labels-with-syntax/) and value labels to the data values. We'll use [data_and_labels.xls](2025/06/21/000%20SPSS/00%20SPSS入门教程/_files_/downloads-data_and_labels.xls.xls) for demonstrating this approach.

## 1. Read the Data Values

Reading Excel data values into SPSS is straightforward. We usually paste the required syntax from _F_ ile ![SPSS Menu Arrow](2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/medias/af5a114f9cbb436fbbd2.png) _O_ pen ![SPSS Menu Arrow](2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/medias/af5a114f9cbb436fbbd2.png)D _a_ ta. The screenshot below shows which options to select.

![SPSS Import Excel Data](2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/medias/47cadcbb222621f9b22e.png) Importing Excel Data into SPSS

## SPSS Syntax for Reading Excel Data

***1. Read data values (pasted syntax from GUI).** GET DATA /TYPE=XLS /FILE='D:\Downloaded\data_and_labels.xls' /SHEET=name 'data' /CELLRANGE=full /READNAMES=on /ASSUMEDSTRWIDTH=32767.

## 2. Create Variable Labels Command

Let's first open our workbook and take a look at how the second sheet is structured. As shown in the screenshot below, the first column holds variable names and the second variable labels.

![SPSS Variable Labels in Excel](2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/medias/cd22fc38ae081940abe8.png) SPSS Variable Labels in Excel

Now we'll read this second sheet with Python instead of SPSS. Note that you need to have the SPSS Python Essentials as well as the [xlrd module](..///xlrd/ ) installed first. The [syntax](..///spss-syntax/ ) below shows how to create the `VARIABLE LABELS` commands as a single (multi line) string. For now we'll just print it for inspection.

## SPSS Python Syntax Example

***2. Create and inspect VARIABLE LABELS commands.** begin program.xlsPath = r'D:\Downloaded\data_and_labels.xls'import xlrdvarLabCmd = ''wb = xlrd.open_workbook(xlsPath)varLabs = wb.sheets()[1]for rowCnt in range(varLabs.nrows): rowVals = varLabs.row_values(rowCnt) varLabCmd += "variable labels %s '%s'.\n"%(rowVals[0],rowVals[1].replace("'","''"))print varLabCmdend program.

## 3. Create Value Labels Command

![SPSS Value Labels in Excel](2025/06/21/000%20SPSS/00%20SPSS入门教程/apply-dictionary-information-from-excel/medias/51039dd0c1120a07fca1.png) SPSS Value Labels in Excel

Remember that Python objects persist over program blocks. We can therefore leave out the first lines of syntax from the previous example. The Excel sheet holding value labels has the same basic structure as the one with variable labels (see screenshot). The main difference is that we'll now insert three pieces of information (variable name, value, value label) into each line. We'll generate our `ADD VALUE LABELS` commands as shown below.

## SPSS Python Syntax Example

***3. Create and inspect ADD VALUE LABELS commands.** begin program.valLabCmd = ''valLabs = wb.sheets()[2]for rowCnt in range(valLabs.nrows): rowVals = valLabs.row_values(rowCnt) valLabCmd += "add value labels %s %d '%s'.\n"%(rowVals[0],rowVals[1],rowVals[2].replace("'","''"))print valLabCmdend program.

## Running the Python Generated Syntax

If neither of the generated commands require any further tweaking, the only thing left to do is just run them by using `spss.Submit`. The syntax below does so and thus finishes this job.

***4. Run both commands.** begin program.import spssspss.Submit(varLabCmd)spss.Submit(valLabCmd)end program.

## Option B: Syntax Generating Syntax

Before Python was introduced to SPSS, a different approach was needed for this situation. It comes down to declaring a new (long) [string variable](..///spss-string-variables-basics/ ) and using CONCAT to create lines of syntax as string values. Next, we save the contents of this string variable as a .txt file with an .sps extension and INSERT it. We don't usually recommend taking this approach but we'll present it anyway for the sake of the demonstration. Some of the commands used by the syntax below are explained in [SPSS Datasets Tutorial 1 - Basics](../spss-datasets-tutorial-1-basics/) and [SPSS String Variables Tutorial](../spss-string-variables-tutorial/).

## SPSS Syntax Generating Syntax

***1. Set working directory.** cd 'd:/downloaded'. /*or wherever Excel file is located.***2. Read data values (pasted syntax from GUI).** GET DATA /TYPE=XLS /FILE='data_and_labels.xls' /SHEET=name 'data' /CELLRANGE=full /READNAMES=on /ASSUMEDSTRWIDTH=32767.dataset name values.***3. Read variable labels.** GET DATA /TYPE=XLS /FILE='data_and_labels.xls' /SHEET=name 'variablelabels' /CELLRANGE=full /READNAMES=off /ASSUMEDSTRWIDTH=32767.dataset name varlabs.dataset activate varlabs.string syntax(a1000).***4. Create syntax in data window.** compute syntax = concat("variable labels ",rtrim(v1),"'",rtrim(replace(v2,"'","''")),"'.").exe.***5. Save variable holding syntax as .sps file.** write outfile 'insert_varlabs.sps'/syntax.exe.dataset close varlabs.***6. Import value labels sheet.** GET DATA /TYPE=XLS /FILE='data_and_labels.xls' /SHEET=name 'valuelabels' /CELLRANGE=full /READNAMES=off /ASSUMEDSTRWIDTH=32767.dataset name vallabs.dataset activate vallabs.string syntax(a1000).***7. Create syntax in data window.** compute syntax = concat("add value labels ",rtrim(v1)," ",ltrim(str(v2,f3)),"'",rtrim(replace(v3,"'","''")),"'.").exe.***8. Save syntax variable as .sps file.** write outfile 'insert_vallabs.sps'/syntax.exe.dataset close vallabs.dataset activate values.***9. Run both syntax files.** insert file = 'insert_varlabs.sps'.insert file = 'insert_vallabs.sps'.***10 Optionally, delete both syntax files.** erase file = 'insert_varlabs.sps'.erase file = 'insert_vallabs.sps'.

# Tell us what you think!

*Required field. Your comment will show up after approval from a moderator.

# THIS TUTORIAL HAS 9 COMMENTS:

  * ![](#)

### By Petri Aaltonen on August 28th, 2016

Dear Ruben

Is there a way to use Python and xlrd (from within SPSS Syntax) to import only specific columns of data from my XLSX data file? I would like to have a row in my XLSX-file with a variable (eg. values 0 or 1) defining whether to import a column to SPSS for further analysis. This is because I have lots of data in the excel sheet that I don't need to analyze in SPSS, and restructuring the excel-file is inconvenient.

Expand [comment](#) | [all comments](#)

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on August 29th, 2016

Hi Petri! Sure that's possible. However, I think it'll be much easier to import _all_ data values with the standard pasted SPSS syntax in one go -which doesn't allow excluding variables. Then apply all dictionary information to these data and then just delete whatever you don't need. Or -reversely- delete everything except for what you need with something like

`add files file */keep v4 v12 v35 v51. execute.`

Alternatively, you could have Python read only columns of data values marked with a 1 in some row but then you'll have to somehow pass these values from Python into SPSS -surely possible but harder than the first approach.

Expand [comment](#) | [all comments](#)

  * ![](#)

### By [Bob Walker](#) on September 20th, 2016

Hi Ruben - I lost your email so am sending this note via your site. I figured it out. On my machine (Windows 10, SPSS V24) I needed the setuptools module. I also had to change this line to read: varLabs = wb.sheets()[0] and not the [1] index. Works well now!

Expand [comment](#) | [all comments](#)

  * ![](#)

### By [Ruben Geert van den Berg](../about-us/) on September 21st, 2016

Dear Bob, I'm happy to hear things are working now! Generally, [0] refers to the first sheet, [1] to the second and so on. With the variable and value labels in sheets 2 and 3, the indices for this example should be [1] and [2] unless you removed the first sheet of course.

Best,

Ruben (not "Reuben")!

Expand [comment](#) | [all comments](#)




[](../apply-dictionary-information-from-excel-comment-page-1/) [1](../apply-dictionary-information-from-excel-comment-page-1/) 2

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

