paragraf = """0
0
40
40
25
50
55
45
55
0
65
60
50
50
62"""

liste = paragraf.split('\n')

liste_str = ', '.join(map(str, liste))
print(liste_str)
