---
title: R语言快速入门练习材料
date: 2022-08-11 17:22:18
tags: R语言
---

这是我的R语言培训视频的练习代码, 视频上架后会在这里放视频链接。

请注意, 我们的教程不追求全面和深入, 我们追求的是快速入门, 
入门之后就要开始做项目, 会随着我个人的科研活动逐渐添加实践教程, 
随着你自己做的项目增多, 逐渐深入和全面, 进而进阶为高级的R研究员,
因此本系列教程是没有结束的,. 

<!-- more -->



# 加载库

```r
knitr::opts_chunk$set(echo = TRUE)

# install.packages("tidyverse")
library(tidyverse)

```

# 基本语法和快捷键

注释快捷键 ctrl-shift-C

```r

my_string <- "comment me with ctrl-shift-C"
print(my_string)


7 # 执行单行代码的快捷键 ctrl-enter

x <- 1
2 -> y 
z = x + y
m = z/y
n = m * y
# 运行代码块的快捷键 ctrl-shift-enter

```

# 数据类型和R对象

与其他编程语言（如 R 中的 C 和 java）相比，R语言的变量未声明为某种数据类型。
变量就是R-Object类型，R-object 的数据类型成为变量的数据类型。

有许多类型的 R 对象。常用的有：


## R objects

- Vectors
- Lists
- Matrices
- Arrays
- Factors
- Data Frames

### Vector

```r

# Logical	TRUE, FALSE	

v <- TRUE 
print(class(v))

# Numeric	12.3, 5, 999	

v <- 23.5
print(class(v))


# Integer	2L, 34L, 0L	

v <- 2L
print(class(v))


# Complex	3 + 2i	

v <- 2+5i
print(class(v))


# Character	'a' , '"good", "TRUE", '23.4'	

v <- "TRUE"
print(class(v))


# Raw	"Hello" is stored as 48 65 6c 6c 6f	

v <- charToRaw("Hello")
print(class(v))
v

##################################################

# Create a vector.
apple <- c('red','green',"yellow")
print(apple)

# Get the class of the vector.
print(class(apple))

```

### Lists

A list is an R-object which can contain many different types of elements inside it like vectors, functions and even another list inside it.

```r

# Create a list.
list1 <- list(c(2,5,3),21.3,sin, TRUE)

# Print the list.
print(list1)

```


### Matrices

A matrix is a two-dimensional rectangular data set. It can be created using a vector input to the matrix function.

```r

# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)

```


### Arrays

```r

# Create an array.
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)

```

### Factors

Factors are the r-objects which are created using a vector. It stores the vector along with the distinct values of the elements in the vector as labels. The labels are always character irrespective of whether it is numeric or character or Boolean etc. in the input vector. They are useful in statistical modeling.

Factors are created using the `factor()` function. The `nlevels` functions gives the count of levels.

```r

# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))

```

### Data Frames

数据框是表格数据对象。与数据框中的矩阵不同，每列可以包含不同类型的数据。第一列可以是数字，第二列可以是字符，第三列可以是boolean。它是等长向量的列表。

数据框是使用 `data.frame()` 函数创建的。



```r

# Create the data frame.
BMI <- 	data.frame(
   gender = factor(c("Male", "Male","Female")), 
   height = c(152, 171.5, 165), 
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)
BMI %>% 
dplyr::filter(gender == 'Male')

```


# 安装和加载库

```r
install.packages("tidyverse")
library(tidyverse)
```


# 清理数据

Dplyr and the Pipe %>%

```r

mpg %>% 
dplyr::filter(model == 'a4') %>%  # return all rows that satisfy conditions

dplyr::arrange(displ, cyl) %>%  # reorder your columns

dplyr::mutate(old = year < 2000,
              full_Wheel_drive = drv == 'f') %>%   # add new preserve old

# dplyr::transmute(full_wheel_drive = drv == 'f') # add new drop old

dplyr::select(-drv) # keep or remove columns

mpg %>% 
dplyr::count(model,sort = T) %>% 
  dplyr::filter(n > 8)# create aggregate stats


```



# 数据可视化


```r
# ggplot(data = <DATA>) + 
#   <GEOM_FUNCTION>(mapping = aes(<MAPPINGS>))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) + 
  facet_wrap(~ class, nrow = 2)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) + 
  facet_grid(drv ~ cyl)

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) 

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy)) +
  geom_smooth(mapping = aes(x = displ, y = hwy))

ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) + 
  geom_point(mapping = aes(color = class)) + 
  geom_smooth()

ggplot(data = diamonds) + 
  geom_bar(mapping = aes(x = cut))

```

# Examples of EDA

```r

smaller <- diamonds %>% 
  filter(carat < 3)
  
ggplot(data = smaller, mapping = aes(x = carat)) +
  geom_histogram(binwidth = 0.3)

ggplot(data = mpg) +
  geom_boxplot(mapping = aes(x = reorder(class, hwy, FUN = median), y = hwy))

diamonds %>% 
  count(color, cut, sort = T) %>%  
  ggplot(mapping = aes(x = color, y = cut)) +
  
    geom_tile(mapping = aes(fill = n))

```

# 加载自己的数据

```r

# read in files

data


# paste tribbles



preg <- tribble(
  ~pregnant, ~male, ~female,
  "yes",     NA,    10,
  "no",      20,    12
)

preg

```


# Party winners

```r

# or use the data pasta package

library(datapasta)










# Ease of making ggplots


library(esquisse)




library(ggplot2)

ggplot(data) +
 aes(x = carat, y = price) +
 geom_point(size = 1L, colour = "#26828e") +
 geom_smooth(span = 0.75) +
 labs(x = "carat", y = "price", title = "heres my title", subtitle = "a view of diamonds", caption = "hello caption") +
 theme_minimal()

data %>%
 filter(depth >= 60L & depth <= 79L) %>%
 ggplot() +
 aes(x = carat, y = price) +
 geom_point(size = 0.78, colour = "#000000") +
 labs(x = "carat", y = "price", title = "heres my title", subtitle = "a view of diamonds", caption = "hello caption") +
 theme_minimal()

data %>%
 filter(depth >= 60L & depth <= 79L) %>%
 ggplot() +
 aes(x = carat, y = price) +
 geom_point(size = 0.78, colour = "#000000") +
 labs(x = "carat", y = "price", title = "heres my title", subtitle = "a view of diamonds", caption = "hello caption") +
 theme_minimal()




# Ray shaded graphics

library(rayshader)

#Here, I load a map with the raster package.
loadzip = tempfile() 
download.file("https://tylermw.com/data/dem_01.tif.zip", loadzip)
localtif = raster::raster(unzip(loadzip, "dem_01.tif"))
unlink(loadzip)

#And convert it to a matrix:
elmat = raster_to_matrix(localtif)

#We use another one of rayshader's built-in textures:
elmat %>%
  sphere_shade(texture = "desert") %>%
  plot_map()

############################################################################

a = data.frame(x = rnorm(20000, 10, 1.9), y = rnorm(20000, 10, 1.2))
b = data.frame(x = rnorm(20000, 14.5, 1.9), y = rnorm(20000, 14.5, 1.9))
c = data.frame(x = rnorm(20000, 9.5, 1.9), y = rnorm(20000, 15.5, 1.9))
data = rbind(a, b, c)

#Lines
pp = ggplot(data, aes(x = x, y = y)) +
  geom_hex(bins = 20, size = 0.5, color = "black") +
  scale_fill_viridis_c(option = "C")

par(mfrow = c(1, 2))
plot_gg(pp, width = 5, height = 4, scale = 300, raytrace = FALSE, preview = TRUE)
plot_gg(pp, width = 5, height = 4, scale = 300, multicore = TRUE, windowsize = c(1000, 800))
render_camera(fov = 70, zoom = 0.5, theta = 130, phi = 35)
Sys.sleep(0.2)
render_snapshot(clear = TRUE)

par(mfrow = c(1, 1))
plot_gg(pp, width = 5, height = 4, scale = 300, raytrace = FALSE, windowsize = c(1200, 960),
        fov = 70, zoom = 0.4, theta = 330, phi = 20,  max_error = 0.01, verbose = TRUE)
```


# 统计分析 T检验 回归

```r
install.packages('gapminder')
library(gapminder)

df=gapminder
# explore data

summary(df)
x = mean(df$lifeExp)
x

attach(df)
median(pop)
hist(lifeExp)
hist(log(pop))
boxplot(lifeExp ~ continent)
plot(lifeExp ~ gdpPercap)

# data operation
library(dplyr)
df %>%
  select(country, lifeExp) %>%
  filter(country=="South Africa" | country=="Ireland") %>%
  group_by(country) %>%
  summarise(aveLife=mean(lifeExp))


#T 检验
df1 = filter(df, country=="South Africa" | country=="Ireland")
df1$country = factor(df1$country)
t.test(data=df1, lifeExp ~ country)

boxplot(data=df1, lifeExp ~ country)

library(ggplot2)
ggplot(df1, aes(x=country, y=lifeExp)) +
  geom_boxplot()

# regression


ggplot(df, aes(x=log(gdpPercap), y=lifeExp, color=continent, size=pop)) +
  geom_point(alpha=0.3) + 
  geom_smooth()

summary(lm(lifeExp ~ gdpPercap, data=df))


res = lm(lifeExp ~ gdpPercap, data=df)

# lifeExp = 5.396 + 7.649e-04 gdpPercap

```
