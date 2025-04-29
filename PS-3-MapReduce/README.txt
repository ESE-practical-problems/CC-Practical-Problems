using vbox: https://medium.com/analytics-vidhya/word-count-using-mapreduce-on-hadoop-6eaefe127502

map-reduce real-world example:

Input fruits = [apple, banana, apple, orange, banana, apple]

Map:
apple → 1
banana → 1
apple → 1
orange → 1
banana → 1
apple → 1

Shuffle:
apple → [1, 1, 1]
banana → [1, 1]
orange → [1]

Reduce:
apple → 3
banana → 2
orange → 1



