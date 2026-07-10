def build_llm_context(context):

    tree = "\n".join(context["tree"][:100])   # first 100 entries only

    dependencies = ""

    for path, content in context["dependencies"].items():
        dependencies += f"\n### {path}\n{content[:1000]}\n"

    source_code = ""

    count = 0
    for path, content in context["source_files"].items():

        source_code += f"""
### {path}

{content[:2000]}
"""

        count += 1
        if count == 3:
            break

    return f"""
Repository Name:
{context['repo']}

Owner:
{context['owner']}

Language:
{context['language']}

README:
{context['readme'][:2000]}

Folder Structure:
{tree}

Dependencies:
{dependencies}

Important Source Files:
{source_code}
"""