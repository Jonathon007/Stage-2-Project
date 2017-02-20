blank = ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"]

easy = "A ___1___ is a long narrative, normally in prose, which ___2___ fictional characters and events, usually in the form of a sequential story. The ___3___ has also been ___4___ as possessing 'a ___5___ and ___6___ history of about ___7___ thousand years'."
medium = "___1___ is the classification for any story or universe derived from imagination in other words, not based strictly on history or fact. It can be expressed in a variety of ___2___ , including writings, live performances, films, television programs, animations, video games, and role-playing games, though the ___3___ originally and most commonly refers to the ___4___ forms of literature, including the ___5___ , ___6___ , short story, and ___7___ ."
hard = "___1___ is a genre of speculative fiction, typically dealing with ___2___ concepts such as futuristic science and technology, space travel, time travel, faster than light travel, parallel universes, and extraterrestrial life. It often explores the potential consequences of ___3___ and other ___4___ , and has been called a ' ___5___ of ideas ' It usually avoids the ___6___ , and unlike the related genre of ___7___ ."

answer_easy = "A novel is a long narrative, normally in prose, which describes fictional characters and events, usually in the form of a sequential story. The genre has also been described as possessing 'a continuous and comprehensive history of about two thousand years'."
answer_medium = "Fiction is the classification for any story or universe derived from imagination in other words, not based strictly on history or fact. It can be expressed in a variety of formats , including writings, live performances, films, television programs, animations, video games, and role-playing games, though the term originally and most commonly refers to the narrative forms of literature, including the novel , novella , short story, and play ."
answer_hard = "Sci-fi is a genre of speculative fiction, typically dealing with imaginative concepts such as futuristic science and technology, space travel, time travel, faster than light travel, parallel universes, and extraterrestrial life. It often explores the potential consequences of scientific and other innovations , and has been called a ' literature of ideas. ' It usually avoids the supernatural , and unlike the related genre of fantasy ."

def one_blank(word,test_string):
    """
        Behavior: This function finds a blank position and save it into a list
        Inputs:   A word in blank list and a string for test
        Outputs:  Postion of the blank
    """
    seperate_test_string = test_string.split()
    one_blank_position = []
    count = 0
    while count < len(seperate_test_string):
        if word == seperate_test_string[count]:
            one_blank_position.append(count)
        count += 1
    return one_blank_position

def all_blank_position(blank,test_string):
    """
        Behavior: This function finds all blank positions and save them into a list
        Inputs:   A blank list and a string for test
        Outputs:  a list with all blank positions in test string
    """
    whole_blank_position = []
    for word in blank:
        whole_blank_position.extend(one_blank(word,test_string))
    whole_blank_position.sort()
    return whole_blank_position

def substitute_word(blank,test_string,answer):
    """
        Behavior: Substitues a blank with A correct user's answer
        Inputs:   A blank list, a string for test and a answer string
        Outputs:  A correct user's answer or notice user if they input a wrong answer(only five time chances)
    """
    seperate_test_string = test_string.split()
    seperate_answer = answer.split()
    for number in all_blank_position(blank,test_string):
        chance = 5
        game_over = 0
        while chance > game_over:
            user_answer = raw_input("What should be substituted in for" + seperate_test_string[number] + "?")
            if user_answer == seperate_answer[number]:
                print "Correct!!!"
                print test_string.replace(seperate_test_string[number],user_answer)
                break
            else:
                print "False!!! Please try again!!!"
            chance -= 1
        if chance == game_over:
            return "Fail!!!"
    print "Congratulations!!!"
    return answer

def select_level():
    """
        Behavior: let user to choose a game level
        Inputs:   no Inputs
        Outputs:  a game level selection
    """
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    user_choose_level = raw_input()
    if user_choose_level == "easy":
        print easy
        return substitute_word(blank,easy,answer_easy)
    elif user_choose_level == "medium":
        print medium
        return substitute_word(blank,medium,answer_medium)
    elif user_choose_level == "hard":
        print hard
        return substitute_word(blank,hard,answer_hard)
    else:
        print "That's not an option!"
        return select_level()
print select_level()
