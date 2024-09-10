from queue import Queue
from utils import test_class

# Maximum Bipartite Matching

# A bipartite graph is a graph whose vertices can be divided into two independent sets
# U & V such that every edge connects a vertex from U to V or from V to U
# In other words, there is no edge that connects vertices of same set

# A matching in a bipartitie graph is a set of the edges chosen in such a way
# that no two edges share an endpoint
# A maximum matching is a matching with maximum number of edges
# There can be more than one maximum matchings for a given bipartite graph

# It can be solved by converting it into a flow network
# Example Problem: There are M applicants and N jobs
# Each applicant has a subset of jobs that he is interested in
# Each job can only accept one applicant
# and an applicant can be appointed to only one job
# Find an assignment of jobs to applicants in such a way that
# as many applicants as possible get jobs

examples = [
  {
    'input': [[
      [0, 1, 1, 0, 0, 0],
      [1, 0, 0, 1, 0, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1]
    ]],
    'output': 5
  }
]

# Time Complexity: O(V * E)
# Auxiliary Space: O(V + E)
class Solution:
  def solve(self, graph):
    self.graph = graph
    # To keep track of the applicant assigned to a job
    # applicant[i] is the applicant number assigned to the job i
    self.applicant = [-1] * len(graph)
    count = 0

    for applicant in range(len(graph)):
      # Mark all jobs as not seen for the current applicant
      seen = [False] * len(graph)

      # Find if the applicant can get a job
      if self.bpm(applicant, seen): count += 1

    return count

  def bpm(self, applicant, seen):
    for job in range(len(self.graph[0])):
      if seen[job]: continue
      # If graph[applicant][job] is 0, then the applicant is not interested in this job
      if self.graph[applicant][job] == 0: continue

      seen[job] = True

      # Assign the job to current applicant if the job is not assigned
      # or if previously assigned applicant has an alternate job available
      # Since the job is marked seen, the previously assigned applicant
      # won't get the current job again in the bpm call below
      job_applicant = self.applicant[job]
      if job_applicant == -1 or self.bpm(job_applicant, seen):
        self.applicant[job] = applicant
        return True

test_class(Solution, examples)
