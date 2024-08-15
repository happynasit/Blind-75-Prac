"""
Number of Suitable Locations
🔥 FULLTIME
Amazon has multiple delivery centers and delivery warehouses all over the world! The world is represented by a number line from -109 to 109. 
There are n delivery centers, the ith one at location center[i]. A location x is called a suitable location for a warehouse if it is possible to bring 
all the products to that point by traveling a distance of no more than d. At any one time, products can be brought from one delivery center and placed at 
point x. Given the positions of n delivery centers, calculate the number of suitable locations in the world. That is, calculate the number of points x on the 
number line (-109 ≤ x ≤ 109) where the travel distance required to bring all the products to that point is less than or equal to d.
Note: The distance between point x and center[i] is |x - center[i]|, their absolute difference

Input:  center = [2, 0, 3, -4], d = 22
Output: 5 
Explanation:
There are 3 suitable locations i.e. {-1, 0, 1, 2, 3}.
1. Place a warehouse at x = -1, total distance traveled is 2 * |-1 - 2| + 2 * |-1 - 0| + 2 * |-1 - 3| + 2 * |-1 - (-4)| = 22 <= d.
2. x = 0, total distance traveled is 2 * |0 - 2| + 2 * |0 - 0| + 2 * |0 - 3| + 2 * |0 - (-4)| = 18 <= d.
3. x = 1, total distance traveled is 2 * |1 - 2| + 2 * |1 - 0| + 2 * |1 - 3| + 2 * |1 - (-4)| = 18 <= d.
4. x = 2, total distance traveled is 2 * |2 - 2| + 2 * |2 - 0| + 2 * |2 - 3| + 2 * |2 - (-4)| = 18 <= d.
5. x = 3, total distance traveled is 2 * |3 - 2| + 2 * |3 - 0| + 2 * |3 - 3| + 2 * |3 - (-4)| = 22 <= d.

https://www.fastprep.io/problems/amazon-number-of-suitable-locations
"""


class Solution:
  def numberOfSuitableLocations(self, center: List[int], d: int) -> int:


