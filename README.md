# docker
To start:

`docker build -t a1-301 .`

`docker run -d --name a1-301-container -p 80:80 a1-301:latest`

`docker start a1-301-container`

To stop/remove container:

`docker stop a1-301-container`

`docker rm a1-301-container`

# heroku
`heroku login`

`heroku create --app <app-server-name>`

`heroku container:login`

`heroku container:push web --app <app-server-name>`

`heroku container:release web --app <app-server-name>`

`heroku open --app <app-server-name>`

# Objective statement

* A **Theatre Blocking APP** should allow the **actors** to know their blocking during and ahead of the play so that they don’t need to spend too much time on memorizing their blocking movements.

* A **Theatre Blocking APP** should allow the **directors** to ensure his / her actors are in the right blockings in real time so that he or she doesn’t need to check blockings of actors manually. Moreover, if **directors** are recruiting more actors, they can add actors to the scripts, or if they are not satisfied with a certain actor, they can delete him / her from the script.

# Personas

1. **Julia**, a ballet director. She is a director who is very loyal to the script and very strict with her actors. She is not satisfied about the current stage allocation procedure so that she wants a better system to direct actors in the right position in a more efficient way.

2. **Stephan**, an opera actor. An uprising movie star who is hard-working and ambitious about his career. He loves actoring but memorizing blocking bothers him a lot, since it always distracts him from performing better.

3. **Jack**, an extra. Jack is a student who is doing a part-time job as an extra at Hart House Theatre, overwhelmed in everyday study. This year is his fourth year in the university so that the course workload becomes quite heavy. Jack doens't want to memorize blockings before his part-time job in order to save more time for study.

# User stories

1. **Julia**: As a ballet director, I know how important the actors being in the right positions is, therefore I want to be able to see if every actor is dancing at where he or she should in real time so that I can focus on something more important, such as the details of their actions. 

2. **Stephan**: As an opera actor, I don’t want to memorize blockings, which is a tedious procedure, so that I don't need to remind myself of my blocking numbers from time to time and I can concentrate myself on my performance on stage.

3. **Jack**: As a part-time student who is doing extra, I don’t have many words to say on stage, so that I hope there is a way that I can see my blockings when I am on stage in order to save a lot of time memorizing my blockings ahead and have more time studying.

# Acceptance criteria

* **Actor** should be able to check his or her **position** in different **parts** of the **scripts** where he or she stars. 

* **Director** should be able to see the **positions** of every actor in all parts of different **scripts**.

* **Only** directors are able to modify the *positions* of the actors in different parts of different script.

* **Only** directors have the permission to add or remove actors from a script.

* **Both** actors and directors should receive a clear instruction when they input an invalid input.

# Enhancements

1. Allow director to add new actors to the blocking stages by entering actors' names in a textbox with id **actorName** and clicking the **Add Actor** button on the **director page**. The director can only do so after clicking **get script blockings** button and a certian script is shown on the page. The newly-added actor has a position number of 0 by default, indicating he is not at stage on the script shown. The director can upload his / her position on that script using the existing script save feature.

2. Allow director to remove existing actors from the blocking stage of a certain script by entering actors' names in a textbox with id **actorName** and clicking the **Remove Actor** button on the **director page**. The director can only do so after clicking **get script blockings** button and that script is shown on the page. If the actor provided cannot be found in any of the script, the action won't be proceed. 

# JSON file

1. Example of **script_get_data.json**
```
[ 
  [ 
     "What bloody man is that? He can report, As seemeth by his plight, of the revolt The newest state.",
     "0",
     "23",
     { 
        "3":[ 
           "Duncun",
           "5"
        ],
        "4":[ 
           "Malcolm",
           "2"
        ],
        "8":[ 
           "Ryan",
           "3"
        ],
        "9":[ 
           "Henry",
           "7"
        ],
        "10":[ 
           "Catherine",
           "0"
        ]
     }
  ],
  [ 
     "What bloody man is that? He can report, As seemeth by his plight, of the revolt The newest state.",
     "24",
     "96",
     { 
        "3":[ 
           "Duncun",
           "2"
        ],
        "4":[ 
           "Malcolm",
           "3"
        ],
        "8":[ 
           "Ryan",
           "7"
        ],
        "9":[ 
           "Henry",
           "6"
        ],
        "10":[ 
           "Catherine",
           "1"
        ]
     }
  ]
]
```
* Entry Explanation
```
 [ 
     "A sentence goes here. <A full sentence of script>",
     "0 <Position of chart starts in sentence>",
     "23 <Poisition of chart ends in sentence>",
     { 
        "3": <Actor number as specified in the csv>:[ 
           "Duncun" <Actor Name>,
           "5" <Actor Place>
        ],
        "4":[
           "Malcolm",
           "2"
        ]
     }
  ]
]
```
2. Example of **script_post_data.json**
```
{ 
    "scriptNum":"3",
    "blocks":[ 
       { 
          "part":1,
          "text":"\"What bloody man is that?\"",
          "actors":[ 
             [ 
                "Duncun",
                "5"
             ],
             [ 
                "Malcolm",
                "2"
             ],
             [ 
                "Ryan",
                "3"
             ],
             [ 
                "Henry",
                "7"
             ],
             [ 
                "Catherine",
                "0"
             ]
          ]
       },
       { 
          "part":2,
          "text":"\" He can report, As seemeth by his plight, of the revolt The newest state.\"",
          "actors":[ 
             [ 
                "Duncun",
                "2"
             ],
             [ 
                "Malcolm",
                "3"
             ],
             [ 
                "Ryan",
                "7"
             ],
             [ 
                "Henry",
                "6"
             ],
             [ 
                "Catherine",
                "1"
             ]
          ]
       }
    ]
 }
```
* Entry Explanation
```
{ 
    "scriptNum <script number entry>":"3 <script number value>",
    "blocks <block entry>":[ 
       { 
          "part <part entry>":1 <part number>,
          "text <script line entry>":"\"What bloody man is that?\ <script line>"",
          "actors <actor entry>":[ 
             [ 
                "Duncun <actor name>",
                "5 <actor position>"
             ],
             [ 
                "Malcolm",
                "2"
             ],
             [ 
                "Ryan",
                "3"
             ],
             [ 
                "Henry",
                "7"
             ],
             [ 
                "Catherine",
                "0"
             ]
          ]
       },
       { 
          "part":2,
          "text":"\" He can report, As seemeth by his plight, of the revolt The newest state.\"",
          "actors":[ 
             [ 
                "Duncun",
                "2"
             ],
             [ 
                "Malcolm",
                "3"
             ],
             [ 
                "Ryan",
                "7"
             ],
             [ 
                "Henry",
                "6"
             ],
             [ 
                "Catherine",
                "1"
             ]
          ]
       }
    ]
 }
```
# URL to the heroku application

[https://chenpangujingjing.herokuapp.com/](https://chenpangujingjing.herokuapp.com/)
