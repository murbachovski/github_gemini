import requests
import pandas as pd
from datetime import datetime

# GitHub API: 별 개수 기준으로 인기 저장소 10개 가져오기
url = "https://api.github.com/search/repositories"

def get_github_start(url):
    params = {
        "q": "stars:>50000",   # 별이 50,000개 이상인 저장소
        "sort": "stars",       # 별 개수 기준 정렬
        "order": "desc",       # 내림차순
        "per_page": 10         # 상위 10개
    }

    res = requests.get(url, params=params)
    data = res.json()

    # CSV 저장용 리스트
    repos_list = []

    for idx, repo in enumerate(data["items"], start=1):
        print(f"{idx}. {repo['full_name']} ⭐ {repo['stargazers_count']}")
        print(f"   URL: {repo['html_url']}")
        print(f"   설명: {repo['description']}\n")

        repos_list.append({
            "Rank": idx,
            "Name": repo["full_name"],
            "Stars": repo["stargazers_count"],
            "URL": repo["html_url"],
            "Description": repo["description"]
        })
    
    # 현재 날짜와 시간(YYYYMMDD_HHMM 형식)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    # Pandas DataFrame으로 변환 후 CSV 저장
    filename = f"top_github_repos_{timestamp}.csv"
    df = pd.DataFrame(repos_list)
    df.to_csv(filename, index=False, encoding="utf-8-sig")

    print(f"✅ 인기 GitHub 저장소 목록이 '{filename}' 파일로 저장되었습니다.")
        
    return repos_list

if __name__ == "__main__":
    get_github_start(url)
