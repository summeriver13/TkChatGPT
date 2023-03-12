import openai

key = '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'

def openai_reply(content):
    openai.api_key = key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",  # gpt-3.5-turbo-0301
        messages=[
            {"role": "user", "content": content}
        ],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    res = response.choices[0].message.content
    return res

if __name__ == '__main__':
    content = '你是谁'
    ans = openai_reply(content)
    print(ans)
