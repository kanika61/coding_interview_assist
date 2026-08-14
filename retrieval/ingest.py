import chromadb
from chromadb.utils import embedding_functions

def ingest_dsa_docs():
    client = chromadb.PersistentClient(path="./chroma_db")

    embed_fn = embedding_functions.OllamaEmbeddingFunction(
        url="http://localhost:11434/api/embeddings",
        model_name="nomic-embed-text"
    )

    collection = client.get_or_create_collection(
        name="dsa_concepts",
        embedding_function=embed_fn
    )

    dsa_docs = [
        {"id": "1",  "text": "Two pointers: use two indices moving inward or in the same direction. Useful for pair sum in sorted arrays, palindrome check, removing duplicates."},
        {"id": "2",  "text": "Sliding window: maintain a subarray of fixed or variable size. Useful for max sum subarray of size k, longest substring without repeating characters."},
        {"id": "3",  "text": "Binary search: halve search space each iteration on a sorted array. O(log n). Use for target search, finding boundaries, rotated array problems."},
        {"id": "4",  "text": "Hash map / dictionary: O(1) average lookup. Useful for frequency counts, two-sum, anagram detection, and grouping."},
        {"id": "5",  "text": "Stack: LIFO structure. Useful for balanced parentheses, next greater element, monotonic stack patterns, and DFS."},
        {"id": "6",  "text": "Queue and BFS: FIFO structure. Useful for level-order traversal, shortest path in unweighted graph, spreading problems."},
        {"id": "7",  "text": "DFS Depth First Search: explore as far as possible before backtracking. Useful for connected components, cycle detection, path finding."},
        {"id": "8",  "text": "Dynamic programming: break problem into overlapping subproblems, cache results. Patterns: 0/1 knapsack, longest common subsequence, coin change."},
        {"id": "9",  "text": "Merge sort: divide array in half recursively, merge sorted halves. O(n log n). Stable sort, good for linked lists."},
        {"id": "10", "text": "Quick sort: pick pivot, partition array around it. O(n log n) average, O(n^2) worst. In-place, cache-friendly."},
        {"id": "11", "text": "Heap and priority queue: min-heap gives smallest element in O(1), insert and delete in O(log n). Useful for k-th largest, merge k sorted lists."},
        {"id": "12", "text": "Trie prefix tree: tree where each node is a character. Useful for autocomplete, word search, prefix matching."},
        {"id": "13", "text": "Union Find Disjoint Set: efficiently union and find connected components. Useful for number of islands, cycle detection in undirected graphs."},
        {"id": "14", "text": "Backtracking: explore all possibilities, prune when constraint violated. Useful for permutations, combinations, N-queens, Sudoku solver."},
        {"id": "15", "text": "Greedy: make locally optimal choice at each step. Useful for interval scheduling, activity selection, jump game."},
    ]

    existing = collection.count()
    if existing == 0:
        collection.add(
            documents=[d["text"] for d in dsa_docs],
            ids=[d["id"] for d in dsa_docs]
        )
        print(f"Ingested {len(dsa_docs)} DSA concepts into ChromaDB.")
    else:
        print(f"ChromaDB already has {existing} documents. Skipping ingest.")

if __name__ == "__main__":
    ingest_dsa_docs()
