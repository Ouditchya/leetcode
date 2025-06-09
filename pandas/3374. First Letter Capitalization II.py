import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    
    def capitalize(s):
        words = s.split(" ")
        for j in range(len(words)):
            word = words[j]
            if "-" in word:
                word_part = word.split("-")
                for i in range(len(word_part)): word_part[i] = word_part[i].title()
                word = "-".join(word_part)
            else:
                word = word.title()
            words[j] = word
        return " ".join(words)
        
    user_content.rename(columns = {"content_text": "original_text"}, inplace = True)
    user_content["converted_text"] = user_content["original_text"].apply(capitalize)

    return user_content