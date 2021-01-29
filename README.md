# Law_Mining 法律数据挖掘
[TOC]

- 文书数据爬取
- 数据清洗、抽取与集成
- 文本挖掘及可视化分析

## Part 1 - 文书数据爬取

原始数据集是从北大法宝爬取的2016年3月1日到2020年12月30日期间案件类型为人身安全保护令的裁判文书数据，其中包含4442份裁定书文本及对应标签。

格式如下：

| 标题                 | 审理程序 | 案由     | 文书类型 | 审理法院                                                   | 案件字号              | 审结日期   | 省份   | 案件类型 | 原文链接                                                     |
| -------------------- | -------- | -------- | -------- | ---------------------------------------------------------- | --------------------- | ---------- | ------ | -------- | ------------------------------------------------------------ |
| 赵某与陈某离婚纠纷案 | 简易程序 | 离婚纠纷 | 裁定书   | 江苏省淮安市清浦区人民法院（原江苏省淮阴市清浦区人民法院） | (2016)苏0811民保令1号 | 2016.03.01 | 江苏省 | 民事     | https://www.pkulaw.com/pfnl/a25051f3312b07f347c2beea0f7a2926b2707a013b55efafbdfb.html |
| ...                  | ...      | ...      | ...      | ...                                                        | ...                   | ...        | ...    | ...      | ...                                                          |


+ 目标数据检索收集

在北大法宝按关键词检索下载对应的excel文件，每次一百条数据，人工将excel进行格式化处理后导出为csv文件（注意编码格式为GBK），通过运行 utils 文件夹下的 df_concat.py 把各个csv文件合并成一个文件
方便爬虫爬取原链接对应文本内容。

+ 数据爬取

安装对应本地 chrome 浏览器版本的 selenium 驱动放到 pku_law_selenium/drivers 目录下，在 configs.py 配置好 selenium（可选择无头浏览器，但是比较慢），编辑路径，运行 pku_law_spider.py 开始爬取。



## Part 2 - 数据清洗、抽取与集成

使用基于规则匹配的方法进行数据清洗和抽取，得到关键数据集成到csv数据集中便于后续分析。



+ 文本预处理

对爬取的源数据进行数据清洗，去除"书记员 XXX"下面所有附加的法条内容。

+ 法律称谓标准化（暂未实现）

对申请人、被申请人、代理人等的称谓标准化，删除审理员、书记员，减小不同称谓对文本分析的影响。

+ 数据抽取与标签构建

1. 根据裁定结果关键词判断申请是否同意、撤销、驳回或延长。

匹配条件：

禁止被申请人*实施家庭暴力

人身安全保护令失效前

如被申请人*违反上述禁令



2. 是否为代申请

匹配条件：


3. 是否有证据、证据数量和来源

匹配条件：


4. 是否有妇联、村委、居委材料

匹配条件：


5. 请求措施或裁定结果

匹配条件：

```angular2
第二十九条　人身安全保护令可以包括下列措施：
　　（一）禁止被申请人实施家庭暴力；
　　（二）禁止被申请人骚扰、跟踪、接触申请人及其相关近亲属；
　　（三）责令被申请人迁出申请人住所；
　　（四）保护申请人人身安全的其他措施。
```



6. 说理内容及丰富程度

匹配条件：





## Part 3 - 文本挖掘及可视化分析




+ 词频分析及可视化

每月申请数量可视化

+ 关联分析
+ 裁决规律挖掘
+ 训练词向量
+ 聚类可视化
+ 