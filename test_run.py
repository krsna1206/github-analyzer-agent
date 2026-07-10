from analyzer import Analyzer

analyzer = Analyzer()

result = analyzer.analyze(
    repo_url="https://github.com/pallets/flask",
    user_prompt="Generate README"
)

for chunk in result:
    print(chunk, end="")