# Memory Management Techniques in Operating Systems  

This project explores different memory management strategies in operating systems, including **Paging, Segmentation, and Virtual Memory**. It demonstrates how these techniques optimize memory allocation, enhance resource utilization, and improve system performance.

## Features  
- Implementation of **Paging, Segmentation, and Virtual Memory** in Python  
- **Logical-to-Physical Address Translation**  
- **Page Fault Handling** and **Segment Fault Detection**  
- Performance analysis of memory management techniques  

---

## **1. Paging System Implementation**  

This project implements a **Paging System** in Python to simulate **memory address translation**.  
Paging helps manage memory efficiently by dividing it into **fixed-size pages**.

### **Features:**
- Dynamically allocates pages to processes  
- Converts **logical addresses** to **physical addresses**  
- Detects **page faults** when a page is missing  

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
Logical Address 100 -> Physical Address 868 (Frame 3, Offset 100)  
Logical Address 260 -> Physical Address 516 (Frame 2, Offset 4)  
Logical Address 50 -> Physical Address 306 (Frame 1, Offset 50)  
Page Fault! Page 0 for Process 3 not found in memory.  
```

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

## **Contributors**  
- **Mamatha Kollamaram**  

---

## **Future Enhancements**  
- Implementing **TLB (Translation Lookaside Buffer) for faster address translation**  
- Adding **GUI-based visualization for memory management**  
- Simulating **different page replacement algorithms (FIFO, LRU, Optimal)**  

