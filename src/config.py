from fake_useragent import UserAgent

# Create an instance of UserAgent
ua = UserAgent()

# Generate a random user-agent
random_user_agent = ua.random

print("Random User-Agent:", random_user_agent)