SYSTEM_PROMPT = """
你是一位专业英语老师。

请分析学生的错题。

请严格按照以下JSON格式返回：

{
  "error_type": "",
  "reason": "",
  "suggestion": ""
}

不要输出JSON以外的其他内容。
"""


def create_prompt(question, student_answer, correct_answer):
    prompt = f"""
题目：
{question}

学生答案：
{student_answer}

正确答案：
{correct_answer}

请分析这道题。
"""

    return prompt