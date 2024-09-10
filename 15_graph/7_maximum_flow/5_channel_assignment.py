from queue import Queue
from utils import test_class

# There are M transmitter and N receiver stations
# Given a matrix that keeps track of the number of packets to be transmitted
# from a given transmitter to a receiver
# During a time slot, a transmitter can send only one packet
# and a receiver can receiver can receive only one packet
# Find the channel assignments so that maximum number of packets are transferred
# from transmitters to receivers during the next time slot

# It can be easily transformed into Maximum Bipartite Matching Problem (MBP)
# that can be solved by converting it into a flow network

examples = [
  {
    'input': [[
      [0, 2, 0],
      [3, 0, 1],
      [2, 4, 0]
    ]],
    'output': 3
  }
]

# Time Complexity: O(V * E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    self.graph = graph
    # To keep track of the sender assigned to a receiver
    # sender[i] is the sender assigned to the receiver i
    self.sender = [-1] * len(graph)
    # Count of receivers assigned to senders
    count = 0

    for sender in range(len(graph)):
      # Mark all receivers as not seen for the current sender
      seen = [False] * len(graph)

      # Find if the sender can be assigned to the receiver
      if self.bpm(sender, seen): count += 1

    return count

  def bpm(self, sender, seen):
    for receiver in range(len(self.graph[0])):
      if seen[receiver]: continue
      # If graph[sender][receiver] is 0, then the sender has no packets to send
      if self.graph[sender][receiver] == 0: continue

      seen[receiver] = True

      # Assign the receiver to the current sender if the receiver is not assigned
      # or if previously assigned receuver has an alternate sender available
      # Since the receiver is marked seen, the previously assigned receiver
      # won't get the current sender again in the bpm call below
      receiver_sender = self.sender[receiver]
      if receiver_sender == -1 or self.bpm(receiver_sender, seen):
        self.sender[receiver] = sender
        return True

test_class(Solution, examples)
