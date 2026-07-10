from ollama import chat

MODEL_NAME = "qwen2.5-coder:7b"


def stream_response(system_prompt, user_prompt):

    stream = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        stream=True,
    )

    response = ""

    for chunk in stream:
        content = chunk["message"]["content"]
        response += content
        yield response