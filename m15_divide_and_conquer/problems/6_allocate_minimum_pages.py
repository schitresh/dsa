from utils import test_class

# Given an array of size n and an integer k, where arr[i] denotes the number of pages
# of a book and k denotes total number of students. All the books need to be allocated
# to k students in contiguous manner, with each student getting at least one book.
# Minimize the maximum number of pages allocated to a student. If it is not possible
# to allocate books to all students, return -1.

examples = [
  {
    'input': [2, [12, 34, 67, 90]],
    'output': 113,
    # [12] and [34, 67, 90], Max pages assigned to a student is 34 + 67 + 90 = 191
    # [12, 34] and [67, 90], Max pages assigned to a student is 67 + 90 = 157.
    # [12, 34, 67] and [90], Max pages assigned to a student is 12 + 34 + 67 = 113
    # The third combination has the minimum pages assigned to a student, i.e. 113
  },
  {
    'input': [2, [34, 90, 12, 67]],
    'output': 124, # 34 + 90
  },
  {
    'input': [5, [15, 17, 20]],
    'output': -1,
    # Since there are more students than total books, it’s impossible to allocate a
    # book to each student
  },
  {
    'input': [1, [22, 23, 67]],
    'output': 112,
  },
]

# Time Complexity: O(n * (sum(book_pages) - max(book_pages)))
# Auxiliary Space: O(1)
class Solution:
  def solve(self, students, book_pages):
    if students > len(book_pages): return -1

    self.students = students
    self.book_pages = book_pages

    min_page_limit = max(book_pages)
    max_page_limit = sum(book_pages)

    for pages in range(min_page_limit, max_page_limit + 1):
      if self.allocate(pages): return pages

    return -1

  def allocate(self, page_limit):
    student = 1
    student_pages = 0

    for pages in self.book_pages:
      if student_pages + pages > page_limit:
        student += 1
        student_pages = pages
      else:
        student_pages += pages

    # If books can assigned to less than k students then
    # it can be assigned to exactly k students as well
    return student <= self.students

test_class(Solution, examples)

# Binary Search
# Time Complexity: O(n * log(sum(book_pages) - max(book_pages)))
# Auxiliary Space: O(1)
class Solution2:
  def solve(self, students, book_pages):
    if students > len(book_pages): return -1

    self.students = students
    self.book_pages = book_pages

    min_page_limit = max(book_pages)
    max_page_limit = sum(book_pages)

    low = min_page_limit
    high = max_page_limit
    result = -1

    while low <= high:
      pages = low + (high - low) // 2
      allocated = self.allocate(pages)

      if allocated:
        result = pages
        high = pages - 1
      else:
        low = pages + 1

    return result

  def allocate(self, page_limit):
    student = 1
    student_pages = 0

    for pages in self.book_pages:
      if student_pages + pages > page_limit:
        student += 1
        student_pages = pages
      else:
        student_pages += pages

    # If books can assigned to less than k students then
    # it can be assigned to exactly k students as well
    return student <= self.students

test_class(Solution2, examples)
