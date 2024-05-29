import autogen
from config import LLM_CONFIG

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

article_writer = autogen.AssistantAgent(
    name="ArticleWriter",
    is_termination_msg=termination_msg,
    system_message="""You are a technical blog writer, you write an article on the topics provided by TopicsGenerator. Each topic should be written with a simple example. Make sure the final response that you give should be in JSON format so that it can be rendered in the UI. It should follow an example structure given below:
     \{
    "Title":"Unraveling Numpy Broadcasting With Clear Examples",
    "Body":\[
        \{
            "Content": "In the vibrant world of Python programming, Numpy stands as a fundamental library that empowers its users with extensive mathematical capabilities. Among these wonderful features of Numpy, a little appreciated yet pivotal one is 'Broadcasting'. This article will vividly explain and illustrate this fairly perplexing aspect of Numpy."
        \},
        \{
            "Heading": "What is Numpy Broadcasting?",
            "Content": "Numpy broadcasting is a powerful feature that allows us to perform arithmetic operations on arrays of different shapes. This could be between a scalar and an array, or between arrays of different shapes, under certain conditions."
        \},
        \{
            "Content": "The concept behind broadcasting pivots on two rules:",
            "List": \[
                \{
                    "ListItem": "If the arrays do not have the same rank, then a 1 will be pre-pended to the smaller ranking array’s shape."
                \}
            \]
        \},
        \{
            "Heading": "Python example of Numpy Broadcasting",
            "Content": "Let's illustrate this concept with a simple Python example.",
            "Code": \[
                \{
                    "CodeBlock": "import numpy as np"
                    "CodeBlock": "A = np.array([1, 2, 3])"
                    "CodeBlock": "B = np.array([2, 2, 2])"
                \},
                \{
                    "Content": "In this example, we're multiplying two arrays of identical shape, so broadcasting isn't necessary. However, observe what happens when we alter the second array:",
                    "CodeBlock": "B = 2"
                \}
            \]
        \}
    \]
\}
No escape sequences in the final json to be used.
""",
    llm_config=LLM_CONFIG,
    description="technical blog writer who writes article on the list of topics provided",
)
