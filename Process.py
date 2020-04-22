import subprocess
import shutil

filename_parameters = 'guests.csv'

# Function to write personal settings to the respective file
def writeForLatex(name, name2, lang, gender):
    if name[0]=='"':
        name = name.split('"')[1::2][0]
    if len(name2)==0:
        name2=''
    else:
        if name2[0]=='"':
            name2 = name2.split('"')[1::2]
            if len(name2)==0:
                name2=''
            else:
                name2=name2[0]
        if not name2[-1]==',':
            name2 = name2 + ','
    if lang[0]=='"':
        lang = lang.split('"')[1::2][0]
    if lang=='zh' and len(name2)>0:
        name2 = name2[:-1]          # Remove comma for Chinese version
    if gender[0]=='"':
        gender = gender.split('"')[1::2][0]
    elif gender[-1:] =='\n':
        gender = gender[:-1]

    with open('setPersonal.tex','w') as f:
        f.write('\\newcommand\\TheName{' + name +  '}\n'
                '\\newcommand\\TheSecondName{' + name2 + '}\n'
                '\\newcommand\\Lang{' + lang + '}\n'
                '\\newcommand\\Gender{' + gender + '}\n')
        f.close()

#Delete old contents of settings file
with open('setPersonal.tex', 'w') as f:
    f.write('')
    f.close()

# Read guest list and call write function
with open(filename_parameters) as f:
    lis=[line.split(',') for line in f]  
    lis = lis[1:]   # First line in input file is for naming the columns
    print('Started processing of {0} guests.'.format(len(lis)))
    for i,x in enumerate(lis):              
        if len(x)==4:
            writeForLatex(x[0],x[1],x[2],x[3])
        elif len(x)==5:
            writeForLatex(x[0],x[1]+x[2],x[3],x[4])
        if i==0:            # for the first entry, run xelatex twice
            print('Preparing LaTeX document.')
            subprocess.call(['./mkxel'])
        subprocess.call(['./mkxel'])
        shutil.copy('./invitation.pdf', './output/invitation_' + x[0] + '.pdf')
        print('Processed guest {0}, Name: {1}.'.format(i+1, x[0]))
    f.close()
    # post-processing (deleting unnecessary files, etc.)
    subprocess.call(['./mkrem'], stdout=None, shell=None) 
    print('Finished.')

    
