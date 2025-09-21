#!/usr/bin/env python

import os
from urllib import parse
import re

HEADER = """#
# 백준, 프로그래머스 문제 풀이 목록
"""

def extract_number_and_title(name):
    """
    '1234. 문제이름' → (1234, 문제이름)
    '문제이름' → ("", 문제이름)
    '1234' → ("", 1234)  # 숫자만 있으면 이름 취급
    """
    if re.match(r"^\d+\.", name):  # "1234.문제"
        number, title = name.split(".", 1)
        return number, title.strip()
    elif name.isdigit():  # "1234" → 이름 취급
        return "", name
    else:  # 그냥 제목
        return "", name


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

        language = path_parts[1]     # C++17, Java, Python 등
        difficulty = path_parts[3]   # Bronze, Silver 등
        problem_dir = path_parts[-1] # "11718. 그대로 출력하기"

        # 디렉토리에서 번호 + 제목 뽑기
        dir_number, dir_title = extract_number_and_title(problem_dir)

        if language not in problems:
            problems[language] = {}
        if difficulty not in problems[language]:
            problems[language][difficulty] = []

        for file in files:
            if file.lower() == "readme.md":
                continue

            filename = os.path.splitext(file)[0]  # 확장자 제거
            file_number, file_title = extract_number_and_title(filename)

            # 우선순위: 디렉토리 정보 > 파일 정보
            number = dir_number if dir_number else file_number
            title = dir_title if dir_title else file_title

            link = parse.quote(os.path.join(root, file))
            problems[language][difficulty].append((number, title, link))


    # 출력
    languages = sorted(problems.keys())
    # Python을 맨 위로
    if "Python" in languages:
        languages.remove("Python")
        languages = ["Python"] + languages

    for language in languages:
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
