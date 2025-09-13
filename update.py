#!/usr/bin/env python

import os
from urllib import parse

HEADER = """# 📚 백준 & 프로그래머스 문제 풀이 목록

프로그래머스의 경우, 푼 문제 목록에 대한 마이그레이션이 필요합니다.

"""

def main():
    """
    폴더 구조를 순회하며 README.md 파일을 생성합니다.
    언어 -> 난이도 -> 문제 번호 순서로 문제 목록을 정리합니다.
    """
    
    content = HEADER
    
    # 문제 데이터를 언어, 플랫폼, 난이도별로 저장할 딕셔너리
    problems = {}
    
    # .git, .github 등 제외할 폴더 목록
    ignore_dirs = {'.git', '.github', '.idea', '__pycache__', 'images'}

    # 현재 디렉토리부터 하위 폴더를 순회
    for root, dirs, files in os.walk("."):
        # 불필요한 폴더는 순회 대상에서 제외
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        # 파일이 없는 폴더는 건너뜁니다.
        if not files:
            continue
        
        # 폴더 경로를 분석하여 언어, 플랫폼, 난이도를 추출
        # 예시: ./C++/백준/Silver -> ['', 'C++', '백준', 'Silver']
        parts = root.strip(os.sep).split(os.sep)

        # 최소한 '언어/플랫폼/난이도' 구조를 가져야 합니다.
        if len(parts) < 3:
            continue
            
        language = parts[0]
        platform = parts[1]
        difficulty = parts[2]
        
        # 문제가 있는 폴더는 보통 문제 번호로 되어있습니다.
        # 폴더 이름이 숫자인 경우에만 문제로 간주합니다.
        try:
            problem_number = int(os.path.basename(root))
        except ValueError:
            continue
            
        # 문제 파일의 경로를 가져옵니다. 여러 파일이 있을 수 있으므로 첫 번째 파일만 사용합니다.
        file_path = os.path.join(root, files[0])

        # problems 딕셔너리에 데이터 정리
        if language not in problems:
            problems[language] = {}
        if platform not in problems[language]:
            problems[language][platform] = {}
        if difficulty not in problems[language][platform]:
            problems[language][platform][difficulty] = []
            
        problems[language][platform][difficulty].append((problem_number, file_path))
        
    # 정리된 데이터를 바탕으로 Markdown 파일 내용 생성
    # 언어별로 정렬
    for language in sorted(problems.keys()):
        content += f"\n## 💻 {language}\n"
        
        for platform in sorted(problems[language].keys()):
            content += f"\n### 📚 {platform}\n"

            # 난이도별로 정렬 (Bronze, Silver, Gold 순서)
            difficulty_order = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond']
            sorted_difficulties = sorted(problems[language][platform].keys(), key=lambda d: difficulty_order.index(d) if d in difficulty_order else len(difficulty_order))

            for difficulty in sorted_difficulties:
                content += f"\n#### ⭐️ {difficulty}\n"
                content += "| 문제 번호 | 링크 |\n"
                content += "| :--- | :--- |\n"
                
                # 문제 번호별로 정렬
                for problem_number, file_path in sorted(problems[language][platform][difficulty]):
                    # URL 인코딩을 통해 한글 파일 경로도 링크로 사용 가능하게 만듭니다.
                    encoded_path = parse.quote(file_path)
                    content += f"| {problem_number} | [문제 풀이]({encoded_path}) |\n"
    
    # README.md 파일에 내용 쓰기
    with open("README.md", "w", encoding='utf-8') as fd:
        fd.write(content)
    
    print("README.md 파일이 성공적으로 생성되었습니다.")

if __name__ == "__main__":
    main()
