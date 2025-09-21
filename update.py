#!/usr/bin/env python

import os
from urllib import parse
import re

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
        difficulty = path_parts[3]        # Bronze, Silver 등

        if language not in problems:
            problems[language] = {}
        if difficulty not in problems[language]:
            problems[language][difficulty] = []

        for file in files:
            if file.lower() == "readme.md":
                continue

            filename = os.path.splitext(file)[0]  # 확장자 제거
            # 파일명에서 숫자(문제번호)와 제목 분리
            match = re.match(r"^(\d+)(?:[.\s]+(.+))?$", filename)
            if match:
                number = match.group(1)
                title = match.group(2) if match.group(2) else ""
            else:
                number, title = "", filename  # 숫자 없는 경우

            link = parse.quote(os.path.join(root, file))
            problems[language][difficulty].append((number, title, link))

    # 출력 파트
    for language in sorted(problems.keys()):
        content += f"## 🖥️ {language}\n\n"
        for difficulty in sorted(problems[language].keys()):
            content += f"### ⭐ {difficulty}\n"
            content += "| 문제번호 | 문제이름 | 링크 |\n"
            content += "| -------- | -------- | ---- |\n"
            for number, title, link in sorted(problems[language][difficulty]):
                content += f"| {number} | {title} | [링크]({link}) |\n"
            content += "\n"

    with open("README.md", "w", encoding="utf-8") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
