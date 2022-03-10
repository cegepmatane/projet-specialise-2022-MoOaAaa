import language_tool_python
tool = language_tool_python.LanguageTool('fr')

text = "Les fleurs mange le pot comme une chien."

matches = tool.check(text)
print(matches)