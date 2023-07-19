import argparse
import json
import random
import sys


def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-a", "--article", type=int, help="指定文章的编号（从0开始）")
    parser.add_argument("-l", "--language", default='zh', help="题库语言，默认为'zh'")

    args = parser.parse_args()
    return args


def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        keys.append(input())

    return keys


def replace(article, keys):
    for i, key in enumerate(keys):
        article = article.replace(f"{{{{{i + 1}}}}}", key)
    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)

    # 筛选相应语言的文章
    articles = [article for article in data["articles"]]

    if not articles:
        print(f"没有找到语言为 {args.language} 的文章")
        sys.exit()


    # 如果用户指定了文章，选择用户指定的文章，否则随机选择一篇文章
        article = articles[args.article]
    else:
        article = random.choice(articles)

    print(f"选择的文章是：{article['title']}")

    # 给出提示，获取用户的输入，替换文章中的词汇，并输出结果
    keys = get_inputs(article['hints'])
    filled_article = replace(article['article'], keys)

    print(f"填词后的文章是：\n{filled_article}")

