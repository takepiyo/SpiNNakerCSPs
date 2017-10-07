"""A set of sudoku puzzles to experiment with the spinnaker_csp package.

the puzzles are containned on the dictionary puzzles, keys are the name of the puzzle and values are tuples with the
puzzle as first element and solution as second element.
"""
puzzles={
#---------------------------------------------------------------------
'Dream': ("dream",
#---------------------------------------------------------------------
[[0 for x in range(9)] for y in range(9)],
None),
#---------------------------------------------------------------------
'easy_chaos':("easy_chaos", # easy from doi:10.1038/srep00725
#---------------------------------------
[[0, 4, 0, 8, 0, 5, 2, 0, 0],
[0, 2, 0, 0, 4, 0, 0, 5, 0],
[5, 0, 0, 0, 0, 0, 0, 0, 4],
[0, 9, 0, 0, 0, 3, 1, 2, 0],
[1, 0, 6, 0, 7, 8, 0, 0, 3],
[3, 7, 0, 9, 0, 4, 0, 8, 0],
[0, 0, 0, 0, 0, 6, 7, 0, 0],
[0, 0, 8, 3, 5, 9, 0, 1, 0],
[0, 1, 9, 0, 0, 7, 6, 0, 0]],
#---------------------------------------
[[9, 4, 7, 8, 3, 5, 2, 6, 1],
[6, 2, 3, 7, 4, 1, 8, 5, 9],
[5, 8, 1, 6, 9, 2, 3, 7, 4],
[8, 9, 4, 5, 6, 3, 1, 2, 7],
[1, 5, 6, 2, 7, 8, 9, 4, 3],
[3, 7, 2, 9, 1, 4, 5, 8, 6],
[4, 3, 5, 1, 2, 6, 7, 9, 8],
[7, 6, 8, 3, 5, 9, 4, 1, 2],
[2, 1, 9, 4, 8, 7, 6, 3, 5]]),
#---------------------------------------------------------------------
'hard':('hard', #  hard puzzle from  https://doi.org/10.1371/journal.pcbi.1003311
#---------------------------------------------------------------------
[[8, 0, 5, 0, 0, 0, 0, 3, 0],
[0, 3, 0, 9, 0, 0, 0, 0, 0],
[4, 0, 6, 0, 3, 0, 0, 0, 0],
[6, 0, 0, 0, 1, 0, 9, 0, 0],
[0, 5, 0, 3, 0, 8, 0, 7, 0],
[0, 0, 9, 0, 4, 0, 0, 0, 1],
[0, 0, 0, 0, 2, 0, 3, 0, 8],
[0, 0, 0, 0, 0, 9, 0, 2, 0],
[0, 7, 0, 0, 0, 0, 5, 0, 4]],
#---------------------------------------------------------------------
[[8, 1, 5, 6, 7, 4, 2, 3, 9],
[7, 3, 2, 9, 5, 1, 4, 8, 6],
[4, 9, 6, 8, 3, 2, 7, 1, 5],
[6, 8, 7, 2, 1, 5, 9, 4, 3],
[1, 5, 4, 3, 9, 8, 6, 7, 2],
[3, 2, 9, 7, 4, 6, 8, 5, 1],
[9, 4, 1, 5, 2, 7, 3, 6, 8],
[5, 6, 3, 4, 8, 9, 1, 2, 7],
[2, 7, 8, 1, 6, 3, 5, 9, 4]]),
#---------------------------------------------------------------------
'AI_escargot': ('AI_escargot',
#---------------------------------------------------------------------
[[1, 0, 0, 0, 0, 7, 0, 9, 0],
[0, 3, 0, 0, 2, 0, 0, 0, 8],
[0, 0, 9, 6, 0, 0, 5, 0, 0],
[0, 0, 5, 3, 0, 0, 9, 0, 0],
[0, 1, 0, 0, 8, 0, 0, 0, 2],
[6, 0, 0, 0, 0, 4, 0, 0, 0],
[3, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 4, 0, 0, 0, 0, 0, 0, 7],
[0, 0, 7, 0, 0, 0, 3, 0, 0]],
#---------------------------------------------------------------------
[[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]),
#---------------------------------------------------------------------
'platinum_blonde':('platinum_blonde', # hard from doi:10.1038/srep00725
#---------------------------------------------------------------------
[[0, 0, 0, 0, 0, 0, 0, 1, 2],
[0, 0, 0, 0, 0, 0, 0, 0, 3],
[0, 0, 2, 3, 0, 0, 4, 0, 0],
[0, 0, 1, 8, 0, 0, 0, 0, 5],
[0, 6, 0, 0, 7, 0, 8, 0, 0],
[0, 0, 0, 0, 0, 9, 0, 0, 0],
[0, 0, 8, 5, 0, 0, 0, 0, 0],
[9, 0, 0, 0, 4, 0, 5, 0, 0],
[4, 7, 0, 0, 0, 6, 0, 0, 0]],
#---------------------------------------------------------------------
[[8, 3, 9, 4, 6, 5, 7, 1, 2],
[1, 4, 6, 7, 8, 2, 9, 5, 3],
[7, 5, 2, 3, 9, 1, 4, 8, 6],
[3, 9, 1, 8, 2, 4, 6, 7, 5],
[5, 6, 4, 1, 7, 3, 8, 2, 9],
[2, 8, 7, 6, 5, 9, 3, 4, 1],
[6, 2, 8, 5, 3, 7, 1, 9, 4],
[9, 1, 3, 2, 4, 8, 5, 6, 7],
[4, 7, 5, 9, 1, 6, 2, 3, 8]])
}

#-----------------TEMPLATE---------------------------------------------
##---------------------------------------------------------------------
# [[0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#-----------------TEMPLATE 16X16----------------------------------------
# #---------------------------------------------------------------------
# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]