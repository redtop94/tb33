"""
Simple Learning AI Agent
A basic agent that learns from interactions and improves over time.
"""

import json
import os
from collections import defaultdict

class LearningAgent:
    def __init__(self, memory_file="agent_memory.json"):
        self.memory_file = memory_file
        self.knowledge = defaultdict(dict)
        self.interactions = []
        self.load_memory()
    
    def load_memory(self):
        """Load previously learned knowledge from file."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                data = json.load(f)
                self.knowledge = defaultdict(dict, data.get('knowledge', {}))
                self.interactions = data.get('interactions', [])
    
    def save_memory(self):
        """Save learned knowledge to file."""
        data = {
            'knowledge': dict(self.knowledge),
            'interactions': self.interactions
        }
        with open(self.memory_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def learn(self, topic, information):
        """Learn a new fact or topic."""
        self.knowledge[topic]['info'] = information
        self.knowledge[topic]['learned_at'] = len(self.interactions)
        
        interaction = {
            'type': 'learn',
            'topic': topic,
            'info': information
        }
        self.interactions.append(interaction)
        self.save_memory()
        
        return f"✓ Learned: {topic}"
    
    def recall(self, topic):
        """Recall learned information."""
        if topic in self.knowledge:
            return self.knowledge[topic].get('info', 'No information stored.')
        return f"✗ I haven't learned about '{topic}' yet."
    
    def respond(self, query):
        """Generate a response based on learned knowledge."""
        # Simple pattern matching
        if query.lower().startswith("tell me about"):
            topic = query.replace("tell me about", "").strip()
            return self.recall(topic)
        
        elif query.lower().startswith("learn"):
            parts = query.split(":")
            if len(parts) >= 2:
                topic = parts[0].replace("learn", "").strip()
                info = ":".join(parts[1:]).strip()
                return self.learn(topic, info)
            return "Format: learn [topic]: [information]"
        
        elif query.lower() == "what do you know?":
            if self.knowledge:
                topics = list(self.knowledge.keys())
                return f"I know about: {', '.join(topics)}"
            return "I haven't learned anything yet."
        
        else:
            return "I can: 'learn [topic]: [info]', 'tell me about [topic]', or 'what do you know?'"
    
    def get_stats(self):
        """Get agent statistics."""
        return {
            'topics_learned': len(self.knowledge),
            'total_interactions': len(self.interactions),
            'knowledge': dict(self.knowledge)
        }


def main():
    """Main interaction loop."""
    agent = LearningAgent()
    print("🤖 Simple Learning Agent Started!")
    print("Commands: 'learn [topic]: [info]', 'tell me about [topic]', 'what do you know?', 'stats', 'exit'\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == "exit":
            print("Agent: Goodbye! Memory saved. 👋")
            break
        
        if user_input.lower() == "stats":
            stats = agent.get_stats()
            print(f"Agent Stats: {json.dumps(stats, indent=2)}\n")
            continue
        
        response = agent.respond(user_input)
        print(f"Agent: {response}\n")


if __name__ == "__main__":
    main()
