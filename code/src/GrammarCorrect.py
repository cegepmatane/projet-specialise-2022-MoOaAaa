import language_tool_python

class GrammarCorrect:



    def __init__(self, lang):
        self.tool = language_tool_python.LanguageTool(lang)

    def check(self, text):
        return self.tool.check(text)

    def correct(self, text):
        return self.tool.correct(text)

text = "Les fleurs mange le pot comme une chien."

# matches = tool.check(text)
# print(matches)