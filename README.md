# Nursing Home Assistant Robot "PillBot"

This repository contains the code of the project "PillBot", a nursing home assistant robot. This robotic application is aimed to support caregivers to manage and deliver the medical treatment for elderly people in a nursing home. Using a Graphical User Interface, PillBot can be programmed at a specific time to deliver a medicine corresponding to the elderly person in their room.

The medicine delivery is performed with the use of a set of automatic pillboxes that the robot carry with it. Once in the elderly person's room, with the help of a RFID sensor and a card, the robot is able to authenticate the nurse. Once the nurse has been authenticated, the correct pillbox will open and the nurse will take the medicine from it to give it to the elder person, ensuring that whoever is going to take it is really the right person.

The Graphical User Interface also supports elderly person's vital signs registration (Temperature, Oxigen and Blood Presure). Once a new set of vital signs data has been entered into the interface, it is shown in a table, and it is sended to a ThingSpeak IoT dashboard as well, for remote monitoring of the health of the elderly person.

This prototype was implemented using a TurtleBot3 Waffle Pi with Robot Operating System (Kinetic Kame).

![robot Pillbot_rec](https://user-images.githubusercontent.com/38736789/143506593-55d2a717-c527-41ba-8f02-57c7f97bd180.jpeg)

## Why is this important? 🚀

This project aims to substantially decrease the risk for the elders of missing a dose or don’t taking it as prescribed, which could possibly harm the person's health. Medication regimens for elderly people can be very complex, and medication errors are more likely to happen, which can be very dangerous. Taking the right dose of each medication at the right time will make the treatment successful.

Moreover, the process of register and store person's vital signs data is digitized, which makes the whole procedure more comfortable for the caregivers, and the data can be consulted and visualized more easily.

## Requirements NASH📋

The following is a list of the software requirements to run this project:

* [ROS Kinetic Kame](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [TurtleBot3 Packages](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Python 2](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [mpg321](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [laser_filters package](https://maven.apache.org/) - Manejador de dependencias

## Software and Hardware tools NASH🛠️

_This is a list of other **software** that we used to build the whole application:_

* [ThingSpeak](https://rometools.github.io/rome/) - Usado para generar RSS
* [Qt Designer](https://maven.apache.org/) - Manejador de dependencias
* [Arduino IDE](https://rometools.github.io/rome/) - Usado para generar RSS
* [Gazebo](https://rometools.github.io/rome/) - Usado para generar RSS
* [RViz](https://rometools.github.io/rome/) - Usado para generar RSS

_And the **hardware** tools used to build the robot:_

* [TurtleBot3 Waffle Pi](https://rometools.github.io/rome/) - Usado para generar RSS
* [Raspberry Pi 3 (included in the Turtlebot)](https://maven.apache.org/) - Manejador de dependencias
* [Arduino UNO board](https://maven.apache.org/) - Manejador de dependencias
* [3 Servomotors](https://rometools.github.io/rome/) - Usado para generar RSS
* [Beats speaker audio AUX cable](https://rometools.github.io/rome/) - Usado para generar RSS
* [RFID RC522 Sensor with a card](https://rometools.github.io/rome/) - Usado para generar RSS

_Others:_

* Extra wood-floor for the TurtleBot
* [Plastic Pillboxes](https://www.amazon.com.mx/Apothecary-Pastillero-Económico-Empaque-paquete/dp/B00DUZVIIA/ref=pd_vtp_2/132-4825623-9585452?pd_rd_w=fjvz8&pf_rd_p=ebc0aaf8-0ad3-456f-b31b-18e7ec1f3d0b&pf_rd_r=BZTA2X6YAYTNQCHV6FWR&pd_rd_r=2b95ae26-e3a1-4ddd-aa61-e0a0172f5cc7&pd_rd_wg=JNFzF&pd_rd_i=B00DUZVIIA&psc=1)
* Metal rods
* Protoboard and cables

## Simulation 🔧

It is possible to run this project in a simulated environment, making use of a house model in Gazebo and the TurleBot3 Waffle simulated model. The following are the steps to run it:

In a terminal, run the launch file to launch the simulation (Gazebo and RViz). This launch file is `nursing_robot_simulation.launch`. Before launch it, please modify in this launch file the path according to the location of the house map in your machine. In this repo, there is already a map of the Gazebo house in the `maps` folder: `mapcasa.pgm` and `mapcasa.yaml`. Then, launch the file using:

    roslaunch nursing_home_robot nursing_robot_simulation.launch

It is recommended to follow the steps listed [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/) to estimate the initial pose of the robot. In another terminal, you can launch the `turtlebot3_teleop_key.launch` to estimate more precisely the pose:

    roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

In another terminal, run the Habitacion Service server:

    rosrun nursing_home_robot Servicio.py

Then, in other terminal, run the main code. The GUI should appear:

    rosrun nursing_home_robot MainPastillero.py

![Interfaz_PillBot](https://user-images.githubusercontent.com/38736789/143507270-3d6ce94a-1934-4592-a9e7-119cdb4861b2.jpeg)

## Running this project in a real TurtleBot3 🔩

If you want to reproduce this project with a real TurtleBot3, check the hardware components used in the "Hardware" section of this README.

### Previous configuration 🔧
First of all, clone this repo in your machine.

This project uses a laser filter to filter scan readings of the robot's sensor. To implemement this, we modified two files of the turtlebot3 packages installation. Please substitute the `move_base.launch` and the `turtlebot3_navigation.launch` files located at `/opt/ros/kinetic/share/turtlebot3_navigation/launch` for the ones with the same name located inside the launch folder of this repo. This in order to remap the `/scan` readings to `/scan_filtered`.

### Running the project  🔧

First, establish communication between the TurtleBot3 and your PC, as decribed [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup).

Then, execute the instructions listed [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/bringup/#bringup) to perform the Bringup of the TurtleBot.

As stated [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/#run-navigation-nodes) in section 5.1, launch the navigation with:

    export TURTLEBOT3_MODEL=burger

    roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml

Make sure to specify the sorrect path to the map. After doing this, RViz will appear. In another terminal located at `/nursing_home_robot`, load the next file to the parameters server:

    rosparam load my_laser_config.yaml scan_to_scan_filter_chain

And run the laser filter:

    rosrun laser_filters scan_to_scan_filter_chain

It is recommended to follow the steps listed [here](https://emanual.robotis.com/docs/en/platform/turtlebot3/nav_simulation/) to estimate the initial pose of the robot. In another terminal, you can launch the `turtlebot3_teleop_key.launch` to estimate more precisely the pose:

    roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

In the SBC of the TurtleBot3, in a terminal located at `/nursing_home_robot/src` run the Habitacion Service server:

    rosrun nursing_home_robot Servicio.py

Then, again in the remote PC, run the main code. The GUI should appear:

    rosrun nursing_home_robot MainPastillero.py

![Interfaz_PillBot](https://user-images.githubusercontent.com/38736789/143507270-3d6ce94a-1934-4592-a9e7-119cdb4861b2.jpeg)

## Interface functionalities
It is possible for a nurse of the nursing home to login into the GUI application using the corresponding credentials. In this case, use `Username` as the Username and `Password` as the Password. Once you clic in the "Iniciar Sesion" button, the different tabs of the GUI will be activated.

![Interfaz_PillBot_user](https://user-images.githubusercontent.com/38736789/143507331-b3191802-e819-4d17-858f-f16c4698868a.jpeg)

### Schedules tab (Horario del dia) ⚙️

In the Schedules tab ("Horario del dia" in Spanish), the nurse can program the robot to deliver medicine to a specific elderly person, at a specific hour. The nurse just need to select the elderly patient from the combo box, and specify the hour at which the robot will visit that person. When the "Guardar" button is clicked, the walk is scheduled in the robot's itinerary.

![Horario_del_dia](https://user-images.githubusercontent.com/38736789/143507470-637ebb9e-223d-4f59-bce8-68d7f348430a.jpeg)


When its time, the robot will visit the elder person's room to deliver medicine. When the robot arrives to the room, it will reproduce an audio to anounce it arrival (using mpg321).

Once the robot has arrived and has said a phrase, the nurse must pass the card in front of the RFID sensor for authentication purposes. Once done, the correct pillbox will be opened, for the nurse to take the pills and give them to the elderly person. When this is finished, the nurse must push the button on the robot, to indicate that the pillbox must close. In the simulation, the authentication of the nurse using the RFID sensor and the card, and the opening of the pillbox is omitted.

After this process, the robot will return to its base, and will wait for another scheduled time to deliver medicine.

### Vital Signs tab (Signos Vitales) ⚙️

The GUI also allows to register data about elderly person's health: Temperature (°C), Oximetry (%) and Blood presure (mmHg). The nurse only need to enter the values in the interface, and when the "Guardar" button is clicked, the values will be added to a table.

![signos_vitales](https://user-images.githubusercontent.com/38736789/143507544-eff83da8-2af1-4e23-92ee-5083a96c821d.jpeg)

####  ThingSpeak ⚙️
Each time a new data entry of vital signs (temperature, oxymetry and blood pressure) is made through the "Signos Vitales" tab of the GUI, these data is sent to the corresponding resident's ThingSpeak dashboard.

![dashboard_1](https://user-images.githubusercontent.com/38736789/143507661-5cf3eeba-43cc-4af2-8b8c-e88e5bd3f4b0.PNG)

In each dashboard, there are three graphs, one for each variable mentioned above, which show the measured data vs. time. Each record shows the obtained value, and the exact time in which the data was received in the cloud. This way, the family members of the resident, who can access the dashboard, can monitor their loved one's health in real time.

![dashboard_2](https://user-images.githubusercontent.com/38736789/143507684-841f70e8-ec09-4327-807e-a6dc45317dbf.png)

You can create your own ThingSpeak account clicking [here](https://thingspeak.com). Substitute your dashboard API Key for an elderly person, in `MainPastillero.py`:

```Python
        if str(nombrePaciente)=='Omar Perez':
            #Substitute here your ThingSpeak API Key
            self.web("PK1UENEO00MJXH4R", int(temperatura), int(oxigeno), int(presion))
```

## Team members ✒️ NASH

This project was developed by:

* **Carlos Mario Bielma Avendaño** - *A017* - [villanuevand](https://github.com/villanuevand)
* **Nashely Martínez Chan** - *Documentación* - [fulanitodetal](#fulanito-de-tal)
* **Jonatan Emanuel Salinas Ávila** - *Documentación* - [fulanitodetal](#fulanito-de-tal)
* **Ximena Aaroni Salinas Molar** - *Documentación* - [fulanitodetal](#fulanito-de-tal)
* **Martín Octavio García García** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

## Video 📄 NASH

Video aca

## Acknowledges 🎁 NASH

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.

---
November 2021.