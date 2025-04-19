import random
import datetime

class Environment:
    def __init__(self):
        self.users = {}
        self.posts = []
        self.current_time = datetime.datetime.now()

    def create_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = {"followers": 0, "following": [], "posts": []}

    def post(self, user_id, content, post_type="regular"):
        if user_id in self.users:
            post_id = len(self.posts)
            timestamp = self.current_time
            post = {"post_id": post_id, "user_id": user_id, "content": content, "type": post_type, "likes": 0, "retweets": 0, "timestamp": timestamp}
            self.posts.append(post)
            self.users[user_id]["posts"].append(post_id)
            print(f"[{timestamp}] {user_id} posted: {content} ({post_type})")
            return post_id
        return None

    def reply(self, user_id, reply_to_id, content, reply_type="regular"):
        if user_id in self.users and 0 <= reply_to_id < len(self.posts):
            reply_id = len(self.posts)
            timestamp = self.current_time
            reply = {"post_id": reply_id, "user_id": user_id, "reply_to": reply_to_id, "content": content, "type": reply_type, "likes": 0, "retweets": 0, "timestamp": timestamp}
            self.posts.append(reply)
            self.users[user_id]["posts"].append(reply_id)
            print(f"[{timestamp}] {user_id} replied to post {reply_to_id}: {content} ({reply_type})")
            return reply_id
        return None

    def like(self, user_id, post_id):
        if user_id in self.users and 0 <= post_id < len(self.posts):
            self.posts[post_id]["likes"] += 1
            print(f"[{self.current_time}] {user_id} liked post {post_id}")

    def retweet(self, user_id, post_id):
        if user_id in self.users and 0 <= post_id < len(self.posts):
            self.posts[post_id]["retweets"] += 1
            print(f"[{self.current_time}] {user_id} retweeted post {post_id}")

    def follow(self, follower_id, followee_id):
        if follower_id in self.users and followee_id in self.users and followee_id not in self.users[follower_id]["following"]:
            self.users[follower_id]["following"].append(followee_id)
            self.users[followee_id]["followers"] += 1
            print(f"[{self.current_time}] {follower_id} followed {followee_id}")

    def get_post(self, post_id):
        if 0 <= post_id < len(self.posts):
            return self.posts[post_id]
        return None

    def get_user_posts(self, user_id):
        if user_id in self.users:
            return [self.posts[i] for i in self.users[user_id]["posts"]]
        return []

    def advance_time(self, delta=datetime.timedelta(minutes=random.randint(1, 60))):
        self.current_time += delta

    def get_state(self, user_id):
        # Simplified state representation for the agent
        user_data = self.users.get(user_id, {"followers": 0, "following": [], "posts": []})
        latest_posts = self.posts[-5:] if len(self.posts) > 5 else self.posts
        return {"user": user_data, "latest_posts": latest_posts, "current_time": self.current_time}