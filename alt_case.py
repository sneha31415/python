# input = sneha output = SnEhA
def alt_cases_C(s: str) -> str:
    alt_case = []
    for pos, char in enumerate(s):
        if pos % 2 == 0:
            char = str.upper(char)
        else:
            char = str.lower(char)
        alt_case.append(char)
    return ''.join(alt_case)

def convert(ch: chr, pos: int) -> chr:
    return str.upper(ch) if pos % 2 == 0 else str.lower(ch) 

def alt_cases_D(s: str) -> str:
    return ''.join(convert(ch, pos) for pos, ch in enumerate(s))

def alt_cases(s: str) -> str:
    cases = [str.upper, str.lower]
    return ''.join(cases[pos%2](char) for pos, char in enumerate(s))

print(alt_cases_C("sneha"))
