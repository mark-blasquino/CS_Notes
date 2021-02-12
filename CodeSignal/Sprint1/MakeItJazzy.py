"""
Create a function that concatenates the number 7 to the end of every chord in a list. If a 
chord already ends with a 7, ignore that chord.

Examples:

csMakeItJazzy(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
csMakeItJazzy(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
csMakeItJazzy(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
csMakeItJazzy([]) ➞ []
Notes:

Return an empty list if the given list is empty.
You can expect all the tests to have valid chords.
"""

def csMakeItJazzy(chords):
    for i in range(len(chords)):
        if chords[i][-1] != "7":
            chords[i] = chords[i] + "7"
    return chords
    
def csMakeItJazzy(chords):
    for i in range(len(chords)):
        if chords[i][-1] != "7":
            chords[i] = chords[i] + "7"
    return chords
def csMakeItJazzy(chords):
    return [f"{c}7" if c[-1] !=
            "7" else c for c in chords]
