import autogen
from config import LLM_CONFIG

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

proof_reader = autogen.AssistantAgent(
    name="ProofReader",
    is_termination_msg=termination_msg,
    system_message="""You are a Proof Reader. You make sure that the article is properly written with code and examples. Rewrite the final article provided to you by ArticleWriter with your suggestions added to it. Make sure the final response that you give should be in JSON format so that it can be rendered in the UI. It should follow an example structure given below:
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
                \},
                \{
                    "ListItem": "The arrays' sizes that comprise their rank should be identical. If the dimension of the arrays is not the same or if one of them is not one, this throws a ValueError indicating that the arrays have incompatible shapes."
                \}
            \]
        \},
        \{
            "Heading": "Python example of Numpy Broadcasting",
            "Content": "Let's illustrate this concept with a simple Python example.",
            "Code": \[
                \{
                    "CodeBlock": "import numpy as np\nA = np.array([1, 2, 3])\nB = np.array([2, 2, 2])\nC = A * B\nprint(C)"
                \},
                \{
                    "Content": "In this example, we're multiplying two arrays of identical shape, so broadcasting isn't necessary. However, observe what happens when we alter the second array:",
                    "CodeBlock": "B = 2\nC = A * B\nprint(C)"
                \},
                \{
                    "Content": "In this case, the scalar `B` is 'broadcast' across the array `A` during multiplication. Thus, broadcasting saves us from manually adjusting the shapes of our data structures to perform these operations."
                \},
                \{
                    "Content": "Now, let's look at a more complex example of broadcasting with two arrays of different shapes:",
                    "CodeBlock": "A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\nB = np.array([1, 0, 1])\nC = A + B\nprint(C)"
                \},
                \{
                    "Content": "In this example, the 1D array `B` is broadcast across the 2D array `A` in a way that it lines up with the last axis (from right to left) of `A`. As a result, even though these arrays do not have the same shape originally, we can still perform element-wise addition."
                \}
            \]
        \},
        \{
            "Content": "Understanding Numpy's broadcasting principle is a boon when performing operations on arrays of different shapes. This convenient feature speeds up your code and allows for a more intuitive numerical computation process. With broadcasting, Numpy once again solidifies its place as a must-have tool in your Python arsenal."
        \}
    \]
\}
Reply `TERMINATE` in the end when everything is done.""",
    llm_config=LLM_CONFIG,
    description="Proof Reeader who makes sure that the article is properly written with code and examples",
)
