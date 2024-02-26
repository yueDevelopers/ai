# import os
# os.environ["http_proxy"] = "http://localhost:7890"
# os.environ["https_proxy"] = "http://localhost:7890"

# from langchain.llms import OpenAI
# api_key= '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'
# llm = OpenAI(model_name="gpt-3.5-turbo-instruct",openai_api_key=api_key)
# prompt = "你好"
# response = llm(prompt)
# print(response)

import dashscope
dashscope.api_key="sk-xxx"

from http import HTTPStatus

def sample_sync_call(message):
    # prompt_text = '用萝卜、土豆、茄子做饭，给我个菜谱。'
    resp = dashscope.Generation.call(
        model='qwen-turbo',
        prompt=message
    )
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if resp.status_code == HTTPStatus.OK:
        print(resp.output)  # The output text
        print(resp.usage)  # The usage information
        return resp.output
    else:
        print(resp.code)  # The error code.
        print(resp.message)  # The error message.
        return resp.message


# sample_sync_call()
