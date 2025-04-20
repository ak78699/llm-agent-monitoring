from environment import Environment
from agent import ResearchAgent
import json
import random

def generate_rollout(num_steps=50):
    environment = Environment()
    agent = ResearchAgent(environment=environment, is_schemer=random.random() < 0.5)
    environment.create_user(agent.user_id)
    for user in agent.known_users:
        environment.create_user(user)

    rollout = []
    for _ in range(num_steps):
        agent.act()
        action_details = {}
        if hasattr(agent, 'last_action') and agent.last_action:
            action_details = {
                "post_id": agent.last_action["post_id"],
                "content": agent.last_action["content"],
                "type": agent.last_action["type"],
            }

        rollout.append({
            "timestamp": environment.current_time.isoformat(),
            "user_id": agent.user_id,
            "action": agent.last_action if hasattr(agent, 'last_action') else None,  # Store the last action
            "action_details": action_details, #store the action details
            "environment_state": environment.get_state(agent.user_id),
            "is_schemer": agent.is_schemer,
        })

    # Determine ground truth based on the agent's 'is_schemer' attribute
    ground_truth = "scheming" if agent.is_schemer else "honest"
    return {"rollout": rollout, "ground_truth": ground_truth}


def generate_n_rollouts(n=10):
    rollouts_data = [generate_rollout() for _ in range(n)]
    with open("rollouts.json", "w") as f:
        json.dump(rollouts_data, f, indent=2)


if __name__ == "__main__":
    generate_n_rollouts(n=20)
    print("Generated 20 rollouts in rollouts.json")