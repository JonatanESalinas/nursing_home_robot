# Nursing Home Assistant Robot "PillBot"

This repository contains the code of the project "PillBot", a nursing home assistant robot. This robotic application is aimed to support caregivers to manage and deliver the medical treatment for elderly people in a nursing home. Using a Graphical User Interface, PillBot can be programmed at a specific time to deliver a medicine corresponding to the elderly person in their room.

The medicine delivery is performed with the use of a set of automatic pillboxes that the robot carry with it. Once in the elderly person's room, with the help of a RFID sensor and a card, the robot is able to authenticate the nurse. Once the nurse has been authenticated, the correct pillbox will open and the nurse will take the medicine from it to give it to the elder person, ensuring that whoever is going to take it is really the right person.

The Graphical User Interface also supports elderly person's vital signs registration (Temperature, Oxigen and Blood Presure). Once a new set of vital signs data has been entered into the interface, it is shown in a table, and it is sended to a ThingSpeak IoT dashboard as well, for remote monitoring of the health of the elderly person.

This prototype was implemented using a TurtleBot3 Waffle Pi with Robot Operating System (Kinetic Kame).

## Why is this important? 🚀

This project aims to substantially decrease the risk for the elders of missing a dose or don’t taking it as prescribed, which could possibly harm the person's health. Medication regimens for elderly people can be very complex, and medication errors are more likely to happen, which can be very dangerous. Taking the right dose of each medication at the right time will make the treatment successful.

Moreover, the process of register and store person's vital signs data is digitized, which makes the whole procedure more comfortable for the caregivers, and the data can be consulted and visualized more easily.

_imagen del robot_

### Requirements NASH📋

_The following is a list of the software requirements to run this project:_

* [ROS Kinetic Kame](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [TurtleBot3 Packages](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Python 2](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [mpg321](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [laser_filters package](https://maven.apache.org/) - Manejador de dependencias

### Software and Hardware tools NASH🛠️

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

### Previous configuration 🔧
First of all, clone this repo in your machine.

This project uses a laser filter to fiter scan readings of the robot's sensor. To implemement this, we modified two files of the turtlebot3 packages installation. Please substitute the move_base.launch and the turtlebot3_navigation.launch files located at /opt/ros/kinetic/share/turtlebot3_navigation/launch for the ones with the same name located inside the launch folder of this repo. This in order to remap the /scan readings to /scan_filtered.

### Simulation 🔧

It is possible to run this project in a simulated environment, making use of a house model in Gazebo and the TurleBot3 Waffle simulated model. The following are the steps to run it:

After doing the steps described in "Previous configuration", the simulation can be run.
In a terminal, run the launch file to launch the simulation (Gazebo and RViz). The launch file to launch is nursing_robot_simulation.launch. Before launch it, please modify the path to the house map according to the location of the house map in your machine. In this repo, there is already a map of the Gazebo house in the maps folder: mapcasa.pgm and mapcasa.yaml. Then, launch the file using:

```
roslaunch nursing_home_robot nursing_robot_simulation.launch
```

After doing this, in other terminal located at /nursing_home_robot, load the next file to the parameters server:
```
rosparam load my_laser_config.yaml scan_to_scan_filter_chain
```
And run the laser filter:
```
rosrun laser_filters scan_to_scan_filter_chain
```
It is recommended to follow the steps listed here to estimate the initial pose of the robot. In other terminal, you can launch the turtlebot3_teleop_key.launch to estimate more precisely the pose:

```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```

In another terminal, run the Habitacion Service server:
```
rosrun nursing_home_robot Servicio.py
```

Then, in other terminal located at /nursing_home_robot/src , run the main code. The GUI should appear:
```
rosrun nursing_home_robot MainPastillero.py
```

    Imagen

It is possible for a nurse of the nursing home to login into the GUI application using the corresponding credentials. In this case, use "Username" as the Username and "Password" as the Password. Once you clic in the button, the different tabs of the GUI will be activated.

    Imagen

## Schedules tab (Horario del dia) ⚙️

In the Schedules tab ("Horario del dia" in Spanish), the nurse can program the robot to deliver medicine to a specific elderly person, at a specific hour. The nurse just need to select the elderly patient from the combo box, and specify the hour at which the robot will visit that person. When the "Guardar" button is clicked, the walk is scheduled in the robot's itinerary.

When its time, the robot will visit the elder person's room to deliver medicine. When the robot arrives to the room, it will reproduce an audio to anounce it arrival (using mpg321).

In the simulation, the authentication of the nurse using the RFID sensor and the card, and the opening of the pillbox is omitted.

After visiting the elder person's room, the robot will return to its base.

## Vital Signs tab (Signos Vitales) ⚙️

The GUI also allows to register data about elderly person's health: Temperature (°C), Oximetry (%) and Blood presure (mmHg). The nurse only need to enter the values in the interface, and when the "Guardar" button is clicked, the values will be added to a table.

#  ThingSpeak ⚙️
Each time a new data entry of vital signs (temperature, oxymetry and blood pressure) is made through the "Signos Vitales" tab of the GUI, these data is sent to the corresponding resident's ThingSpeak dashboard.

    Imagen

In each dashboard, there are three graphs, one for each variable mentioned above, which show the measured data vs. time. Each record shows the obtained value, and the exact time in which the data was received in the cloud. This way, the family members of the resident, who can access the dashboard, can monitor their loved one's health in real time.

You can create your own ThingSpeak account clicking here. Substitute your dashboard API Key for an elderly person, in MainPastillero.py:

```
        if str(nombrePaciente)=='Omar Perez':
            #Substitute here your ThingSpeak API Key
            self.web("PK1UENEO00MJXH4R", int(temperatura), int(oxigeno), int(presion))
```

### Running this project in a real TurtleBot3 🔩

If you want to reproduce this project with a real TurtleBot3

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_
_Explica como ejecutar las pruebas automatizadas para este sistema_



_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_



## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

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