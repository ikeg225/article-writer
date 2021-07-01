import nlpcloud

class nlp:
    def __init__(self, api):
        self.api = api

    def line(self, single):
        '''
        Returns a string that is a summarization of the input string.
        '''
        client = nlpcloud.Client("bart-large-cnn", self.api)
        summary = client.summarization(single)
        return list(summary.values())[0]

    def multiple_lines(self, lis):
        '''
        Takes in a list of strings and returns a list of summarized strings.
        '''
        para = []
        for i in lis:
            para.append(self.line(i))
        return para