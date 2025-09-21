#!/usr/bin/env python

import os
from urllib import parse

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER + "\n"

    problems = {}

    for root, dirs, files in os.walk("."):
        dirs.sort()

        if root == ".":
            for dir in (".git", ".github", "images"):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        path_parts = root.split(os.sep)

        if len(path_parts) < 4:
            continue

        # 예: baekjoon-coding/C++17/백준/Bronze
        language = path_parts[1]          # C++17, Java, Python 등
        site = path_parts[2]              # 백준 or 프로그래머스
        difficulty = path_parts[3]        # Bronze, Silver 등

        if language not in problems:
            problems[language] = {}
        if site not in problems[language]:
            problems[language][site] = {}
        if difficulty not in problems[language][site]:
            problems[language][site][difficulty] = []

        for file in files:
            # 불필요한 파일 제외
            if file.lower() == "readme.md":
                continue

            filename = os.path.splitext(file)[0]  # "11098.첼시를 도와줘!"
            number = filename.split(".")[0]       # "11098"
            link = parse.quote(os.path.join(root, file))
            problems[language][site][difficulty].append((number, link))

    # 출력 파트
    for language in sorted(problems.keys()):
        content += f"## 🖥️ {language}\n\n"
            for difficulty in sorted(problems[language][site].keys()):
                content += f"### ⭐️ {difficulty}\n"
                content += "| 문제번호 | 문제이름 | 링크 |\n"
                content += "| -------- | -------- | ---- |\n"
                for number, title, link in sorted(problems[language][site][difficulty]):
                    content += f"| {number} | {title} | [링크]({link}) |\n"
                content += "\n"

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
