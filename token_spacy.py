import spacy

#Use en_core_web_sm for efficiency and en_core_web_trf for accuracy
nlp = spacy.load("en_core_web_sm") 

def para_token(x):
    '''
    Takes in paragraph string and returns a list of tokenized string values.
    '''
    lis, doc = [], nlp(x)
    for token in doc:
        lis.append(token.text)
    return lis

a = para_token("Apple is looking at buying U.K. startup for $1 billion")
print(a)