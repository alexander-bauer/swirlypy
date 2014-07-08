#!/usr/bin/python3

import yaml

print("Loading yaml/lesson.yaml with extreme precaution.")
with open('yaml/lesson.yaml', 'r') as f: 
    y = yaml.safe_load(f)

print("y is a ", type(y))
print("y[1] is a ", type(y[1]))
print("y[2]['CorrectAnswer'] is ", y[2]['CorrectAnswer'] )
