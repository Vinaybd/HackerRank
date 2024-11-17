
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.



def minion_game(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    
    vowel_pt = 0
    consonant_pt = 0
  
    
 
    for i in range(len(string)):
        if string[i] in vowel:
          vowel_pt += (len(string) - i)
        
        else:
            consonant_pt +=(len(string) - i)
                
    if vowel_pt > consonant_pt:
        print("Kevin", vowel_pt)
    
    elif consonant_pt > vowel_pt:
        print("Stuart", consonant_pt)
    else:
        print("Draw")
    # your code goes here

if __name__ == '__main__':
    s = input("Enter the string :")
    minion_game(s)