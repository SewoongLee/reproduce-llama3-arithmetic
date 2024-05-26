import random

# def nshot_prompt(nshot_data: list, n: int, question: str, bos='<|begin_of_text|>', eos='<|eot_id|>') -> str:
#     random.seed(42)

#     prompt = ''
#     for qna in random.sample(nshot_data, n):
#         prompt += f'''
#         {bos}[INST]{qna["question"]}[/INST]
#         Assistant: {qna["answer"]}{eos}
#         '''

#     return prompt + f'''
#     {bos}[INST]{question}'[/INST]
#     Assistant: '''  # no eos here!


def nshot_chats(nshot_data: list, n: int, question: str) -> dict:
    random.seed(42)

    chats = []
    for qna in random.sample(nshot_data, n):
        chats.append({"role": "user", "content": qna["question"]})
        chats.append({"role": "assistant", "content": qna["answer"]})

    chats.append({"role": "user", "content": question})
    return chats


def extract_ans_from_response(answer: str, eos=None):
    if eos:
        answer = answer.split(eos)[0].strip()

    answer = answer.split('####')[-1].strip()
    answer = answer.replace(',', '').replace('$', '')

    return answer
