import pandas as pd
from pku_law_selenium.actions import Init


def save2txt(filepath, content):
    # 保存文本到文件
    if content is not None:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
    else:
        print(f"ERROR:None filepath:{filepath} content:{str(content)}")


if __name__ == '__main__':
    link_csv = "dataset/law_data_2016-2020.csv"
    save_path = "E:/Law_AI/law_mining/dataset/txt"

    df = pd.read_csv(link_csv, encoding='gbk')
    total = len(df)
    t=0
    begin_i = 0
    for i in range(begin_i,total):
        import time
        t1 = time.time()

        # 获取df的内容
        name = df["标题"][i]
        caseid = df["案件字号"][i]
        url = df["原文链接"][i]
        end_date = df["审结日期"][i]
        txt_filename = f"{end_date}_{caseid}_{name}_{url.split('/')[-1][:-5]}.txt"

        # selenium 爬虫操作
        # 初始化网页
        init = Init(str_url=url)
        # 点击复制
        init.copy_fulltext()
        # 获取裁决书内容文本
        ft = init.get_fulltext()
        # 保存
        save2txt(save_path + '/' + txt_filename, ft)

        t2 = time.time()
        cost_time = t2 - t1
        t += cost_time
        print(f"{i + 1}>>>{txt_filename} \n 本次耗时：{cost_time}s 平均耗时：{t/(i+1-begin_i)}s")
    print(f"总耗时：{t}")

