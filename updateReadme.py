import textwrap
import datetime

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
date = now.strftime('%Y/%m/%d %I:%M:%S.%f(%p)')

docs_str = textwrap.dedent('''
[![Domain Renewal](https://github.com/2288-256-sub/2288-256-sub.github.io/actions/workflows/main.yml/badge.svg)](https://github.com/2288-256-sub/2288-256-sub.github.io/actions/workflows/main.yml)

## 概要
TwitterのURL欄に表示しているURLのリポジトリ

## IP最終更新日
{da}
''').format(da=date).strip()

with open('README.md', 'w') as f:
    f.write(docs_str)
