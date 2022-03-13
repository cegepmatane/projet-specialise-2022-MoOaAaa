import language_tool_python

class GrammarCorrect:

    tool = language_tool_python.LanguageTool('fr')

    def correct(self, text):
        return self.tool.check(text)

text = "Les fleurs mange le pot comme une chien."

# matches = tool.check(text)
# print(matches)