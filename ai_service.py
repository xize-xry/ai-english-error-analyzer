import json


def call_deepseek(client, system_prompt, prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("调用DeepSeek失败：", e)
        return None


def parse_result(answer):
    try:
        return json.loads(answer)

    except json.JSONDecodeError:
        print("模型返回格式错误")
        print("原始回答：")
        print(answer)

        return None