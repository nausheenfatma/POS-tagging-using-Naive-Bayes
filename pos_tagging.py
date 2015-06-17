# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:34:32 2015

@author: nausheenfatma
"""

#POS tagging using Naive Bayes

import random

f1=open("data/English_train.txt","r")
tag_dict={}      #dictionary containing each tag with its count value
word_tag_dict={} #dictionary to keep count of a word and tag occuring together
for line in f1:
    tokens=line.rstrip().split()
    for token in tokens:
        token=token.lower()
        if not token in word_tag_dict.keys():
            word_tag_dict[token]=1
        else:
            word_tag_dict[token]=word_tag_dict[token]+1        
        token_break=token.split("_")
        word=token_break[0]
        tag=token_break[1]
        if not tag in tag_dict.keys():
            tag_dict[tag]=1
        else:
            tag_dict[tag]=tag_dict[tag]+1
        
total_no_of_tags=sum(tag_dict.values())

##########TESTING################################

f1=open("data/Test_POS_Tagging.txt","r")
f2=open("output/Test_results.txt","w")
f3=open("output/probability_of_all_tags_given_word.txt","w")
tag_given_word={}
for line in f1:
    #f2.write(line)
    words=line.rstrip().split()
    for word_token in words :
        word=word_token.lower()
        max_prob_of_tag=0
        predicted_tags_with_max_probability=[] #list of tags with max probability.All tags in this list have equal probability which is maximum.
        predicted_tags_with_max_probability.append("NNP") #take default tag as NNP 
        for tag in tag_dict.keys():
            prior_of_tag=tag_dict[tag]/float(total_no_of_tags) #prior=count_of_tag/count_of_total_no_tags
            word_tag=word+"_"+tag   
            if word_tag in word_tag_dict.keys():
                likelihood_of_word_given_tag=word_tag_dict[word_tag]/float(tag_dict[tag])
                prob_tag_given_word=prior_of_tag * likelihood_of_word_given_tag
                
                if prob_tag_given_word>max_prob_of_tag:
                    predicted_tags_with_max_probability=[] #if probabilty is greater create new list of predicted tags
                    predicted_tags_with_max_probability.append(tag)
                elif prob_tag_given_word==max_prob_of_tag:  #if probabilty is same add to list of predicted tags
                    predicted_tags_with_max_probability.append(tag)
                    
                
                if not word_tag in tag_given_word.keys():
                    tag_given_word[word_tag]=prob_tag_given_word
                    f3.write("P("+tag.upper()+"|"+word_token+")"+":"+str(tag_given_word[word_tag])+"\n")
            else :
                if not word_tag in tag_given_word.keys():
                    tag_given_word[word_tag]=0
                    f3.write("P("+tag.upper()+"|"+word_token+")"+":"+str(tag_given_word[word_tag])+"\n")
        f2.write(word_token+"_"+random.choice(predicted_tags_with_max_probability).upper()+" ") #randomly choose from list of max & equal probable tags
       # f2.write(word_token+"_"+predicted_tag.upper()+" ")
    f2.write("\n")    
f3.close()
f2.close()    

            
