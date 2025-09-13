#!/usr/bin/env python

import os
from urllib import parse

HEADER = """# 📘 알고리즘 문제 풀이 모음

백준 & 프로그래머스 문제 풀이 목록입니다.  
(프로그래머스의 경우, 푼 문제 목록에 대한 마이그레이션이 필요합니다.)

"""

def main():
    content = HEADER
    root_dirs = ["백준", "프로그래머스"]

    for root_dir in root_dirs:
        if not os.path.exists(root_dir):
            continue

        content += f"\n## 📚 {root_dir}\n"

        # 언어별
        for lang in sorted(os.listdir(root_dir)):
            lang_path = os.path.join(root_dir, lang)
            if not os.path.isdir(lang_path):
                continue

            content += f"\n### 💻 {lang}\n"

            # 난이도별
            for level in sorted(os.listdir(lang_path)):
                level_path = os.path.join(lang_path, level)
                if not os.path.isdir(level_path):
                    continue

                content += f"\n#### 🏅 {level}\n"
                content += "| 문제번호 | 링크 |\n"
                content += "| ------ | ----- |\n"

                for file in sorted(os.listdir(level_path)):
                    problem_id = os.path.splitext(file)[0]
                    file_path = parse.quote(os.path.join(level_path, file))
                    content += f"| {problem_id} | [풀이]({file_path}) |\n"

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
