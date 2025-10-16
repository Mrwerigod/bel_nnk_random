 EMG Jel Szimulátor – ROS 2 Beadandó

Cél: 

Ez a kis ROS 2 projekt egy egyszerű **EMG-jel szimulációt** valósít meg, amelyben
a `publisher` véletlenszerű EMG-értékeket generál, amelyek az ujjak
**behajlítását és kinyújtását** szimulálják.  
A `subscriber` ezeket az értékeket fogadja, és valós időben
**kiszámolja az átlagos izomaktivitást**.

 Futtatás;)  
 Build: 
 cd ~/ros2_ws
colcon build
source install/setup.bash 

Futtatás:
 ros2 launch my_robot_package emg_launch.py  
 Eredmény:  
 A `publisher` EMG értéket generál (0-1 között). 
 A `subscriber` ki írja az átlag izom aktivitást a Terminálba.
 
Node-ok és Topic-ok

```mermaid
graph TD;
    A[emg_publisher] -->|emg_data| B[emg_subscriber]

