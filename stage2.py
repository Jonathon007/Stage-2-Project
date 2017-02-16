blank = ["___1___","___2___","___3___","___4___","___5___","___6___","___7___"]

easy = "A ___1___ is a long narrative, normally in prose, which ___2___ fictional characters and events, usually in the form of a sequential story. The ___3___ has also been ___4___ as possessing 'a ___5___ and ___6___ history of about ___7___ thousand years'."
medium = "___1___ is the classification for any story or universe derived from imagination—in other words, not based strictly on history or fact. It can be expressed in a variety of ___2___, including writings, live performances, films, television programs, animations, video games, and role-playing games, though the ___3___ originally and most commonly refers to the ___4___ forms of literature, including the ___5___, ___6___, ___7___, and play."
hard = "___1___ is a genre of speculative fiction, typically dealing with ___2___ concepts such as futuristic science and technology, space travel, time travel, faster than light travel, parallel universes, and extraterrestrial life. It often explores the potential consequences of ___3___ and other ___4___, and has been called a ' ___5___ ' It usually avoids the ___6___, and unlike the related genre of ___7___."

answer1 = "A novel is a long narrative, normally in prose, which describes fictional characters and events, usually in the form of a sequential story. The genre has also been described as possessing 'a continuous and comprehensive history of about two thousand years'."
answer2 = "Fiction is the classification for any story or universe derived from imagination—in other words, not based strictly on history or fact. It can be expressed in a variety of formats, including writings, live performances, films, television programs, animations, video games, and role-playing games, though the term originally and most commonly refers to the narrative forms of literature, including the novel, novella, short story, and play."
answer3 = "Sci-fi is a genre of speculative fiction, typically dealing with imaginative concepts such as futuristic science and technology, space travel, time travel, faster than light travel, parallel universes, and extraterrestrial life. Science fiction often explores the potential consequences of scientific and other innovations, and has been called a ' literature of ideas. ' It usually avoids the supernatural, and unlike the related genre of fantasy, historically science fiction stories were intended to have a grounding in science-based fact or theory at the time the story was created, but this connection is now limited to hard science fiction."

def check_one_word(word,test_string):
    #find each blank in a string
    seperate_string = test_string.split()
    one_word_position = []
    count = 0
    while count < len(seperate_string):
        if word == seperate_string[count]:
            one_word_position.append(count)
        count +=1
    return one_word_position

def every_word_position(blank,test_string):
    #make each blank in a list
    whole_word_position = []
    for word in blank:
        whole_word_position.extend(check_one_word(word,test_string))
    whole_word_position.sort()
    return whole_word_position

def each_word_position(blank,test_string,answer):
    #user input a string instead of a blank
    seperate_string = test_string.split()
    seperate_answer = answer.split()
    for number in every_word_position(blank,test_string):
        count = 1
        while count<=6:
            user_input2 = raw_input("What should be substituted in for" + seperate_string[number] + "?")
            if user_input2 == seperate_answer[number]:
                break
            count += 1
            print "False!!!"
            if count == 6:
                return "Fail!!!"
    print "Correct!!!"
    print "Congratulations!!!"
    return answer

def select_level():
    #begin a quiz with selecting a level
    print "Please select a game difficulty by typing it in!"
    print "Possible choices include easy, medium, and hard."
    user_input1 = raw_input()
    if user_input1 == "easy":
        print easy
        return each_word_position(blank,easy,answer1)
    if user_input1 == "medium":
        print medium
        return each_word_position(blank,medium,answer2)
    if user_input1 == "hard":
        print hard
        return each_word_position(blank,hard,answer3)
    else:
        print "That's not an option!"
        return select_level()
print select_level()
