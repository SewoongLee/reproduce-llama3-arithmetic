def parse_into_num_ans(full_answer: str) -> int:
    delimiter = '####'
    if delimiter not in full_answer:
        return None
    
    return int(full_answer.split(delimiter)[1].replace(',',''))

def nshot_prompt(data: list, n: int) -> str:
    prompt = ''
    for i in range(n):
        prompt += f'Question: {data[i]["question"]}\nAnswer: {data[i]["answer"]}\n\n'

    prompt += 'Question: '
    return prompt