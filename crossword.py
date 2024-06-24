

crossword = [   '        #      ',\
                ' # # # ### # # ',\
                '        #      ',\
                ' # # # # # # # ',\
                '           ####',\
                ' # ### # # # # ',\
                '     #         ',\
                ' # # # # # # # ',\
                '         #     ',\
                ' # # # # ### # ',\
                '####           ',\
                ' # # # # # # # ',\
                '      #        ',\
                ' # # ### # # # ',\
                '      #        ' ]

WHITE = ' '
BLACK = '#'
PADDED_SIZE = 17
SIZE = 15
MARK = BLACK + WHITE + WHITE



def BWW_down(crossword: list[str], row: int, coln: int) -> bool:
 return crossword[row - 1][coln] + crossword[row][coln] + crossword[row + 1][coln] == MARK

def BWW_across(crossword: list[str], row: int, coln: int) -> bool:
    return crossword[row][coln - 1] + crossword[row][coln] + crossword[row][coln + 1] == MARK

def crossword_rows( crossword_str: str) -> list[str]:
    return crossword_str.split("\n")

def padding(crossword : list[str]) -> list[str]:
    for i in range (len(crossword)):
        crossword[i] = BLACK + crossword[i] + BLACK
    crossword.insert(0, BLACK * (PADDED_SIZE))
    crossword.append(BLACK * (PADDED_SIZE))
    return crossword

    
def marking_numbers (crossword: str) -> list[tuple]:
    updated_cword = padding(crossword)
    clue_marking, clue_no = [], 1
    for r in range(1, SIZE+1):
        for c in range(1, SIZE + 1):
            if BWW_across (updated_cword, r, c) or BWW_down (updated_cword, r, c):
                clue_marking.append((r - 1, c - 1, clue_no))
                clue_no += 1
    return clue_marking

print(marking_numbers(crossword))


  
  
  
    


