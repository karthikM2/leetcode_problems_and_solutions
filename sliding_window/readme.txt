🔍 What is Sliding Window?

The Sliding Window pattern is used for problems involving contiguous subarrays or substrings
Instead of using nested loops (which take O(n²)), you move a "window" across the array to keep track of a subset of elements.

🧠 Core Idea:

    Maintain a start and end pointer that defines a window.

    Expand the window by moving end.

    Shrink the window by moving start when needed (e.g., to maintain size or condition).

    Useful for fixed or dynamic window size problems.
    
    📌 When to Use:

    Find the max/min sum of k elements.

    Longest substring with certain conditions.

    Number of substrings with a given property.