"""
Data Collector for Electronics Tools Hub
Author: Tarun 
Description: Collects and organizes electronics engineering tools data
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
import os

class ElectronicsToolsCollector:
    def __init__(self):
        self.tools_data = []
        # HTTP headers I use for web scraping
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def collect_github_trending(self):
        """My method to collect trending repositories from GitHub"""
        print("Collecting GitHub trending repositories...")
        
        try:
            url = "https://github.com/trending"
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            repos = soup.find_all('article', class_='Box-row')
            
            for repo in repos[:8]:  # Get top 8 trending repos
                try:
                    # Extract repository name and link
                    title_elem = repo.find('h2', class_='h3')
                    if not title_elem:
                        continue
                    
                    link_elem = title_elem.find('a')
                    if not link_elem:
                        continue
                    
                    name = link_elem.get_text().strip().replace('\n', '').replace(' ', '')
                    link = f"https://github.com{link_elem.get('href')}"
                    
                    # Extract description
                    desc_elem = repo.find('p', class_='col-9')
                    description = desc_elem.get_text().strip() if desc_elem else "No description available"
                    
                    # Extract stars
                    stars_elem = repo.find('a', href=lambda x: x and '/stargazers' in x)
                    stars = stars_elem.get_text().strip() if stars_elem else "0"
                    
                    # Extract language
                    lang_elem = repo.find('span', {'itemprop': 'programmingLanguage'})
                    language = lang_elem.get_text().strip() if lang_elem else "Unknown"
                    
                    self.tools_data.append({
                        'name': name,
                        'description': description,
                        'category': 'GitHub Trending',
                        'popularity': f"{stars} stars",
                        'link': link,
                        'language': language,
                        'source': 'GitHub'
                    })
                    
                except Exception as e:
                    print(f"Error processing repo: {e}")
                    continue
                    
        except Exception as e:
            print(f"Error collecting GitHub trending: {e}")
    
    def collect_electronics_tools(self):
        """Collect curated electronics engineering tools by domain"""
        print("Collecting electronics engineering tools...")

        # Comprehensive list of electronics engineering tools by domain
        electronics_tools = [
            # Analog Circuit Design
            {
                'name': 'LTspice',
                'description': 'Free SPICE simulator for analog circuits. Very popular among students and professionals.',
                'category': 'Analog Circuit Design',
                'popularity': 'Very Popular',
                'link': 'https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html',
                'license': 'Free',
                'source': 'Analog Devices'
            },
            {
                'name': 'Cadence Virtuoso',
                'description': 'Professional tool for analog IC design. Used in most semiconductor companies.',
                'category': 'Analog Circuit Design',
                'popularity': 'Industry Standard',
                'link': 'https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-design/virtuoso-studio.html',
                'license': 'Commercial',
                'source': 'Cadence'
            },
            {
                'name': 'TINA-TI',
                'description': 'Texas Instruments SPICE simulator. Good for beginners.',
                'category': 'Analog Circuit Design',
                'popularity': 'Popular',
                'link': 'https://www.ti.com/tool/TINA-TI',
                'license': 'Free',
                'source': 'Texas Instruments'
            },
            {
                'name': 'PSpice',
                'description': 'Classic SPICE simulator from Cadence. Still widely used.',
                'category': 'Analog Circuit Design',
                'popularity': 'Popular',
                'link': 'https://www.pspice.com/',
                'license': 'Commercial',
                'source': 'Cadence'
            },
            {
                'name': 'Multisim',
                'description': 'Circuit simulation software from National Instruments. Easy to use.',
                'category': 'Analog Circuit Design',
                'popularity': 'Popular',
                'link': 'https://www.ni.com/en-us/shop/software/products/multisim.html',
                'license': 'Commercial',
                'source': 'National Instruments'
            },

            # Digital VLSI Design
            {
                'name': 'Synopsys Design Compiler',
                'description': 'RTL synthesis tool. Industry standard for digital design.',
                'category': 'Digital VLSI Design',
                'popularity': 'Industry Standard',
                'link': 'https://www.synopsys.com/implementation-and-signoff/rtl-synthesis-test/design-compiler-graphical.html',
                'license': 'Commercial',
                'source': 'Synopsys'
            },
            {
                'name': 'Cadence Innovus',
                'description': 'Place and route tool for digital chips.',
                'category': 'Digital VLSI Design',
                'popularity': 'Industry Standard',
                'link': 'https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/soc-implementation-and-floorplanning/innovus-implementation-system.html',
                'license': 'Commercial',
                'source': 'Cadence'
            },
            {
                'name': 'Yosys',
                'description': 'Open source synthesis tool. Good for learning VLSI.',
                'category': 'Digital VLSI Design',
                'popularity': 'Growing',
                'link': 'https://yosyshq.net/yosys/',
                'license': 'Open Source',
                'source': 'YosysHQ'
            },
            {
                'name': 'Vivado',
                'description': 'Xilinx FPGA design tool. Very popular for FPGA development.',
                'category': 'Digital VLSI Design',
                'popularity': 'Very Popular',
                'link': 'https://www.xilinx.com/products/design-tools/vivado.html',
                'license': 'Free/Commercial',
                'source': 'AMD Xilinx'
            },
            {
                'name': 'Quartus Prime',
                'description': 'Intel FPGA design software. Alternative to Vivado.',
                'category': 'Digital VLSI Design',
                'popularity': 'Popular',
                'link': 'https://www.intel.com/content/www/us/en/software/programmable/quartus-prime/overview.html',
                'license': 'Free/Commercial',
                'source': 'Intel'
            },

            # Mixed Signal Design
            {
                'name': 'Cadence AMS Designer',
                'description': 'Mixed-signal verification platform for complex designs.',
                'category': 'Mixed Signal Design',
                'popularity': 'Industry Standard',
                'link': 'https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/mixed-signal-design/ams-designer.html',
                'license': 'Commercial',
                'source': 'Cadence'
            },
            {
                'name': 'Mentor Questa ADMS',
                'description': 'Advanced mixed-signal simulator for verification.',
                'category': 'Mixed Signal Design',
                'popularity': 'Professional',
                'link': 'https://eda.sw.siemens.com/en-US/ic/questa/adms/',
                'license': 'Commercial',
                'source': 'Siemens EDA'
            },

            # Signal Processing
            {
                'name': 'MATLAB Signal Processing Toolbox',
                'description': 'Complete signal processing toolkit. Very comprehensive.',
                'category': 'Signal Processing',
                'popularity': 'Industry Standard',
                'link': 'https://www.mathworks.com/products/signal.html',
                'license': 'Commercial',
                'source': 'MathWorks'
            },
            {
                'name': 'GNU Radio',
                'description': 'Free software for software-defined radio. Great for learning.',
                'category': 'Signal Processing',
                'popularity': 'Popular',
                'link': 'https://www.gnuradio.org/',
                'license': 'Open Source',
                'source': 'GNU Radio Community'
            },
            {
                'name': 'SciPy Signal',
                'description': 'Python library for signal processing. Free and powerful.',
                'category': 'Signal Processing',
                'popularity': 'Very Popular',
                'link': 'https://docs.scipy.org/doc/scipy/reference/signal.html',
                'license': 'Open Source',
                'source': 'SciPy Community'
            },
            {
                'name': 'LabVIEW',
                'description': 'Graphical programming for signal processing and data acquisition.',
                'category': 'Signal Processing',
                'popularity': 'Popular',
                'link': 'https://www.ni.com/en-us/shop/labview.html',
                'license': 'Commercial',
                'source': 'National Instruments'
            }
        ]

        self.tools_data.extend(electronics_tools)
    
    def collect_wireless_comm_tools(self):
        """Collect tools for wireless communication engineers"""
        print("Collecting wireless communication tools...")

        wireless_tools = [
            {
                'name': 'Keysight SystemVue',
                'description': 'System-level design for wireless communications. Professional tool.',
                'category': 'Wireless Communication',
                'popularity': 'Industry Standard',
                'link': 'https://www.keysight.com/us/en/products/software/pathwave-design-software/pathwave-system-design.html',
                'license': 'Commercial',
                'source': 'Keysight'
            },
            {
                'name': 'Wireless InSite',
                'description': 'Radio propagation software for network planning.',
                'category': 'Wireless Communication',
                'popularity': 'Professional',
                'link': 'https://www.remcom.com/wireless-insite-em-propagation-software',
                'license': 'Commercial',
                'source': 'Remcom'
            },
            {
                'name': 'SDR-Radio',
                'description': 'Software defined radio receiver. Free and easy to use.',
                'category': 'Wireless Communication',
                'popularity': 'Popular',
                'link': 'https://www.sdr-radio.com/',
                'license': 'Free',
                'source': 'SDR-Radio'
            },
            {
                'name': 'HFSS',
                'description': 'Electromagnetic simulation software for antennas and RF circuits.',
                'category': 'Wireless Communication',
                'popularity': 'Industry Standard',
                'link': 'https://www.ansys.com/products/electronics/ansys-hfss',
                'license': 'Commercial',
                'source': 'Ansys'
            },
            {
                'name': 'CST Studio Suite',
                'description': 'Electromagnetic simulation for wireless and RF applications.',
                'category': 'Wireless Communication',
                'popularity': 'Popular',
                'link': 'https://www.3ds.com/products-services/simulia/products/cst-studio-suite/',
                'license': 'Commercial',
                'source': 'Dassault Systemes'
            }
        ]

        self.tools_data.extend(wireless_tools)

    def collect_embedded_systems_tools(self):
        """Collect tools for embedded systems engineers"""
        print("Collecting embedded systems tools...")

        embedded_tools = [
            {
                'name': 'Keil MDK',
                'description': 'IDE for ARM microcontrollers. Industry standard but expensive.',
                'category': 'Embedded Systems',
                'popularity': 'Industry Standard',
                'link': 'https://www2.keil.com/mdk5',
                'license': 'Commercial',
                'source': 'ARM'
            },
            {
                'name': 'Arduino IDE',
                'description': 'Simple IDE for Arduino. Perfect for beginners.',
                'category': 'Embedded Systems',
                'popularity': 'Very Popular',
                'link': 'https://www.arduino.cc/en/software',
                'license': 'Open Source',
                'source': 'Arduino'
            },
            {
                'name': 'PlatformIO',
                'description': 'Modern IDE for embedded development. Works with many boards.',
                'category': 'Embedded Systems',
                'popularity': 'Growing',
                'link': 'https://platformio.org/',
                'license': 'Open Source',
                'source': 'PlatformIO'
            },
            {
                'name': 'STM32CubeIDE',
                'description': 'Free IDE for STM32 microcontrollers. Good documentation.',
                'category': 'Embedded Systems',
                'popularity': 'Popular',
                'link': 'https://www.st.com/en/development-tools/stm32cubeide.html',
                'license': 'Free',
                'source': 'STMicroelectronics'
            },
            {
                'name': 'MPLAB X IDE',
                'description': 'IDE for Microchip microcontrollers. Free to use.',
                'category': 'Embedded Systems',
                'popularity': 'Popular',
                'link': 'https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide',
                'license': 'Free',
                'source': 'Microchip'
            },
            {
                'name': 'ESP-IDF',
                'description': 'Development framework for ESP32. Good for IoT projects.',
                'category': 'Embedded Systems',
                'popularity': 'Growing',
                'link': 'https://docs.espressif.com/projects/esp-idf/en/latest/esp32/',
                'license': 'Open Source',
                'source': 'Espressif'
            }
        ]

        self.tools_data.extend(embedded_tools)

    def collect_ml_electronics_tools(self):
        """Collect machine learning tools for electronics engineers"""
        print("Collecting ML tools for electronics...")

        ml_tools = [
            {
                'name': 'TensorFlow Lite for Microcontrollers',
                'description': 'Run ML models on microcontrollers. Good for IoT projects.',
                'category': 'ML for Electronics',
                'popularity': 'Growing',
                'link': 'https://www.tensorflow.org/lite/microcontrollers',
                'license': 'Open Source',
                'source': 'Google'
            },
            {
                'name': 'Edge Impulse',
                'description': 'Easy platform for ML on edge devices. Great for beginners.',
                'category': 'ML for Electronics',
                'popularity': 'Growing Rapidly',
                'link': 'https://www.edgeimpulse.com/',
                'license': 'Freemium',
                'source': 'Edge Impulse'
            },
            {
                'name': 'MATLAB Deep Learning Toolbox',
                'description': 'Professional ML tools. Expensive but comprehensive.',
                'category': 'ML for Electronics',
                'popularity': 'Professional',
                'link': 'https://www.mathworks.com/products/deep-learning.html',
                'license': 'Commercial',
                'source': 'MathWorks'
            },
            {
                'name': 'PyTorch Mobile',
                'description': 'Deploy PyTorch models on mobile and embedded devices.',
                'category': 'ML for Electronics',
                'popularity': 'Growing',
                'link': 'https://pytorch.org/mobile/home/',
                'license': 'Open Source',
                'source': 'Meta'
            }
        ]

        self.tools_data.extend(ml_tools)

    def collect_pcb_design_tools(self):
        """Collect PCB design tools"""
        print("Collecting PCB design tools...")

        pcb_tools = [
            {
                'name': 'Altium Designer',
                'description': 'Professional PCB design software. Industry standard but expensive.',
                'category': 'PCB Design',
                'popularity': 'Industry Standard',
                'link': 'https://www.altium.com/altium-designer/',
                'license': 'Commercial',
                'source': 'Altium'
            },
            {
                'name': 'KiCad',
                'description': 'Free and open source PCB design tool. Great for students.',
                'category': 'PCB Design',
                'popularity': 'Very Popular',
                'link': 'https://www.kicad.org/',
                'license': 'Open Source',
                'source': 'KiCad Community'
            },
            {
                'name': 'Eagle',
                'description': 'Easy to use PCB design software. Good for hobbyists.',
                'category': 'PCB Design',
                'popularity': 'Popular',
                'link': 'https://www.autodesk.com/products/eagle/overview',
                'license': 'Commercial',
                'source': 'Autodesk'
            },
            {
                'name': 'Cadence Allegro',
                'description': 'High-end PCB design for complex boards. Used in industry.',
                'category': 'PCB Design',
                'popularity': 'Professional',
                'link': 'https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis.html',
                'license': 'Commercial',
                'source': 'Cadence'
            },
            {
                'name': 'EasyEDA',
                'description': 'Web-based PCB design tool. Free and simple to use.',
                'category': 'PCB Design',
                'popularity': 'Growing',
                'link': 'https://easyeda.com/',
                'license': 'Free',
                'source': 'JLCPCB'
            }
        ]

        self.tools_data.extend(pcb_tools)

    def collect_power_electronics_tools(self):
        """Collect power electronics tools"""
        print("Collecting power electronics tools...")

        power_tools = [
            {
                'name': 'PSIM',
                'description': 'Power electronics simulation software. Good for power circuits.',
                'category': 'Power Electronics',
                'popularity': 'Popular',
                'link': 'https://powersimtech.com/products/psim/',
                'license': 'Commercial',
                'source': 'PowerSim'
            },
            {
                'name': 'PLECS',
                'description': 'Power electronics simulation tool. Easy to use.',
                'category': 'Power Electronics',
                'popularity': 'Popular',
                'link': 'https://www.plexim.com/products/plecs',
                'license': 'Commercial',
                'source': 'Plexim'
            },
            {
                'name': 'MATLAB Simscape Power Systems',
                'description': 'Power system simulation in MATLAB. Very comprehensive.',
                'category': 'Power Electronics',
                'popularity': 'Professional',
                'link': 'https://www.mathworks.com/products/simscape-electrical.html',
                'license': 'Commercial',
                'source': 'MathWorks'
            },
            {
                'name': 'PowerWorld Simulator',
                'description': 'Power system analysis software. Good for grid studies.',
                'category': 'Power Electronics',
                'popularity': 'Professional',
                'link': 'https://www.powerworld.com/',
                'license': 'Commercial',
                'source': 'PowerWorld'
            }
        ]

        self.tools_data.extend(power_tools)

    def collect_test_measurement_tools(self):
        """Collect test and measurement tools"""
        print("Collecting test and measurement tools...")

        test_tools = [
            {
                'name': 'LabVIEW',
                'description': 'Graphical programming for test and measurement. Very popular.',
                'category': 'Test and Measurement',
                'popularity': 'Industry Standard',
                'link': 'https://www.ni.com/en-us/shop/labview.html',
                'license': 'Commercial',
                'source': 'National Instruments'
            },
            {
                'name': 'Python with PyVISA',
                'description': 'Control instruments using Python. Free and flexible.',
                'category': 'Test and Measurement',
                'popularity': 'Growing',
                'link': 'https://pyvisa.readthedocs.io/',
                'license': 'Open Source',
                'source': 'PyVISA Community'
            },
            {
                'name': 'MATLAB Instrument Control Toolbox',
                'description': 'Control instruments from MATLAB. Good integration.',
                'category': 'Test and Measurement',
                'popularity': 'Popular',
                'link': 'https://www.mathworks.com/products/instrument.html',
                'license': 'Commercial',
                'source': 'MathWorks'
            },
            {
                'name': 'Keysight Command Expert',
                'description': 'Easy instrument control software. Free from Keysight.',
                'category': 'Test and Measurement',
                'popularity': 'Popular',
                'link': 'https://www.keysight.com/us/en/lib/software-detail/computer-software/command-expert-downloads-2151326.html',
                'license': 'Free',
                'source': 'Keysight'
            }
        ]

        self.tools_data.extend(test_tools)

    def collect_all_data(self):
        """Collect data from all sources"""
        print("Starting electronics tools data collection...")
        self.tools_data = []

        # Collect from different domains
        self.collect_electronics_tools()
        self.collect_wireless_comm_tools()
        self.collect_embedded_systems_tools()
        self.collect_ml_electronics_tools()
        self.collect_pcb_design_tools()
        self.collect_power_electronics_tools()
        self.collect_test_measurement_tools()

        # Save to JSON file
        data = {
            'tools': self.tools_data,
            'last_updated': datetime.now().isoformat(),
            'total_count': len(self.tools_data)
        }

        os.makedirs('data', exist_ok=True)
        with open('data/tools.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Collected {len(self.tools_data)} electronics tools successfully!")
        return data

if __name__ == "__main__":
    collector = ElectronicsToolsCollector()
    collector.collect_all_data()
