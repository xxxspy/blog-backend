
---

title: JSON-Schema介绍和入门
date: 2019-10-31 12:44:03
tags: [JSONSchema ]

---

JSON Schema 是对json数据进行数据结构描述的一个协议, 我们按照协议的规定, 可以对json数据结构进行描述, 也可以验证json数据。

在很多json编辑器中会用到json schema进行数据有效性的验证。

<!-- more -->

### 简介

JSON Schema是一个词汇表，可用于注释和验证JSON文档。

具体来说他们有如下作用:

- 描述您现有的数据格式。
- 提供清晰的人类和机器可读文档。
- 验证对以下有用的数据：
- 自动化测试。
- 确保客户提交数据的质量。



### 前言

以下示例绝不是JSON Schema可以提供的所有值的最终定义。因此，你需要深入了解有关JSON schema更多信息，请访问http://json-schema.org/specification.html。

假设我们正在与基于JSON的产品目录数据进行交互。该数据包含以下属性：

- 标识符：productId
- 产品名称：productName
- 消费者的销售成本：price
- 一组可选标签：tags。

我们的json数据看起来是这样的:

```json
{
  "productId": 1,
  "productName": "A green door",
  "price": 12.50,
  "tags": [ "home", "green" ]
}
```

看到这个数据的案例, 我们会产生很多疑问, 比如:

- 什么是productId？
- productName是必须的吗？
- 价格可以为零（0）吗？
- 所有的标签tags都是字符串值吗？

在谈论数据格式时，你会希望有一个元数据来描述他们，包括这些键的有效输入。 JSON Schema是一个提议的IETF标准，该标准可以帮助你回答上面的问题。



### 开始第一个schema

下面是一个schema的例子:

```json
{
  "`$schema": "http://json-schema.org/draft-07/schema#",
  "$`id": "http://example.com/product.schema.json",
  "title": "Product",
  "description": "A product in the catalog",
  "type": "object"
}
```


schema是一个json对象, 它有很多属性, 也叫做关键词, 例如:

- ``$schema`关键字指出此schema是根据标准的特定标准编写的，出于各种原因（主要是版本控制）而使用, 直白来说, 你根据什么规则写的schema。
- `$`

### 描述产品目录json数据

上面我们举了一个产品的json数据的例子:

```json
{
  "productId": 1,
  "productName": "A green door",
  "price": 12.50,
  "tags": [ "home", "green" ]
}
```

它对应的schema是这样的:

```json
{
  "`$schema": "http://json-schema.org/draft-07/schema#",
   "$`

### 嵌套的数据结构

到目前为止，我们一直在处理一个非常扁平的schema-仅一个级别。本节演示嵌套数据结构。

现在, 我们的商品信息需要增加一个属性"dimensions", 也就是商品的尺寸, 所以我们在properties中可以增加这样一个定义:

```JSON
    "dimensions": {
      "type": "object",
      "properties": {
        "length": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        }
      }
```

我们的dimensions属性的数据格式也是一个object, 它也包含properties, 所以定义了三个properties, 分别是: length, width, height, 他们的数据格式都是number。

### 引用外部的schema

到目前为止，我们的 JSON schema 都是自我包含的, 没有外部的引用。为了重用，可读性和可维护性，在许多数据结构之间共享 JSON schema 是很常见的。

在此示例中，我们引入了一个新的JSON schema, 这个数据结构定义的是一个地点, 它有经度和维度这两个属性：

```JSON
{
  "`$id": "https://example.com/geographical-location.schema.json",
  "$`schema": "http://json-schema.org/draft-07/schema#",
  "title": "Longitude and Latitude",
  "description": "A geographical coordinate on a planet (most commonly Earth).",
  "required": [ "latitude", "longitude" ],
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number",
      "minimum": -90,
      "maximum": 90
    },
    "longitude": {
      "type": "number",
      "minimum": -180,
      "maximum": 180
    }
  }
}
```


下面我们定义一个新的schema, 在其中我们会引用上面的schema, 上面的schema就是一个地点的数据结构, 下面的schema中用到的地点, 所以就直接引用上面的schema:

```JSON
{
  "`$schema": "http://json-schema.org/draft-07/schema#",
  "$`id": "http://example.com/product.schema.json",
  "title": "Product",
  "description": "A product from Acme's catalog",
  "type": "object",
  "properties": {
    "productId": {
      "description": "The unique identifier for a product",
      "type": "integer"
    },
    "productName": {
      "description": "Name of the product",
      "type": "string"
    },
    "price": {
      "description": "The price of the product",
      "type": "number",
      "exclusiveMinimum": 0
    },
    "tags": {
      "description": "Tags for the product",
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "uniqueItems": true
    },
    "dimensions": {
      "type": "object",
      "properties": {
        "length": {
          "type": "number"
        },
        "width": {
          "type": "number"
        },
        "height": {
          "type": "number"
        }
      },
      "required": [ "length", "width", "height" ]
    },
    "warehouseLocation": {
      "description": "Coordinates of the warehouse where the product is located.",
      "`$ref": "https://example.com/geographical-location.schema.json"
    }
  },
  "required": [ "productId", "productName", "price" ]
}

```

在上面的schema中, 我们定义了一个warehouseLocation属性, 这个属性有一个`$`

### 数据的真实面目

上面一大堆都是为了定义一个json数据结构, 下面我们来看一下一个真实的json数据, 结合上面的schema, 你基本就能使用json schema定义你自己的数据结构了。

```json
  {
    "productId": 1,
    "productName": "An ice sculpture",
    "price": 12.50,
    "tags": [ "cold", "ice" ],
    "dimensions": {
      "length": 7.0,
      "width": 12.0,
      "height": 9.5
    },
    "warehouseLocation": {
      "latitude": -78.75,
      "longitude": 20.4
    }
  }
```


> **注意**
> 本文由jupyter notebook转换而来, 您可以在这里下载[notebook](JSON Schema介绍和入门.ipynb)
> 有问题可以直接在下方留言
> 或者给我发邮件675495787[at]qq.com
> 请记住我的网址: mlln.cn 或者 jupyter.cn
