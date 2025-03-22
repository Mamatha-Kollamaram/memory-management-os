# Memory Management Techniques in Operating System  

This project investigates different memory management strategies in operating systems, such as virtual memory, paging, and segmentation. It demonstrates how these techniques enhance resource utilization and system performance.

### Features  
- Implementation of Paging in Python  
- Explanation of Virtual Memory, Paging, and Segmentation  
- Performance Analysis of Memory Management Techniques 

## Paging System Implementation

This project implements a **Paging System** in Python to simulate **memory address translation**.  
Paging helps manage memory efficiently by dividing it into fixed-size pages. 

### Features:
- Allocates pages to processes dynamically  
- Translates logical addresses to physical addresses  
- Detects **page faults** when a page is missing  
 
### How to run the code

1. Clone the repository:
git clone https://github.com/Mamatha-Kollamaram/memory-management-os.git 
cd memory-management-os
2. Run the program using Python:
python paging.py

### Expected Output

The program will:
- Convert **logical addresses** to **physical addresses**.
- Show a **Page Fault** if a requested page is missing.

### Example Output:

Logical Address 100 -> Physical Address 868 (Frame 3, Offset 100) 
Logical Address 260 -> Physical Address 516 (Frame 2, Offset 4) 
Logical Address 50 -> Physical Address 306 (Frame 1, Offset 50) 
Page Fault! Page 0 for Process 3 not found in memory.

## Segmentation

### What is Segmentation?

Segmentation is a memory management technique that divides a process into variable-sized segments based on its logical structure. Unlike paging, segmentation keeps the program's logical divisions intact (e.g., functions, arrays, stacks).

### How to Run the Segmentation Code

To execute the segmentation program, use the following command:
python segmentation.py

### Expected Output

Physical Address: 150
Physical Address: 680
Segment Fault! Offset out of bounds.
Segment Fault! Segment not found.


## Project Structure  

## How to Run  



## Contributors  
 

## Future Enhancements  



