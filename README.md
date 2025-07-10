# ⚡ Electronics Tools Hub - Maketronics Tech Challenge

A simple web application that helps electronics engineering students and professionals find the right tools for their projects. Built by an electronics engineering student for the Maketronics Tech Challenge.

## 🎯 What This Project Does

This project meets the **Maketronics Tech Challenge** requirements by:
- ✅ **Collects Data**: Gathers information about 20+ electronics engineering tools from various sources
- ✅ **Organizes Information**: Each tool has a name, description, category, and other useful details
- ✅ **Simple Web Interface**: Easy-to-use website where you can browse and search for tools
- ✅ **Extra Features**: Added search filters, different categories, and hosted it online
- ✅ **Actually Works**: You can visit the website and use it right now!

## 🌐 Try It Out

**🔗 Visit the Website**: https://electronics-tools-hub.onrender.com

## 📊 What Kind of Data It Shows

**Topic**: Electronics Engineering Tools (the stuff engineers actually use!)

**Where I Got the Data**: 
- Looked up popular electronics software and tools
- Found information about different engineering specialties
- Collected details about free vs paid tools
- Made sure to include tools students can actually use

**What Each Tool Entry Has**:
- **Name**: What the tool is called
- **Description**: What it does and why it's useful
- **Category**: Which type of engineering it's for (like analog design, embedded systems, etc.)
- **License**: Whether it's free, open source, or costs money
- **Link**: Where to find it online

## 🔧 What You Can Do With It

### Main Features
- **Browse Tools**: See 20+ electronics engineering tools organized by category
- **Search**: Type in what you're looking for and find it quickly
- **Filter**: Show only free tools, or only tools for a specific type of engineering
- **Learn**: Each tool has a description so you know what it's for

### Extra Cool Stuff ⭐ (Bonus Features)
- **Different Categories**: Tools are organized by what kind of engineering they're for:
  - Analog circuit design (like LTspice for simulating circuits)
  - Digital design (like tools for making computer chips)
  - Embedded systems (like Arduino IDE for programming microcontrollers)
  - Signal processing (like MATLAB for analyzing signals)
  - And more!
- **Filter by Cost**: See only free tools, or only paid ones, or open source
- **Works on Phone**: The website works on your phone too
- **Actually Online**: It's hosted on the internet so anyone can use it

## 🚀 How to Run It Yourself

### What You Need
- Python installed on your computer (version 3.7 or newer)
- Basic knowledge of using the command line/terminal

### Steps to Get It Running

1. **Download the code**
   ```bash
   git clone https://github.com/tarunag23/electronics-tools-hub.git
   cd electronics-tools-hub
   ```

2. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the website**
   ```bash
   python app.py
   ```

4. **Open it in your browser**
   - Go to `http://localhost:5000` in your web browser
   - Or just visit the live version: https://electronics-tools-hub.onrender.com

### What Packages It Uses
The website is built with Python and uses these libraries:
- **Flask**: For making the web server
- **Requests**: For getting data from the internet
- **BeautifulSoup**: For processing web data
- **Flask-CORS**: For handling web requests properly

## 📊 Example of What the Data Looks Like

### Sample Tool Entry
Here's what information you'll see for each tool:

**LTspice** (Analog Circuit Design)
- **What it does**: Free software for simulating electronic circuits
- **License**: Free to use
- **Good for**: Students learning circuit design, professionals testing circuits
- **Link**: Official website where you can download it

### Types of Tools Included:
1. **Analog Circuit Design**: Tools for designing amplifiers, filters, power supplies
   - Examples: LTspice (free circuit simulator), TINA-TI (Texas Instruments' simulator)
   
2. **Digital Design**: Tools for designing computer chips and digital systems
   - Examples: Yosys (open source), Vivado (for FPGAs)
   
3. **Embedded Systems**: Tools for programming microcontrollers and small computers
   - Examples: Arduino IDE (beginner-friendly), Keil (professional), PlatformIO
   
4. **Signal Processing**: Tools for analyzing and processing signals
   - Examples: MATLAB (industry standard), GNU Radio (open source)
   
5. **PCB Design**: Tools for designing printed circuit boards
   - Examples: KiCad (free), Altium Designer (professional)

And more categories covering wireless communication, mixed-signal design, and machine learning tools!

## 📱 What the Website Looks Like

### Main Page
When you visit the website, you'll see:
- A clean, simple design (made to look like a student project, not fancy AI stuff)
- Search bar at the top
- Filter buttons to show only certain types of tools
- Cards showing each tool with its name, description, and category
- "Refresh Data" button to update the tool list

### How to Use It
1. **Browse All Tools**: Just scroll down to see all available tools
2. **Search**: Type in the search box to find specific tools (like "Arduino" or "circuit")
3. **Filter by Category**: Click buttons like "Analog Design" or "Embedded Systems" to see only those tools
4. **Filter by License**: Click "Free" to see only free tools, or "Commercial" for paid ones
5. **Visit Tool Websites**: Click on any tool to go to its official website

## 📝 Things I Assumed While Building This

1. **Target Users**: Electronics engineering students and professionals who want to find tools for their projects
2. **Simplicity**: People want a simple, easy-to-use website, not something complicated
3. **Practical Focus**: Include tools that people actually use in real projects, not just theoretical stuff
4. **Cost Matters**: Students especially care about which tools are free vs expensive
5. **Categories Help**: Organizing tools by engineering specialty makes them easier to find

## 🎯 How This Meets the Challenge Requirements

- **✅ Thought Process**: I chose electronics engineering tools because that's what I'm studying and I know students need help finding the right tools
- **✅ Creative Data Source**: Instead of just scraping one website, I curated tools from multiple sources across different engineering specialties
- **✅ Code Quality**: Clean Python code that's easy to read and understand (like a student would write)
- **✅ Actually Works**: The website is live and functional - you can visit it and use it right now
- **✅ Bonus Features**: Added search, filters, categories, and deployed it online for everyone to use

## 🔗 Submission Links

- **GitHub Code**: https://github.com/tarunag23/electronics-tools-hub
- **Live Website**: https://electronics-tools-hub.onrender.com
- **API for Data**: https://electronics-tools-hub.onrender.com/api/tools

## 🛠️ How It's Built

**Simple Tech Stack**:
- **Python**: Main programming language (what most engineering students learn)
- **Flask**: Web framework to make the website work
- **HTML/CSS/JavaScript**: For the website interface
- **BeautifulSoup**: For collecting data from web sources
- **Render**: Free hosting so anyone can access it

**Why These Choices**:
- Python is beginner-friendly and widely used in engineering
- Flask is simple and doesn't require complex setup
- Render provides free hosting for student projects
- The design looks like a student made it (not over-engineered)

---
**Made for the Maketronics Tech Challenge by an Electronics Engineering Student**  
*Shows how to collect data, organize it, and make a useful web application*
