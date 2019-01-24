
---
title: pandas练习-多层索引的创建和各种操作(multiindex)第二部分
date: 2019-01-24 20:17:55
tags: [pandas]
toc: true
xiongzhang: true
xiongzhang_images: [main.jpg]

---

<span></span>
<!-- more -->

### 使用切片(slicers)

你可以使用切片来选择MultiIndex, `slice`是python内置的函数(其实是一个类), 他的用法是这样的:


```python
alist = list('abcdefg' * 3)
selector = slice(1, 6, 2)
alist[selector]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    ['b', 'd', 'f']

</div>
{% endraw %}



我们可以使用`slice`来选择MultiIndex。

下面先创建一个DataFrame:


```python
import pandas as pd
import numpy as np
def mklbl(prefix,n):
    return ["%s%s" % (prefix,i)  for i in range(n)]


miindex = pd.MultiIndex.from_product([mklbl('A',4),
                                     mklbl('B',2),
                                mklbl('C',4),
                                   mklbl('D',2)])


micolumns = pd.MultiIndex.from_tuples([('a','foo'),('a','bar'),
                                   ('b','foo'),('b','bah')],
                                 names=['lvl0', 'lvl1'])


dfmi = pd.DataFrame(np.arange(len(miindex)*len(micolumns)).reshape((len(miindex),len(micolumns))),
                  index=miindex,
                columns=micolumns).sort_index().sort_index(axis=1)

dfmi.head()
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">A0</th>
      <th rowspan="5" valign="top">B0</th>
      <th rowspan="2" valign="top">C0</th>
      <th>D0</th>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>2</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>5</td>
      <td>4</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>9</td>
      <td>8</td>
      <td>11</td>
      <td>10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>13</td>
      <td>12</td>
      <td>15</td>
      <td>14</td>
    </tr>
    <tr>
      <th>C2</th>
      <th>D0</th>
      <td>17</td>
      <td>16</td>
      <td>19</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



下面我们需要选择出MultiIndex第一层为A1或A2或A3, 第二层不做选择, 第三层只包括C1和C3的行:


```python
dfmi.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>73</td>
      <td>72</td>
      <td>75</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>77</td>
      <td>76</td>
      <td>79</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>89</td>
      <td>88</td>
      <td>91</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>93</td>
      <td>92</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>105</td>
      <td>104</td>
      <td>107</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>109</td>
      <td>108</td>
      <td>111</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>121</td>
      <td>120</td>
      <td>123</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>125</td>
      <td>124</td>
      <td>127</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>137</td>
      <td>136</td>
      <td>139</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>141</td>
      <td>140</td>
      <td>143</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>153</td>
      <td>152</td>
      <td>155</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>157</td>
      <td>156</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>169</td>
      <td>168</td>
      <td>171</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>173</td>
      <td>172</td>
      <td>175</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>185</td>
      <td>184</td>
      <td>187</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>189</td>
      <td>188</td>
      <td>191</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>201</td>
      <td>200</td>
      <td>203</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>205</td>
      <td>204</td>
      <td>207</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>217</td>
      <td>216</td>
      <td>219</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>221</td>
      <td>220</td>
      <td>223</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>233</td>
      <td>232</td>
      <td>235</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>237</td>
      <td>236</td>
      <td>239</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>249</td>
      <td>248</td>
      <td>251</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>253</td>
      <td>252</td>
      <td>255</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



你还可以使用`pandas.IndexSlic`类来实现类似的选择:


```python
idx = pd.IndexSlice

dfmi.loc[idx['A1': 'A3', :, ['C1', 'C3']], :]
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th colspan="2" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>bar</th>
      <th>foo</th>
      <th>bah</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>73</td>
      <td>72</td>
      <td>75</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>77</td>
      <td>76</td>
      <td>79</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>89</td>
      <td>88</td>
      <td>91</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>93</td>
      <td>92</td>
      <td>95</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>105</td>
      <td>104</td>
      <td>107</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>109</td>
      <td>108</td>
      <td>111</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>121</td>
      <td>120</td>
      <td>123</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>125</td>
      <td>124</td>
      <td>127</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>137</td>
      <td>136</td>
      <td>139</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>141</td>
      <td>140</td>
      <td>143</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>153</td>
      <td>152</td>
      <td>155</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>157</td>
      <td>156</td>
      <td>159</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>169</td>
      <td>168</td>
      <td>171</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>173</td>
      <td>172</td>
      <td>175</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>185</td>
      <td>184</td>
      <td>187</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>189</td>
      <td>188</td>
      <td>191</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>201</td>
      <td>200</td>
      <td>203</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>205</td>
      <td>204</td>
      <td>207</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>217</td>
      <td>216</td>
      <td>219</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>221</td>
      <td>220</td>
      <td>223</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>233</td>
      <td>232</td>
      <td>235</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>237</td>
      <td>236</td>
      <td>239</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>249</td>
      <td>248</td>
      <td>251</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>253</td>
      <td>252</td>
      <td>255</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



同样是上面的例子, 我们可以选择出列索引第二层为bar的列:


```python
dfmi.loc[idx['A1': 'A3', :, ['C1', 'C3']], idx[:, 'foo']]
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>foo</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>76</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>88</td>
      <td>90</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>92</td>
      <td>94</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>104</td>
      <td>106</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>108</td>
      <td>110</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>120</td>
      <td>122</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>124</td>
      <td>126</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A2</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>136</td>
      <td>138</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>140</td>
      <td>142</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>152</td>
      <td>154</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>156</td>
      <td>158</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>168</td>
      <td>170</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>172</td>
      <td>174</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>184</td>
      <td>186</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>188</td>
      <td>190</td>
    </tr>
    <tr>
      <th rowspan="8" valign="top">A3</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>200</td>
      <td>202</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>204</td>
      <td>206</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>216</td>
      <td>218</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>220</td>
      <td>222</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>232</td>
      <td>234</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>236</td>
      <td>238</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C3</th>
      <th>D0</th>
      <td>248</td>
      <td>250</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>252</td>
      <td>254</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



另外, 我们可以使用布尔的蒙版来配合`IndexSlice`选择数据, 下面我们选择出foo列的数值小于100的行:


```python
mask = (dfmi[('a', 'foo')] < 100) & (dfmi[('b', 'foo')] < 100)

dfmi.loc[idx[mask, :, ['C1', 'C2']], idx[:, 'foo']]
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl0</th>
      <th>a</th>
      <th>b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th>lvl1</th>
      <th>foo</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="8" valign="top">A0</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>12</td>
      <td>14</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>16</td>
      <td>18</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>20</td>
      <td>22</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">B1</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>40</td>
      <td>42</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>44</td>
      <td>46</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>48</td>
      <td>50</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>52</td>
      <td>54</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">A1</th>
      <th rowspan="4" valign="top">B0</th>
      <th rowspan="2" valign="top">C1</th>
      <th>D0</th>
      <td>72</td>
      <td>74</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>76</td>
      <td>78</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">C2</th>
      <th>D0</th>
      <td>80</td>
      <td>82</td>
    </tr>
    <tr>
      <th>D1</th>
      <td>84</td>
      <td>86</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 按索引聚合数据和数据对齐

在多层索引中, 我们可以依据某一层进行数据聚合, 比如求和, 求均值, 下面我们先来创建一个dataframe:


```python
midx = pd.MultiIndex(levels=[['zero', 'one'], ['x','y']],
                      labels=[[1,1,0,0],[1,0,1,0]])


df = pd.DataFrame(np.random.randn(4,2), index=midx)

df
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-0.634407</td>
      <td>0.272985</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.546991</td>
      <td>0.001771</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>1.801089</td>
      <td>-1.132311</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.213100</td>
      <td>2.339203</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



求第一层索引的均值:


```python
df2 = df.mean(level=0)
df2
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>one</th>
      <td>-0.590699</td>
      <td>0.137378</td>
    </tr>
    <tr>
      <th>zero</th>
      <td>1.007094</td>
      <td>0.603446</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



如果我们想用均值替换原先的所有值, 我们可以恢复到原始数据的形状和索引:


```python
df3 = df2.reindex(df.index, level=0)
df3
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-0.590699</td>
      <td>0.137378</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.590699</td>
      <td>0.137378</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>1.007094</td>
      <td>0.603446</td>
    </tr>
    <tr>
      <th>x</th>
      <td>1.007094</td>
      <td>0.603446</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



上面就是一个数据对齐的过程, df2的索引和df的索引按照第一层对齐, 也就是[one, zero]对齐, 假如不对齐, 我们会得到什么结果?


```python
df4 = df2.reindex(df.index)
df4
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>x</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>x</th>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



我们可以使用更直观的方式去对齐数据:


```python
df_a, df2_a = df.align(df2, level=0)
df2_a
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-0.590699</td>
      <td>0.137378</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.590699</td>
      <td>0.137378</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>1.007094</td>
      <td>0.603446</td>
    </tr>
    <tr>
      <th>x</th>
      <td>1.007094</td>
      <td>0.603446</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



需要注意的是, 上面的方法可能会更改df和df2, 所以有两个返回值。

### 交换多层索引的层序

直接看例子就好了, 对比交换前后的index:


```python
df
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>y</th>
      <td>-0.634407</td>
      <td>0.272985</td>
    </tr>
    <tr>
      <th>x</th>
      <td>-0.546991</td>
      <td>0.001771</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">zero</th>
      <th>y</th>
      <td>1.801089</td>
      <td>-1.132311</td>
    </tr>
    <tr>
      <th>x</th>
      <td>0.213100</td>
      <td>2.339203</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
df.swaplevel(0, 1, axis=0)
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>y</th>
      <th>one</th>
      <td>-0.634407</td>
      <td>0.272985</td>
    </tr>
    <tr>
      <th>x</th>
      <th>one</th>
      <td>-0.546991</td>
      <td>0.001771</td>
    </tr>
    <tr>
      <th>y</th>
      <th>zero</th>
      <td>1.801089</td>
      <td>-1.132311</td>
    </tr>
    <tr>
      <th>x</th>
      <th>zero</th>
      <td>0.213100</td>
      <td>2.339203</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



另外, 可以使用reorder_levels达到相同的目的, 只不过它可以一次性修改多层index的次序:


```python
df.reorder_levels([1, 0], axis=0)
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>y</th>
      <th>one</th>
      <td>-0.634407</td>
      <td>0.272985</td>
    </tr>
    <tr>
      <th>x</th>
      <th>one</th>
      <td>-0.546991</td>
      <td>0.001771</td>
    </tr>
    <tr>
      <th>y</th>
      <th>zero</th>
      <td>1.801089</td>
      <td>-1.132311</td>
    </tr>
    <tr>
      <th>x</th>
      <th>zero</th>
      <td>0.213100</td>
      <td>2.339203</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



### 排序

我们可以使用sort_index对索引进行排序。


```python
import random; 

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
          ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
 

tuples = list(zip(*arrays))
random.shuffle(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
s = pd.Series(np.random.randn(8), index=pd.MultiIndex.from_tuples(tuples))
s
```




{% raw %}
<div class="output">
输出(plain):<br/>

    baz  one    0.035299
    <br />foo  one   -1.021257
    <br />baz  two   -0.225705
    <br />foo  two   -0.369259
    <br />bar  one   -0.681788
    <br />     two    0.873609
    <br />qux  two    0.325956
    <br />     one   -1.330222
    <br />dtype: float64

</div>
{% endraw %}



默认情况下, sort_index可以逐层排序, 首先排level=0的层:


```python
s.sort_index()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    bar  one   -0.681788
    <br />     two    0.873609
    <br />baz  one    0.035299
    <br />     two   -0.225705
    <br />foo  one   -1.021257
    <br />     two   -0.369259
    <br />qux  one   -1.330222
    <br />     two    0.325956
    <br />dtype: float64

</div>
{% endraw %}



但是我们可以选择只对某一层排序:


```python
s.sort_index(level=1)
```




{% raw %}
<div class="output">
输出(plain):<br/>

    bar  one   -0.681788
    <br />baz  one    0.035299
    <br />foo  one   -1.021257
    <br />qux  one   -1.330222
    <br />bar  two    0.873609
    <br />baz  two   -0.225705
    <br />foo  two   -0.369259
    <br />qux  two    0.325956
    <br />dtype: float64

</div>
{% endraw %}



如果多层索引设置了names属性, 我们可以使用名称作为参数:


```python
s.index.names=['a', 'b']
s.sort_index(level='b')
```




{% raw %}
<div class="output">
输出(plain):<br/>

    a    b  
    <br />bar  one   -0.681788
    <br />baz  one    0.035299
    <br />foo  one   -1.021257
    <br />qux  one   -1.330222
    <br />bar  two    0.873609
    <br />baz  two   -0.225705
    <br />foo  two   -0.369259
    <br />qux  two    0.325956
    <br />dtype: float64

</div>
{% endraw %}




除了对索引进行排序, 我们还可以对DataFrame.columns排序, 先来看一下我们的数据:


```python
dft = df.T
dft
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">one</th>
      <th colspan="2" halign="left">zero</th>
    </tr>
    <tr>
      <th></th>
      <th>y</th>
      <th>x</th>
      <th>y</th>
      <th>x</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.634407</td>
      <td>-0.546991</td>
      <td>1.801089</td>
      <td>0.213100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.272985</td>
      <td>0.001771</td>
      <td>-1.132311</td>
      <td>2.339203</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}




```python
dft.sort_index(level=1, axis=1)
```




{% raw %}
<div class="output" contenteditable="true">
输出(html):<br>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>one</th>
      <th>zero</th>
      <th>one</th>
      <th>zero</th>
    </tr>
    <tr>
      <th></th>
      <th>x</th>
      <th>x</th>
      <th>y</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.546991</td>
      <td>0.213100</td>
      <td>-0.634407</td>
      <td>1.801089</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.001771</td>
      <td>2.339203</td>
      <td>0.272985</td>
      <td>-1.132311</td>
    </tr>
  </tbody>
</table>
</div>
</div>
{% endraw %}



index排序后有一个好处, 就是你可以使用切片来选择数据, 但是如果index没有排序, 你可能会遇到错误:


```python
s.loc[('baz', 'one' ): ('bar', 'one')]
```


    ---------------------------------------------------------------------------

    UnsortedIndexError                        Traceback (most recent call last)

    <ipython-input-62-4b4f60d21813> in <module>
    ----> 1 s.loc[('baz', 'one' ): ('bar', 'one')]
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexing.py in __getitem__(self, key)
       1476 
       1477             maybe_callable = com._apply_if_callable(key, self.obj)
    -> 1478             return self._getitem_axis(maybe_callable, axis=axis)
       1479 
       1480     def _is_scalar_access(self, key):
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexing.py in _getitem_axis(self, key, axis)
       1864         if isinstance(key, slice):
       1865             self._validate_key(key, axis)
    -> 1866             return self._get_slice_axis(key, axis=axis)
       1867         elif com.is_bool_indexer(key):
       1868             return self._getbool_axis(key, axis=axis)
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexing.py in _get_slice_axis(self, slice_obj, axis)
       1509         labels = obj._get_axis(axis)
       1510         indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop,
    -> 1511                                        slice_obj.step, kind=self.name)
       1512 
       1513         if isinstance(indexer, slice):
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexes\base.py in slice_indexer(self, start, end, step, kind)
       4105         """
       4106         start_slice, end_slice = self.slice_locs(start, end, step=step,
    -> 4107                                                  kind=kind)
       4108 
       4109         # return a slice
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexes\multi.py in slice_locs(self, start, end, step, kind)
       2144         # This function adds nothing to its parent implementation (the magic
       2145         # happens in get_slice_bound method), but it adds meaningful doc.
    -> 2146         return super(MultiIndex, self).slice_locs(start, end, step, kind=kind)
       2147 
       2148     def _partial_tup_index(self, tup, side='left'):
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexes\base.py in slice_locs(self, start, end, step, kind)
       4306         start_slice = None
       4307         if start is not None:
    -> 4308             start_slice = self.get_slice_bound(start, 'left', kind)
       4309         if start_slice is None:
       4310             start_slice = 0
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexes\multi.py in get_slice_bound(self, label, side, kind)
       2088         if not isinstance(label, tuple):
       2089             label = label,
    -> 2090         return self._partial_tup_index(label, side=side)
       2091 
       2092     def slice_locs(self, start=None, end=None, step=None, kind=None):
    

    d:\mysites\deeplearning.ai-master\.env\lib\site-packages\pandas\core\indexes\multi.py in _partial_tup_index(self, tup, side)
       2151                 'Key length (%d) was greater than MultiIndex'
       2152                 ' lexsort depth (%d)' %
    -> 2153                 (len(tup), self.lexsort_depth))
       2154 
       2155         n = len(tup)
    

    UnsortedIndexError: 'Key length (2) was greater than MultiIndex lexsort depth (0)'


我们可以使用is_lexsorted来判断是否经过了排序:


```python
s.index.is_lexsorted()
```




{% raw %}
<div class="output">
输出(plain):<br/>

    False

</div>
{% endraw %}




```python
ss = s.sort_index()
ss.loc[('bar', 'one' ): ('baz', 'one')]
```




{% raw %}
<div class="output">
输出(plain):<br/>

    a    b  
    <br />bar  one   -0.681788
    <br />     two    0.873609
    <br />baz  one    0.035299
    <br />dtype: float64

</div>
{% endraw %}




> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](pandas练习-多层索引的创建和各种操作(multiindex)第二部分.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
