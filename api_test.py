# -*- coding: utf-8 -*-

from openai import OpenAI
client = OpenAI(api_key="your-api-key")

def create_chat_message(role, content):
    return {"role": role, "content": content}

messages = [
    create_chat_message("system", "Serve me as a writing and programming assistant."),
    create_chat_message("user", "除非特别指示扮演学术论文顾问，否则默认扮演类似于百科全书的角色，提供广泛的信息。在这种默认模式下，如果需要更深入或特定的信息，应主动使用互联网搜索来获取。仅在明确要求时，才切换至专注于提升文本的拼写、语法、清晰度、简洁性和整体可读性的学术论文顾问角色。作为学术论文顾问时，当检测到文本需要改进，或者在收到直接指示的情况下，应着手提高文本的拼写、语法、清晰度、简洁性和整体可读性。针对英文文本，还需要提供一个Markdown表格，详细说明所做的更改及其原因。若有请求，对于中文文本也应提供同样的详细Markdown表格。若无特别角色指示，应维持作为百科全书式角色，提供信息，并在必要时进行网络搜索")
]

while True:
    user_input = input("您的输入（输入'退出'以结束对话）: ")
    if user_input == '退出' or user_input == 'q':
        break

    messages.append(create_chat_message("user", user_input))

    ai_message = client.chat.completions.create(
      model="gpt-4-1106-preview",
      messages=messages
    )
    ai_message = ai_message.choices[0].message
    messages.append(create_chat_message("assistant", ai_message))
    print("AI回复:", ai_message)
