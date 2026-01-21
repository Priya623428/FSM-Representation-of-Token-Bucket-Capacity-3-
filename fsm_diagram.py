from graphviz import Digraph

# Create a directed graph
fsm = Digraph("TokenBucketFSM", format="png")
fsm.attr(rankdir="LR", size="8")

# Define states (3, 2, 1, 0 tokens)
fsm.attr("node", shape="circle")
fsm.node("3", "3 Tokens")
fsm.node("2", "2 Tokens")
fsm.node("1", "1 Token")
fsm.node("0", "0 Tokens (halt)")

# Transitions when sending a packet
fsm.edge("3", "2", label="send")
fsm.edge("2", "1", label="send")
fsm.edge("1", "0", label="send")

# From 0 → stay in 0 if sending
fsm.edge("0", "0", label="send (blocked)")

# Refill transitions
fsm.edge("0", "3", label="refill")
fsm.edge("1", "3", label="refill")
fsm.edge("2", "3", label="refill")

# Save and render diagram
fsm.render("token_bucket_fsm_diagram", view=True)

print("✅ FSM diagram generated as token_bucket_fsm_diagram.png")
