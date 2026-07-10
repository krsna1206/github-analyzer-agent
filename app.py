import gradio as gr

from repo_parser import build_repository_context

from analyzer import (
    generate_readme,
    find_bugs,
    review_repository,
)


def analyze_repository(repo_url, user_prompt, feature):

    context = build_repository_context(repo_url)

    if feature == "README Generator":
        yield from generate_readme(context, user_prompt)

    elif feature == "Bug Finder":
        yield from find_bugs(context, user_prompt)

    elif feature == "Repository Reviewer":
        yield from review_repository(context, user_prompt)

    try:
        context = build_repository_context(repo_url)

    except Exception as e:
        yield f"❌ Unable to load repository.\n\n{e}"
        return
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
         ]
    ],

    flagging_mode="never",
)

view.launch(share=True)