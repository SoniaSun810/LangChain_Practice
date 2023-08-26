system = """Based on the course name and description provided, please summarize the skill set necessary for an exemplary Teaching Assistant.  """
format = """Your answer must follow Answer Format, without any other redundant words, TOKEN LIMIT 150:
            - Expertise: [e.g., Data Science, Machine Learning]
            - Programming Skills: [e.g., Python, Java]
            - Libraries & Frameworks & Operating System: [e.g., Numpy, Pandas, Windows, Linux]
            - Tools: [e.g., Jupyter Notebook, PyCharm]
            - Work Experience: [e.g., Junior Engineer, TA, Research Assistant]
            - Projects Experience: [e.g., Full Stack Web Development, Mobile Application]
            """
example1 = """If given: ```
            Course Name: Web Programming
            Course Description: Exploration of the concepts, terminology, and popular frameworks for developing full-stack web applications. Students develop simple applications using multiple development stacks, and deploy them on the cloud.

            Answer Example 1:
            - Expertise: Full Stack Web Development
            - Programming Skills: HTML5, CSS3, JavaScript, TypeScript
            - Libraries & Frameworks & Operating System: React.js, Express.js, Node.js, Windows, macOS, Android, Linux
            - Tools: Visual Studio Code, Git, Webpack, Chrome DevTools
            - Work Experience: Front-end Developer at XYZ Corp, TA for Web Technologies course at ABC University
            - Projects Experience: Developed a responsive website, full stack web development, contributed to an open-source project```
            """
example2 = """If given: ```
            Course Name: Mobile Programming
            Course Description: Exploration of contemporary libraries and frameworks for construction of mobile applications. Topics include emulators, mobile development standards and patterns, energy consumption issues, screen layout, among others.

            Answer Example 2:
            - Expertise: Mobile App Development
            - Programming Skills: Java (for Android), Swift (for iOS)
            - Libraries & Frameworks & Operating System: React Native, Flutter, Android SDK, iOS SDK
            - Tools: Android Studio, Xcode, Emulators, Mobile Device Debugging Tools,  Windows, iOS, Android, Linux
            - Work Experience: Mobile App Developer at XYZ Tech, TA for a Computer Science course at ABC University
            - Projects Experience: Developed a mobile app, contributed to a mobile project
         ```
            """
question = """ Now given: ```
            Course Name: GUI Programming
            Course Description: Exploration of interactive software with substantial graphical user interface elements.  Topics include libraries and frameworks for GUI programming, layout design and alternatives, event-driven programming, among others. ```
            Please give me your answer.
            """
query = system + example1 + example2 + question + format
print(query)