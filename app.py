import gradio as gr

from repo_parser import build_repository_context
from advancements.state import AgentState
from analyzer import generate_readme, find_bugs, review_repository


def analyze_repository(repo_url, user_prompt, feature):
    try:
        if not repo_url.strip():
            yield "❌ Please provide a GitHub repository URL."
            return

        context = build_repository_context(repo_url)

        state = AgentState(
            repo_url=repo_url,
            user_prompt=user_prompt,
            context=context,
        )

        if feature == "README Generator":
            state.current_tool = "README Generator"
            yield from generate_readme(state)

        elif feature == "Bug Finder":
            state.current_tool = "Bug Finder"
            yield from find_bugs(state)

        elif feature == "Repository Reviewer":
            state.current_tool = "Repository Reviewer"
            yield from review_repository(state)

        else:
            yield "❌ Invalid feature selected."

    except Exception as e:
        yield f"""# ❌ Analysis Failed

An error occurred while analyzing the repository.

### Error
```text
{e}
```"""


repo_input = gr.Textbox(
    label="GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

prompt_input = gr.Textbox(
    label="Additional Instructions",
    placeholder="Optional instructions...",
    lines=4
)

feature_selector = gr.Dropdown(
    choices=[
        "README Generator",
        "Bug Finder",
        "Repository Reviewer"
    ],
    value="README Generator",
    label="Feature"
)

output = gr.Markdown(label="Analysis")

view = gr.Interface(
    fn=analyze_repository,
    title="🚀 GitHub Repository Analyzer",
    description="""
Analyze GitHub repositories using AI.

Choose a feature, enter the repository URL,
optionally provide additional instructions,
and let the AI analyze the project.
""",
    inputs=[
        repo_input,
        prompt_input,
        feature_selector,
    ],
    outputs=output,
    examples=[
        [
            "https://github.com/huggingface/transformers",
            "Generate a professional README for this project.",
            "README Generator",
        ],
        [
            "https://github.com/pallets/flask",
            "Find possible bugs and suggest fixes.",
            "Bug Finder",
        ],
        [
            "https://github.com/gradio-app/gradio",
            "Review the overall project structure and code quality.",
            "Repository Reviewer",
        ],
        [
            "https://github.com/psf/requests",
            "Generate a concise, beginner-friendly README.",
            "README Generator",
        ],
    ],
    flagging_mode="never",
)

view.queue()
view.launch(share=True)