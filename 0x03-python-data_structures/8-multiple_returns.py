#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        a = None
        return (len(sentence), a)
    else:
        a = (sentence[0],)
        b = ""
        return (len(sentence), b.join(a))
