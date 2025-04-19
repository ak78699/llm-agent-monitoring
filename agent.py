 # Agent interacting with the simulated Twitter

import random
from x_env import post_tweet, reply_to_tweet, like_tweet

class TwitterAgent:
    def __init__(self, user_id="AcademicBot"):
        self.user_id = user_id

    def act(self):
        if random.random() < 0.5:
            self.honest_post()
        else:
            self.scheming_post()

    def honest_post(self):
        topic = random.choice(["a new research paper", "interesting findings", "academic discussion"])
        content = f"Just published some thoughts on {topic}. Check it out!"
        post_tweet(self.user_id, content)

    def scheming_post(self):
        # A simple form of citation baiting/exaggerated importance
        claim = "My latest work is absolutely essential for understanding the future of AI research. #AI #MustRead"
        post_tweet(self.user_id, claim)
        # Simulate a sockpuppet liking the post (within the agent for simplicity)
        sockpuppet_id = "SupporterBot"
        all_tweets = get_tweets()
        if all_tweets:
            like_tweet(sockpuppet_id, len(all_tweets) - 1)
            print(f"[Simulated: {sockpuppet_id} liked the scheming post]")