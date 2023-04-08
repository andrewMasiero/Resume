import pyperclip
import pyautogui
import time
import keyboard

management = ['Analytical ', 'Conceptual', 'Negotiation', 'Requirements gathering',
              'Project Management', 'Process Mapping', 'Work process design', 'Change management']
methodology = ['Waterfall', 'Agile', 'Scrum', 'SDLC']
teamwork = ['Collaboration', 'Interpersonal', 'Training', 'Mentoring']
writing = ['Policy, standards, and procedures',
           'Writing documentation & descriptions']
tools = {'process': ['Jira configuration design', 'Workflow diagrams', 'Visio and Draw.io'],
         'office': ['Word', 'Excel', 'Power Point', 'Access'],
         'technical': ['Reports', 'Automated reports', 'Confluence', 'Splunk', 'Jenkins', 'Web Services'],
         'developer': ['Jira', 'Unit testing', 'GIT', 'Sublime', 'Visual Studio Code', 'Atom']
         }
languages = ['Python', 'Flask', 'Object Relational Mapping (ORM)', 'SQLAlchemy', 'REST APIs', 'JavaScript', 'SQL', 'HTML',
             'CSS ', 'JSON', 'Bootstrap', 'JQL', 'Jira API', 'SOAP/XML', 'Selenium', 'Java']
testing = ['Postman', 'SOAP UI', 'Jmeter', 'ALM',
           'Automated testing', 'System Integration testing', 'Test case design', 'User Acceptance Testing']

developerPriority = [languages, tools['developer'], tools['technical'], testing, methodology, management, teamwork, writing, tools['process'],
                     tools['office']]

pyautogui.hotkey('alt', 'tab')
skills = ''

for skillSet in developerPriority:
    for skill in skillSet:
        if keyboard.is_pressed('esc'):
            print('key break')
            break
        time.sleep(0.2)
        pyperclip.copy(skill)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        # skills += f'{skill}\n'

# pyperclip.copy(skills)
# print(skills)
