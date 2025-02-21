import tweepy
import time

def search_tweets(query, max_results=10, max_retries=5):
    #get bearer token in https://developer.x.com/en/portal
    BEARER_TOKEN = 'your_bearer_token'

    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    if max_results < 10 or max_results > 100:
        print("Invalid max_results value. Setting it to the default value of 10.")
        max_results = 10

    retry_count = 0
    while retry_count < max_retries:
        try:
            response = client.search_recent_tweets(query=query, max_results=max_results)
            
            if response.data:
                tweets = [tweet.text for tweet in response.data]
                return tweets
            else:
                print("No tweets found.")
                return []

        except tweepy.TooManyRequests as e:
            print(f"Rate limit exceeded. Retrying in {2 ** retry_count} seconds...")
            time.sleep(2 ** retry_count)
            retry_count += 1

        except Exception as e:
            print(f"Error: {e}")
            return []

    print("Max retries reached. Could not fetch tweets.")
    return []

if __name__ == "__main__":
    custom_query = input("Enter your search query: ")
    try:
        max_results_input = int(input("Enter the number of tweets to retrieve (10-100): "))
    except ValueError:
        print("Invalid input. Using default value of 10.")
        max_results_input = 10

    tweets = search_tweets(custom_query, max_results=max_results_input)

    if tweets:
        print("\nRetrieved Tweets:")
        for i, tweet in enumerate(tweets, start=1):
            print(f"{i}. {tweet}\n")