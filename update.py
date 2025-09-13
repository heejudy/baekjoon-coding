#!/usr/bin/env python3

import os
from urllib import parse

HEADER = """# 📘 백준 & 프로그래머스 문제 풀이 목록

프로그래머스의 경우, 푼 문제 목록에 대한 마이그레이션이 필요합니다.

"""

def main():
    content = HEADER
    # 최상위 디렉토리 (백준, 프로그래머스)
    for site in sorted(os.listdir(".")):
        if site in [".git", ".github", "images", "__pycache__"]:
            continue
        if not os.path.isdir(site):
            continue

        content += f"\n## 📚 {site}\n"

        # 언어별 (Python, C++, Java 등)
        for lang in sorted(os.listdir(site)):
            lang_path = os.path.join(site, lang)
            if not os.path.isdir(lang_path):
                continue

            content += f"\n### 🚀 {lang}\n"

            # 난이도별 (Bronze, Silver, Gold ...)
            for level in sorted(os.listdir(lang_path)):
                level_path = os.path.join(lang_path, level)
                if not os.path.isdir(level_path):
                    continue

                content += f"\n#### 🎯 {level}\n"
                content += "| 문제번호 | 링크 |\n"
                content += "| ------- | ---- |\n"

                # 문제 파일들
                for file in sorted(os.listdir(level_path)):
                    file_path = os.path.join(level_path, file)
                    if os.path.isfile(file_path):
                        problem_num = os.path.splitext(file)[0]
                        link = parse.quote(file_path)
                        content += f"| {problem_num} | [링크]({link}) |\n"

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
