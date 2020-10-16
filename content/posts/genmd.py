import json
from datetime import datetime

if __name__ == '__main__':
    # Fetch projects from json and convert to python dictionary
    with open ('./projects.json') as f:
        projects = json.load(f)

    # For each project
    for p in projects:
        # fileName = 'Arduino Digital Alarm Clock(December 2019)' --> 'Arduino-Digital-Alarm-Clock.md'
        fileName = (p.replace(' ','-').split('(')[0][:-1])+".md"
        postName = fileName.replace('-',' ')[:-3]
        # dateOrig = 'Arduino Digital Alarm Clock(December 2019)' --> 'December 2019'
        dateOrig = (p.split('(')[1][:-1])
        # dateHugo = dateOrig --> 2019-12-01T00:00:00-05:00
        timestamps = str(datetime.strptime(dateOrig,"%B %Y")).split(' ')
        dateHugo = timestamps[0]+"T"+timestamps[1]+"-05:00"
        # Creates file in local directory for 'Arduino-Digital-Alarm-Clock.md'
        newFile = open('./%s' %fileName,'w')
        # Write the header for a Hugo Blog Post
        newFile.write(f"---\ntitle: \"{postName}\"\ndate: {dateHugo}\ndraft: false\n---")
        # Writes a Markdown Header of 'Arduino Digital Alarm Clock', followed by the date and project description
        newFile.write(f"\n# {postName}\n## {dateOrig}\n{projects[p]}")
        # Close the file to be nice to your computer memory
        newFile.close()
    f.close()

