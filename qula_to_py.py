def sep_string(s: str) -> tuple:
    nums = ''
    assert s != ''
    for i, char in enumerate(s):
        if char.isdigit():
            nums += char
        elif char == '.' and nums[-1] != '.':
            if s[i+1] != ' ':
                nums += '.'
            else:
                return nums, s[i+2:] + '\n', 'question'
        elif char == ':' and nums[-1] != '.' and s[i+1] == ' ':
            return nums, s[i+2:] + '\n', 'answer'
        else:
            return None, s + '\n', 'continue'
    if char == '.' and nums[-1] != '.':
        return nums, s[i+2:] + '\n', 'question'
    elif char == ':' and nums[-1] != '.':
        return nums, s[i+2:] + '\n', 'answer'


def qula_dicts(filename: str) -> tuple:
    with open(filename, 'r') as f:
        lines = f.readlines()

    questions = {'ignore': ''}
    answers = {'ignore': {}}
    current_question = 'ignore'
    current_answer = 'ignore'
    current_block = ('question', 'ignore')

    for line in lines:
        if line.isspace():
            continue
        num, txt, txt_type = sep_string(line.strip())
        if txt.startswith('/'):
            txt = txt[1:]
        if txt_type == 'question':
            current_question = num
            current_block = ('question', num)
            questions[num] = txt
        elif txt_type == 'answer':
            current_block = ('answer', num)
            if current_question in answers:
                answers[current_question].update({num: txt})
            else:
                answers[current_question] = {num: txt}
        else:
            if current_block[0] == 'question':
                questions[current_question] += txt
            elif current_block[0] == 'answer':
                answers[current_answer].update({num: txt})
    return questions, answers


if __name__ == '__main__':
    questions, answers = qula_dicts('example.qula')
    print(f'questions={questions}')
    print(f'answers={answers}')
