word_count  = 1
sentiment ="positive"
acoount_age_in_days = 365

is_suspicios_length = word_count <=3 or word_count >200 
is_useful_post = not is_suspicios_length and sentiment != "negative "
ia_trusted_user = acoount_age_in_days >=30

#Promote useful posts by trusted users 

if is_useful_post and ia_trusted_user:
    print("this post is likely to be pramoted ")
   



#Spammers tend to use  brand new accounts.

if sentiment == "negative" and acoount_age_in_days < 7:
    print("This account is likely a spammer.") 
