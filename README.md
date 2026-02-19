# Anti Proxy Attendance System (APAS)

Open-source, Raspberry Pi–based biometric attendance that eliminates proxy attendance using R307 fingerprint verification, faculty-controlled sessions, and exportable records—recognized among standout innovations showcased at Smart India Hackathon 2024 and aligned with SIH’s mission to scale student-built solutions nationwide. Built on Raspberry Pi OS (formerly Raspbian), the stack follows documented UART integration practices for Python and Adafruit’s fingerprint library, ensuring reproducibility on common classroom hardware.[1][2][3][4][5]

## Story — by Adil Deokar

APAS started as a simple question: how can attendance be accurate, auditable, and fast without burdening teachers? As a CSE student and AI developer, Adil Deokar prototyped a portable, faculty-authenticated flow, iterating on real classroom constraints—speed, accuracy, and zero tolerance for proxy. The design pairs low-cost Raspberry Pi hardware with proven UART fingerprint workflows, refined through multiple testing cycles with R307-class sensors and the Adafruit ecosystem, culminating in a robust, classroom-ready tool that resonated with SIH evaluators focused on deployable impact across institutions.[2][4][6][1]

## Why open source

- Transparency and trust: Biometric systems must be auditable; open code invites scrutiny and improvement by the community and educators.[1]
- Accessibility and scale: Raspberry Pi OS support and commodity sensors reduce cost barriers for colleges and labs, aligning with SIH’s scale-out ethos from prototype to production use across campuses.[5][1]
- Shared standards: Built atop widely used Adafruit fingerprint libraries and UART patterns so contributors can extend features confidently and safely.[7][4]

## Highlights

- Biometric accuracy via R307 optical fingerprint over UART (57600) with fast search, enroll, delete, and image capture.[4][7]
- Faculty-controlled sessions with start/stop verification and PIN-based termination for integrity of class logs.[1]
- Low-cost Raspberry Pi stack on Raspberry Pi OS (formerly Raspbian), following best-practice serial setup on Bookworm/Bullseye releases.[3][5]
- Instant CSV/Excel-ready exports and clean data flows to feed LMS or dashboards later.[1]

## Tech stack

- Raspberry Pi 4, Raspberry Pi OS (Bookworm/Bullseye).[5]
- R307 sensor over UART; serial port setup per Adafruit’s Pi UART guidance.[4]
- Python, pyserial, Adafruit CircuitPython Fingerprint library; optional Pillow/openpyxl/pandas/reportlab for images/reports.[7][4]

## Hardware and wiring

- R307 TX → Pi RX (GPIO15), R307 RX → Pi TX (GPIO14), VCC → 5V, GND → GND; disable serial console and enable serial port in raspi-config to free UART for the sensor per Adafruit docs.[8][4]
- Optional 5" display for in-class UX; headless operation supported via terminal or SSH.[5]

## Setup

1) Raspberry Pi OS: update, enable UART, disable serial console, keep serial hardware active per Adafruit’s UART guide on Linux/Pi.[8][4]
2) Dependencies:  
- pip install: pyserial, adafruit-circuitpython-fingerprint, pillow, openpyxl, pandas, reportlab.[7][4]
3) Port: confirm sensor on /dev/ttyS0 or /dev/ttyAMA0 and set in code accordingly, as shown in Adafruit examples for Pi.[9][4]
4) Run: start the script, enroll template pairs, verify faculty, then circulate device for fast, proxy-proof roll calls.[4]

## Usage flow

- Enroll: two scans per student finger; templates stored and indexed for rapid matching.[6]
- Start class: choose subject, authenticate faculty fingerprint; begin attendance session.[1]
- Mark presence: circulate; matches log presence with confidence and identifiers; export as needed.[4]
- Close: faculty ends session with PIN; produce present/absent summary for records.[1]

## Security notes

- Restrict physical access to device and sensor; rotate strong faculty PINs and manage who can start/stop sessions.[1]
- Store templates/exports securely; align with local biometric consent and data protection policies in educational settings.[1]

## Results and SIH 2024 recognition

APAS demonstrated how low-cost hardware and open libraries can yield deployable outcomes—addressing a real institutional pain point and echoing SIH’s emphasis on production-grade student solutions across ministries and campuses, with winners recognized across multiple nodes and problem statements nationwide in 2024. The project’s demo-centric reliability and portability were core to its success narrative within SIH events hosted across India’s leading institutes and nodal centers.[2][1]

## Roadmap

- Web dashboard and analytics for class-level and institution-wide insights.[1]
- LMS integration via CSV/API bridges; automated alerts and attendance thresholds.[1]
- Optional multi-biometrics (face/iris) and encrypted template vaults for enhanced security.[6]

## Contributing

- Fork, branch, PR; include tests where feasible and update docs.  
- File issues for bugs/features; adhere to code style and commit messages referencing modules touched.[7]

## License

- MIT License for broad educational and research use; attribution appreciated to acknowledge community stewardship and SIH heritage.[7]

## Acknowledgments

- Adafruit’s CircuitPython Fingerprint library and UART guidance for Pi, enabling quick iteration on Raspberry Pi OS.[4][7]
- Educators, peers, and SIH organizers who champion reproducible, scalable student innovation across India’s institutions.[2][1]

## Quick start

- pip install pyserial adafruit-circuitpython-fingerprint pillow openpyxl pandas reportlab.[7][4]
- python3 apas.py and follow on-screen prompts for enroll, attendance, and export.[4]

Built with care by Adil Deokar—open, auditable, and ready to scale accurate attendance everywhere classrooms meet code.[2][1]

[1](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2085000)
[2](https://news.iitgn.ac.in/iitgn-celebrates-the-winners-of-smart-india-hackathon-sih-2024/)
[3](https://www.tomshardware.com/news/raspberry-pi-os-no-longer-raspbian)
[4](https://learn.adafruit.com/adafruit-optical-fingerprint-sensor/circuitpython)
[5](https://www.raspberrypi.com/documentation/computers/os.html)
[6](https://docs.circuitpython.org/projects/fingerprint/en/latest/)
[7](https://github.com/adafruit/Adafruit_CircuitPython_Fingerprint)
[8](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/uart-serial)
[9](https://docs.circuitpython.org/projects/fingerprint/en/1.1.6/examples.html)
[10](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2084190)
[11](https://www.djsce.ac.in/docs/SIH%20GRAND%20FINALE%202024.pdf)
[12](https://www.spsu.ac.in/innovation-meets-excellence-solar-masters-winning-journey-at-smart-india-hackathon-2024/)
[13](https://www.hindustantimes.com/cities/pune-news/students-of-army-institute-of-technology-win-big-at-smart-india-hackathon-2024-101734462028273.html)
[14](https://www.electromaker.io/blog/article/what-is-raspberry-pi-os)
[15](https://en.wikipedia.org/wiki/Raspberry_Pi_OS)
[16](https://www.reddit.com/r/raspberry_pi/comments/pd5omp/new_naming_convention_for_raspbian/)
[17](https://www.youtube.com/watch?v=TgNL3StNveg)
[18](https://www.raspberrypi.com/news/bookworm-the-new-version-of-raspberry-pi-os/)
[19](https://stackoverflow.com/questions/78565384/adafruit-fingerprint-sensor-library-error-on-a-raspberry-pi-4)
[20](https://en.wikipedia.org/wiki/Raspberry_Pi)
