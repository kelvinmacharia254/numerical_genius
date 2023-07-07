#!/usr/bin/env python3
# Author: Kelvin Macharia
# Purpose: Generate random Arithmetic queries

import itertools
import random
import time

class question_model:
    def generate_questions(self):
        lst = []
        sample_space = [3,4,5,6,7,8,9,11,12,13]
        for pair in list(itertools.combinations(sample_space, 2)):
            lst.append(str(pair[0]) + ' + ' + str(pair[1]))
            lst.append(str(pair[0]) + ' - ' + str(pair[1]))
            lst.append(str(pair[0]) + ' * ' + str(pair[1]))
        return random.choice(lst)

    def verify_answer(self,question, answer):
        try:
            int(answer)
            if int(answer) == eval(question):
                return "correct"
            else:
                return "wrong"
                # print("Wrong! {} = {}".format(choice_qn,eval(choice_qn)))
                # print(f"Wrong! {qn} = {eval(qn)}")
        except:
            return "invalid"











