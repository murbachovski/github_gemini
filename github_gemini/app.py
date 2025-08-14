from google import genai
import pandas as pd
from get_api import get_github
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
from rich import box
from termcolor import colored
import pyfiglet
from datetime import datetime

console = Console()

# ==============================
# 1️⃣ 터미널 제목 표시
# ==============================
title = pyfiglet.figlet_format("GitHub Daily Bot", font="slant")
console.print(colored(title, "cyan"))

# ==============================
# 2️⃣ GitHub 데이터 가져오기
# ==============================
url = get_github.url
console.print("[bold yellow]▶ GitHub 인기 저장소 수집 중...[/bold yellow]")

try:
    github_data = get_github.get_github_start(url)
    df = pd.DataFrame(github_data)  # 리스트 → DataFrame
    console.print(f"[green]✅ {len(df)}개의 저장소 데이터를 성공적으로 가져왔습니다.[/green]")
except Exception as e:
    console.print(f"[red]❌ GitHub 데이터 수집 실패: {e}[/red]")
    exit(1)

# ==============================
# 3️⃣ 수집 데이터 테이블 출력
# ==============================
table = Table(title="GitHub Top 10 인기 저장소", box=box.DOUBLE_EDGE, show_lines=True)
table.add_column("Rank", style="bold magenta")
table.add_column("Name", style="bold cyan")
table.add_column("Stars", justify="right", style="yellow")
table.add_column("URL", style="green")
table.add_column("Description", style="white")

for idx, row in df.iterrows():
    table.add_row(str(row["Rank"]), row["Name"], str(row["Stars"]), row["URL"], str(row["Description"]))

console.print(table)

# ==============================
# 4️⃣ Gemini 분석
# ==============================
console.print("[bold yellow]\n▶ Gemini 분석 시작...[/bold yellow]")
GENAI_API_KEY = ""
client = genai.Client(api_key=GENAI_API_KEY)

data_records = df.to_dict(orient="records")

prompt = f"""
다음은 GitHub 인기 저장소 10개의 정보입니다.
- 1. 데이터를 분석해서 어떤 유형의 프로젝트가 인기를 끄는지 간략히 설명해줘
- 2. 언어, 분야, 목적, 특징 위주로 간략히 요약해줘.
- 3. 어떤 공부를 하면 좋을지 간략히 추천해줘.
- 4. 앞으로의 프로그래밍 방향성에 대해서 간략히 요약해줘.

데이터:
{data_records}
"""

try:
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    analysis_result = resp.text
except Exception as e:
    console.print(f"[red]❌ Gemini 분석 실패: {e}[/red]")
    analysis_result = None

# ==============================
# 5️⃣ 분석 결과 출력
# ==============================
if analysis_result:
    md = Markdown(analysis_result)
    panel = Panel(md, title="Gemini 분석 결과", subtitle=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                  border_style="bright_blue", expand=True)
    console.print(panel)

# ==============================
# 6️⃣ 디버깅 출력 (원본 데이터 일부)
# ==============================
# console.print("[bold yellow]\n▶ 디버깅: 수집 원본 데이터 샘플[/bold yellow]")
# console.print(df.head(3).to_dict(orient="records"))
