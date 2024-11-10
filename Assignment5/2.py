facebook_friends = {"Alice", "Bob", "Charlie"}
twitter_friends = {"Bob", "Charlie", "David"}
linkedin_friends = {"Bob", "Charlie", "Emma"}
mutualf=facebook_friends
mutualf &=linkedin_friends
mutualf &=twitter_friends
print(mutualf)