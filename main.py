from config import create_client
from prompts import create_prompt, SYSTEM_PROMPT
from ai_service import call_deepseek, parse_result


def show_result(result):
    print("错误类型：", result.get("error_type", "未知"))
    print("错误原因：", result.get("reason", "未知"))
    print("改进建议：", result.get("suggestion", "暂无建议"))


def main():
    client = create_client()

    question = input("请输入题目：")
    student_answer = input("请输入学生答案：")
    correct_answer = input("请输入正确答案：")

    if not question.strip():
        print("题目不能为空")
        return

    if not student_answer.strip():
        print("学生答案不能为空")
        return

    if not correct_answer.strip():
        print("正确答案不能为空")
        return

    prompt = create_prompt(
        question,
        student_answer,
        correct_answer
    )

    answer = call_deepseek(
        client,
        SYSTEM_PROMPT,
        prompt
    )

    if not answer:
        return

    result = parse_result(answer)

    if not result:
        return

    show_result(result)


if __name__ == "__main__":
    main()