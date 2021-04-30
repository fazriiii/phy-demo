
def chapter_list(text):
    return {"fulfillmentMessages": [
      {
         "text": {
           "text": [
             # "We have few projects that you might be interested"
             "{}".format(text)
           ]
         },
         "platform": "FACEBOOK"
      },
      {
        "payload": {
          "facebook": {
            "attachment": {
              "type": "template",
              "payload": {
                "template_type": "generic",
                "elements": [
                  {
                    "image_url": "https://i.ibb.co/s22z5FK/es.png",
                    "title": "CH1: ELECTROSTATIC",
                    "subtitle": "Study of electromagnetic phenomena that occur when there are no moving charges.",
                    "buttons": [
                      {
                        "type": "postback",
                        "title": "SELECT",
                        "payload": "SELECT"
                      }
                    ]
                  },
                  {
                    "image_url": "https://i.ibb.co/RHzZBXf/coming-soon.png",
                    "title": "CH2: ????",
                    "subtitle": "Content will be available soon.",
                    "buttons": [
                      {
                        "type": "postback",
                        "title": "SELECT",
                        "payload": "SELECT"
                      }
                    ]
                  }
                ]
              }
            }
          }
        },
        "platform": "FACEBOOK"
      }
    ]}

def file_selector():
    return {"fulfillmentMessages": [
      # {
      #   "text": {
      #     "text": [
      #       # "We have few projects that you might be interested"
      #       "{}".format(text)
      #     ]
      #   },
      #   "platform": "FACEBOOK"
      # },
      {
        "payload": {
          "facebook": {
            "attachment": {
              "type": "template",
              "payload": {
                "template_type": "generic",
                "elements": [
                  {
                    "image_url": "https://i.ibb.co/YRWJBpS/latihan-quiz.png",
                    "title": "Animasi",
                    "subtitle": "",
                    "buttons": [
                      {
                        "type": "web_url",
                        "title": "WATCH",
                        "url": "https://phet.colorado.edu/sims/html/coulombs-law/latest/coulombs-law_en.html"
                      }
                    ]
                    # "default_action": {
                    #   "url": "https://petersfancybrownhats.com/view?item=103",
                    #   "webview_height_ratio": "tall",
                    #   "type": "web_url"
                    # }
                  },
                  {
                    "image_url": "https://i.ibb.co/YRWJBpS/latihan-quiz.png",
                    "title": "Latihan / Quiz",
                    "subtitle": "",
                    "buttons": [
                      {
                        "type": "web_url",
                        "title": "Latihan/Quiz",
                        "url": "https://drive.google.com/file/d/1ld6EIt2Ert3ts752hY3UT3nmcuA48_pG/view?usp=sharing"
                      }
                      # ,
                      # {
                      #   "type": "web_url",
                      #   "title": "Quiz",
                      #   "url": "https://drive.google.com/file/d/1ld6EIt2Ert3ts752hY3UT3nmcuA48_pG/view?usp=sharing"
                      # }
                    ]
                  },
                  {
                    "image_url": "https://i.ibb.co/YRWJBpS/latihan-quiz.png",
                    "title": "Nota Kuliah",
                    "subtitle": "",
                    "buttons": [
                      {
                        "type": "web_url",
                        "title": "Download",
                        "url": "https://drive.google.com/file/d/1UcDgFJ5FfEteml1yYaFiw77e8GrtZAGS/view?usp=sharing"
                      }
                    ]
                  },
                  {
                    "image_url": "https://i.ibb.co/YRWJBpS/latihan-quiz.png",
                    "title": "Tutorial",
                    "subtitle": "",
                    "buttons": [
                      {
                        "type": "web_url",
                        "title": "Download",
                        "url": "https://drive.google.com/file/d/1x90JAOOw1nKcJHVJtinvjgT6WNLMcRir/view?usp=sharing"
                      }
                    ]
                  },
                  {
                    "image_url": "https://i.ibb.co/YRWJBpS/latihan-quiz.png",
                    "title": "Video",
                    "subtitle": "",
                    "buttons": [
                      {
                        "type": "web_url",
                        "title": "Watch",
                        "url": "https://www.youtube.com/watch?v=yUPdtFqilXo"
                      }
                    ]
                  }
                ]
              }
            }
          }
        },
        "platform": "FACEBOOK"
      },
      {
        "quickReplies": {
          "title": "Please select options below",
          "quickReplies": [
            "Back to subchapter",
            "Main Menu"
          ]
        },
        "platform": "FACEBOOK"
      }
    ]}
