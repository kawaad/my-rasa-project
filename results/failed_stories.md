## happy path 1
* greet: hello there!   <!-- predicted: bot_challenge: hello there! -->
    - utter_greet   <!-- predicted: utter_iamabot -->
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->


## happy path 2
* greet: hello there!   <!-- predicted: bot_challenge: hello there! -->
    - utter_greet   <!-- predicted: utter_iamabot -->
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->
* goodbye: bye-bye!   <!-- predicted: bem: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_bem -->


## sad path 1
* greet: hello   <!-- predicted: negar: hello -->
    - utter_greet   <!-- predicted: utter_poxa -->
* mood_unhappy: not good   <!-- predicted: negar: not good -->
    - utter_cheer_up   <!-- predicted: utter_poxa -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: despedir: yes -->
    - utter_happy   <!-- predicted: utter_tchau -->


## sad path 2
* greet: hello   <!-- predicted: negar: hello -->
    - utter_greet   <!-- predicted: utter_poxa -->
* mood_unhappy: not good   <!-- predicted: negar: not good -->
    - utter_cheer_up   <!-- predicted: utter_poxa -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: bot_challenge: not really -->
    - utter_goodbye   <!-- predicted: utter_iamabot -->


## sad path 3
* greet: hi   <!-- predicted: negar: hi -->
    - utter_greet   <!-- predicted: utter_poxa -->
* mood_unhappy: very terrible   <!-- predicted: negar: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_poxa -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: negar: no -->
    - utter_goodbye   <!-- predicted: utter_poxa -->


## say goodbye
* goodbye: bye-bye!   <!-- predicted: bem: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_bem -->


