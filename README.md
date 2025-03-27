# Memory Management Techniques in Operating Systems  

This project explores different memory management strategies in operating systems, including **Paging, Segmentation, and Virtual Memory**. It demonstrates how these techniques optimize memory allocation, enhance resource utilization, and improve system performance.

## Features  
- Implementation of **Paging, Segmentation, and Virtual Memory** in Python with GUI support  
- **Logical-to-Physical Address Translation**  
- **Page Fault Handling** and **Segment Fault Detection**  
- Performance analysis of memory management techniques  
- **Comparison of different page replacement algorithms (FIFO, LRU, Optimal)**  
- **Graphical User Interface (GUI) for better interaction**  

---

## **1. Paging System Implementation**  

This project implements a **Paging System** in Python to simulate **memory address translation**. Paging helps manage memory efficiently by dividing it into **fixed-size pages**.

### **Features:**
- Dynamically allocates pages to processes  
- Converts **logical addresses** to **physical addresses**  
- Detects **page faults** when a page is missing  
- Compares **FIFO, LRU, and Optimal page replacement algorithms**  
- **Displays results using a graphical interface**  

### **How to Run the Paging Code**  

1. Clone the repository:  
   ```sh
   git clone https://github.com/Mamatha-Kollamaram/memory-management-os.git  
   cd memory-management-os  
   ```
2. Run the program using Python:
   ```sh
   python main.py
   ```

### **Expected Output:**
Refer to `example_output.txt` for detailed expected outputs.

---

## **2. Segmentation System Implementation**  

### **What is Segmentation?**  
Segmentation is a memory management technique that divides a process into variable-sized segments based on its logical structure. Unlike paging, segmentation keeps the program's logical divisions intact (e.g., functions, arrays, stacks).

### **Features:**
- Uses **variable-sized** memory segments  
- Performs **logical-to-physical address translation**  
- Detects **segment faults** when an invalid segment or offset is accessed  
- **Visualizes memory allocation per process in GUI**  
- **Displays translation success vs. faults using interactive UI**  

### **How to Run the Segmentation Code**  

Run the following command:
```sh
python main.py
```

### **Expected Output:**
Refer to `example_output.txt` for detailed expected outputs.

---

## **3. Virtual Memory System Implementation**  

### **What is Virtual Memory?**  
Virtual memory allows a system to use **more memory than physically available** by storing parts of a process in secondary storage (disk) and loading them into RAM when needed.

### **Features:**
- Simulates **demand paging**  
- Handles **page faults** when a required page is not in memory  
- Maps **logical addresses to physical memory frames**  
- **Compares FIFO, LRU, and Optimal page replacement algorithms**  
- **GUI-based visualization for better understanding**  

### **How to Run the Virtual Memory Code**  

Run the following command:
```sh
python main.py
```

### **Expected Output:**
Refer to `example_output.txt` for detailed expected outputs.

---

## **Project Structure**  

```
memory-management-os/  
│── icons/                   # Contains UI icons  
│── paging/                  # Paging system implementation  
│   │── p_main.py            # Main file for paging GUI  
│   │── paging.py            # Paging logic implementation  
│   │── paging_gui.py        # GUI for Paging  
│   │── __init__.py          # Package init file  
│── segmentation/            # Segmentation system implementation  
│   │── s_main.py            # Main file for segmentation GUI  
│   │── segmentation.py      # Segmentation logic implementation  
│   │── segmentation_gui.py  # GUI for Segmentation  
│   │── __init__.py          # Package init file  
│── virtual-memory/          # Virtual memory system implementation  
│   │── vm_main.py           # Main file for virtual memory GUI  
│   │── virtual_memory.py    # Virtual memory logic implementation  
│   │── virtual_memory-gui.py # GUI for Virtual Memory  
│   │── __init__.py          # Package init file  
│── main.py                  # Integrates all memory management techniques  
│── example_output.txt       # Sample outputs from execution  
│── memory_image.webp        # Image representation of memory management concepts  
│── README.md                # Project documentation  
```

---

## **How to Run**  

1. Clone the repository:  
   ```sh
   git clone https://github.com/Mamatha-Kollamaram/memory-management-os.git  
   cd memory-management-os  
   ```
2. Run the integrated GUI program:  
   ```sh
   python main.py  
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
   git commit -m "Updated GUI and fixed address translation issues"
   ```
4. Push the changes to GitHub:
   ```sh
   git push origin main
   ```

---

## **Contributors**  
- **Mamatha Kollamaram**  
- **Kandula Venkata Sivakrishna Reddy**  
- **Chinthala Sai**  

---

## **Future Enhancements**  
- Implementing **TLB (Translation Lookaside Buffer) for faster address translation**  
- **Advanced memory visualization techniques**  
- Adding **real-time paging and segmentation simulation**  
- Simulating **hybrid memory management models**  

