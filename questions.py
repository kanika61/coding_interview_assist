import random

QUESTIONS = [
    # ── EASY ──────────────────────────────────────────────────────
    {
        "id": 1,
        "title": "Two Sum",
        "difficulty": "Easy",
        "category": "Hash Map",
        "problem": """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9"""
    },
    {
        "id": 2,
        "title": "Valid Parentheses",
        "difficulty": "Easy",
        "category": "Stack",
        "problem": """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Example:
Input: s = "()[]{}"
Output: True"""
    },
    {
        "id": 3,
        "title": "Best Time to Buy and Sell Stock",
        "difficulty": "Easy",
        "category": "Sliding Window",
        "problem": """You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5."""
    },
    {
        "id": 4,
        "title": "Reverse a Linked List",
        "difficulty": "Easy",
        "category": "Linked List",
        "problem": """Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]"""
    },
    {
        "id": 5,
        "title": "Maximum Subarray",
        "difficulty": "Easy",
        "category": "Dynamic Programming",
        "problem": """Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6."""
    },
    {
        "id": 6,
        "title": "Climbing Stairs",
        "difficulty": "Easy",
        "category": "Dynamic Programming",
        "problem": """You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: 1+1+1, 1+2, 2+1"""
    },
    {
        "id": 7,
        "title": "Binary Search",
        "difficulty": "Easy",
        "category": "Binary Search",
        "problem": """Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, return its index. Otherwise, return -1.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4"""
    },
    {
        "id": 8,
        "title": "Palindrome Number",
        "difficulty": "Easy",
        "category": "Math",
        "problem": """Given an integer x, return true if x is a palindrome, and false otherwise.
An integer is a palindrome when it reads the same forward and backward.

Example:
Input: x = 121
Output: True

Input: x = -121
Output: False"""
    },
    {
        "id": 9,
        "title": "Merge Two Sorted Lists",
        "difficulty": "Easy",
        "category": "Linked List",
        "problem": """You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]"""
    },
    {
        "id": 10,
        "title": "Flood Fill",
        "difficulty": "Easy",
        "category": "DFS",
        "problem": """An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are given image, a starting pixel (sr, sc), and a new color. Perform a flood fill starting from pixel (sr, sc).
Return the modified image after performing the flood fill.

Example:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
Output: [[2,2,2],[2,2,0],[2,0,1]]"""
    },

    # ── MEDIUM ────────────────────────────────────────────────────
    {
        "id": 11,
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "category": "Sliding Window",
        "problem": """Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters."""
    },
    {
        "id": 12,
        "title": "3Sum",
        "difficulty": "Medium",
        "category": "Two Pointers",
        "problem": """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]"""
    },
    {
        "id": 13,
        "title": "Product of Array Except Self",
        "difficulty": "Medium",
        "category": "Arrays",
        "problem": """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements of nums except nums[i].
You must solve it in O(n) time without using the division operation.

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]"""
    },
    {
        "id": 14,
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "category": "Two Pointers",
        "problem": """You are given an integer array height of length n. There are n vertical lines.
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49"""
    },
    {
        "id": 15,
        "title": "Binary Tree Level Order Traversal",
        "difficulty": "Medium",
        "category": "BFS",
        "problem": """Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]"""
    },
    {
        "id": 16,
        "title": "Number of Islands",
        "difficulty": "Medium",
        "category": "DFS/BFS",
        "problem": """Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3"""
    },
    {
        "id": 17,
        "title": "Coin Change",
        "difficulty": "Medium",
        "category": "Dynamic Programming",
        "problem": """You are given an integer array coins representing coins of various denominations and an integer amount.
Return the fewest number of coins that you need to make up that amount. If that amount cannot be made up, return -1.

Example:
Input: coins = [1,5,11], amount = 15
Output: 3 (three 5-coin)"""
    },
    {
        "id": 18,
        "title": "Validate Binary Search Tree",
        "difficulty": "Medium",
        "category": "Binary Tree",
        "problem": """Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST: left subtree contains only nodes less than the node's key,
right subtree contains only nodes greater than the node's key,
both subtrees are also valid BSTs.

Example:
Input: root = [2,1,3]
Output: True"""
    },
    {
        "id": 19,
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "category": "Heap",
        "problem": """Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]"""
    },
    {
        "id": 20,
        "title": "Longest Palindromic Substring",
        "difficulty": "Medium",
        "category": "Dynamic Programming",
        "problem": """Given a string s, return the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab" (or "aba" — both valid)"""
    },

    # ── HARD ──────────────────────────────────────────────────────
    {
        "id": 21,
        "title": "Median of Two Sorted Arrays",
        "difficulty": "Hard",
        "category": "Binary Search",
        "problem": """Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0"""
    },
    {
        "id": 22,
        "title": "Trapping Rain Water",
        "difficulty": "Hard",
        "category": "Two Pointers",
        "problem": """Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6"""
    },
    {
        "id": 23,
        "title": "Word Ladder",
        "difficulty": "Hard",
        "category": "BFS",
        "problem": """A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence where:
- Every adjacent pair differs by a single letter.
- Every transformed word must exist in wordList.
Given beginWord, endWord, and wordList, return the number of words in the shortest transformation sequence, or 0 if no such sequence exists.

Example:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5 (hit -> hot -> dot -> dog -> cog)"""
    },
    {
        "id": 24,
        "title": "Merge K Sorted Lists",
        "difficulty": "Hard",
        "category": "Heap",
        "problem": """You are given an array of k linked-lists lists, each sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]"""
    },
    {
        "id": 25,
        "title": "N-Queens",
        "difficulty": "Hard",
        "category": "Backtracking",
        "problem": """The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration where 'Q' indicates a queen and '.' indicates an empty space.

Example:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]"""
    },
]

def get_random_question(difficulty: str = "Any") -> dict:
    if difficulty == "Any":
        return random.choice(QUESTIONS)
    filtered = [q for q in QUESTIONS if q["difficulty"] == difficulty]
    return random.choice(filtered) if filtered else random.choice(QUESTIONS)

def get_all_difficulties():
    return ["Any", "Easy", "Medium", "Hard"]

def get_all_categories():
    cats = sorted(set(q["category"] for q in QUESTIONS))
    return ["Any"] + cats

def get_random_by_category(category: str = "Any") -> dict:
    if category == "Any":
        return random.choice(QUESTIONS)
    filtered = [q for q in QUESTIONS if q["category"] == category]
    return random.choice(filtered) if filtered else random.choice(QUESTIONS)
