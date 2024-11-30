import os
import ast


with open("segments.txt", "r", encoding="utf-8") as file:
    data = file.read()
    segments = ast.literal_eval(data)
    # print(segments)

    prompt = ""

    for segment in segments:
        prompt += str(segment["start"]) + " - " + str(segment["end"]) + " : " + str(segment["text"]) + " "


    print(prompt)


