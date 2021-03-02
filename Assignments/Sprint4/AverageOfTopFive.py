""" 
Given a list of different students' scores, write a function that 
returns the average of each student's top five scores. You should 
return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) 
and the student's score (scores[i][1]). The averages should be 
calculated using integer division.
"""

def csAverageOfTopFive(scores):
    if not scores:
        return []
    
    score_map = {}
    for score in scores:
        if score[0] in score_map:
            score_map[score[0]].append(score[1])
        else:
            score_map[score[0]] = [score[1]]
        
    result = []
    for key, value in score_map.items():
        value.sort(reverse=True)
        if len(value) >= 5:
            average = value[:5]
        else:
            average = value
        score_map[key] = sum(average) // len(average)
        result.append([key, score_map[key]])
        
    return result