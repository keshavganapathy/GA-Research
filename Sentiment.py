from textblob import TextBlob

class Independant:

    def doSentiment(self, text):
        blob = TextBlob(text)
        print(blob.sentiment)
        arr = [blob.polarity, blob.subjectivity]
        return arr

one = Independant()
print(str(one.doSentiment("I want to fly")[0]) + str(one.doSentiment("I want to fly")[1]))
