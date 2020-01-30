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

# Write your documentation below

Write your documentation here.
# Objective statement

* A **Theatre Blocking APP** should allow the **actors** to know their blocking during the play so that they don’t need to spend too much time on memorizing their blocking movements before the rehearsal.

* A **Theatre Blocking APP** should allow the **directors** to ensure his / her actors are in the right blockings in real time so that he or she doesn’t need to check blockings of actors manually.

# Personas && User stories

1. **Julia**, a ballet director. 
-- She is a director who is very loyal to the script and very strict to her actors.
-- As a ballet director, I know how important the actors being in the right positions is, therefore I want to be able to see if every actor is dancing at where he or she should in real time so that I can focus on something more important, such as the details of their actions. 

2. **Stephan**, an opera actor
-- An uprising movie star who is hard-working and ambitious about his career
-- As an opera actor, I don’t want to memorize blockings, which is a tedious procedure, so that I can concentrate myself on my performance on stage.

3. **Jack**, an extra.
-- Jack is a student who is doing a part-time job as an extra at  Hart House Theatre, overwhelmed in every study.
-- As a part-time student who is doing extra, I don’t have many words to say on stage, so I hope there is a way that I can see my blockings when I am on stage, so that I can save a lot of time memorizing and have more time studying.

# Acceptance criteria

* Both the **actors** and **directors** should be able to see blockings for the actors during the rehearsal.
* Only **directors** can manage blocks for actors in real time.
* All **actors** can skim through the blocking of the entire play before the rehearsal.

# Enhancements
1. Allow director to add new actors to the blocking stage. The newly-added actor has a position number of 0, the director can upload his / her positipn using the existing script save feature.
2. Allow director to delete existing actors from the blocking stage. If the actor provided cannot be found in any of the script, the action won't be proceed.

# JSON file
1. Example of ##script_get_data.json##
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
           "Duncun"<Actor Name>,
           "5"<Actor Place>
        ],
        "4":[
           "Malcolm",
           "2"
        ]
     }
  ]
]
```
2. Example of ##script_post_data.json##
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
* Entry Explanation
```
{ 
    "scriptNum<Script number entry>":"3<Script number value>",
    "blocks<block entry>":[ 
       { 
          "part<part entry>":1<part number>,
          "text<script line entry>":"\"What bloody man is that?\<script line>"",
          "actors<actor entry>":[ 
             [ 
                "Duncun<actor name>",
                "5<actor position>"
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
