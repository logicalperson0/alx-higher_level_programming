#!/usr/bin/python3
def remove_char_at(str, n):
    tempo = ""
    for i in range(len(str)):
        if (i == n):
            continue
        tempo = tempo + str[i]
    return tempo
