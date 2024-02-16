# Suppose you have a dataset containing social media posts with information 
# on post_id, likes, shares, and comments. Write a Python script to:
	# Calculate the total engagement for each post (sum of likes, shares, and comments).
	# Identify the top 5 posts with the highest total engagement.
	# Calculate the average engagement per post.
	# Display the results with relevant details for each post.
	# You can use this question to practice tasks such as sorting, aggregation, and basic statistical calculations on social media engagement data. Feel free to create dummy data for posts and engagement metrics to test and implement your solution.

social_media_data = [
    {"post_id": 1, "likes": 100, "shares": 50, "comments": 30},
    {"post_id": 2, "likes": 150, "shares": 70, "comments": 25},
    {"post_id": 3, "likes": 80, "shares": 40, "comments": 20},
    {"post_id": 4, "likes": 120, "shares": 60, "comments": 35},
    {"post_id": 5, "likes": 200, "shares": 90, "comments": 40},
    {"post_id": 6, "likes": 800, "shares": 40, "comments": 20},
    {"post_id": 7, "likes": 334, "shares": 60, "comments": 35},
    {"post_id": 8, "likes": 200, "shares": 90, "comments": 40},
    # Add more rows as needed
]
def total_engagement_def(social_media_data):
	total_engagement_dct = {}

	for post_data in social_media_data:
		e = 0 
		# post_id = flr(-1)
		for k,v in post_data.items():
			if k != 'post_id' :
				e += v  
			else :
				post_id = v

		total_engagement_dct[post_id] = e

	return total_engagement_dct

def highest_engagement(total_engagement_each_post):
	print(total_engagement_each_post)
	new = dict(sorted(total_engagement_each_post.items(), key=lambda item: item[1],reverse = True))
	return new

total_engagement = total_engagement_def(social_media_data)
print(highest_engagement(total_engagement))



