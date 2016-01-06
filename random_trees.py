'''
# What do you think would happen if we split on GPA first and then SAT scores---would we get the same groupings? (i.e. what is the best way to split?)
## High GPA does not necessarily mean if I SAT. GPA is tied to getting good grades, which can be influenced by easy classes or  simply a student that is good at doing homework. SAT is tied towards knowledge and "smartness", which cannot easily be faked in the SAT testing environment. Splitting by SAT first is more likely to find the "smarter" students

# What if we used more criteria such as essay evaluation scores, extracurriculars, awards and distinctions in sports etc? (i.e. how many attributes should we use to create splits, and what are the most significant attributes?)
## Many schools take these criteria into consideration. The criteria used will depend on how  the school in question weighs each of the criterion

# We were given averages, but what about the spread, what about outliers? (i.e. how does the distribution of attributes affect misclassification?)
## Outliers on the top end could increase the overall averages that are used in the decision tree, which  could lead to a higher threshold for admission which leads to fewer students being admitted. If the school needs X amount of students  admitted, you might need to create a list based on the SAT/GPA tree and then admit the top X students, excluding any that might be denied for other reasons (financial, criminal, etc.)
'''

# GOAL
## Classify persons activity based on data collected from smartphone

import pandas as pd

#Build data frame using raw data, activity number, and subject number
col_data = pd.read_csv('data/features.txt', sep=' ', header=None, names=['index', 'vars'])
COLS = col_data.vars.tolist()
volunteer_data = pd.read_csv('data/train/X_train.txt', names=COLS)
activity_data = pd.read_csv('data/train/y_train.txt', header=None, names=['activity'])
volunteer_data['activity'] = activity_data['activity']
subject_data = pd.read_csv('data/train/subject_train.txt', header=None, names=['subject'])
volunteer_data['subject'] = subject_data['subject']

col_names = list(volunteer_data.columns.values)
print col_names
#print volunteer_data
