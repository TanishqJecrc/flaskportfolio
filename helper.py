

# put all my changing info here
# gets imported into app.py

titles = {'portfolio': 'Flask Portfolio',
          'about': 'More About Me',
          'index': "Hello, I'm Tanishq Singh",
          'arcade': "My Arcade",
          'blog': 'My Hobbies',
          'apps': 'Web Apps and Dashboards'
          }
messages = {'portfolio': ['Featured below are some of my recent projects.',
                          'The skills for each project are noted in the descriptions'],
          'about': ['I am a Computer Science BTech Engineering Student currently doing a dual degree in Data Science and Programming from IITM too.',
                    "See What I learned so far."],
          'index': ["I am a person that wants to learn different skills  in data science, Game Development, application development, machine learning, deep learning, and designing."],
          'arcade': ['Here are Some of my favorite games I have played so far.',
                     'These also includes some overviews of the games too.',
                     'Enjoy!'],
           'blog': ['I have many hobbies some of them are given below.',
                    "Hobbies: {}, {}, {}, {}, {}, {}, and {}".format('Music', 'Gaming', 'New technologys', 'Anime', 'Manga', 'Designing', 'etc.')],
           'apps': ['This website was made using Python and Flask.',
                      'I have learnt Flask and simple webapp design during my Dual degree as well as Industrial Training at Blackcoffers Delhi.'
                      ]
          }

# latest projects
# each article [title, address, image]
blog_posts = [
            ['Music',
             'https://music.youtube.com/',
             'static/images/music.jpg', 'Level Up Music'],
            ['Gaming',
             'https://store.steampowered.com/',
             'static/images/gg.webp', 'Level Up Gaming'],
            ['Game Development',
             'https://learn.unity.com/',
             'static/images/gd.jpeg', 'Towards Game Development'],
            ['Animation',
               'https://www.udemy.com/topic/animation/free/',
               'static/images/ai.webp', 'Towards Animations'],
            ['Software Development',
               'https://www.udemy.com/topic/software-development/',
               'static/images/sd.webp', 'Level Up development'],
              ['Web Application Development',
               'https://study.iitm.ac.in/ds/',
               'static/images/top.png', 'Python in Web app'],
             
              ]

# each project [title, address, image, whet2lookfor]
projects = [['BDM Capstone Project',
                'https://docs.google.com/presentation/d/1X2acFOBxDsBIA2Z38ygtMUxTUCLhqP-r/edit?usp=drive_link&ouid=109768980914285487830&rtpof=true&sd=true',
                'static/images/BDM Capstone.png',
                '''Significant data management and analysis project which combines data from a business firm and builds them into a single Excel file.  Features Relations, Advice derived from data, graphs, and use of different analysis methods.'''],

            ['Portfolio site',
                '/index',
                'static/images/ps.png',
                '''A flask based portfolio web application with basic functionality and responsiveness'''],

            ['Old portfolio site using google sites',
                'https://sites.google.com/student.onlinedegree.iitm.ac.in/tanishqsingh/home',
                'static/images/project.png',
                '''I used Google sites to create a Student Portfolio site as a activity part of project and containing my information with all other activities done.
                I used Google site predefined tools to design a student portfolio website with my basic informations
I made a Home page, Level page, course pages, Statistics page with its introduction and statistics activities menu page where all done activities are listed with their python codes in Google Collab notebook 
'''],

            ['Monte Carlo Simulation Experiment',
                'https://colab.research.google.com/drive/1rtk3VAcq5gLzgcFArxlUCz8Oy7Sg7wAG?usp=sharing',
                'static/images/project2.png',
                '''The probability of an event A can be estimated as follows. We can simulate the experiment repeatedly and independently, say N times, and count the number of times the event occurred, say NA.
A good estimate of P(A) is the following:
 P(A)≈NA/N
As N grows larger and larger, the estimate becomes better and better. This method is generally termed as Monte Carlo simulation.
This simulation is done on Baised Gamblers run in which if a Gambler if wins N units of money he wins and quits casino while if we he loses he will go bankrupt
'''],

            ['Fitting a Distribution to Data and Parameters Estimations',
             'https://colab.research.google.com/drive/12NUY3C0pY43nQetWUrx0VcrC_UnqVWV-?usp=sharing',
             'static/images/collegeproject4.png',
             '''This colab project was made for the IIT Madras B.S. Program > Statistics II for Data Science class. It intends to demonstrate the fitting of a model to some sample data. The model will allow us to predict the population distribution and estimate the values for μ and σ^2 . Finally, we try and estimate the error and calculate the confidence intervals for the estimation.
'''],

            ]

# each project [title, address, image, whet2lookfor]
apps = [
            ['Portfolio site',
                '/index',
                'static/images/ps.png',
                '''A flask based portfolio web application with basic functionality and responsiveness. Currently done only this app soon 5 more projects will be joined here'''],

          ]

# Arcade games
games = [['CyberPunk 2077',
                'https://www.cyberpunk.net/us/en/',
                'static/images/cyberpunk_2077.jpg',
                '''Cyberpunk 2077 is an action role-playing video game developed by CD Projekt Red and published by CD Projekt. The game is based on the Cyberpunk subgenre of science fiction, which is characterized by a combination of lowlife and high tech, featuring futuristic technological and scientific achievements, such as artificial intelligence and cyberware, juxtaposed with societal collapse, dystopia or decay. The game is set in a dystopian cyberpunk universe, where the player assumes the role of “V”, a mercenary in the fictional Californian city known as “Night City”. The game’s story revolves around a heist gone wrong that results in an experimental cybernetic “bio-chip” containing an engram of the legendary rock star and terrorist Johnny Silverhand (played by Keanu Reeves) threatening to slowly overwrite V’s mind. As the story progresses, V and Johnny must work together to find a way to be separated and save V’s life.
                 '''],

         ['Grand Theft Autos',
          'https://www.rockstargames.com/gta-v',
          'static/images/gta5.png',
          '''"Grand Theft Auto V is an action-adventure game played from either a third-person or first-person perspective. Players complete missions—linear scenarios with set objectives—to progress through the story. Outside of the missions, players may freely roam the open world. The game was developed by Rockstar North and published by Rockstar Games. It is the seventh main entry in the Grand Theft Auto series, following 2008’s Grand Theft Auto IV, and the fifteenth installment overall. The Grand Theft Auto series, belonging to, and to some extent defining the genre of free-roaming video games called “sandbox games”, grants a large amount of freedom to the player in deciding what to do and how to do it through multiple methods of transport and weapons.
           '''],

    ['Assassin\'s Creed',
          'https://www.ubisoft.com/en-gb/game/assassins-creed',
          'static/images/ac.png',
          '''"The Assassin’s Creed video game series is an open-world, action-adventure, and stealth game franchise published by Ubisoft and developed mainly by its studio Ubisoft Montreal.
          the series depicts a fictional millennia-old struggle between the Order of Assassins, who fight for peace and free will, and the Knights Templar, who desire peace through order and control. The series features historical fiction, science fiction, and fictional characters intertwined with real-world historical events and historical figures. In most games, players control a historical Assassin while also playing as an Assassin Initiate or someone caught in the Assassin–Templar conflict in the present-day framing story.
           '''],

    ['Devil May Cry',
          'https://www.devilmaycry.com/en/',
          'static/images/dmc.png',
          '''"The Devil May Cry video game series is an action-adventure hack and slash game franchise created by Hideki Kamiya. It is primarily developed and published by Capcom. The series centers on the demon hunter Dante and his efforts to thwart various demon invasions of Earth. Its gameplay consists of combat scenes in which the player must attempt to extend long chains of attacks, avoiding damage and exhibiting stylized combat by varying their attacks; this combat, along with time and the number of items collected and used, are considered in grading the player\’s performance. Across the series, new characters with unique skills are available.
        '''],

    ['Hogwart\'s Legacy',
          'https://www.hogwartslegacy.com/en-gb',
          'static/images/hl.png',
          '''"Hogwarts Legacy is an immersive, open-world action RPG set in the world first introduced in the Harry Potter books. The game is developed by Avalanche Software and published by Warner Bros. Games under its Portkey Games label. It is part of the Wizarding World franchise, taking place a century prior to the events chronicled in the Harry Potter novels. The game allows you to be a student at Hogwarts School of Witchcraft and Wizardry, where users are free to explore the “Harry Potter” world. Players are allowed to create and customize their own character, even being able to get sorted by the Sorting Hat. Embark on a journey through familiar and new locations as you explore and discover magical beasts, craft potions, master spell casting, upgrade talents and become the wizard you want to be.'''],

         ]




about_title_text = "About title text"
skills = [["Programming Languages", [['Python', 4, '5+ years'],  # language, level, years
                                     ['C++', 3, '1+ years'],
                                     ['JavaScript', 1, '0 years'],
                                     ['Java', 1, '0 years'],
                                     ] ],
         ["Data Analysis", [['Data Wrangling', 3, 'Pandas, NumPy, SQL'],  # language, level, years
                                     ['Data Visualization', 3, 'Matplotlib, Seaborn, Excel'],
                                     ['Statistics', 4, 'Inferential and Descriptive'],
                               ]
          ],

            ["Software Engineering", [['Front End', 2, 'HTML, CSS, JavaScript, Vue'],  # language, level, years
                                     ['Frameworks', 3, 'Flask, Django'],
                                     ['Database', 3, 'SQLite, MySQL, PostgreSQL'],
                                     ['Deployment', 1, 'Netlifyapp'],
                               ]
             ],

            ["Machine Learning", [['Supervised', 2, 'Classification, Regression, sklearn'],  # language, level, years
                                     ['Unsupervised', 2, 'Clustering, PCA'],
                                     ['Deep Learning', 1, 'CNN, RNN, TensorFlow', 'PyTorch'],
                               ]
             ],

            ]
