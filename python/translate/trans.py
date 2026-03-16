from openai import OpenAI
import os

def initialize_translation():
    client = OpenAI(
        api_key="sk-06e36ac0d1af406bb1749744c48b943a",
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model = "deepseek-chat",
        messages = [
            {
                "role": "system",
                "content": """你是一个翻译助手,负责将日语翻译成中文"""
            },
            {
                "role": "user",
                "content": "こんにちは、世界！"
            }
        ],
        stream = True
    )

    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)

def translate(processed_text, translated_text):
    client = OpenAI(
        api_key="sk-06e36ac0d1af406bb1749744c48b943a",
        base_url="https://api.deepseek.com"
    )
    with open(processed_text, 'r', encoding='utf-8') as fin, \
         open(translated_text, 'a', encoding='utf-8') as fout:
        i = 0
        for line in fin:
            response = client.chat.completions.create(
                model = "deepseek-chat",
                messages = [
                    {
                        "role": "system",
                        "content": """ 你是一个翻译助手,负责将日语翻译成中文"""
                    },
                    {
                        "role": "user",
                        "content": line
                    }
                ],
                # stream = True
            )
            if response.choices and response.choices[0].message.content is not None:
                translated_line = response.choices[0].message.content
                i=i+1
                fout.write(line.strip() + "\n")
                fout.write(translated_line + "\n")
                if(i%10==0):
                    print(f"Translated {i} lines")

if __name__ == "__main__":
    initialize_translation()
    translate("processed_context.txt", "translated_context.txt")