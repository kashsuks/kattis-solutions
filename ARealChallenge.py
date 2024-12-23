"""
Old MacDonald had a farm, and on that farm she had a square-shaped pasture, and on that pasture she had a cow that was prone to escape. So now Old MacDonald wants to set up a fence around the pasture. Given the area of the pasture, how long a fence does Old MacDonald need to buy?
Input
The input consists of a single integer 
 (
), the area in square meters of Old MacDonald’s pasture.

Output
Output the total length of fence needed for the pasture, in meters. The length should be accurate to an absolute or relative error of at most 
.

Sample Input 1	Sample Output 1
16
16
Sample Input 2	Sample Output 2
5
8.94427190999915878564
"""

area = int(input())

print((area**0.5)*4)