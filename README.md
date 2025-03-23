# Memory Management Techniques in Operating Systems  

This project explores different memory management strategies in operating systems, including **Paging, Segmentation, and Virtual Memory**. It demonstrates how these techniques optimize memory allocation, enhance resource utilization, and improve system performance.

## Features  
- Implementation of **Paging, Segmentation, and Virtual Memory** in Python  
- **Logical-to-Physical Address Translation**  
- **Page Fault Handling** and **Segment Fault Detection**  
- Performance analysis of memory management techniques  
- **Comparison of different page replacement algorithms (FIFO, LRU, Optimal)**  
- **Graphical representation of performance metrics**  

---

## **1. Paging System Implementation**  

This project implements a **Paging System** in Python to simulate **memory address translation**.  
Paging helps manage memory efficiently by dividing it into **fixed-size pages**.

### **Features:**
- Dynamically allocates pages to processes  
- Converts **logical addresses** to **physical addresses**  
- Detects **page faults** when a page is missing  
- Compares **FIFO, LRU, and Optimal page replacement algorithms**  
- **Displays page faults and execution time using bar graphs**  

### **How to Run the Paging Code**  

1. Clone the repository:  
   ```sh
   git clone https://github.com/Mamatha-Kollamaram/memory-management-os.git  
   cd memory-management-os  
   ```
2. Run the program using Python:
   ```sh
   python paging.py
   ```

### **Expected Output:**
```
FIFO: Page Faults = 12, Execution Time = 0.00125 seconds
LRU: Page Faults = 10, Execution Time = 0.00115 seconds
Optimal: Page Faults = 8, Execution Time = 0.00105 seconds
```

Additionally, a **graph will be generated** showing the performance of different algorithms.

---

## **2. Segmentation System Implementation**  

### **What is Segmentation?**  
Segmentation is a memory management technique that divides a process into variable-sized segments based on its logical structure. Unlike paging, segmentation keeps the program's logical divisions intact (e.g., functions, arrays, stacks).

### **Features:**
- Uses **variable-sized** memory segments  
- Performs **logical-to-physical address translation**  
- Detects **segment faults** when an invalid segment or offset is accessed  

### **How to Run the Segmentation Code**  

Run the following command:
```sh
python segmentation.py
```

### **Expected Output:**
```
Physical Address: 150  
Physical Address: 680  
Segment Fault! Offset out of bounds.  
Segment Fault! Segment not found.  
```

---

## **3. Virtual Memory System Implementation**  

### **What is Virtual Memory?**  
Virtual memory allows a system to use **more memory than physically available** by storing parts of a process in secondary storage (disk) and loading them into RAM when needed.

### **Features:**
- Simulates **demand paging**  
- Handles **page faults** when a required page is not in memory  
- Maps **logical addresses to physical memory frames**  

### **How to Run the Virtual Memory Code**  

Run the following command:
```sh
python virtual_memory.py
```

### **Expected Output:**
```
Page 0 of Process 1 is in RAM.  
Page Fault! Page 2 of Process 1 not found.  
```

---

## **Project Structure**  

```
memory-management-os/  
│── paging.py                # Paging system implementation  
│── segmentation.py          # Segmentation system implementation  
│── virtual_memory.py        # Virtual memory system implementation  
│── README.md                # Project documentation  
│── example_output.txt       # Sample outputs from execution  
│── graph_output.png         # Graph visualization of page replacement algorithms  
```

---

## **How to Run**  

1. Clone the repository:  
   ```sh
   git clone https://github.com/Mamatha-Kollamaram/memory-management-os.git  
   cd memory-management-os  
   ```
2. Run the desired memory management program:  
   ```sh
   python paging.py  
   python segmentation.py  
   python virtual_memory.py  
   ```

---

## **How to Contribute**  

### **Committing and Pushing Changes**  

1. Make changes to the code or documentation.
2. Stage the changes:
   ```sh
   git add .
   ```
3. Commit with a meaningful message:
   ```sh
   git commit -m "Updated paging system with graph visualization"
   ```
4. Push the changes to GitHub:
   ```sh
   git push origin main
   ```

---

## **Contributors**  
- **Mamatha Kollamaram**  

---

## **Future Enhancements**  
- Implementing **TLB (Translation Lookaside Buffer) for faster address translation**  
- Adding **GUI-based visualization for memory management**  
- Simulating **different page replacement algorithms (FIFO, LRU, Optimal)**  
- **Implementing Working Set Model for better page replacement**  
